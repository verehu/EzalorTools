#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2018 - huwei <huwei@gionee.com>
"""
This is a python script for the ezalor tools which is used to io monitor.
You can use the script to open or off the switch, or point the package name which you want to monitor it only.
The core function is to export data what ezalor is record.
"""

import os
import re
import sys, getopt
import sqlite3
import subprocess

import numpy as np
import xlsxwriter as xw
from style import Style
from datetime import datetime

DB_NAME_REG = "^ezalor_{0}(.*).db$"

tableheaders = ["path", "process", "thread", "processId", "threadId",
                "readCount", "readBytes", "readTime", "writeCount", "writeBytes", "writeTime", "stacktrace",
                "openTime", "closeTime", "mark"]
envDir = "/sdcard/ezalor/"
AUTOCOLUMN_WIDTH_INDEXS = [0, 1, 2, 12, 13, 14]


def print_help_and_exit():
    print("\n"
          "This is a python script for the ezalor tools which is used to io monitor.You can use the script to open or\n"
          "off the switch, or point the package name which you want to monitor it only.The core function is to export\n"
          "data what ezalor is record.\n"
          "\n"
          "Usage : ezalor [Options] [Args]\n"
          "\n"
          "     Options:\n"
          "         -h, --help                              :Print the message and exit\n"
          "         -e, --export [packageName] [exportPath] :export a html to the path\n"
          "\n"
          "     Examples:\n"
          "         ezalor -s on                            switch on the ezalor\n"
          "         ezalor -e com.android.gallery2          export html\n"
          )
    sys.exit(0)


def write_to_file(path, content):
    if ("." == path):
        htmlPath = "export.html"
    else:
        htmlPath = path + "export.html"

    fo = open(htmlPath, "w")
    fo.write(content)
    fo.close()
    return htmlPath


def export(packageName, path):
    print("export to path:" + path + "  begin.")

    workbook = xw.Workbook(path)
    # style
    style = Style(workbook)
    worksheet = workbook.add_worksheet("ioHistory")
    # get process by packageName
    processes = get_process_by_package(packageName)

    # loop create table group by process
    row = 0
    for process in processes:
        row = create_table(worksheet, style, process, row, get_data_by_process(packageName, process))

    workbook.close()
    print("export successful!")


def get_data_by_process(packageName, process):
    # pull db file from mobile
    os.system("adb pull /sdcard/ezalor/" + packageName + "/ezalor_" + process + ".db ezalor.db")
    # fetch data from db file
    cursor = get_cursor("ezalor.db")
    cursor.execute("select * from iohistory")
    results = cursor.fetchall()
    # clear db file
    os.remove("ezalor.db")
    return results


def create_table(worksheet, style, process, row, data):
    # set column width
    worksheet.set_column('N:N', None, style.column_auto_fit)

    # write a title of table
    worksheet.write(row, 0, process + " ioHistory")
    row += 1
    # write headers of table
    for index, item in enumerate(tableheaders):
        worksheet.write(row, index, tableheaders[index], style.table_headers)
    row += 1
    # write contents of table
    column_max_width_array = [0] * len(AUTOCOLUMN_WIDTH_INDEXS)
    for record in data:
        for column, columnValue in enumerate(record):
            value = get_value(column, record)
            worksheet.write(row, column, value, get_style(style, column, record))
            # get max width
            if (column in AUTOCOLUMN_WIDTH_INDEXS):
                i = AUTOCOLUMN_WIDTH_INDEXS.index(column)
                column_max_width_array[i] = max(column_max_width_array[i], len(value))

        row += 1

    # set column width
    for j in range(len(column_max_width_array)):
        worksheet.set_column(AUTOCOLUMN_WIDTH_INDEXS[j], AUTOCOLUMN_WIDTH_INDEXS[j], column_max_width_array[j])

    return row


def get_value(column, record):
    if column == 13 or column == 12:
        java_timestamp = record[column]
        return datetime.fromtimestamp(java_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    return record[column]


def get_style(style, column, record):
    return style.common


def get_process_by_package(packageName):
    # exec adb shell ls
    dbDir = envDir + packageName
    results = subprocess.getstatusoutput("adb shell ls " + dbDir)
    # get db fileName by reg
    files = []
    if (results[0] == 0):
        for file in results[1].split("\n"):
            print(file)
            if (re.match(DB_NAME_REG.format(packageName), file)):
                files.append(re.findall(r"ezalor_(.+?).db", file)[0])
    return files


def transpose(list_):
    return [list(i) for i in np.array(list_).T]


#    os.system("rm " + path + "ezalor.db")
def get_cursor(dbpath):
    conn = sqlite3.connect(dbpath)
    return conn.cursor()


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:e:", ["help", "switch", "export"])
    except getopt.GetoptError:
        print_help_and_exit()
    if len(opts) == 0:
        print_help_and_exit()
        return

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help_and_exit()
        elif opt in ("-e", "--export"):
            if (len(arg) == 0):
                print_help_and_exit()

            packageName = arg
            outPath = packageName + ".xlsx" if len(args) == 0 \
                else args[0] + "/" + packageName + ".xlsx"

            export(packageName, outPath)


if __name__ == "__main__":
    main(sys.argv[1:])
