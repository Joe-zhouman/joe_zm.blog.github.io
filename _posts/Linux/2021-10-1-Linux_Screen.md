---
layout: blog
istop : true
book : true
title: Linux中Screen命令的使用
category: knowledge
tags: Linux
background-image: Linux.jpg
date: 2021-10-1 10:57:01 + 0800
---

记录Linux中Sceen命令的使用方法，方便自己使用。<!-- more -->
# 基本用法
```shell
screen -S yourname -> 新建一个叫yourname的session
screen -ls         -> 列出当前所有的session
screen -r yourname -> 回到yourname这个session
screen -d yourname -> 远程detach某个session
screen -d -r yourname -> 结束当前session并回到yourname这个session
```
# 语法
```shell
$> screen [-AmRvx -ls -wipe][-d <作业名称>][-h <行数>][-r <作业名称>][-s ][-S <作业名称>]
```
 
* -A 　将所有的视窗都调整为目前终端机的大小。
* -d   <作业名称> 　将指定的screen作业离线。
* -h   <行数> 　指定视窗的缓冲区行数。
* -m 　即使目前已在作业中的screen作业，仍强制建立新的screen作业。
* -r   <作业名称> 　恢复离线的screen作业。
* -R 　先试图恢复离线的作业。若找不到离线的作业，即建立新的screen作业。
* -s 　指定建立新视窗时，所要执行的shell。
* -S   <作业名称> 　指定screen作业的名称。
* -v 　显示版本信息。
* -x 　恢复之前离线的screen作业。
* -ls或--list 　显示目前所有的screen作业。
* -wipe 　检查目前所有的screen作业，并删除已经无法使用的screen作业。


# 快捷键

* Ctrl+A ? -> 显示所有键绑定信息
* Ctrl+A c -> 创建一个新的运行shell的窗口并切换到该窗口
* Ctrl+A n -> Next，切换到下一个 window 
* Ctrl+A p -> Previous，切换到前一个 window 
* Ctrl+A 0..9 -> 切换到第 0..9 个 window
* Ctrl+A [Space] -> 由视窗0循序切换到视窗9
* Ctrl+A Ctrl+A -> 在两个最近使用的 window 间切换 
* Ctrl+A x -> 锁住当前的 window，需用用户密码解锁
* Ctrl+A d -> detach，暂时离开当前session，将目前的 screen session (可能含有多个 windows) 丢到后台执行，并会回到还没进 screen 时的状态，此时在 screen session 里，每个 window 内运行的 process (无论是前台/后台)都在继续执行，即使 logout 也不影响。 
* Ctrl+A z -> 把当前session放到后台执行，用 shell 的 fg 命令则可回去。
* Ctrl+A w -> 显示所有窗口列表
* Ctrl+A t -> time，显示当前时间，和系统的 load 
* Ctrl+A k -> kill window，强行关闭当前的 window
* Ctrl+A [ -> 进入 copy mode，在 copy mode 下可以回滚、搜索、复制就像用使用 vi 一样
* Ctrl+B Backward，PageUp 
* Ctrl+F Forward，PageDown 
* H(大写) High，将光标移至左上角 
* L Low，将光标移至左下角 
* 0 移到行首 
* $ 行末 
* w forward one word，以字为单位往前移 
* b backward one word，以字为单位往后移 
* Space 第一次按为标记区起点，第二次按为终点 
* Esc 结束 copy mode 
* Ctrl+A ] -> paste，把刚刚在 copy mode 选定的内容贴上

# 官方教程
[Screen User’s Manual](https://www.gnu.org/software/screen/manual/screen.html)