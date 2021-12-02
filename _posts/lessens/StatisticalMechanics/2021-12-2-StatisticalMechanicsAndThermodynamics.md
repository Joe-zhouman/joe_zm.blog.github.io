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

## 理想气体
对于理想气体，每个分子均看做质点，则

$$
\Omega(N, E, V) \propto V^{N}
$$

$$
\frac{P}{T} \equiv k\left(\frac{\partial \ln \Omega(N, E, V)}{\partial V}\right)_{N, E}=k \frac{N}{V}
$$

$$ PV = nkT$$

> 关于气体分子不在可以视作质点时的推导参见[经典气体](https://www.joezhouman.com/2021/12/02/ClassiclGases.html)

在边长为L的方箱内，粒子的波函数接近于三维的无限深势阱，对应的能量本征值为

$$
\varepsilon\left(n_{x}, n_{y}, n_{z}\right)=\frac{h^{2}}{8 m L^{2}}\left(n_{x}^{2}+n_{y}^{2}+n_{z}^{2}\right) ; \quad n_{x}, n_{y}, n_{z}=1, 2, 3, \ldots
$$

$\Omega(N, V, E)$为以下方程正整数解的个数：

$$
\sum_{r=1}^{3 N} n_{r}^{2}=\frac{8 m V^{2 / 3} E}{h^{2}}=E^{*}
$$

故而

$$
S(N, V, E) \equiv S\left(N, V^{2 / 3} E\right)
$$

绝热过程，N和S不变，则

 $$V^{2 / 3} E=Const$$

$\Omega(N, V, E)$, 或更确切地说, 
$\Omega_{N}(E^{\star})$, 就等于处在半径为 
$\sqrt{E^{\star}}$ 的 
$3 N$ 维球面上正整数的阵点数。

$\Sigma_{N}(E^{\star})$ 
定义为处于半径为 $\sqrt{E^{\star}}$ 的 
$3 N$ 维球面内的正整数阵点数，则

$$
\Sigma(N, V, E)=\sum_{E^{\prime} \leq E} \Omega\left(N, V, E^{\prime}\right)
$$

$$
\lim _{\varepsilon^{*} \rightarrow \infty} \frac{\Sigma_{1}\left(\varepsilon^{*}\right)}{(\pi / 6) \varepsilon^{* 3 / 2}}=1
$$

去除含0坐标的点

$$
\Sigma_{1}\left(\varepsilon^{*}\right) \approx \frac{\pi}{6} \varepsilon^{* 3 / 2}-\frac{3 \pi}{8} \varepsilon^{*}
$$

加上所有含0坐标点

$$
\Sigma_{1}^{\prime}\left(\varepsilon^{*}\right) \approx \frac{\pi}{6} \varepsilon^{* 3 / 2}+\frac{3 \pi}{8} \varepsilon^{*}
$$

![20211201210813.png](https://i.loli.net/2021/12/01/YGCBL7x6erDK5Vz.png)

$$
\Sigma(N, V, E) \approx\left(\frac{V}{h^{3}}\right)^{N} \frac{(2 \pi m E)^{3 N / 2}}{(3 N / 2) !}
$$

由[斯特林公式](https://baike.baidu.com/item/%E6%96%AF%E7%89%B9%E6%9E%97%E5%85%AC%E5%BC%8F/9583086?fr=aladdin)

$$
\ln (n !) \approx n \ln n-n \quad(n \gg 1)
$$

故

$$
\ln \Sigma(N, V, E) \approx N \ln \left[\frac{V}{h^{3}}\left(\frac{4 \pi m E}{3 N}\right)^{3 / 2}\right]+\frac{3}{2} N
$$

根据不确定度原理，及测量误差的影响，我们难以获得精确处于$E$的能量态，而是位于$E-\Delta/2$
和$E+\Delta/2$之间的态。并有$\Delta \ll E$，则这一范围内的微观态有:

$$
\Gamma(N, V, E ; \Delta) \simeq \frac{\partial \Sigma(N, V, E)}{\partial E} \Delta \approx \frac{3 N}{2} \frac{\Delta}{E} \Sigma(N, V, E), 
$$

$$
\ln \Gamma(N, V, E ; \Delta) \approx N \ln \left[\frac{V}{h^{3}}\left(\frac{4 \pi m E}{3 N}\right)^{3 / 2}\right]+\frac{3}{2} N+\left\{\ln \left(\frac{3 N}{2}\right)+\ln \left(\frac{\Delta}{E}\right)\right\}
$$

而现在有$N\gg 1$，$\Delta \ll E$，故而大括号内的项可以忽略不计。

$$
\ln \Gamma \approx \ln \Sigma \approx N \ln \left[\frac{V}{h^{3}}\left(\frac{4 \pi m E}{3 N}\right)^{3 / 2}\right]+\frac{3}{2} N
$$

$E$的领域的配容数与从0到$E$的配容数的总和相差无几，故而对配容数影响的主要因素其实就是其领域内的配容数。

### 吉布斯佯谬

$$
S(N, V, E)=kln \Gamma=N k \ln \left[\frac{V}{h^{3}}\left(\frac{4 \pi m E}{3 N}\right)^{3 / 2}\right]+\frac{3}{2} N k
$$

以上公式中，$S$不是广延量。对配分函数除以$N!$，对于$S$来说，其减去$lnN!$。在根据斯特林公式，即可得到下式：

$$
\begin{aligned}
S(N, V, E) &=N k \ln \left[\frac{V}{N h^{3}}\left(\frac{4 \pi m E}{3 N}\right)^{3 / 2}\right]+\frac{5}{2} N k \\
&=N k \ln \left(\frac{V}{N}\right)+\frac{3}{2} N k\left\{\frac{5}{3}+\ln \left(\frac{2 \pi m k T}{h^{2}}\right)\right\}
\end{aligned}
$$

> 粒子全同且不可分辨。相当于**组合**而不是**排列**。故而相差一个因子:($N!/\Pi n_i!$)。除以$N!$在所有粒子能量都不相同是是完全正确的
> 但在其他情况有些问题，但在经典极限下正确度足够了。考虑更详细的因子，则进入量子统计物理的领域。

> 当$P(n_i>1)\rightarrow 0$时，这样方法越来越接近实际。可以通过充分高的温度及充分低的密度来实现这一情况。
> 故而统计力学的经典极限可表示为$\left<n\right>\ll 1$

### 物理量的推导

$$
T=\left(\frac{\partial E}{\partial S}\right)_{N, \nabla}=\frac{2}{3} \frac{E}{N k}
$$

$$
E=N\left(\frac{3}{2} k T\right)=n\left(\frac{3}{2} R T\right)
$$

$$
C_{V}=\left(\frac{\partial E}{\partial T}\right)_{N, V}=\frac{3}{2} N k=\frac{3}{2} n R
$$

$$
P=-\left(\frac{\partial E}{\partial V}\right)_{N, S}=\frac{2}{3} \frac{E}{V}
$$

$$
P=\frac{N k T}{V} \quad \text { or } \quad P V=n R T
$$

$$
C_{P}=\left(\frac{\partial(E+P V)}{\partial T}\right)_{N, P}=\frac{5}{2} n R
$$

$$
\gamma=C_{P} / C_{V}=\frac{5}{3}
$$

$$
\mu \equiv\left(\frac{\partial E}{\partial N}\right)_{V, S}=E\left[\frac{5}{3 N}-\frac{2 S}{3 N^{2} k}\right]
$$

$$
\mu=\frac{1}{N}[E+P V-T S] \equiv \frac{G}{N}
$$

$$
\mu(N, V, T)=k T \ln \left\{\frac{N}{V}\left(\frac{h^{2}}{2 \pi m k T}\right)^{3 / 2}\right\}
$$

$$
A=E-T S=G-P V=N k T\left[\ln \left\{\frac{N}{V}\left(\frac{h^{2}}{2 \pi m k T}\right)^{3 / 2}\right\}-1\right]
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

