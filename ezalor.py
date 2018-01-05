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
import webbrowser

import pandas as pd
import numpy as np

tableheaders = ["filepath", "process", "thread", "readcount", "readbytes", "readtime",
                "writecount", "writebytes", "writetime", "stacktrace", "opentime", "closetime"]

def printHelpAndExit():
    print("\n"
          "This is a python script for the ezalor tools which is used to io monitor.You can use the script to open or \n"
          "off the switch, or point the package name which you want to monitor it only.The core function is to export \n"
          "data what ezalor is record.\n"
          "\n"
          "Usage : ezalor [Options] [Args]\n"
          "\n"
          "     Options:\n"
          "         -h, --help                              :Print the message and exit\n"
          "         -s, --switch [on][off][status]          :enable or disable the ezalor\n"
          "         -e, --export [processname] [exportpath] :export a html to the path\n"
          "\n"
          "     Examples:\n"
          "         ezalor -s on                            switch on the ezalor\n"
          "         ezalor -e com.android.gallery2          export html\n"
          )
    sys.exit(0)

def wrtieToFile(path, content):
    if ("." == path):
        htmlPath = "export.html"
    else:
        htmlPath = path + "export.html"

    fo = open(htmlPath, "w")
    fo.write(content)
    fo.close()
    return htmlPath

def convert2html(tableHeaders, result):
    d = {}
    index = 0
    for t in tableHeaders:
        d[t] = result[index]
        index = index + 1
    df = pd.DataFrame(d)
    df = df[tableHeaders]
    h = df.to_html(index=False)
    return h

def export(processname, path):
    os.system("adb pull /sdcard/ezalor/" + processname + "/ezalor.db" + "     " + path)

    cursor = getCursor("ezalor.db")
    cursor.execute("select * from iohistory")
    results = cursor.fetchall()

    htmlPath = wrtieToFile(path, convert2html(tableheaders, transpose(results)))
    print("html has exported to " + htmlPath)

    webbrowser.open(htmlPath)

def transpose(list_):
    return [list(i) for i in np.array(list_).T]

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
            if (len(arg) == 0):
                printHelpAndExit()

            processname = arg
            outPath = "." if len(args) == 0 else args[0]

            export(processname, outPath)

if __name__ == "__main__":
    main(sys.argv[1:])