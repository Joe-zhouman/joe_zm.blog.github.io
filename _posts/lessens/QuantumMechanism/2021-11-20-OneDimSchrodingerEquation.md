layout: code
istop : true
book : true
title: 一维定态薛定谔方程波函数的性质
category: knowledge
tags: 量子力学 matlab
background-image: quantum.jpg
date: 2021-3-9 17:54:39 + 0800

一维定态薛定谔方程解的一些性质 <!-- more -->

# 束缚态与游离态

* **归一化条件**
  $\int_R\psi^*\psi dV < +\infty$
  * **推论** $\lim\limits_{x\rightarrow\infty}\psi(x)=0$
* **束缚态** 可归一化
* **游离态** 不可归一化

# 一维定态方程的解

> $\psi_1$,$\psi_2$ 为能量本征值为$E$的解，则$\psi_{1} \psi_{2}^{\prime}-\psi_{2} \psi_{1}^{\prime}=C$

$\psi_{1}^{\prime \prime}+\frac{2 m}{\hbar^{2}}[E-V(x)] \psi_{1}=0$
$\psi_{2}^{\prime \prime}+\frac{2 m}{\hbar^{2}}[E-V(x)] \psi_{2}=0$
$\psi_{1} \psi_{2}^{\prime \prime}-\psi_{2} \psi_{1}^{\prime \prime}=0$
$\left(\psi_{1} \psi_{2}^{\prime}-\psi_{2} \psi_{1}^{\prime}\right)^{\prime}=0$
积分后可得上式。

# 一维方程最多二重简并

> 一维方程，每个能级最多有两个简并态。

$\psi_{1} \psi_{2}^{\prime}-\psi_{2} \psi_{1}^{\prime}=C_{1}$
$\psi_{1} \psi_{3}^{\prime}-\psi_{3} \psi_{1}^{\prime}=C_{2}$
$\psi_{1}\left(C_{2} \psi_{2}^{\prime}-C_{1} \psi_{3}^{\prime}\right)-\left(C_{2} \psi_{2}-C_{1} \psi_{3}\right) \psi_{1}^{\prime}=0$
$\varphi=C_{2} \psi_{2}-C_{1} \psi_{3}$
$\psi_{1} \varphi^{\prime}-\varphi \psi_{1}^{\prime}=0$
$\psi_{1}^{2}\left(\frac{\varphi}{\psi_{1}}\right)^{\prime}=0, \quad$ 或 $\quad \varphi^{2}\left(\frac{\psi_{1}}{\varphi}\right)^{\prime}=0$
$\left(\frac{\varphi}{\psi_{1}}\right)^{\prime}=0, \quad \varphi=C \psi_{1}$
$C \psi_{1}=C_{2} \psi_{2}-C_{3} \psi_{3}$

# 一维规则势场束缚态无简并

对束缚态 $\lim\limits_{x\rightarrow\infty}(\psi_{1}\psi_{2}^{\prime}-\psi_{2} \psi_{1}^{\prime})=0$
由上一部分的结论，在全空间，有$\psi_{1} \psi_{2}^{\prime}=\psi_{2} \psi_{1}^{\prime}$
在$\psi_1$,$\psi_2$ 不为0的区域，有

$$
\frac{\psi_{1}^{\prime}}{\psi_{1}}=\frac{\psi_{2}^{\prime}}{\psi_{2}}

$$

$$
\psi_{1}(x)=C \psi_{2}(x)

$$

# 波函数的连续性

> $|V(x)|\lt\infty$，则$\psi(x)$,$\psi^{\prime}(x)$连续;
> $V(x)\rightarrow\infty$,$\psi(x)\rightarrow 0$,$\psi^\prime(x)$可能不连续；
> $V(x)\rightarrow-\infty$,可能有$\psi(x)\rightarrow \infty$,$\psi^\prime(x)$可能不连续；

$$
\frac{2 m}{\hbar^{2}}\left(E_{2}-E_{1}\right) \int_{-\infty}^{+\infty} \psi_{1} \psi_{2} \mathrm{~d} x 
=\int_{-\infty}^{+\infty} \frac{\mathrm{d}}{\mathrm{d} x}\left(\psi_{2} \psi_{1}^{\prime}-\psi_{1} \psi_{2}^{\prime}\right) 
\mathrm{d} x =\left.\left(\psi_{2} \psi_{1}^{\prime}-\psi_{1} \psi_{2}^{\prime}\right)\right|_{-\infty} ^{+\infty}=0

$$

# 波函数的宇称

> 若$V(x)$为偶宇称，则每个波函数都有明确的宇称性。

# 束缚态的波函数的正交性

> $V(x)$无奇点，则不同能级的本征函数相互正交

$$
\int_{-\infty}^{\infty} \psi_{n}(x) \psi_{m}(x) \mathrm{d} x=C\delta_{nm}

$$

$$
\psi_{1}^{\prime \prime}=\frac{2 m}{\hbar^{2}}\left[V(x)-E_{1}\right] \psi_{1}

$$

$$
\psi_{2}^{\prime \prime}=\frac{2 m}{\hbar^{2}}\left[V(x)-E_{2}\right] \psi_{2}

$$

$$
\frac{2 m}{\hbar^{2}}\left(E_{2}-E_{1}\right) \psi_{1} \psi_{2}=\psi_{2} \psi_{1}^{\prime \prime}-\psi_{1}
 \psi_{2}^{\prime \prime}=\frac{\mathrm{d}}{\mathrm{d} x}\left(\psi_{2} \psi_{1}^{\prime}-\psi_{1} \psi_{2}^{\prime}\right)

$$

$$
\frac{2 m}{\hbar^{2}}\left(E_{2}-E_{1}\right) \int_{-\infty}^{+\infty} \psi_{1} \psi_{2} \mathrm{~d} x 
\mathrm{d} x =\left.\left(\psi_{2} \psi_{1}^{\prime}-\psi_{1} \psi_{2}^{\prime}\right)\right|_{-\infty} ^{+\infty}=0

$$

# 束缚态波函数的奇点

> 束缚态基态波函数在有限处无奇点

> 束缚态基态波函数无简并（与之前的相关结论比较，这里对势场没有要求）

若有简并，$\psi_1$,$\psi_2$,则$c_1 \psi_{1}+c_2 \psi_{2}$也是一个本征函数。可以通过改变常数项使其等于0。
故而假设不成立。

> 推论：束缚态非基态波函数有根

若$\psi_n=0$无根，由上面的结论，

$$
\int_{-\infty}^{+\infty} \psi_{n} \psi_{0}=0

$$

$\psi_0>0 or \psi_0<0$ 恒成立，则基态波函数$\psi_0\equiv 0$显然不可能。推论得证。

> 推论：束缚态非基态波函数无一阶以上的奇点

若$\psi_n=0$有两级以上的零点,设其为$a$，即$\psi_n(a)=0$,$\psi_n^{\prime}(a)=0$,不妨取一点b，在$(a,b)$
上有$\psi_n>0 or \psi_n<0$。对该区间积分

$$
\frac{2 m}{\hbar^{2}}\left(E_{n}-E_{0}\right) \int_{a}^{b} \psi_{n} \psi_{0} \mathrm{~d} x
=\int_{a}^{b} \frac{\mathrm{d}}{\mathrm{d} x}\left(\psi_{0} \psi_{n}^{\prime}-\psi_{0} \psi_{n}^{\prime}\right)
\mathrm{d} x =\left.\left(\psi_{n} \psi_{0}^{\prime}-\psi_{0} \psi_{n}^{\prime}\right)\right|_{a} ^{b}=0

$$

同之前的证明由这一假设不成立。故推论得证。

> 第n+1个能级的波函数有n个奇点
