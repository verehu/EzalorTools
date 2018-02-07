# EzalorTools

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![platform](https://img.shields.io/badge/platform-Python3-yellow.svg)](https://www.android.com)
[![PRs Welcome](https://img.shields.io/badge/prs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Code Climate](https://img.shields.io/codeclimate/issues/github/me-and/mdf.svg)](https://github.com/WellerV/Ezalor/issues)

EzalorTools是[Ezalor][1]'的数据导出工具。目前只支持导出excel,导出结果会对io操作进行分析,标记出不合理的位置.
 
 ![export][2]

## 开始
首先, 你需要安装[Python3][3]环境。
如果你得到以下结果,说明环境可用。
```shell
$ python3 --version

Python 3.x.x
```

## 导出数据
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
运行下面命令导出数据:
```shell
python3 ezalor.py -e com.wellerv.ezalor.sample [path]
```

 不同的颜色代表不同的等级:
 1. **red** -> error
 2. **yellow** -> warning
 3. **white** -> ok
 
 ## 不同等级
 不同的情况将会被标为不同的等级。
 ### 1. error
 - io in main thread: io操作发生在主线程
 ### 2. warning
 - unbufferedIO: io操作缓存不合理,太小。
判断调节和谷歌android o源码相同,
 ![ioTracker][4]
 ### 3.ok
 - ok : 通过

## 支持
有任何问题?

1. 提交issues
2. 通过[email][5]联系我


  [1]: https://github.com/WellerV/Ezalor
  [2]: http://on8vjlgub.bkt.clouddn.com/%E5%B0%8F%E4%B9%A6%E5%8C%A0/ezalortools_export.png "ezalortools_export"
  [3]: https://www.python.org/download/releases/3.0/
  [4]: http://on8vjlgub.bkt.clouddn.com/%E5%B0%8F%E4%B9%A6%E5%8C%A0/iotracker.jpg "iotracker"
  [5]: huweigoodboy@126.com