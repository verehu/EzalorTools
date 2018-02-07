# EzalorTools

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![platform](https://img.shields.io/badge/platform-Python3-yellow.svg)](https://www.android.com)
[![PRs Welcome](https://img.shields.io/badge/prs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Code Climate](https://img.shields.io/codeclimate/issues/github/me-and/mdf.svg)](https://github.com/WellerV/Ezalor/issues)

EzalorTools is [Ezalor][1]'s export tool.Now it supports excel.
 
 ![export][2]
 
 ## [中文版点击这里](README_CN.md)
 
## Getting started
First, you need [Python3][3] environment.
It's ok if you get the result like follow in terminal.
```shell
$ python3 --version

Python 3.x.x
```

## Export Data
This is a python script for the ezalor tools which is used to io monitor.You can use the script to open or
off the switch, or point the package name which you want to monitor it only.The core function is to export
data what ezalor is record.
```
Usage : ezalor [Options] [Args]

     Options:
         -h, --help                              :Print the message and exit
         -e, --export [packageName] [exportPath] :export a html to the path

     Examples:
         ezalor -e com.wellerv.ezalor.sample          export excel
```
When you want to export data, command like this:
```shell
python3 ezalor.py -e com.wellerv.ezalor.sample [path]
```

 Different colors in the data represent different levels, 
 1. **red** -> error
 2. **yellow** -> warning
 3. **white** -> ok
 
 ## Different level
 ### 1. error
 - io in main thread: Marked when io operation occurs on main thread
 ### 2. warning
 - unbufferedIO: Marked when  io operation bufferr is too small.
 The condition like google code in Android O:
 ![ioTracker][4]
 ### 3.ok
 - ok : ok

## Support
Any problem?

1. Submit issues
2. Contact me for help by [email][5]


  [1]: https://github.com/WellerV/Ezalor
  [2]: http://on8vjlgub.bkt.clouddn.com/%E5%B0%8F%E4%B9%A6%E5%8C%A0/ezalortools_export.png "ezalortools_export"
  [3]: https://www.python.org/download/releases/3.0/
  [4]: http://on8vjlgub.bkt.clouddn.com/%E5%B0%8F%E4%B9%A6%E5%8C%A0/iotracker.jpg "iotracker"
  [5]: huweigoodboy@126.com