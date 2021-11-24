# 势阶
## 势能
$$
V(x)=\left\{\begin{array}{cl}
V_{0}, & x>0 \\
0, & x \le 0
\end{array}\right.
$$
## $E>V_0$

$$\sqrt{\frac{2 m E}{\hbar^{2}}} =k_{1} ,x\le0$$
$$\sqrt{\frac{2 m\left(E-V_{0}\right)}{\hbar^{2}}} =k_{2},x\gt0$$
$$\varphi_{\mathrm{I}}(x)=A_{1} \mathrm{e}^{\mathrm{i} k_{1} x}+A_{1}^{\prime} 
\mathrm{e}^{-\mathrm{i} k_{1} x},x\le0$$
$$\varphi_{\mathrm{II}}(x)=A_{2} \mathrm{e}^{\mathrm{i} k_{2} x}+A_{2}^{\prime}
 \mathrm{e}^{-\mathrm{i} k_{2} x},x\gt0$$
只考虑从无限远处射入的粒子，则$A_2^{\prime}=0$,则由波函数的连续性

$$\frac{A_{1}^{\prime}}{A_{1}}=\frac{k_{1}-k_{2}}{k_{1}+k_{2}}$$

$$\frac{A_{2}}{A_{1}}=\frac{2 k_{1}}{k_{1}+k_{2}}$$

* 透射率
$$R=\left|\frac{A_{1}^{\prime}}{A_{1}}\right|^{2}=
1-\frac{4 k_{1} k_{2}}{\left(k_{1}+k_{2}\right)^{2}}$$

* 反射率
$$T=\frac{k_{2}}{k_{1}}\left|\frac{A_{2}}{A_{1}}\right|^{2}
T=\frac{4 k_{1} k_{2}}{\left(k_{1}+k_{2}\right)^{2}}$$
### 小结

* $T+R=1$，粒子或者透射过去或者反射回来。与经典力学的预言相反，入射粒子遭到反射的概率并不为零。
* $A_{1}^{\prime} / A_{1}, A_{2} / A_{1}$ 为实数，量子粒子在反射或透射时都没有相位滞后
* $E \gg V_{0}$, 则 $T \simeq 1$如果入射粒子的能量足够大，以致可略去势阶的高度，则粒子将一跃而过，好像势阶不存在似的。

## $E\le V_0$
$$
\sqrt{\frac{2 m E}{\hbar^{2}}}=k_{1}
$$
$$
\sqrt{\frac{2 m\left(V_{0}-E\right)}{\hbar^{2}}}=\rho_{2}
$$
$$
\varphi_{\mathrm{I}}(x)=A_{1} \mathrm{e}^{\mathrm{i} k_{1} x}+A_{1}^{\prime} \mathrm{e}^{-\mathrm{i} k_{1} x}
$$
$$
\varphi_{\text {II }}(x)=B_{2} \mathrm{e}^{\rho_{2} x}+B_{2}^{\prime} \mathrm{e}^{-\rho_{2} x}
$$
根据波函数的有限性：
$$ \lim\limits_{x\rightarrow\infty}\varphi_{\text {II }}(x)\lt +\infty\Rightarrow B_2=0$$
$$
\frac{A_{1}^{\prime}}{A_{1}}=\frac{k_{1}-\mathrm{i} \rho_{2}}{k_{1}+\mathrm{i} \rho_{2}}
$$
$$
\frac{B_{2}^{\prime}}{A_{1}}=\frac{2 k_{1}}{k_{1}+\mathrm{i} \rho_{2}}
$$
$$
R=\left|\frac{A_{1}^{\prime}}{A_{1}}\right|^{2}=\left|\frac{k_{1}-\mathrm{i} \rho_{2}}{k_{1}+\mathrm{i} \rho_{2}}\right|^{2}=1
$$
### 小结
* 同在经典力学中一样，粒子只能返回（全反射）
* 存在$\mathrm{e}^{-\rho_{2} x}$，粒子出现在经典理论不允许它进人的空间区域的概率并不等于零
* 反射时将出现相位的改变
# 势垒
## 势能
$$
V(x)=\left\{\begin{array}{cl}
V_{0}, & 0\lt x\lt l \\
0, & x \le 0,x\ge l
\end{array}\right.
$$
## $E>V_0$
$$\varphi_{\mathrm{I}}(x)=A_{1} \mathrm{e}^{\mathrm{i} k_{1} x}+A_{1}^{\prime} \mathrm{e}^{-\mathrm{i} k_{1} x}$$
$$\varphi_{\mathrm{II}}(x)=A_{2} \mathrm{e}^{\mathrm{i} k_{2} x}+A_{2}^{\prime} \mathrm{e}^{-\mathrm{i} k_{2} x}$$
$$\varphi_{\mathrm{III}}(x)=A_{3} \mathrm{e}^{\mathrm{i} k_{1} x}+A_{3}^{\prime} \mathrm{e}^{-\mathrm{i} k_{1} x}$$
$$
A_{1}=\left[\cos k_{2} l-\mathrm{i} \frac{k_{1}^{2}+k_{2}^{2}}{2 k_{1} k_{2}} \sin k_{2} l\right] \mathrm{e}^{\mathrm{i} k_{1} l} A_{3}
$$
$$
A_{1}^{\prime}=\mathrm{i} \frac{k_{2}^{2}-k_{1}^{2}}{2 k_{1} k_{2}} \sin k_{2} l \mathrm{e}^{\mathrm{i} k_{1} l} A_{3}
$$
$$
R=\left|\frac{A_{1}^{\prime}}{A_{1}}\right|^{2}=\frac{\left(k_{1}^{2}-k_{2}^{2}\right) \sin ^{2} k_{2} l}{4 k_{1}^{2} k_{2}^{2}+\left(k_{1}^{2}-k_{2}^{2}\right)^{2} \sin ^{2} k_{2} l}
$$
$$
T=\left|\frac{A_{3}}{A_{1}}\right|^{2}=\frac{4 k_{1}^{2} k_{2}^{2}}{4 k_{1}^{2} k_{2}^{2}+\left(k_{1}^{2}-k_{2}^{2}\right)^{2} \sin ^{2} k_{2} l}
$$
$$
T=\frac{4 E\left(E-V_{0}\right)}{4 E\left(E-V_{0}\right)+V_{0}^{2} \sin ^{2}\left[\sqrt{2 m\left(E-V_{0}\right)} l / \hbar\right]}
$$
![透射率随势垒宽度的变化](https://i.loli.net/2021/11/21/NprMzQgYWlRkIhL.png)

### 小结
* $l$等于粒子在区域Ⅱ中的半波长的整数倍时，便发生共振
* 远离共振点，则在$x=0$及$x=l$处反射的那些波将因干涉而相消，于是波函数的值变得很小
* 共振条件得到满足，则波包通过区域Ⅱ需费较长的时间；这个现象在量子力学中叫做**共振散射**

## $E<V_0$
$$
T=\left|\frac{A_{3}}{A_{1}}\right|^{2}=\frac{4 E\left(V_{0}-E\right)}{4 E\left(V_{0}-E\right)+V_{0}^{2} \sinh ^{2}\left[\sqrt{2 m\left(V_{0}-E\right)} l / \hbar\right]}
$$
当 $\rho_{2} l \gg 1$ 时
$$T \simeq \frac{16 E\left(V_{0}-E\right)}{V_{0}^{2}} \mathrm{e}^{-2 \rho_{2} l}$$
### 小结
* 和经典的预言相反，粒子越过势垒的概率不等于零。
# 有限深势阱
## 势能
$$
V(x)=\left\{\begin{array}{cl}
-V_{0}, & |x|<a \\
0, & |x| \geqslant a
\end{array}\right.
$$
## 方程
$$
k=\frac{\sqrt{2 m\left(E+V_{0}\right)}}{\hbar}
$$
$$
\psi^{\prime \prime}+k^{2} \psi=0
$$
## 游离态
同势垒($E>V_0$)的分析
## 束缚态 
$$\beta=\frac{\sqrt{-2 m E}}{\hbar}>0$$
$$
\psi^{\prime \prime}-\beta^{2} \psi=0, \quad|x| \geqslant a
$$
$\psi<\infty$
$$
\psi(x)= \begin{cases}C \mathrm{e}^{-\beta x}, & x \geqslant a \\ C^{\prime} \mathrm{e}^{\beta x}, & x \leqslant-a\end{cases}
$$
### 偶宇称
$$
\psi(x)= \begin{cases}C \mathrm{e}^{-\beta x}, & x \geqslant a \\ \cos k x, & -a<x<a \\ C \mathrm{e}^{\beta x}, & x \leqslant-a\end{cases}
$$
$x=a$处$\psi,\psi^\prime$连续：
$$
C \mathrm{e}^{-\beta a}=\cos k a
$$
$$
-\beta C \mathrm{e}^{-\beta a}=-k \sin k a
$$
$$
k \tan k a=\beta
$$
$$
k^{2}+\beta^{2}=\frac{2 m V_{0}}{\hbar^{2}}
$$
### 奇宇称
$$
\psi(x)= \begin{cases}C^{\prime} \mathrm{e}^{-\beta x}, & x \geqslant a \\ \sin k x, & -a<x<a \\ -C^{\prime} \mathrm{e}^{\beta x}, & x \leqslant-a\end{cases}
$$
$$
k \cot k a=\beta
$$
# 无限深方势阱

## 势能

$$
V(x)= \begin{cases}0, & -a<x<a \\ \infty, & x<-a, \quad x>a\end{cases}
$$

## 解

在势阱外，有$\psi=0$

在势阱内，

$$
k=\sqrt{\frac{2 m E}{\hbar^{2}}}
$$

则方程可写作

$$
\psi^{\prime \prime}+k^{2} \psi=0, \quad-a<x<a
$$

势函数为偶宇称，故而解的本征函数有明确的宇称性

### 偶宇称态

$$
\psi(x)=A \cos k x, \quad-a<x<a
$$

根据波函数的连续性$\psi(a)=\psi(-a)=0$

$$
\cos k a=0, \quad k=\frac{n \pi}{2 a}, \quad n=1,3,5, \cdots
$$

归一化条件

$$
\int_{-\infty}^{\infty}|\psi|^{2} \mathrm{~d} x=\int_{-a}^{a} \psi^{2} \mathrm{~d} x=1 \Rightarrow A=\frac{1}{\sqrt{a}}
$$

### 奇宇称态

$$
\psi(x)=A \sin k x, \quad-a<x<a
$$

同上由连续性：

$$
\sin k a=0, \quad k=\frac{n \pi}{2 a}, \quad n=2,4,6, \cdots
$$

### 图像

![波函数图像](https://i.loli.net/2021/11/20/X3KY8gJ69aLnMsA.png)

## 小结

* 基态


$$
E_{1}=\frac{\hbar^{2} k_1^{2}}{2 m}=\frac{1}{2 m}\left(\frac{\pi \hbar}{2 a}\right)^{2}
$$

* 能级

$$
E_{n}=\frac{1}{2 m}\left(\frac{n \pi \hbar}{2 a}\right)^{2}, \quad n=1,2,3, \cdots
$$
## 无限深方势阱的态密度
### 一维
$$
\varepsilon_{n}=\frac{\pi^{2} \hbar^{2} n^{2}}{2 m L^{2}}, \quad n=1,2, \cdots
$$
$$
D(\varepsilon)=\frac{\mathrm{d} n}{\mathrm{~d} \varepsilon}=\frac{2 L}{h}\left(\frac{m}{2 \varepsilon}\right)^{1 / 2}
$$
### 二维
$$
r^2=n_{x}^{2}+n_{y}^{2}=\frac{2 m L^{2}}{\pi^{2} \hbar^{2}} \varepsilon
,n_x,n_y=1,2,3,\cdots
$$

$$
\mathrm{d} r=\left(\frac{2 m L^{2}}{\pi^{2} \hbar^{2}}\right)^{1 / 2} \frac{1}{2} \varepsilon^{-1 / 2} \mathrm{~d} \varepsilon
$$
换至极坐标中运算,每个量子态占据一个单位面积,r变化dr时，面积变化为
$$
dn =\int_0^{\frac{\pi}{2}}rdrd\theta = \frac{1}{2}\pi rdr
$$
$$
D(\varepsilon)=\frac{\mathrm{d} n}{\mathrm{~d} \varepsilon}=\frac{\mathrm{d} n}{\mathrm{d}r}\frac{\mathrm{d} r}{\mathrm{~d} \varepsilon}=\frac{ L^{2}}{2 \pi \hbar^{2}} m
$$
### 三维
$$
r^2 = n_{x}^{2}+n_{y}^{2}+n_{z}^{2}=\frac{2 m L^{2}}{\pi^{2} \hbar^{2}} \varepsilon
$$
$$
\mathrm{d} r=\left(\frac{2 m L^{2}}{\pi^{2} \hbar^{2}}\right)^{1 / 2} \frac{1}{2} \varepsilon^{-1 / 2} \mathrm{~d} \varepsilon
$$
每个量子态占据一个单位面积,r变化dr时，面积变化为
$$
dn = \int_0^{\frac{\pi}{2}}\int_0^{\frac{\pi}{2}}r^2sin\theta drd\theta d\varphi= \frac{1}{2}\pi r^2dr
$$
$$
D(\varepsilon)=\frac{\mathrm{d} n}{\mathrm{~d} \varepsilon}=\frac{\mathrm{d} n}{\mathrm{d}r}\frac{\mathrm{d} r}{\mathrm{~d} \varepsilon}=\frac{ L^{2}}{2 \pi \hbar^{2}} m
=\frac{ L^{3}}{4\pi^2\hbar^{3}}(2 m)^{3 / 2} \varepsilon^{1 / 2}
$$
# $\delta$势阱
## 势能
对有限深方势阱，令$V_0\rightarrow \infty$,$a\rightarrow 0$，但仍保持
$$
\int_{-\infty}^{\infty} V(x) \mathrm{d} x=-2 V_{0} a :=-\gamma
$$
即
$$V(x)=-\gamma\delta(x)$$