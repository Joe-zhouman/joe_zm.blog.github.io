---
layout: code
istop : true
book : true
title: python自动联网的脚本
category: code
tags: python 爬虫
background-image: python.jpeg
date: 2021-1-13 10:15:16 + 0800
---
更新后的校园网老断，用python写了个自动联网的脚本。<!-- more -->

# 更新

* 2022-1-7 09:27:49 学校的联网入口改了，故而改成最新的了。

# 问题简述

本问题的实质是利用python的requests模块模拟发出联网的请求。

# 准备工作

需要

+ `Chrome`浏览器
+ `python` 3.6及以上版本
+ python的`requests`模块

# 抓包

在这里以某大学校园网为例

1. 用`Chrome`打开校园网登陆页面，并按`F12`进入开发者模式

![ac1.png](https://i.loli.net/2021/03/18/sEp7wCRVW5Kl6XD.png)

2. 进入`network`选项卡，并勾选`Preserve log`选项

![ac2.png](https://i.loli.net/2021/03/18/fvyx8ER5HkMichz.png)

3. 登陆校园网，可以看到下面出来很多东西，这些其实是我们登陆过程中发送和接受到的所有请求
4. 找到含`login`的请求，点击查看，打开header选项卡，找到`Request Headers`和`Query String Parameters`两部分

![header.png](https://i.loli.net/2021/03/18/34MIJjbqVv8egk1.png)

# 准备

安装`requests`模块

```bash
pip install requests
```

# 程序

将`Request Headers`和`Query String Parameters`里面的内容填入下面的代码里

```python

# -*- coding:utf-8 -*-
__author__ = 'joe_zhouman'

import os
import time

import requests

class Login:

    # 初始化
    def __init__(self):
        # 检测间隔时间，单位为秒
        self.every = 60

    # 模拟登录
    def login(self):
        print(self.getCurrentTime(), u"拼命连网中...")

        url = "http://10.0.1.5/drcom/login"
        # 消息头
        headers = {
            'Accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Connection': "keep-alive",
            'Cookie': "PHPSESSID=p743j2ds11nc93vn0vg8f5vs46",
            'Host': "10.0.1.5",
            'Referer': "http://10.0.1.5/a79.htm?isReback=1",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            'X-Requested-With': "XMLHttpRequest"
        }
        # key value
        kv = {
            'callback': "dr1356976306480",
            'DDDDD': "",##改成自己的账号
            'upass': "",##改成自己的密码
            '0MKKey': "123456",
            'R1': "0",
            'R3': "0",
            'R6': "0",
            'para': "00",
            'v6ip': "",
            '_': "1356976296832"
        }
        try:
            requests.get(url, params=kv, headers=headers)
            print(self.getCurrentTime(), u'连上了...现在开始看连接是否正常')
        except:
            print("error")
    # 判断当前是否可以连网

    def CanConnect(self):
        try:
            exit_code = os.system('ping www.baidu.com')
            if not exit_code:
                return True
            else:
                return False
        except:
            print('error')

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 主函数
    def main(self):
        print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        can_connect = self.CanConnect()
        while not can_connect:
            print(self.getCurrentTime(), u"未能连接网络,请重试...")
            self.login()
      
            can_connect = self.CanConnect()          
            time.sleep(self.every)
        print(self.getCurrentTime(), u"联网成功...")


login = Login()
login.main()


```

运行程序，大功告成。

# 开机启动

建立一个`.bat`文件,在里面写上

```bat
python "{PyFilePath}"
```

如我的
![bat.png](https://i.loli.net/2021/03/18/RdIaDTl1rQJYPw7.png)
在windows的`任务计划程序`中新建一个定时启动的任务,按下图设置:
![计划任务设置-常规](https://i.loli.net/2021/03/18/Y1Dcs6iVTRJyOpz.png))
![计划任务设置-触发器](https://i.loli.net/2021/03/18/bv4DsOauxHK7FNY.png)
![计划任务设置-操作](https://i.loli.net/2021/03/18/rQuCvUA3HBTegFk.png)
这里的`启动程序`就是你之前建立的`.bat`文件.

其余的按默认设置即可.

# 说明

本程序针对校园网的登陆请求为`get`，一般还有很多使用`post`请求的。请求类型同样可以在上面的header里查看。

![get.png](https://i.loli.net/2021/03/18/GXKDUlWjypVTCch.png)

如果有需要的话，可以再写个程序。

# 问题

Q: `python`,`pip`命令无效？

A: 把`python`,`pip`路径加入环境变量`path`中，`pip`一般在`python`安装路径下面的`Scripts`文件夹中
