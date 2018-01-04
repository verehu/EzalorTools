#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2018 - huwei <huwei@gionee.com>
"""
This is a python script for the ezalor tools which is used to io monitor.
You can use the script to open or off the switch, or point the package name which you want to monitor it only.
The core function is to export data what ezalor is record.
"""

import os
import sys, getopt
import sqlite3
import pandas as pd

tableheaders = {"filepath", "process", "thread", "readcount", "readbytes", "readtime",
                "writecount", "writebytes", "writetime", "stacktrace", "opentime", "closetime"}

def printHelpAndExit():
    print("This is a python script for the ezalor tools which is used to io monitor.\n"
          "You can use the script to open or off the switch, or point the package name which you want to monitor it only.\n"
          "The core function is to export data what ezalor is record.\n"
          "\n"
          "Usage : ezalor [Options] [Args]\n"
          "\n"
          "     Options:\n"
          "         -h, --help                           :Print the message and exit\n"
          "         -s, --switch [on][off][status]       :enable or disable the ezalor\n"
          )
    sys.exit(0)

def convert2html(tableHeaders, result):
    d = {}
    index = 0
    for t in tableHeaders:
        d[t] = tableHeaders[index]
        index = index + 1
    df = pd.DataFrame(d)
    h = df.to_html(index=False)
    return h

def export(processname, path):
    os.system("adb pull /sdcard/ezalor/" + processname + "/ezalor.db" + "     " + path)

    cursor = getCursor(path + "/ezalor.db")
    results = cursor.fetchall()

    print(results)

#    os.system("rm " + path + "ezalor.db")
def getCursor(dbpath):
    conn = sqlite3.connect(dbpath)
    return conn.cursor()

def switch(flag):
    os.system("adb shell setprop persist.ezalor.enable " + flag)

def status():
    output = os.popen("adb shell getprop persist.ezalor.enable").read().strip('\n')
    print("ezalor switch status:" + ("on" if output == "true" else "off"))

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:e:", ["help", "switch", "export"])
    except getopt.GetoptError:
         printHelpAndExit()
    if len(opts) == 0:
        printHelpAndExit()
        return

    isExport = False
    processname = ""
    outPath = "."

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printHelpAndExit()
        elif opt in ("-s", "--switch"):
            if ("on" == arg):
                switch("true")
                status()
            elif ("off" == arg):
                switch("false")
                status()
            elif ("status" == arg):
                status()
            else:
                printHelpAndExit()
        elif opt in ("-e", "--export"):
            isExport = True
            processname = arg
        elif opt in ("-o", "--output"):
            if isExport:
                outPath = arg

    if isExport:
        if "" == processname:
            printHelpAndExit()
        else:
            export(processname, outPath)



if __name__ == "__main__":
    main(sys.argv[1:])