---
layout: code
istop : true
book : true
title: 经典气体的配分函数
category: code
tags: 统计力学 经典气体
background-image: StatisticalMechanics.jpg
date: 2021-12-2 14:44:58 + 0800
---
经典气体的配分函数 <!-- more -->

# 硬圆球结构

> 在粒子直径为 $\sigma$ 的硬球所组成的经典气体中, 
> 粒子的空间分布 $E$ 不再是无关联的. 粗略地说, 在该系统里由于 $N$ 个粒子的存在, 
> 仅仅剩下可 供第 $\left(N^{\prime}+1\right)$ 个粒子占据的体积为 $\left(V-N^{\prime} v_{0}\right)$. 
> 显然, $v_{0}$ 将正比于 $\sigma^{3}$. 假设 $N v_{0} \ll V$。 


$$
\Omega \propto V\left(V-\mathrm{v}_{0}\right)\left(V-2 \mathrm{v}_{0}\right) \ldots\left(V-\overline{N-1} \mathrm{v}_{0}\right)
$$

$$
\ln \boldsymbol{\Omega}=C+\sum_{j=0}^{N-1}\ln(V-jv_0)=C+N\ln V+\sum_{j=0}^{N-1}\ln(1-j\frac{v_0}{V})
$$

$Nv_0\ll V$，则

$$\ln(1-j\frac{v_0}{V})\simeq-j\frac{v_0}{V}$$

$$\ln \boldsymbol{\Omega}=C+N\ln V-\sum_{j=0}^{N-1}j\frac{v_0}{V}\simeq C+N\ln V-\frac{N^2v_0}{V}$$

$$
\frac{\partial \Omega}{\partial V}=\frac{N}{V}+\frac{N^2v_0}{V^2}=\frac{P}{kT}
$$

$$
P V\left(1+\frac{N{v}_{0}}{2 V}\right)^{-1}=N k T
$$

再次使用近似

$$\left(1+\frac{N{v}_{0}}{2 V}\right)^{-1}\simeq -\frac{N{v}_{0}}{2 V}$$

则

$$b = \frac12 Nv_0$$

考虑以下的情形: 当空间存在一个硬球，则另一个球的质心不可能存在于以该圆球质心为球心，圆球直径为半径的球内，
故而分子的实际占用空间

$$v_0=4v_m$$

$v_m$为分子的体积

$$P(V-b)=kNT=nRT$$
