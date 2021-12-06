---
layout: code
istop : true
book : true
title: 统计力学与热力学
category: code
tags: 统计力学
background-image: StatisticalMechanics.jpg
date: 2021-12-02 13:42:12 + 0800
---
统计力学与热力学，配分函数等的简单关系 <!-- more -->

# 前言

# 宏观态与微观态

> **热力学极限** $N\rightarrow \infty$, $V\rightarrow \infty$, $N/V=n$

> * **广延量** 正比于系统大小($N, V$)
> * **强度量** 与系统大小无关

系统的能量为所有分子能量的总和

$$
E=\sum_{i} n_{i} \varepsilon_{i}
$$

同时
$$
N=\sum_{i} n_{i}
$$

给定N, V, E，可以完全确定一个系统的**宏观态**。但此时系统的微观状态有许多种。

> 等先验几率(equal a priori probabilities)：系统处在每一种微观态的可能性是均等的

> when there are no other constraints, that at
> any time t the system is equally likely to be in any one of these microstates.

微观态的数目与宏观参量相关，记为
$$\Omega(N, V, E)$$

# 热力学和统计力学

![处于热接触的两个物理系统](https://i.loli.net/2021/12/01/cgywhnUpYoibBVS.png)

$V_1, V_2; N_1, N_2$不变，粒子分别处于$\Omega_1(E_1)$, $\Omega_2(E_2)$决定的微观态中。

同时有

$$
E^{(0)}=E_{1}+E_{2}=Const, 
$$

复合系统等概率的处于$\Omega^{(0)}\left(E_{1}, E_{2}\right)$的微观态中。

$$
\Omega_{1}\left(E_{1}\right) \Omega_{2}\left(E_{2}\right)=\Omega_{1}\left(E_{1}\right) \Omega_{2}\left(E^{(0)}-E_{1}\right)=\Omega^{(0)}\left(E^{(0)}, E_{1}\right)
$$

> a physical system, left to itself, 
> proceeds naturally in a direction that enables it to assume an ever-increasing number
> of microstates until it finally settles down in a macrostate that affords the **largest possible number** of microstates.

> 一个物理系统，如果听其自然，它将沿着使其配容数不断增加的方向进行，
> 直到最后处于配容数达到可能的**最大值**的状态。

> 对于一个典型的系统，即使稍微偏离最可几状态的任一状态，
> 其配容数也比最可几状态的配容数要小“若于个数量级”.
> 因此，一个系统的**最可几状态**就是系统在其中渡过它**绝大部分时间**的那个状态。
> 于是我们把最可几状态视为该系统的**平衡态**那就很自然了

## 温度

$\Omega^{(0)}\left(E^{(0)}, E_{1}\right)$取最大值，此时$E_1, E_2$取$\bar{E_1}, \bar{E_2}$，则

$$
\left.\frac{d\Omega^{0}}{dE_1}\right|_{(\bar{E_1}, \bar{E_2})}=0
$$

即

$$
\left(\frac{\partial \Omega_{1}\left(E_{1}\right)}{\partial E_{1}}\right)_{E_{1}=\bar{E}_{1}} \Omega_{2}\left(\bar{E}_{2}\right)+\Omega_{1}\left(\bar{E}_{1}\right)\left(\frac{\partial \Omega_{2}\left(E_{2}\right)}{\partial E_{2}}\right)_{E_{2}=\bar{E}_{2}} \cdot \frac{\partial E_{2}}{\partial E_{1}}=0
$$

而$\partial E_1/\partial E_2 = -1$（总能量不变）

$$
\left(\frac{\partial \ln \Omega_{1}\left(E_{1}\right)}{\partial E_{1}}\right)_{E_{1}=\bar{E}_{1}}=\left(\frac{\partial \ln \Omega_{2}\left(E_{2}\right)}{\partial E_{2}}\right)_{E_{2}=\bar{E}_{2}}
$$

令

$$
\beta \equiv\left(\frac{\partial \ln \Omega(N, V, E)}{\partial E}\right)_{N, V, E=\bar{E}}
$$

则平衡条件变为：

$$\beta_1=\beta_2$$

联系宏观表象，一定有

$$T = f(\beta)$$

## 熵

$$
\left(\frac{\partial S}{\partial E}\right)_{N, V}=\frac{1}{T}
$$

$$
\frac{\partial S}{\partial(\ln \Omega)}=\left(\frac{\partial S}{\partial E}\right)
\left(\frac{\partial \ln \Omega}{\partial E}\right)=\frac{1}{\beta T}=\text { const }
$$

故而有

$$
S=k \ln \Omega, \beta = \frac{1}{kT}
$$

> 式中不带任何附加的常数$S_0$。于是，熵为零对应于一个特殊状态:
> 仅有一个微观态是可能的（=1）—所谓的“唯一位形”；
> 从而，统计方法也为热力学第三定律提供了一个理论基础

> 一个系统的嫡是关 于系统中的所谓无序度的一种量度. 
> 这种无序度是该系统所能具有 的大量配容数的一种表现. 
> 配容的选择性越大, 系统中可测程度 或有序度就越小. 
> 当 (而且只有当) 系统除了处于一个唯一状态 $(\Omega=1)$ 之外别无其他选择时, 
> 系统才能达到完全有序; 这也就对 应于樀变为零的状态.

## 配分函数和其他热力学量

若系统的体积也可变化，但仍有$V^{(0)}=V_1+V_2$，配分数取最大值，则有:

$$\frac{\partial \Omega^{(0)}}{\partial E_1}=0$$

$$\frac{\partial \Omega^{(0)}}{\partial V_1}=0$$

按以上做同样的处理：

$$
\left(\frac{\partial \ln \Omega_{1}}{\partial E_{1}}\right)_{N_{1}, V_{1} ; E_{1}=\bar{E}_{1}}=\left(\frac{\partial \ln \Omega_{2}}{\partial E_{2}}\right)_{N_{2}, V_{2} ; E_{2}=\bar{E}_{2}}
$$

$$
\left(\frac{\partial \ln \Omega_{1}}{\partial V_{1}}\right)_{N_{1}, E_{1} ; V_{1}=\bar{V}_{1}}=\left(\frac{\partial \ln \Omega_{2}}{\partial V_{2}}\right)_{N_{2}, E_{2} ; V_{2}=\bar{V}_{2}} .
$$

$$
\eta \equiv\left(\frac{\partial \ln \Omega(N, V, E)}{\partial V}\right)_{N, E, V=\bar{V}}
$$

同理有

$$
\zeta \equiv\left(\frac{\partial \ln \Omega(N, V, E)}{\partial N}\right)_{V, E, N=\bar{N}}
$$

$$
d(\ln \Omega)=\beta d E+\eta d V+\xi d N
$$

$$
d E=T d S-(\eta k T) d V-(\zeta k T) d N
$$

而

$$
d E=T d S-P d V+\mu d N
$$

故

$$
\eta=\frac{P}{k T} \quad , \quad \zeta=-\frac{\mu}{k T}
$$



# 习题

## Q1

> 试证明: 对于热接触的两个大系统, 1.2 节中的数 $\Omega^{(0)}\left(E^{(0)}\right.$, $E_{1}$ ) 可以表示成变是 $E_{1}$ 的高斯函數. 
> 试通过与该问题有关的其他量, 确定 $E_{1}$ 和平均值 $\bar{E}_{1}$ 的方均根偏差的表示式。对于理想气体，其显式形式

将$\Omega^{(0)}$按$E_1-\bar{E_1}$展开:

$$
\begin{aligned}
\ln \boldsymbol{\Omega}^{(0)}\left(E_{1}\right) \equiv &\ln \boldsymbol{\Omega}_{1}\left(E_{1}\right)+\ln \boldsymbol{\Omega}_{2}\left(E_{2}\right)  \\
=&\left\{\ln \boldsymbol{\Omega}_{1}\left(\bar{E}_{1}\right)+\ln \boldsymbol{\Omega}_{2}\left(\bar{E}_{2}\right)\right\}+\\
&\left\{\frac{\partial \ln \boldsymbol{\Omega}_{1}\left(E_{1}\right)}{\partial E_{1}}+\frac{\partial \ln \boldsymbol{\Omega}_{2}\left(E_{2}\right)}{\partial E_{2}} \frac{\partial E_{2}}{\partial E_{1}}\right\}_{E_{1}=\bar{E}_{1}}\left(E_{1}-\bar{E}_{1}\right)+\\
& \frac{1}{2}\left\{\frac{\partial^{2} \ln \boldsymbol{\Omega}_{1}\left(E_{1}\right)}{\partial E_{1}^{2}}+\frac{\partial^{2} \ln \boldsymbol{\Omega}_{2}\left(E_{2}\right)}{\partial E_{2}^{2}}\left(\frac{\partial E_{2}}{\partial E_{1}}\right)^{2}\right\}_{E_{1}=\bar{E}_{1}}\left(E_{1}-\bar{E}_{1}\right)^{2}+\cdots .
\end{aligned}
$$

第一项为常数记为$\ln C$，第二项为0，考虑第三项，利用$\partial E_1/\partial E_2 = -1$和$\beta$的定义，写作

$$
\frac{1}{2}\left\{\frac{\partial \beta_{1}}{\partial E_{1}}+\frac{\partial \beta_{2}}{\partial E_{2}}\right\}_{e q .}\left(E_{1}-\bar{E}_{1}\right)^{2}=-\frac{1}{2}\left\{\frac{1}{k T_{1}^{2}\left(C_{\mathrm{v}}\right)_{1}}+\frac{1}{k T_{2}^{2}\left(C_{\mathrm{v}}\right)_{2}}\right\}\left(E_{1}-\bar{E}_{1}\right)^{2}
$$

等号用到了

$$\frac{\partial \beta}{\partial E}=\frac{\partial T}{\partial E}\frac{d \beta}{d T}$$

而$T_1=T_2$.

故

$$
{\Omega}^{(0)}= C\exp{\left[-\frac{(E_1-\bar{E_1})^2}{2kT^2C_{v1}C_{v2}/(C_{v1}+C_{v2})}\right]}
$$

显然是一个高斯分布。

$$\sigma=T\sqrt{\frac{kC_{v1}C_{v2}}{C_{v1}+C_{v2}}}$$

对于理想气体:

$$C_v=\frac32 Nk$$

$$\sigma=kT\sqrt{\frac{N_1N_2}{N_1+N_2}}$$

## Q2

> 把成分相同的两个系统 $A$ 和 $B$ 敗在一起, 允许其能量和粒子相互 交换, 而体积 $V_{A}$ 和 $V_{B}$ 保持不变. 
> 证明:  $\left(d E_{A} / d N_{A}\right)$ 的最小值由下式决定：
> $$\frac{\mu_{A} T_{B}-\mu_{B} T_{A}}{T_{B}-T_{A}}$$

体积保持不变，则$dV=0$

$$ dE_A = T_AdS_A+\mu_AdN_A$$

$$ dE_B = T_BdS_B+\mu_BdN_B$$

而同时有$dE_A = -dE_B$，$dN_A=-dN_B$。

交换过程要求

$$dS_A+dS_B\ge 0$$

可得

$$\frac{dE_A}{dN_A}\ge\frac{\mu_{A} T_{B}-\mu_{B} T_{A}}{T_{B}-T_{A}}$$

