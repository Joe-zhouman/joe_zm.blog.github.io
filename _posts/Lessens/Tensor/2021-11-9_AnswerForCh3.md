---
layout: blog
istop : true
book : true
title: 张量分析第三章习题解答（个人）
category: knowledge
tags: 数学 张量分析
background-image: math.jpg
date: 2021-11-9 20:06:23 + 0800
---

# 3.1
## 题目
已知：$\mathbf{v}$为矢量。$f = e^{\mathbf{v}^2}$
## 解
$$f = e^{(Q\cdot v)\cdot(Q\cdot v)} = e^{(v\cdot Q^T)\cdot(Q\cdot v)} = f$$

# 3.1
## 题目 
T为二阶张量，求
1. 在某一特定笛卡尔坐标系中$f = \sum\sum(T_{ij})^2$
2. $f=T^T:T$

## 解

1. 2
2. $f=T^{T}: T=T_{\cdot j}^{i} g_j g_{i}: T_{\cdot l}^{k} g_{k} g^{l}=T_{\cdot j}^{i} T_{\cdot l}^{k} g^{j k }g_{i l}=T_{\cdot j} T_{\cdot i}^{j}=\mathscr{f}_{2}^{*}$
