---
layout: code
istop : true
book : true
title: C#串口数据读取及处理解决方案--祖传代码修改记
category: code
tags: C# multithreading 多线程 queue 队列
background-image: CSharpDotNet.png
date: 2021-3-14 17:17:41 + 0800
---
花了很多功夫，终于把祖传代码重构了，重构后的方案基本可以用作串口数据读取处理的通用方案。<!-- more -->

# 原方案

首先说明一下，我对串口通信的理解不深，所有关于这方面的说明会有很多纰漏，有时会词不达意，各位图一乐就好。

## 代码

~~~cs
private char _start; // 起始位标志
private char _end;   // 结束位标志
private string recvstr;         // 用于存储一组数据的全局变量

public void sendMsg(){
    Thread thread;
    thread = new Thread(() =>//新开线程，执行接收数据操作
    {
        while (enablescan)//如果标识为true
        {
            Thread.Sleep(1);
            try
            {
                serialPort1.WriteLine(":READ?");
                Thread.Sleep(AppCfg.devicepara.Scan_interval);
            }
            catch (Exception ex){;}
        }
    });
    thread.Start();//启动线程
    thread.IsBackground = true;
}

private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            string str = serialPort1.ReadExisting();
            if (str.IndexOf(_start) != -1)//当前数据存在起始位
            {
                str = str.Substring(str.IndexOf(_start), str.Length - str.IndexOf(_start);//截取起始位到字符串末尾
            }
            if(str.IndexOf(_end==-1)//当前数据不存在结束位
                recvstr += str;
            else{//当前数据存在起始位
                str = str.Substring(0, str.IndexOf(_end);
                recvstr = recvstr + str;
                DoSomething(recvstr)//对一组串口数据进行其他处理
                recvstr = "";//清空数据
            }
            
        }
~~~

## 基本思路

### 串口通信基本原理
说先说明一下采集仪发送数据的方式。一组数据一般由一个`起始位`标识开始，由一个`结束位`标识结束，中间为实际数据字符。
我们以`S`表示起始位，`E`表示结束位，`D`表示有效数据，那么一组数据是这样的

`SDDDDDDDDDDDDDDE`

而且，一组数据一般不是一次完整发送过来的，而是分段发送, 如:

`SDDD`
`DDDD`
`DDDD`
`DDDE`

发送过来的数据会放在串口通信的`缓存区`里。

### 采集数据流程
1. 开始采集, `enablescan`由`false` 变为 `true`
2. 开启新线程，若检测到`enablescan`为`true`，则每个一段时间向采集仪发送采集信号
3. 采集仪向串口发送数据，将数据放入缓冲区
4. 串口接收到数据后触发`serialPort_DataRecived`事件，取走当前缓冲区的所有数据，进行处理（详细处理的方式见代码）
5. 数据处理完后，退出`serialPort_DataRecived`函数，等待事件的下一次触发
6. 停止采集，`enablescan`由`true` 变为 `false`
7. 发送数据的线程检测到`enablescan`为`false`，结束工作，销毁线程。


## 问题

在实际使用中，接受到的数据经常会缺失一部分，`DoSomething`时经常会抛出异常，造成了很大的困扰。

最开始的思路是用`try...catch`捕获异常，丢掉有问题的数据，但有时不赶巧，一组正常的数据都没有，而且这一问题出现的频率不低。
痛定思痛，决定重构这一祖传代码，真是`前人拉屎总不冲，后人难忍终清洁`。

# 重构

## 问题复盘

我们首先复盘一下问题发生的过程
正常的过程应该是这样的

|采集仪动作|接收事件|当前缓存区|str|recvstr|
|---|---|---|---|---|
|开始|待命中|null|null|null|
|发送数据|触发事件|SDDD|SDDD|SDDD|
|发送数据|-处理中-|DDDD|SDDD|SDDD|
|-发送间隔-|处理完成|DDDD|SDDD|SDDD|
|发送数据|触发事件|DDDDDDDE|DDDDDDDE|SDDDDDDDDDDE|
|开始休息|处理完成|null|null|null|

产生错误时:

|采集仪动作|接收事件|当前缓存区|str|recvstr|
|---|---|---|---|---|
|开始|待命中|null|null|null|
|发送数据|触发事件|SDDD|SDDD|SDDD|
|发送数据|-处理中-|DDDD|SDDD|SDDD|
|发送数据|-处理中-|DDDDDDDE|SDDD|SDDD|
|-待机-|处理完成|DDDDDDDE|SDDD|SDDD|
|-待机-|-待命中-|DDDDDDDE|SDDD|SDDD|
|发送数据|触发事件|DDDDDDDESDDD|SDDD|SDDDSDDD|

看，原本应该接收到`SDDDDDDDDDDESDDD...`，现在真正这组收到的是`SDDDSDDD...`，部分数据丢失。

对源代码进行修改太麻烦，故而选择直接重构该部分功能。

## 重构过程

### ReadTo函数

首先想到的是，难到不能读到一组完整的数据再进行处理吗？

其实是可以的。`C#`内置了`ReadTo`方法
[MSDN](https://docs.microsoft.com/zh-cn/dotnet/api/system.io.ports.serialport.readto?view=netframework-4.7.2)

一直读到结束位标识后，再这一组数据放到指定的参数中，底层肯定有一些细节，总而言之，可以保证每次读到一组完整的数据。

其用法为
~~~cs
    string endStr = ((char)13).ToString
    string targetStr = SerialPort.ReadTo("endStr");
~~~

### 多线程

`ReadTo`解决了数据读取的问题，然而当该方法在读取数据时，整个一直在等待，等读取成功后，再执行之后的操作，在这个等待过程中，
其他任何的触发事件都无法完成，呈现出的效果就是软件“卡住了”。

未解决这一问题，我们可以采用多线程的方法。一个线程专门负责读取数据，一个线程处理数据。
为了几个线程之间的通信，我们设计一个`池`
读到的数据不断放入`池`中，另一个线程不断从`池`中提取数据。除此之外，我们还要保证先放入池中的数据先被处理。

根据以上特点，我们自然而然的想到了一种`先入先出`的数据结构--[`队列`](https://baike.baidu.com/item/%E9%98%9F%E5%88%97/14580481?fr=aladdin)。

---
说句题外话，老有人说小学时的问题`一个池子，一边注水，一边放水`这种问题很傻，没有现实意义。。。其实现实中处处都有。
不一定是真实的`池`，也可以是抽象的`池`。
---

话不多说，上代码。

### 代码
~~~cs
private char _start; // 起始位标志
private char _end ;   // 结束位标志
private private Queue<string> _serialPortData; // 数据池

///<summary>
///向测试仪发送读取信号及接受测试仪发回数据的线程。根据之前所说ReadTo的性质，正好保证读完一组数据后，再发送指令让测试仪测试下一组数据
///<summary>
public void ReadDataThread() {
    _enableScan = true;
    Thread thread = new Thread(() => //新开线程，执行接收数据操作
    {
         while (_enableScan) //如果标识为true
        {
            Thread.Sleep(1);
            try {
                serialPort1.WriteLine(":READ?");
                Thread.Sleep(10);
                if (serialPort1.BytesToRead != 0) _serialPortData.Enqueue(serialPort1.ReadTo(_end));//将读到的数据放入池中
                Thread.Sleep(100);
            }
            catch (Exception ex) {//其他的改进
                HandleException(ex);//加上异常处理，是系统更稳健
                Log.Error(ex);//打logger，记录异常原因，为修改bug提供依据
            }
        }
    });
    thread.Start(); //启动线程
    thread.IsBackground = true;//线程在后台运行
}

public void SolveDataThread(){
    Thread thread = new Thread(() => //新开线程，执行接收数据操作
    {
        while (_enableScan) //如果标识为true
        {
            if (_serialPortData.Count == 0)continue; 
            try{
                string str = _serialPortData.Dequeue();//从池中读取数据
                DoSomething(str);
                thread.Sleep(100);
            }
            catch (Exception ex) {//其他的改进
                HandleException(ex);//加上异常处理，是系统更稳健
                Log.Error(ex);//打logger，记录异常原因，为修改bug提供依据
            }
        }
}


~~~
信息说明都在代码注释里。