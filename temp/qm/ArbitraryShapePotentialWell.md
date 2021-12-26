# 任意形状的势阱

## 束缚态

![image-20211219203145787](https://s2.loli.net/2021/12/19/IYBrOvEAsDehmtZ.png)

对于束缚态，波函数平方可积，则$E<0$，且
$$
\varphi_{\mathrm{I}}(x)=e^{\rho x}， \quad   x<x_{1}
$$

$$
\rho=\sqrt{-\frac{2 m E}{\hbar^{2}}}
$$

在$x_1\le x\le x_2$中，将$\varphi_I$解析延拓到该区间内。其与$V(x)$的具体形式及$\rho$有关。

在$x\gt x_2$区域
$$
\varphi_{\text {III }}(x)=\widetilde{B} \mathrm{e}^{\rho x}+\widetilde{B^{\prime}} \mathrm{e}^{-\rho x}
$$
式中 $\widetilde{B}$ 和 $\widetilde{B^{\prime}}$ 都是实常数, 决定于 $\varphi(x)$ 和 $\mathrm{d} \varphi / \mathrm{d} x$ 在 $x=x_{2}$ 处的两个连续性条 件; $\widetilde{B}$ 和 $\widetilde{B^{\prime}}$ 除依赖于函数 $V(x)$ 以外还依赖于 $\rho$.

于是, 我们便构成方程的这样一个解。 在一般情况下它不是平方可积的, 除非 $\widetilde{B}=0$ . 但是, 对于一个给定的函数 $V(x)$ 来 说, $\widetilde{B}$ 通过 $\rho$ 而成为 $E$ 的函数. 因此, 只有对应于束俌态的那些 $E$ 值才是方程 $\widetilde{B}(E)=0$ 的解. 这些解 $E_{1}, E_{2}, \cdots$ 组成一个离散谱, 它当然依赖势函数。

![image-20211219204609309](https://s2.loli.net/2021/12/19/eBO6oUMjCsXrKLV.png)

>  处于任意形状的势阱中的粒子, 其束缚态能量的可 能值组成一个离散谱。

![image-20211219204907134](https://s2.loli.net/2021/12/19/6dbWA2KkNJamrwO.png)

> 对于每一个这样的定态, 画一条横线, 使 它的纵坐标等于对应的能量. 只保留这条横线被 $V(x)$ 的曲线截取的那一段; 也就是说, 只保留相同能量的经典运动所能覆盖的区段; 这个区段大体上标志波函数的展延范围.

### 基态能级

束缚态波函数可归一化
$$
E=\langle T\rangle+\langle V\rangle
$$

$$
\langle T\rangle=-\frac{\hbar^{2}}{2 m} \int_{-\infty}^{+\infty} \mathrm{d} x \varphi^{*}(x) \frac{\mathrm{d}^{2}}{\mathrm{~d} x^{2}} \varphi(x)=\frac{\hbar^{2}}{2 m} \int_{-\infty}^{+\infty} \mathrm{d} x\left|\frac{\mathrm{d}}{\mathrm{d} x} \varphi(x)\right|^{2}
$$

利用了分部积分和无穷远处波函数为0的性质。
$$
E=\langle T\rangle+\langle V\rangle\gt\langle V\rangle \geqslant-V_{0}
$$

> 和在经典力学中一样, 束缚态的 能量永远介于 $-V_{0}$ 和 0 之间.

> 虽然在经典力学 中, 粒子的能量可以等于 $-V_{0}$ (粒子静止于点 $M_{0}$ 处的情况) 或略大于 $-V_{0}$ (微 小摆动的情况), 但在量子力学中情况却不是这样, 在量子力学中, 能量的最低 可能值是基态能量 $E_{1}$, 其值一定大于 $-V_{0}$ .

## 非束缚态

![image-20211219210218165](https://s2.loli.net/2021/12/19/iB7jhHM2uG8UKsS.png)
$$
k=\sqrt{\frac{2 m E}{\hbar^{2}}}
$$

### 透射矩阵

有
$$
\left\{\begin{array}{l}
 x<-\frac{l}{2}: v_{k}(x)=\mathrm{e}^{\mathrm{i} k x} \\
 x>+\frac{l}{2}: v_{k}(x)=F(k) \mathrm{e}^{\mathrm{i} k x}+G(k) \mathrm{e}^{-\mathrm{i} k x}
\end{array}\right.
$$
或
$$
\left\{\begin{array}{l}
x<-\frac{l}{2}: v_{k}^{\prime}(x)=\mathrm{e}^{-\mathrm{i} k x} \\
 x>+\frac{l}{2}: v_{k}^{\prime}(x)=F^{\prime}(k) \mathrm{e}^{\mathrm{i} k x}+G^{\prime}(k) \mathrm{e}^{-\mathrm{i} k x}
\end{array}\right.
$$

$$
\varphi_{k}(x)=A v_{k}(x)+A^{\prime} v_{k}^{\prime}(x)
$$

$$
x<-\frac{l}{2}: \varphi_{k}(x)=A \mathrm{e}^{\mathrm{i} k x}+A^{\prime} \mathrm{e}^{-\mathrm{i} k x}
$$

$$
x>+\frac{l}{2}: \varphi_{k}(x)=\widetilde{A} \mathrm{e}^{\mathrm{i} k x}+\widetilde{A}^{\prime} \mathrm{e}^{-\mathrm{i} k x}
$$

$$
\left(\begin{array}{c}
\tilde{A} \\
\widetilde{A}^{\prime}
\end{array}\right)=M(k)\left(\begin{array}{c}
A \\
A^{\prime}
\end{array}\right)
$$

$$
M(k)=\left(\begin{array}{ll}
F(k) & F^{\prime}(k) \\
G(k) & G^{\prime}(k)
\end{array}\right)
$$

称为透射矩阵

### 透射矩阵的性质

$V(x)$为实函数
$$
v_{k}^{*}(x)=v_{k}^{\prime}(x)
$$

$$
M(k)=\left(\begin{array}{ll}
F(k) & G^{*}(k) \\
G(k) & F^{*}(k)
\end{array}\right)
$$

$$
|A|^{2}-\left|A^{\prime}\right|^{2}=|\tilde{A}|^{2}-\left|\tilde{A}^{\prime}\right|^{2}
$$

而
$$
|\tilde{A}|^{2}-\left|\tilde{A}^{\prime}\right|^{2}=\left[|F(k)|^{2}-|G(k)|^{2}\right]\left[|A|^{2}-\left|A^{\prime}\right|^{2}\right]
$$
故
$$
|F(k)|^{2}-|G(k)|^{2}=\operatorname{Det} M(k)=1
$$

---

若 $V(x)=V(-x)$, 那么 $G(k)$ 是一个纯虚数.

系数 $A$ 和 $\tilde{A}^{\prime}$ 属于 “进来" 的平面波, 与这种波相 联系的粒子分别来自 $x=-\infty$ 和 $x=+\infty$ 处并进人势场作用范围 (入射粒子); 另一方面, 系数 $\tilde{A}$ 和 $A^{\prime}$ 属于 “出去” 的平面波, 与这种波相联系的 粒子是离开势场的 (即透射的和反射的粒子). 
$$
\left(\begin{array}{l}
\tilde{A} \\
A^{\prime}
\end{array}\right)=S(k)\left(\begin{array}{l}
A \\
\tilde{A}^{\prime}
\end{array}\right)
$$

$$
S(k)=\frac{1}{F^{*}(k)}\left(\begin{array}{cc}
1 & G^{*}(k) \\
-G(k) & 1
\end{array}\right)
$$

---

### 反射系数和透射系数

考虑一个能量为 $E_{i}$ 的来自左方的人射粒子. 与它对应的波包就是取 $\tilde{A}^{\prime}=0$ 时诸函数 $\varphi_{k}(x)$ 以 $g(k)$ 为系数叠加的结果, 而函数 $g(k)$ 在点$k=k_{i}=\sqrt{2 m E / \hbar^{2}}$ 附近具有显著的峰值.
$$
\tilde{A}(k)=\frac{1}{F^{*}(k)} A(k)
$$

$$
A^{\prime}(k)=-\frac{G(k)}{F^{*}(k)} A(k)
$$

$$
R_{1}\left(k_{i}\right)=\left|\frac{A^{\prime}\left(k_{i}\right)}{A\left(k_{i}\right)}\right|^{2}=\left|\frac{G\left(k_{i}\right)}{F\left(k_{i}\right)}\right|^{2}
$$

$$
T_{1}\left(k_{i}\right)=\left|\frac{\tilde{A}\left(k_{i}\right)}{A\left(k_{i}\right)}\right|^{2}=\frac{1}{\left|F\left(k_{i}\right)\right|^{2}}
$$

从右边入射的粒子
$$
T_{2}(k)=\left|\frac{A^{\prime}(k)}{\tilde{A}^{\prime}(k)}\right|^{2}=\frac{1}{|F(k)|^{2}}
$$

$$
R_{2}(k)=\left|\frac{\tilde{A}(k)}{\tilde{A}^{\prime}(k)}\right|^{2}=\left|\frac{G(k)}{F(k)}\right|^{2}
$$

$T_{1}(k)=T_{2}(k)$ 而且 $R_{1}(k)=R_{2}(k)$; 这就是说, 只要能量已经给定,一个势垒 (不论是否对称) 的可穿透性对于来自左方与来 自右方的粒子永远是一样的.

另外
$$
|F(k)| \geqslant 1
$$
此式中的等号成立时, 反射系数等于零, 而透射系数等于 1 (即共振). 但是与此 相反的情况是不可能的, 而我们 $|F(k)|>|G(k)|$。