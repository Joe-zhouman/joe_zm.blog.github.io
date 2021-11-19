---
layout: blog
istop : true
book : true
title: 泛函分析笔记（一）距离空间
category: knowledge
tags: 数学 泛函分析
background-image: math.jpg
date: 2021-9-25 08:45:38 + 0800
---

常用的距离空间及其距离 <!-- more -->
# 距离空间定义

> $$X\ne \emptyset, \forall x,y \in X,\exists \rho (x,y),$$满足
> * 非负性：$$\rho(x,y)\le 0,\rho(x,t)=0 \Leftrightarrow x=y$$
> * 对称性: $$\rho(x,y)=\rho(y,x)$$
> * 三角不等式:$$\forall z\in X, \rho(x,y)\le \rho(x,z)+\rho(z,y)$$
> 则X为**距离空间**，$$\rho$$为X的一个**距离**，记作$$(X,\rho)$$

# 常用距离空间
## n维欧式空间$$R^n(C^n)$$
### 定义
$$R^n=\{x|x=(\xi_1,...,\xi_n),\xi_i\in R,i=1,...,n\}$$

### 距离
$$\rho(x,y)=\left(\sum\limits_{k=1}^n|\xi_k-\eta_k|^2\right)^{1/2}$$
$$\rho(x,y)=\max\limits_{1\le k\le n}|\xi_k-\eta_k|$$

### 证明
$$\sum\limits_{k=1}^n(a_k+b_k)^2=\sum\limits_{k=1}^na_k^2+2\sum\limits_{k=1}^n
 a_kb_k+\sum\limits_{k=1}^nb_k^2$$

$$\qquad\qquad\qquad\le\sum\limits_{k=1}^na_k^2+2(\sum\limits_{k=1}^na_k^2
+\sum\limits_{k=1}^n b_k^2)^{1/2}+\sum\limits_{k=1}^nb_k^2 (柯西不等式)$$

$$\qquad\qquad\qquad=\left[\left(\sum\limits_{k=1}^na_k^2\right)^{1/2}
+\left(\sum\limits_{k=1}^nb_k^2\right)^{1/2}\right]^2$$


## $$C[a,b]$$
### 定义
$$C[a,b]\{x|t\in [a,b],f(t)\in R,f(t)连续\}$$ 

### 距离
$$\rho(x,y)=\max\limits_{a\le t\le b}|x(t)-y(t)|$$ 

## $$L^p(F)$$
## $$L^\infty(F)$$
### 定义
### 距离
## $$l^p(F)$$
## $$l^\infty(F)$$