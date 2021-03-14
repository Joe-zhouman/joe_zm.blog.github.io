---
layout: blog
istop : true
book : true
title: 态密度（PDOS）曲线和声子色散曲线（PDC）的联系
category: knowledge
tags: 分子动力学
background-image: graphene.jpg
date: 2021-3-4 19:02:42 + 0800
---
态密度（PDOS）曲线和声子色散曲线（PDC）之间是相互关联的，这里讲讲他们的关联性<!-- more -->

# 态密度（PDOS）曲线

我们通常会使用归一化之后的PDOS，及PDOS曲线与坐标轴围成的图形面积为1，这样一来，PDOS就可看做一个
[概率密度函数](https://baike.baidu.com/item/%E6%A6%82%E7%8E%87%E5%AF%86%E5%BA%A6%E5%87%BD%E6%95%B0/5021996?fr=aladdin)。
这个概率可以理解为体系内声子的分布概率（宏观角度），也可以理解为声子处于某种状态的概率（量子力学角度）。

# 声子色散曲线（PDC）
色散关系其实就是频率与波失的关系函数，对于一个晶胞内含有N个独特原子的体系，其色散关系曲线一个有3N个分支，其中3个光学枝，3(N-1)个声学支。

色散关系一个重要的应用是用来得到群速度 $v_g = d\omega/dK$，及色散曲线的斜率。

# PDOS与PDC的关系

![]({{site.url}}/figures/MD/PdosAndPdc/pdc.png)
以上为六方氮化硼的声子色散曲线，曲线上的每一个点都代表一种声子模，统计一下以上点的概率分布，与PDOS相比较，可以看到，两者的形状神相似。
理论上，如果体系足够大，声子模足够多，这两个曲线应该是重合的。
![]({{site.url}}/figures/MD/PdosAndPdc/PdosAndPdc.png)
