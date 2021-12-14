---
layout: code
istop : true
book : true
title: 能量均分定理及位力定理
category: knowledge
tags: 统计力学
background-image: StatisticalMechanics.jpg
date: 2021-12-5 00:16:59 + 0800
---
能量均分定理及位力定理 <!-- more -->
# 能量均分定理

$x_i,x_j$为$6N$个相空间坐标中的

$$
\left\langle x_{i} \frac{\partial H}{\partial x_{j}}\right\rangle=\frac{\int\left(x_{i} \frac{\partial H}{\partial x_{j}}\right) e^{-\beta H} d \omega}{\int e^{-\beta H} d \omega} \quad\left(d \omega=d^{3 N} q d^{3 N} p\right)
$$

对其中一个坐标$x_j$积分，上面的分子变为

$$
\int\left[-\left.\frac{1}{\beta} x_{i} e^{-\beta H}\right|_{\left(x_{j}\right)_{1}} ^{\left(x_{j}\right)_{2}}+\frac{1}{\beta} \int\left(\frac{\partial x_{i}}{\partial x_{j}}\right) e^{-\beta H} d x_{j}\right] d \omega_{(j)} ;
$$

$d\omega(j)$表示对除$x_j$以外的坐标求积分。$(x_j)_\alpha$表示$x_j$坐标的极值。
当其取极值时，哈密顿量为无穷大，故第一项为0。

> 我们者到, 倘若 $x_{j}$ 是一个空间坐标, 则它的极值将对应于 “在容器壁上的位置", 
> 因此, 此时系统的势能将变为无限大. 另一方面, 如果 $x_{j}$ 是一个动量坐标, 
> 则其极值本身将为 $\pm \infty$, 在这种情况下系统的动能将变为无限大.

${\partial x_{i}}/{\partial x_{j}}=\delta_{ij}$,

$$
\left\langle x_{i} \frac{\partial H}{\partial x_{j}}\right\rangle=\delta_{i j} k T
$$

$$
\left\langle p_{i} \frac{\partial H}{\partial p_{i}}\right\rangle \equiv\left\langle p_{i} \dot{q}_{i}\right\rangle=k T
$$

$$
\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle \equiv-\left\langle q_{i} \dot{p}_{i}\right\rangle=k T
$$

很多系统的哈密顿量是一个二次型，可以将其化为标准形式

$$
H=\sum_{j} A_{j} P_{j}^{2}+\sum_{j} B_{j} Q_{j}^{2}
$$

$$
\sum_{j}\left(P_{j} \frac{\partial H}{\partial P_{j}}+Q_{j} \frac{\partial H}{\partial Q_{j}}\right)=2 H
$$

$$
\langle H\rangle=\frac{1}{2} f k T,
$$

$f$为哈密顿量里的平方项个数

# 位力定理

系统的`Virial`：

$$\mathscr{V}=\left\langle\sum_{i} q_{i} \dot{p}_{i}\right\rangle$$

即各个粒子的坐标及作用在上面的作用力的乘积的期望。

$$
\mathscr{V}=-3 N k
$$

例如气体对壁面的压力的位力

$$
\mathcal{V}_{0}=\left(\sum_{i} q_{i} F_{i}\right)_{0}=-P \oint_{S} r \cdot d S
$$

$$
\mathcal{V}_{0}=-P \int_{V}(\operatorname{div} \boldsymbol{r}) d V=-3 P V
$$

则$PV=NkT$