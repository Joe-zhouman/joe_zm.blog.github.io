---
layout: code
istop : true
book : true
title: python自动联网的脚本
category: code
tags: python 爬虫
background-image: python.jpeg
date: 2019-07-19 10:28:09 + 0800
code: true
---
更新后的校园网老断，用python写了个自动联网的脚本。<!-- more -->

# python自动联网的脚本

## 问题简述

本问题的实质是利用python的requests模块模拟发出联网的请求。

## 准备工作

需要

+ `Chrome`浏览器

+ `python` 3.6及以上版本

+ python`requests`模块

## 抓包

在这里以某大学校园网为例

1. 用`Chrome`打开校园网登陆页面，并按`F12`进入开发者模式

[]{{site.url}}/style/auto_connector/ac1.png

2. 进入`network`选项卡，并勾选`Preserve log`选项

[]{{site.url}}/style/auto_connector/ac2.png

3. 登陆校园网，可以看到下面出来很多东西，这些其实是我们登陆过程中发送和接受到的所有请求

4. 找到含`login`的请求，点击查看，打开header选项卡，找到`Request Headers`和`Query String Parameters`两部分

[]{{site.url}}/style/auto_connector/header.png

## 程序

将`Request Headers`和`Query String Parameters`里面的内容填入下面的代码里

```python

#-*- coding:utf-8 -*-
__author__ = 'joe_zhouman'

import time
import requests
import os
class Login:

    #初始化
    def __init__(self):
        #检测间隔时间，单位为秒
        self.every = 1800

    #模拟登录
    def login(self):
        print(self.getCurrentTime(), u"拼命连网中...")

        url="http://10.36.254.11/drcom/login"
        #消息头
        headers={
            'Accept':"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            'Accept-Encoding':"gzip, deflate",
            'Accept-Language':"zh-CN,zh;q=0.9,zh-TW;q=0.8",
            'Connection':"keep-alive",
            'Cookie':"",
            'Host':"",
            'Referer':"",
            'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
            'X-Requested-With':"XMLHttpRequest"
        }
        #key value
        kv = {
            'callback':"",
            'DDDDD':"",    
            'upass':"",
            '0MKKey':"",
            'R1':"0",
            'R3':"0",
            'R6':"0",
            'para':"00",
            'v6ip':"",
            '_':""
        }
        try:
            requests.get(url, params = kv, headers = headers)
            print( self.getCurrentTime(),u'连上了...现在开始看连接是否正常')
        except:
            print("error")
    #判断当前是否可以连网
    def CanConnect(self):
        try:
            exit_code = os.system('ping www.baidu.com')
            if not exit_code:
                return True
            else:
                return False
        except:
            print( 'error')

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #主函数
    def main(self):
        print( self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        while True:
            self.login()
            while True:
                can_connect = self.CanConnect()
                if not can_connect:
                    print( self.getCurrentTime(),u"断网了...")
                    self.login()
                else:
                    print( self.getCurrentTime(), u"一切正常...")
                time.sleep(self.every)
            time.sleep(self.every)

login = Login()
login.main()

```

运行程序，大功告成。

## 开机启动

用python的`installer`模块将程序打包成exe，将其快捷方式放入启动中，就可以开机启动啦~~~

反正我是很久没进过登陆页面了。

## 说明

本程序针对校园网的登陆请求为`get`，一般还有很多使用`post`请求的。请求类型同样可以在上面的header里查看。

[]{{site.url}}/style/auto_connector/get.png