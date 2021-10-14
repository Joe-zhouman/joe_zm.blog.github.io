---
layout: blog
istop : true
book : true
title: 泛函分析笔记（二）距离空间相关定理
category: knowledge
tags: 数学 泛函分析
background-image: math.jpg
date: 2021-10-9 20:30:08 + 0800
---
泛函分析距离空间的一些定理汇总 <!-- more -->

# 不等式

# 距离空间中的收敛

>$$ \forall \epsilon>0,\exists N>0, n>N \Rightarrow \rho(x_n,x_0)<\epsilon $$ 

* $$\{x_n\}收敛\Rightarrow$$
    1. $$\{x_n\}$$极限唯一 
    2. $$\forall y_0 \in X, {\rho(x_0,y_0)}有界$$ 

* $$\{x_n\} 是X中的收敛点列，则\{x_n\}\rightarrow x_0\Leftrightarrow 
\forall \{x_{k_n}\}\subset\{x_n\},\{x_{k_n}\}\rightarrow x_0$$

# 距离空间上的点集

> $$A为开集\Leftrightarrow A=A^o$$ 
> $$A为闭集\Leftrightarrow A=\bar{A}$$ 

* 距离空间X及空集为开集，也为闭集
* 任意个开集的交为开集，有限个闭集的交为闭集
* 有限个开集的并为开集，任意个闭集的并为闭集

* $$A,B\subset (X,\rho)\Rightarrow$$ 
  1.  $$A\subset \bar{A}$$ 
  2.  $$\overline{\overline{A}}=\bar{A}$$ 
  3.  $$\overline{A\cup B}=\bar{A}\cup \bar{B}$$ 
  4.  $$\bar{\emptyset}=\emptyset$$ 

* $$A为开集\Leftrightarrow A^c 为闭集$$ 
* $$A为闭集\Leftrightarrow A^c 为开集$$ 


## 稠密与可分
> B在A中**稠密**$$\Leftrightarrow$$ 
> $$A,B\subset X, A\subset \bar{B} \Leftrightarrow $$ 
> $$\forall x\in A,\forall \epsilon > 0,\exists y\in B,\rho(x,y),\epsilon \Leftrightarrow$$ 
> $$\forall \epsilon > 0, \bigcup_{x_0\in B}S(x_0,\epsilon)\supset A\Leftrightarrow$$ 
> $$\forall x\in A,\exists\{x_n\}\subset B,\{x_n\}\rightarrow x$$ 


> X存在可列稠子集$$\Leftrightarrow$$X**可分**

## 连续映射

>$$ T在x_0连续\Leftrightarrow$$ 
>$$ x_0\in X, \forall \epsilon>0,\exists \delta >0,\rho(x,x_0)<\delta
> \Rightarrow \rho_1(Tx,Tx_0)<\epsilon$$ 
> $$ \Leftrightarrow\forall \{x_n\}\in X \&\{x_n\}\rightarrow x_0 \Rightarrow \{Tx_n\}\rightarrow Tx_0$$ 


* $$T:X\rightarrow Y连续 \Leftrightarrow$$
  $$G\subset Y,T^{-1}(G)\subset X$$
  $$G为开集\Rightarrow T^{-1}(G) 为开集$$
  $$G为闭集\Rightarrow T^{-1}(G) 为闭集$$

* $$B = A^c\Leftrightarrow T^{-1}(B)=(T^{-1}(A))^c$$ 