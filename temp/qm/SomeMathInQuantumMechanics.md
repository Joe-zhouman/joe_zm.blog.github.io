# 波函数的基

## 定义

若$u_{i}(r) \in \mathscr{F}$，$\mathscr{F}$为波函数空间。若
$$
\left(u_{i}, u_{j}\right)=\int \mathrm{d}^{3} r u_{i}^{*}(r) u_{j}(r)=\delta_{i j}
$$
则集合$\{u_{i}(r)\}$为**正交归一**的。

若每个波函数都可以按$u_{i}(r)$有唯一展开，则其构成一正交归一基。
$$
\psi(\boldsymbol{r})=\sum_{i} c_{i} u_{i}(\boldsymbol{r})
$$

$$
c_{i}=\left(u_{i}, \psi\right)=\int \mathrm{d}^{3} r u_{i}^{*}(r) \psi(r)
$$

## 封闭性关系式

$$
\begin{aligned}
\psi(\boldsymbol{r}) &=\sum_{i} c_{i} u_{i}(\boldsymbol{r}) \\
&=\sum_{i}\left(u_{i}, \psi\right) u_{i}(\boldsymbol{r}) \\
&=\sum_{i}\left[\int \mathrm{d}^{3} r^{\prime} u_{i}^{*}\left(\boldsymbol{r}^{\prime}\right) \psi\left(\boldsymbol{r}^{\prime}\right)\right] u_{i}(\boldsymbol{r})
\end{aligned}
$$

交换求和和求积的顺序
$$
\psi(\boldsymbol{r})=\int \mathrm{d}^{3} r^{\prime} \psi\left(\boldsymbol{r}^{\prime}\right)\left[\sum_{i} u_{i}(\boldsymbol{r}) u_{i}^{*}\left(\boldsymbol{r}^{\prime}\right)\right]
$$

$$
\psi(\boldsymbol{r})=\int \mathrm{d}^{3} \boldsymbol{r}^{\prime} \psi\left(\boldsymbol{r}^{\prime}\right) F\left(\boldsymbol{r}, \boldsymbol{r}^{\prime}\right)
$$

$F$具有$\delta$函数的筛选性，故
$$
\sum_{i} u_{i}(r) u_{i}^{*}\left(r^{\prime}\right)=\delta\left(r-r^{\prime}\right)
$$
以上即为封闭性关系
$$
\psi(\boldsymbol{r})=\int \mathrm{d}^{3} r^{\prime} \psi\left(\boldsymbol{r}^{\prime}\right) \delta\left(\boldsymbol{r}-\boldsymbol{r}^{\prime}\right)
$$

## 连续基

正交归一式
$$
\left(w_{\alpha}, w_{\alpha^{\prime}}\right)=\int \mathrm{d}^{3} r w_{\alpha}^{*}(r) w_{\alpha^{\prime}}(r)=\delta\left(\alpha-\alpha^{\prime}\right)
$$
封闭性关系
$$
\int \mathrm{d} \alpha w_{\alpha}(\boldsymbol{r}) w_{\alpha}^{*}\left(\boldsymbol{r}^{\prime}\right)=\delta\left(\boldsymbol{r}-\boldsymbol{r}^{\prime}\right)
$$
分量
$$
c(\alpha)=\left(w_{\alpha}, \psi\right)=\int \mathrm{d}^{3} r^{\prime} w_{\alpha}^{*}\left(\boldsymbol{r}^{\prime}\right) \psi\left(\boldsymbol{r}^{\prime}\right)
$$

##  不属于波函数空间的基

与某一物理状态对应的总是一个平方可积的波函数，在任何情况下，$v_{p}(r)$ 或 $\xi_{r_{0}}(r)$ 都不能表示粒子的态. 这些函数仅仅是在对波函数 $\psi(r)$ 进行运算时, 很方便的一些工具, 而波函数才是描述物理状态的函数.

### 平面波

$$
v_{p}(x)=\frac{1}{\sqrt{2 \pi \hbar}} \mathrm{e}^{\mathrm{i} p x / \hbar}
$$

是一个平面波，遍及$Ox$轴，并非平方可积

单每一个波函数都可按平面波展开
$$
\psi(x)=\int_{-\infty}^{+\infty} \mathrm{d} p \bar{\psi}(p) v_{p}(x)
$$
封闭性关系
$$
\frac{1}{2 \pi} \int_{-\infty}^{+\infty} \mathrm{d} k \mathrm{e}^{\mathrm{i} k u}=\delta(u)
$$

$$
\int_{-\infty}^{+\infty} \mathrm{d} p v_{p}(x) v_{p}^{*}\left(x^{\prime}\right)=\frac{1}{2 \pi} \int \frac{\mathrm{d} p}{\hbar} \mathrm{e}^{\mathrm{i} \frac{p}{\hbar}\left(x-x^{\prime}\right)}=\delta\left(x-x^{\prime}\right)
$$

$$
\left(v_{p}, v_{p^{\prime}}\right)=\frac{1}{2 \pi} \int \frac{\mathrm{d} x}{\hbar} \mathrm{e}^{\mathrm{i} \frac{x}{\hbar}\left(p^{\prime}-p\right)}=\delta\left(p-p^{\prime}\right)
$$

### $\delta$函数

$$
\xi_{r_{0}}(r)=\delta\left(r-r_{0}\right)
$$

$$
\psi(\boldsymbol{r})=\int \mathrm{d}^{3} r_{0} \psi\left(\boldsymbol{r}_{0}\right) \xi_{r_{0}}(\boldsymbol{r})
$$

波函数可按该函数唯一展开
$$
\psi\left(\boldsymbol{r}_{0}\right)=\left(\xi_{r_{0}}, \psi\right)=\int \mathrm{d}^{3} r \xi_{r_{0}}^{*}(\boldsymbol{r}) \psi(\boldsymbol{r})
$$
为在基函数上的分量

正交归一关系
$$
\left(\xi_{r_{0}}, \xi_{r_{0}^{\prime}}\right) =\int \mathrm{d}^{3} r \delta\left(\boldsymbol{r}-\boldsymbol{r}_{0}\right) \delta\left(\boldsymbol{r}-\boldsymbol{r}_{0}^{\prime}\right) 
=\delta\left(\boldsymbol{r}_{0}-\boldsymbol{r}_{0}^{\prime}\right)
$$
封闭性关系
$$
\int \mathrm{d}^{3} r_{0} \xi_{r_{0}}(r) \xi_{r_{0}}^{*}\left(\boldsymbol{r}^{\prime}\right) =\int \mathrm{d}^{3} r_{0} \delta\left(\boldsymbol{r}-\boldsymbol{r}_{0}\right) \delta\left(\boldsymbol{r}^{\prime}-\boldsymbol{r}_{0}\right) 
=\delta\left(\boldsymbol{r}-\boldsymbol{r}^{\prime}\right)
$$

# 态空间及狄拉克符号

> 左矢为bra，右矢为ket，合起来就是bracket，即方括号

任何物理体系的量子态由一个态矢量来描述, 态矢量属于 $\mathscr{E}$ 空间, 即体系的态空间.

## 右矢

右矢$\ket{\psi}$为态空间中的一个矢量，每一个平方可积函数都对应一个右矢。

 $\psi(r)$ 为右矢 $|\psi\rangle$ 在某一个基中的分量的集合, $r$ 则起着指标的作用 。 为了确定一个矢量, 我们的做法是: **先用这个矢量在某一特定坐标系中的分量来表示这个矢量, 然后把这个特定坐标系放在 和一切其他坐标系相同的地位上研究.**

## 左矢

 定义在右矢 $|\psi\rangle \in \mathscr{E}$ 上的线性泛函的集合构成一个矢量空间, 叫做 $\mathscr{E}$ 的对偶空间, 记作 $\mathscr{E}^{*}$.$\mathscr{E}^{*}$ 空间中的每一个元素, 或矢量, 都叫做左矢, 我们用符号 $\bra{}$ 来表示它.

例如, 左矢 $\langle\chi|$ 表示线性泛函 $\chi$, 并且今后将线性泛函 $\langle\chi| \in \mathscr{E}^{*}$ 作用于右矢 $|\psi\rangle \in \mathscr{E}$ 得到的那个数 记作 $\langle\chi \mid \psi\rangle$ :
$$
\chi(|\psi\rangle)=\bra{\chi}\ket{\psi}
$$

## 左矢右矢之间的关系

> 每一个右矢对应一个左矢

右矢 $|\varphi\rangle$ 可以决定这样一个线性泛函, 它按线性方式使得每一个 右矢 $|\psi\rangle \in \mathscr{E}$ 都有一个对应的复数, 而且这个复数就是 $|\varphi\rangle$ 和 $|\psi\rangle$ 的标量积 $(|\varphi\rangle,|\psi\rangle)$. 假设 $\langle\varphi|$ 就是这个线性泛函, 那么它应由下式所决定
$$
\langle\varphi \mid \psi\rangle=(|\varphi\rangle,|\psi\rangle)
$$

> 对应为反线性

$$
\begin{aligned}
\left(\lambda_{1}\left|\varphi_{1}\right\rangle+\lambda_{2}\left|\varphi_{2}\right\rangle,|\psi\rangle\right) &=\lambda_{1}^{*}\left(\left|\varphi_{1}\right\rangle,|\psi\rangle\right)+\lambda_{2}^{*}\left(\left|\varphi_{2}\right\rangle,|\psi\rangle\right) \\
&=\lambda_{1}^{*}\left\langle\varphi_{1} \mid \psi\right\rangle+\lambda_{2}^{*}\left\langle\varphi_{2} \mid \psi\right\rangle \\
&=\left(\lambda_{1}^{*}\left\langle\varphi_{1}\left|+\lambda_{2}^{*}\left\langle\varphi_{2}\right|\right) \mid \psi\right\rangle\right.
\end{aligned}
$$

$$
\lambda_{1}\left|\varphi_{1}\right\rangle+\lambda_{2}\left|\varphi_{2}\right\rangle \Longrightarrow \lambda_{1}^{*}\left\langle\varphi_{1}\right|+\lambda_{2}^{*}\left\langle\varphi_{2}\right|
$$

> 左矢不一定有对应的右矢

$$
\left\langle\xi_{x_{0}} \mid \psi\right\rangle=\psi\left(x_{0}\right)
$$

但$\xi_{x_0}$本身不是平方可积的。

可定义广义右矢，但其不表示真实的物理状态。

## 线性算符

线性算符 $A$ 使每一个右矢 $|\psi\rangle \in \mathscr{E}$ 都有一个对应的右矢 $\left|\psi^{\prime}\right\rangle \in \mathscr{E}$, 而且这 种对应关系是线性的:
$$
\left|\psi^{\prime}\right\rangle=A|\psi\rangle
$$

$$
A\left(\lambda_{1}\left|\psi_{1}\right\rangle+\lambda_{2}\left|\psi_{2}\right\rangle\right)=\lambda_{1} A\left|\psi_{1}\right\rangle+\lambda_{2} A\left|\psi_{2}\right\rangle
$$

$$
(A B)|\psi\rangle=A(B|\psi\rangle)
$$

$$
\langle\varphi|(A|\psi\rangle)
$$

为A的矩阵元，显然，其是一个数。

### 投影算符

$$
\langle\psi \mid \psi\rangle=1
$$

$$
P_{\psi}=|\psi\rangle\langle\psi|
$$

$$
P_{\psi}|\varphi\rangle=|\psi\rangle\langle\psi \mid \varphi\rangle
$$

将 $P_{\psi}$ 作用于任一右矢 $|\varphi\rangle$ 便得到一个与 $|\psi\rangle$ 成正比的右矢, 比例 系数就是 $|\psi\rangle$ 和 $|\varphi\rangle$ 的标量积 $\langle\psi \mid \varphi\rangle$.$P_{\psi}$ 的 “几何” 意义是在右矢 $|\psi\rangle$ 上进行 “垂直投影" 的算符.
$$
P_{\psi}^{2}=P_{\psi} P_{\psi}=|\psi\rangle\langle\psi \mid \psi\rangle\langle\psi|=P_{\psi}
$$
假设有 $q$ 个已归一化的、两两正交的矢量: $\left|\varphi_{1}\right\rangle,\left|\varphi_{2}\right\rangle, \cdots,\left|\varphi_{q}\right\rangle$ :
$$
\left\langle\varphi_{i} \mid \varphi_{j}\right\rangle=\delta_{i j} ; \quad i, j=1,2, \cdots, q
$$
这 $q$ 个矢量在 $\mathscr{E}$ 空间中所张成的子空间记作 $\mathscr{E}_{q}$.
$$
P_{q}=\sum_{i=1}^{q}\left|\varphi_{i}\right\rangle\left\langle\varphi_{i}\right|
$$

$$
P_{q}^{2}=\sum_{i=1}^{q} \sum_{j=1}^{q}\left|\varphi_{i}\right\rangle\left\langle\varphi_{i} \mid \varphi_{j}\right\rangle\left\langle\varphi_{j}\right|=\sum_{i=1}^{q} \sum_{j=1}^{q}\left|\varphi_{i}\right\rangle\bra{\varphi_{j}}\ket{\delta_{i j}}=\sum_{i=1}^{q}| \varphi_{i}\rangle\left\langle\varphi_{i}\right|=P_{q}
$$

将 $P_{q}$ 作用于 $|\psi\rangle$ 上, 得到 $|\psi\rangle$ 在这些 $\left|\varphi_{i}\right\rangle$ 上的投影的线性组合, 也就是 $|\psi\rangle$ 在子空间 $\mathscr{E}_{q}$ 上的投影.

## 厄米共轭

> 算符 $A$ 给每一个左矢 $\langle\varphi|$ 联系上一个新左矢 $\langle\varphi| A$.

$$
\langle\varphi|A| \psi\rangle=(\langle\varphi| A)|\psi\rangle=\langle\varphi|(A|\psi\rangle)
$$

> $A\langle\varphi|$ 是没有意义的.

![image-20211208122405128](https://s2.loli.net/2021/12/08/ITiRsUW5q4Kw3GH.png)
$$
\left|\psi^{\prime}\right\rangle=A|\psi\rangle \Longleftrightarrow\left\langle\psi^{\prime}\right|=\langle\varphi| A^{\dagger}
$$

$$
\left\langle\psi\left|A^{\dagger}\right| \varphi\right\rangle=\langle\varphi|A| \psi\rangle^{*}
$$

$$
|A \psi\rangle=A|\psi\rangle
$$

$$
\langle A \psi|=\langle\psi| A^{\dagger}
$$

> 一个右 (左) 矢的厄米共轭是一个左 (右) 矢; 一个算符的厄米共轭 是它的伴随算符; 一个数的厄米共轭是它的共轭复数. 采用狄拉克符号, 厄米

### 厄米算符

$$
A=A^{\dagger}
$$

$$
P_{\psi}^{\dagger}=|\psi\rangle\langle\psi|=P_{\psi}
$$

厄米算符满足$[A, B]=0$

## 幺正算符

$$
U^{\dagger} U=U U^{\dagger}=\mathbb{1}
$$

则$U$为**幺正算符**
$$
\left\langle\tilde{\psi}_{1} \mid \tilde{\psi}_{2}\right\rangle=\left\langle\psi_{1}\left|U^{\dagger} U\right| \psi_{2}\right\rangle=\left\langle\psi_{1} \mid \psi_{2}\right\rangle
$$
幺正算符对应的幺正变换保持标量积不变。

> 1. 若 $A$ 是厄米算符, 则 $T=e^{\mathrm{i} A}$ 是幺正算符;
> 1. 两个幺正算符的乘积也是幺正算符.
> 1. 幺正算符是正交算符在任意维复空间中的推广。
> 1. 幺正算符的充要条件是其将一个正交基变为另一个正交基。
> 1. 幺正算符分矩阵有$\sum_{k} U_{k i}^{*} U_{k j}=\delta_{i j}$
> 1. 幺正算符的本征值为模为1的复数。

### 幺正变换

幺正变换作用于算符上，$\widetilde{A}=U A U^{\dagger}$

> $\widetilde{A}$ 的本征矢就是 $A$ 的本征矢 $\left|\varphi_{a}\right\rangle$ 的变换 $\left|\widetilde{\varphi}_{a}\right\rangle=U\ket{\varphi_\alpha}$; 本征值不变.

### 无限小幺正算符

$$
U(\varepsilon)=1+\varepsilon G+\cdots
$$ {$$}

$$
U^{\dagger}(\varepsilon)=\mathbb{1}+\varepsilon G^{\dagger}+\cdots
$$

$$
U(\varepsilon) U^{\dagger}(\varepsilon)=U^{\dagger}(\varepsilon) U(\varepsilon)=1+\varepsilon\left(G+G^{\dagger}\right)+\cdots
$$

其为幺正算符，故
$$
G+G^{\dagger}=0
$$
$G$为一反厄米算符，令$F=iG$,则$F$为一厄米算符，
$$
U(\varepsilon)=1-\mathrm{i} \varepsilon F
$$

$$
\widetilde{A}-A=-\mathrm{i} \varepsilon[F, A]
$$

# 表象

选择一种表象就是在态空间 $\mathscr{E}$ 中选择一个离散的或连续的正交归一基. 在选定的基中, 矢量和算符都是用数来表示的: 对于矢量, 这些数就是它的分 量; 对于算符, 这些数就是它的矩阵元. 矢量运算就变成了对这些数进行矩阵运算. 

正交归一关系
$$
\left\langle u_{i} \mid u_{j}\right\rangle=\delta_{i j}
$$

$$
\left\langle w_{\alpha} \mid w_{\alpha^{\prime}}\right\rangle=\delta\left(\alpha-\alpha^{\prime}\right)
$$

在基中展开
$$
|\psi\rangle=\sum_{i} c_{i}\left|u_{i}\right\rangle
$$

$$
|\psi\rangle=\int \mathrm{d} \alpha c(\alpha)\left|w_{\alpha}\right\rangle
$$

封闭性关系
$$
P_{\left\{u_{i}\right\}}=\sum_{i}\left|u_{i}\right\rangle\left\langle u_{i}\right|=I
$$

$$
P_{\left\{w_{\alpha}\right\}}=\int \mathrm{d} \alpha\left|w_{\alpha}\right\rangle\left\langle w_{\alpha}\right|=I
$$

## 左矢和右矢的表象

右矢$\ket{\psi}$为列向量，分量为$\bra{u_i}\ket{\psi}$，左矢$\bra{\varphi}$为行向量,分量为$\bra{\varphi}\ket{u_i}$

利用封闭性关系
$$
\langle\varphi|=\langle\varphi| 1=\langle\varphi| P_{\left\{u_{i}\right\}}=\sum_{i}\left\langle\varphi \mid u_{i}\right\rangle\left\langle u_{i}\right|
$$

$$
\langle\varphi|=\langle\varphi| \mathbb{1}=\langle\varphi| P_{\left\{w_{\alpha}\right\}}=\int \mathrm{d} \alpha\left\langle\varphi \mid w_{\alpha}\right\rangle\left\langle w_{\alpha}\right|
$$

$$
\langle\varphi \mid \psi\rangle =\langle\varphi|\mathbb{1}| \psi\rangle=\left\langle\varphi\left|P_{\left\{u_{i}\right\}}\right| \psi\right\rangle =\sum_{i}\left\langle\varphi \mid u_{i}\right\rangle\left\langle u_{i} \mid \psi\right\rangle
$$

$\bra{\psi}$和$\ket{\psi}$的表象互相厄米共轭。

## 算符的表象

$$
A_{i j}=\left\langle u_{i}|A| u_{j}\right\rangle
$$

$$
A\left(\alpha, \alpha^{\prime}\right)=\left\langle w_{\alpha}|A| w_{\alpha^{\prime}}\right\rangle
$$

算符的表象是方阵。

伴随算符的矩阵为其厄米共轭矩阵。

### 算符的函数

$$
F(z)=\sum_{n=0}^{\infty} f_{n} z^{n}
$$

则算符的函数
$$
F(A)=\sum_{n=0}^{\infty} f_{n} A^{n}
$$

> 若 $\left|\varphi_{a}\right\rangle$ 是算符 $A$ 的本征矢, 属于本征值 $a$, 则 $\left|\varphi_{a}\right\rangle$ 也是算 符 $F(A)$ 的本征矢, 属于本征值 $F(a)$.

> 考虑一个可对角化的算符 $A$ (只要 $A$ 是观察算符, 这总是可以的), 现在取这样一个基, 在 其中表示 $A$ 的矩阵是对角的 (因而非零矩阵元就是 $A$ 的诸本征值 $a_{i}$ ); 按定义， $F(A)$ 是这样一个算符, 它在这同一个基中由元素为 $F\left(a_{i}\right)$ 的对角矩阵表示.

### 算符的导数

$$
\left(\frac{\mathrm{d} A}{\mathrm{~d} t}\right)_{i j}=\frac{\mathrm{d}}{\mathrm{d} t} A_{i j}
$$

## 表象的变换

从$\{\ket{u_i}\}$到$\{\ket{t_k}\}$，用好以下关系式
$$
P_{\left\{u_{i}\right\}}=\sum\left|u_{i}\right\rangle\left\langle u_{i}\right|=1
$$

$$
P_{\left\{t_{k}\right\}}=\sum_{k}\left|t_{k}\right\rangle\left\langle t_{k}\right|=1
$$

$$
\left\langle u_{i} \mid u_{j}\right\rangle=\delta_{i j}
$$

$$
\left\langle t_{k} \mid t_{l}\right\rangle=\delta_{k l}
$$

不用死记硬背。

由右矢 $|\psi\rangle$ 在旧基中的分量 $\left\langle u_{i} \mid \psi\right\rangle$ 得出它在新基中的分量 $\left\langle t_{k} \mid \psi\right\rangle$,
$$
\left\langle t_{k} \mid \psi\right\rangle =\left\langle t_{k}|1| \psi\right\rangle=\left\langle t_{k}\left|P_{\left\{u_{i}\right\}}\right| \psi\right\rangle 
=\sum_{i}\left\langle t_{k} \mid u_{i}\right\rangle\left\langle u_{i} \mid \psi\right\rangle
$$

$$
\left\langle u_{i} \mid \psi\right\rangle =\left\langle u_{i}|\mathbb{1}| \psi\right\rangle=\left\langle u_{i}\left|P_{\left\{t_{k}\right\}}\right| \psi\right\rangle 
=\sum_{k}\left\langle u_{i} \mid t_{k}\right\rangle\left\langle t_{k} \mid \psi\right\rangle
$$

左矢也一样
$$
\left\langle\psi \mid t_{k}\right\rangle =\left\langle\psi|1| t_{k}\right\rangle=\left\langle\psi\left|P_{\left\{u_{i}\right\}}\right| t_{k}\right\rangle 
=\sum_{i}\left\langle\psi \mid u_{i}\right\rangle\left\langle u_{i} \mid t_{k}\right\rangle
$$
算符
$$
\left\langle t_{k}|A| t_{l}\right\rangle =\left\langle t_{k}\left|P_{\left\{u_{i}\right\}} A P_{\left\{u_{j}\right\}}\right| t_{l}\right\rangle 
=\sum_{i, j}\left\langle t_{k} \mid u_{i}\right\rangle\left\langle u_{i}|A| u_{j}\right\rangle\left\langle u_{j} \mid t_{l}\right\rangle
$$

## 本征值与本征矢

$$
A|\psi\rangle=\lambda|\psi\rangle
$$

式中 $\lambda$ 是一个复数, 则我们称 $|\psi\rangle$ 为线性算符 $A$ 的本征矢 (或本征右矢); 称方程  为线性筫符 $A$ 的本征值方程, 我们将研究此方程的一些性质. 一般说来, 只有当 $\lambda$ 取某些特殊值, 即所谓 $A$ 的本征值时, 这个方程才有解. 这些本征值的集合叫做 $A$ 的谱.

注意, 如果 $|\psi\rangle$ 是 $A$ 的属于本征值 $\lambda$ 的本征矢, 那么, $\alpha|\psi\rangle$ ( $\alpha$ 为任意复 数) 也是 $A$ 的属于同一本征值的本征矢。约定本征矢进行了归一化
$$
\bra{\psi}\ket{\psi}=1
$$
当然，这种做法并没有完全消除不确定性, 因为 $\mathrm{e}^{\mathrm{i} \theta}|\psi\rangle$ ( $\theta$ 为任意实数) 和 $|\psi\rangle$ 具有相同的模方. 不过在量子力学中, 从 $|\psi\rangle$ 和从 $\mathrm{e}^{\mathrm{i} \theta}|\psi\rangle$ 得到的物理预言是一样的.

如果本征值 $\lambda$ 只对应于一个本征矢 (除一个倍乘因子以外), 也就是说与 $\lambda$ 对应的全体本征矢是共线的, 我们便称这个本征值是**非简并**的 (或简单的). 反之, 如果至少有两个线性无关的右矢都是 $A$ 的属于同一本征值的本征矢, 我们便称这个本征值是**简并**的; 属于这个本征值的线性无关本征矢的个数, 叫做该本征值的**简并度** (一个本征值的简并度可以是有限的, 也可以是无限的). 例如, 假设 $\lambda$ 是 $g$ 重简并的, 那么, 和它对应的就有 $g$ 个线性无关的右矢 $\left|\psi^{i}\right\rangle(i=1,2, \cdots, g)$, 它们都满足方程:
$$
A\left|\psi^{i}\right\rangle=\lambda\left|\psi^{i}\right\rangle
$$

$$
|\psi\rangle=\sum_{i=1}^{g} c_{i}\left|\psi^{i}\right\rangle
$$

都是$A$属于$\lambda$的本征矢，其构成一个**g维向量空间**，为本征值的**本征子空间**

---

对投影算符
$$
P_{\psi}|\varphi\rangle=\lambda|\varphi\rangle
$$
此式左端的右矢永远和 $|\psi\rangle$ 共线, 或者为零. 因而, $P_{\psi}$ 的本征矢有两种, 一种就是 $|\psi\rangle$ 本身, 它属于本征值 $\lambda=1$; 另一种是一切与 $|\psi\rangle$ 正交的 $|\varphi\rangle$, 它们属于本征值 $\lambda=0 .$于是 $P_{\psi}$ 的谱只包含两个数: 1 和 0 . 前者是非简并的, 后者是简并的。其对应于 $\lambda=0$ 的本征子空间就是 $|\psi\rangle$ 的**正交补空间** .

---

$$
\sum_{j}\left\langle u_{i}|A| u_{j}\right\rangle\left\langle u_{j} \mid \psi\right\rangle=\lambda\left\langle u_{i} \mid \psi\right\rangle
$$

$$
\sum_{j}\left[A_{i j}-\lambda \delta_{i j}\right] c_{j}=0
$$

上式为非平凡解，要求
$$
\operatorname{Det}[\mathscr{A}-\lambda I]=0
$$
一个算符的本征值就是它的特征方程的根.

若$\lambda_0$为特征方程的单根，只有一个本征矢。

若$\lambda_0$为特征方程的$q$重根，若其对应的特征方程仍有$N-p$组独立方程，则本征矢有$p$个。为$p$重简并。从线性代数的角度来说，$p$为几何重数，$q$为代数重数。有$p\le q$。$p=q$时，才能相似对角化。

对厄米算符，其必定可相似对角化。

## 观察算符

> 厄米算符的本征值都是实数

$$
\langle\psi|A| \psi\rangle^{*}=\left\langle\psi\left|A^{\dagger}\right| \psi\right\rangle=\langle\psi|A| \psi\rangle
$$

$$
\langle\psi|A| \psi\rangle=\lambda\langle\psi \mid \psi\rangle
$$

故$\lambda$为实数。

> 厄米算符的属于两个互异本征值的本征矢互相正交.

$$
A|\psi\rangle=\lambda|\psi\rangle \qquad
A|\varphi\rangle=\mu|\varphi\rangle
$$

$$
\langle\varphi|A| \psi\rangle=\lambda\langle\varphi \mid \psi\rangle=\mu\langle\varphi \mid \psi\rangle
$$

如果 $(\lambda-\mu) \neq 0$, 则 $|\varphi\rangle$ 与 $|\psi\rangle$ 正交.

> 如果 $\mathscr{E}$ 是有限多维空间, 就一定可以用一 个厄米算符的全体本征矢来构成一个基. 如果 $\mathscr{E}$ 是无限多维空间, 情况就末必如此. 

若果厄密算符的正交归一系构成一个基，则其为一个观察算符
$$
\sum_{n=1}^{\infty} \sum_{i=1}^{g_{n}}\left|\psi_{n}^{i}\right\rangle\left\langle\psi_{n}^{i}\right|=1
$$
对连续谱
$$
\sum_{n} \sum_{i=1}^{g_{n}}|\psi_{n}^{i}\rangle\langle\psi_{n}^{i}|+\int_{\nu_{1}}^{\nu_{2}} \mathrm{~d} \nu| \psi_{\nu}\rangle\langle\psi_{\nu}|=\mathbb{1}
$$

### 正则共轭观察算符的性质

两个观察算符$\left[Q_{i}, P_{i}\right]=\mathrm{i} \hbar$

对应算符
$$
S(\lambda)=\mathrm{e}^{-\mathrm{i} \lambda P / \hbar}
$$
易知该算符为幺正的。
$$
[Q, S(\lambda)]=\mathrm{i} \hbar\left(-\frac{\mathrm{i} \lambda}{\hbar}\right) \mathrm{e}^{-\mathrm{i} \lambda P / \hbar}=\lambda S(\lambda)
$$
可写作
$$
Q S(\lambda)=S(\lambda)[Q+\lambda]
$$
假设 $Q$ 有一个非零本征矢 $|q\rangle$, 属于本征值 $\boldsymbol{q}$ :
$$
\boldsymbol{Q}|\boldsymbol{q}\rangle=\boldsymbol{q}|\boldsymbol{q}\rangle
$$

$$
Q S(\lambda)|q\rangle =S(\lambda)(Q+\lambda)|q\rangle 
=S(\lambda)(q+\lambda)|q\rangle=(q+\lambda) S(\lambda)|q\rangle
$$

这个等式表明, $S(\lambda)|q\rangle$ 是 $Q$ 的另一个非零本征矢 $(S(\lambda)$ 是幺正的, 故 $S(\lambda)|q\rangle$ 不为零, 属于本征值 $(q+\lambda)$. 因此, 从 $Q$ 的一个本征矢出发, 应用算符 $S(\lambda)$, 便可以构成 $Q$ 的另一个本征矢, 属于任意的实本征值 (因为 $\lambda$ 可以取一 切实数值). 可见 $Q$ 的谱是一个连续谱, 包含实轴上的一切可能值。

> 在有限的 $N$ 维空间 $\mathscr{E}$ 中, 不存在对易子等于 $\mathrm{i} \hbar$ 的观察算符 $Q$ 和 $P$; 这是因为 $Q$ 的本征值的个数不可能在小于或等于 $N$ 的同时又是无穷大.

>  若 $q$ 是非简并 的, 则 $Q$ 的所有其他本征值也是非简并的. $Q$的全体本征值有相同的简并度。

$|q\rangle=S(q)|0\rangle$，则
$$
S(\lambda)|q\rangle=S(\lambda) S(q)|0\rangle=S(\lambda+q)|0\rangle=|q+\lambda\rangle
$$
从此可得到全部本征矢

> $在$$\{\ket{q}\}$表象中表现为用$q$去倍称。

> 算符 $S(\lambda)$ 在 $\{|q\rangle\}$ 表象中的作用就是将波函数平行于 $q$ 轴移动一个量 $\lambda$. 称 $S(\lambda)$ 为位移算符.

> $P$ 在 $\{|q\rangle\}$ 表象中的作用和 $\frac{\hbar}{\mathrm{i}} \frac{\mathrm{d}}{\mathrm{d} q} 一$ 样.

> 算符 $P$ 在 $\{|p\rangle\}$ 表象中的作用相当于用 $p$ 去倍乘; 而算符 $Q$ 的作用则相 当于算符 $\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} p}$.

---

## 可对易观察算符

> 如果两个算符 $A$ 和 $B$ 是可对易的, 而且 $|\psi\rangle$ 是 $A$ 的一个本征矢, 则 $B|\psi\rangle$ 也是 $A$ 的本征矢, 且属于同一本征值.

$$
A|\psi\rangle=a|\psi\rangle
$$

$$
B A|\psi\rangle=a B|\psi\rangle
$$

$AB$可对易，则
$$
A(B|\psi\rangle)=a(B|\psi\rangle)
$$
下面讨论两种可能的情况:

1. 假设 $a$ 是非简并的本征值, 则按定义, 属于它的全体本征矢是共线的, 因而 $B|\psi\rangle$ 必然正比于 $|\psi\rangle$, 可见 $|\psi\rangle$ 也是 $B$ 的本征矢.
1. 如果 $a$ 是简并的本征值, 我们就只能说 $B|\psi\rangle$ 属于算符 $A$ 的对应于本 征值 $a$ 的本征子空间 $\mathscr{E}_{a}$. 因此, 对于任意的 $|\psi\rangle \in \mathscr{E}_{a}$, 有

$$
B|\psi\rangle \in \mathscr{E}_{a}
$$

> 如果两个观察算符 $A$ 与 $B$ 是可对易的, 又若 $\left|\psi_{1}\right\rangle$ 和 $\left|\psi_{2}\right\rangle$ 是 $A$ 的两个本征矢, 属于不同的本征值, 则矩阵元 $\left\langle\psi_{1}|B| \psi_{2}\right\rangle$ 等于零.

$$
A|\psi_1\rangle=\lambda|\psi_1\rangle \qquad
A|\psi_2\rangle=\mu|\psi_2\rangle
$$

$$
\left\langle\psi_{1}|(A B-B A)| \psi_{2}\right\rangle=\left(a_{1}-a_{2}\right)\left\langle\psi_{1}|B| \psi_{2}\right\rangle=0
$$

$a_1\ne a_2$，得证。

> 如果两个观察算符 $A$ 与 $B$ 可对易, 则 $A$ 和 $B$ 的共同本征矢构成态空间的 个正交归一基.

$A$ 是一个观察算符, 所以至少有一个 $A$ 的正交归一 本征矢的集合可以用来构成态空间 $\mathscr{E}$ 的基. 将这些本征矢记作 $\left|u_{n}^{i}\right\rangle$ :
$$
A\left|u_{n}^{i}\right\rangle=a_{n}\left|u_{n}^{i}\right\rangle ;  n=1,2, \cdots ;i=1,2, \cdots, g_{n}
$$

$$
\left\langle u_{n}^{i} \mid u_{n^{\prime}}^{i^{\prime}}\right\rangle=\delta_{n n^{\prime}} \delta_{i i^{\prime}}
$$

当$n\ne n^{\prime}$,矩阵元 $\left\langle u_{n}^{i}|B| u_{n^{\prime}}^{i^{\prime}}\right\rangle$ 为零,则$B$在该表象下为一个分块对角矩阵。

$a_n$非简并，相应子块为$1\times 1$矩阵，即一个数，对应本征矢为$A,B$的共同本征矢。

$a_n$简并，在其本征子空间$\mathscr{E}_n$中，任意一个右矢均为其本征矢。任选其中一组基，$A$均为对角矩阵。由于$B$是厄密的，可以选取一组基，使$B$为对角的。则这组基也是$B$的本征矢。

综上所述

> $A$ 的属于简并本征值的本征矢不一定是 $B$ 的本征矢，但在 $A$ 的每一个本征子空间中, 总可以选出这 样一个基, 它是由 $A$ 和 $B$ 的共同本征矢构成的.

> **逆定理** 如果存在由 $A$ 和 $B$ 的共同本征矢 构成的一个基, 则这两个观察算符是对易的. 

> 观察算符$C=A+B \quad$ 而且 $[A, B]=0$，则$A,B$的共同本征矢也是$C$的本征矢，且其本征值有$a_n+b_p$的形式。

> 观察算符 $A, B, C \cdots$ 的一个集合成为**可对易观察算符的完全集合**(*ECOC*或*CSCO*)的条件是: 存在着由共同本征矢构成的一个正交归一基, 而且这个基是唯一的。

且有

* 所有算符两两对易
* 对全体算符本征值的一个组合，可以找到唯一的一个共同本征值。

## 坐标表象及动量表象

$$
\xi_{r_{0}}(r)=\delta\left(r-r_{0}\right)\Leftrightarrow\ket{r_0}
$$

$$
v_{p_{0}}(r)=(2 \pi \hbar)^{-3 / 2} \mathrm{e}^{\frac{1}{\hbar} p_{0} \cdot r}\Leftrightarrow\ket{p_0}
$$

即坐标表象和动量表象。
$$
\left\langle\boldsymbol{r}_{0} \mid \boldsymbol{r}_{0}^{\prime}\right\rangle=\int \mathrm{d}^{3} r \xi_{r_{0}}^{*}(\boldsymbol{r}) \xi_{r_{0}^{\prime}}(\boldsymbol{r})=\delta\left(\boldsymbol{r}_{0}-\boldsymbol{r}_{0}^{\prime}\right)
$$

$$
\left\langle\boldsymbol{p}_{0} \mid \boldsymbol{p}_{0}^{\prime}\right\rangle=\int \mathrm{d}^{3} r v_{p_{0}}^{*}(\boldsymbol{r}) v_{p_{0}^{\prime}}(\boldsymbol{r})=\delta\left(\boldsymbol{p}_{0}-\boldsymbol{p}_{0}^{\prime}\right)
$$

以上即为正交归一关系。

对任意右矢


$$
|\psi\rangle=\int \mathrm{d}^{3} r_{0}\left|\boldsymbol{r}_{0}\right\rangle\left\langle\boldsymbol{r}_{0} \mid \psi\right\rangle
$$

$$
|\psi\rangle=\int \mathrm{d}^{3} p_{0}\left|\boldsymbol{p}_{0}\right\rangle\left\langle\boldsymbol{p}_{0} \mid \psi\right\rangle
$$

$$
\left\langle\boldsymbol{r}_{0} \mid \psi\right\rangle=\int \mathrm{d}^{3} r \xi_{r_{0}}^{*}(\boldsymbol{r}) \psi(\boldsymbol{r})
$$

$$
\left\langle\boldsymbol{p}_{0} \mid \psi\right\rangle=\int \mathrm{d}^{3} r v_{p_{0}}^{*}(\boldsymbol{r}) \psi(\boldsymbol{r})
$$

则
$$
\left\langle\boldsymbol{r}_{0} \mid \psi\right\rangle=\psi\left(\boldsymbol{r}_{0}\right)
$$

$$
\left\langle\boldsymbol{p}_{0} \mid \psi\right\rangle=\bar{\psi}\left(\boldsymbol{p}_{0}\right)
$$

$\bar{\psi}(\boldsymbol{p})$ 是 $\psi(\boldsymbol{r})$ 的傅里叶变换.

> 由此可见, 波函数在点 $r_{0}$ 处的值 $\psi\left(\boldsymbol{r}_{0}\right)$ 就是右矢 $|\psi\rangle$ 在 $\left\{\left|\boldsymbol{r}_{0}\right\rangle\right\}$ 表象中的基矢 $\left|r_{0}\right\rangle$ 上的分量; “动量空间中的波函数" $\bar{\psi}(p)$ 也可以得到类似的解释. 

### 表象变换

$$
A\left(\boldsymbol{p}^{\prime}, \boldsymbol{p}\right)=(2 \pi \hbar)^{-3} \int \mathrm{d}^{3} r \int \mathrm{d}^{3} r^{\prime} \mathrm{e}^{\frac{1}{\hbar}\left(\boldsymbol{p} \cdot \boldsymbol{r}-\boldsymbol{p}^{\prime} \cdot \boldsymbol{r}^{\prime}\right)} A\left(\boldsymbol{r}^{\prime}, \boldsymbol{r}\right)
$$

### R算符和P算符

$$
\left|\psi^{\prime}\right\rangle=X|\psi\rangle
$$

在坐标表象中，
$$
\left\langle\boldsymbol{r} \mid \psi^{\prime}\right\rangle=\psi^{\prime}(\boldsymbol{r}) \equiv \psi^{\prime}(x, y, z)=X_\alpha\psi(x, y, z)
$$
由封闭性关系，
$$
\langle\varphi|X| \psi\rangle =\int \mathrm{d}^{3} r\langle\varphi \mid \boldsymbol{r}\rangle\langle\boldsymbol{r}|X| \psi\rangle 
=\int \mathrm{d}^{3} r \varphi^{*}(\boldsymbol{r}) X_alpha \psi(\boldsymbol{r})
$$
对动量算符$P_\alpha$在动量表象中
$$
\left\langle\boldsymbol{p}\left|P_{\alpha}\right| \psi\right\rangle=p_{\alpha}\langle\boldsymbol{p} \mid \psi\rangle
$$
在坐标表象中
$$
\left\langle\boldsymbol{r}\left|P_{x}\right| \psi\right\rangle =\int \mathrm{d}^{3} p\langle\boldsymbol{r} \mid \boldsymbol{p}\rangle\left\langle\boldsymbol{p}\left|P_{x}\right| \psi\right\rangle 
=(2 \pi \hbar)^{-3 / 2} \int \mathrm{d}^{3} p \mathrm{e}^{\frac{1}{\hbar} p \cdot \boldsymbol{r}} p_{x} \bar{\psi}(\boldsymbol{p})
$$
就是 $p_{x} \bar{\psi}(\boldsymbol{p})$ 的逆傅里叶变换, 根据傅里叶变换的性质，也就是 
$$
\frac{\hbar}{\mathrm{i}} \frac{\partial}{\partial x} \psi(\boldsymbol{r})
$$

$$
\langle\boldsymbol{r}|\boldsymbol{P}| \psi\rangle=\frac{\hbar}{\mathrm{i}} \nabla\langle\boldsymbol{r} \mid \psi\rangle
$$

故$P=-i\hbar\nabla$

矩阵元


$$
\left\langle\varphi\left|P_{x}\right| \psi\right\rangle =\int \mathrm{d}^{3} r\langle\varphi \mid \boldsymbol{r}\rangle\left\langle\boldsymbol{r}\left|P_{x}\right| \psi\right\rangle =\int \mathrm{d}^{3} r \varphi^{*}(\boldsymbol{r})\left[\frac{\hbar}{\mathrm{i}} \frac{\partial}{\partial x}\right] \psi(\boldsymbol{r})
$$
对易子
$$
\begin{aligned}
\left\langle\boldsymbol{r}\left|\left[X, P_{x}\right]\right| \psi\right\rangle &=\left\langle\boldsymbol{r}\left|\left(X P_{x}-P_{x} X\right)\right| \psi\right\rangle \\
&=x\left\langle\boldsymbol{r}\left|P_{x}\right| \psi\right\rangle-\frac{\hbar}{\mathrm{i}} \frac{\partial}{\partial x}\langle\boldsymbol{r}|X| \psi\rangle \\
&=\frac{\hbar}{\mathrm{i}} x \frac{\partial}{\partial x}\langle\boldsymbol{r} \mid \psi\rangle-\frac{\hbar}{\mathrm{i}} \frac{\partial}{\partial x} x\langle\boldsymbol{r} \mid \psi\rangle \\
&=\mathrm{i} \hbar\langle\boldsymbol{r} \mid \psi\rangle
\end{aligned}
$$
则$[X,P_x]=i\hbar$

> $X$和$P$算符均为厄密算符

$$
\langle\varphi|X| \psi\rangle =\int \mathrm{d}^{3} r \varphi^{*}(\boldsymbol{r}) x \psi(\boldsymbol{r}) =\left[\int \mathrm{d}^{3} r \psi^{*}(\boldsymbol{r}) x \varphi(\boldsymbol{r})\right]^{*} 
=\langle\psi|X| \varphi\rangle^{*}
$$

$$
\begin{aligned}
\left\langle\varphi\left|P_{x}\right| \psi\right\rangle &=\frac{\hbar}{\mathrm{i}} \int \mathrm{d} y \mathrm{~d} z \int_{-\infty}^{+\infty} \mathrm{d} x \varphi^{*}(\boldsymbol{r}) \frac{\partial}{\partial x} \psi(\boldsymbol{r}) \\
&=\frac{\hbar}{\mathrm{i}} \int \mathrm{d} y \mathrm{~d} z\left\{\left[\varphi^{*}(\boldsymbol{r}) \psi(\boldsymbol{r})\right]_{x=-\infty}^{x=+\infty}-\int_{-\infty}^{+\infty} \mathrm{d} x \psi(\boldsymbol{r}) \frac{\partial}{\partial x} \varphi^{*}(\boldsymbol{r})\right\}
\end{aligned}
$$

根据波函数的性质，在$\pm\infty$处趋于0，故前一项为0.
$$
\left\langle\varphi\left|P_{x}\right| \psi\right\rangle =-\frac{\hbar}{\mathrm{i}} \int \mathrm{d}^{3} r \psi(r) \frac{\partial}{\partial x} \varphi^{*}(r) 
=\left[\frac{\hbar}{\mathrm{i}} \int \mathrm{d}^{3} r \psi^{*}(r) \frac{\partial}{\partial x} \varphi(r)\right]^{*} =\left\langle\psi\left|P_{x}\right| \varphi\right\rangle^{*}
$$

$$
\left\langle\boldsymbol{r}|X| \boldsymbol{r}_{0}\right\rangle=x\left\langle\boldsymbol{r} \mid \boldsymbol{r}_{0}\right\rangle=x \delta\left(\boldsymbol{r}-\boldsymbol{r}_{0}\right)=x_{0} \delta\left(\boldsymbol{r}-\boldsymbol{r}_{0}\right)=x_{0}\left\langle\boldsymbol{r} \mid \boldsymbol{r}_{0}\right\rangle
$$

故$X\left|\boldsymbol{r}_{0}\right\rangle=x_{0}\left|\boldsymbol{r}_{0}\right\rangle$，即$x_0$为本征值，$r_0$为本征矢。故$\ket{r}$为$X,Y,Z$的共同本征矢。

同理，也有，$p_\alpha$为$\ket{p}$的本征值，$\ket{\mathbf{p}}$为算符$P_\alpha$的共同本征矢。

> $\hat{r}$和$\hat{p}$为观察算符。

> $\hat{r}$和$\hat{p}$为的分量各自构成$\mathscr{E}_r$中的一个CSCO

> $\{r_\alpha,p_\beta,p_\gamma\}$构成一个CSCO

### 坐标表象和动量表象的的薛定谔方程

$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t}|\psi(t)\rangle=H|\psi(t)\rangle
$$

$$
H=\frac{1}{2 m} \boldsymbol{P}^{2}+V(\boldsymbol{R})
$$

坐标表象中
$$
\mathrm{i} \hbar \frac{\partial}{\partial t}\langle\boldsymbol{r} \mid \psi(t)\rangle=\frac{1}{2 m}\left\langle\boldsymbol{r}\left|\boldsymbol{P}^{2}\right| \psi(t)\right\rangle+\langle\boldsymbol{r}|V(\boldsymbol{R})| \psi(t)\rangle
$$

$$
\mathrm{i} \hbar \frac{\partial}{\partial t} \psi(\boldsymbol{r}, t)=\left[-\frac{\hbar^{2}}{2 m} \Delta+V(\boldsymbol{r})\right] \psi(\boldsymbol{r}, t)
$$

动量表象中，
$$
\mathrm{i} \hbar \frac{\partial}{\partial t}\langle\boldsymbol{p} \mid \psi(t)\rangle=\frac{1}{2 m}\left\langle\boldsymbol{p}\left|\boldsymbol{P}^{2}\right| \psi(t)\right\rangle+\langle\boldsymbol{p}|V(\boldsymbol{R})| \psi(t)\rangle
$$

$$
\frac{\partial}{\partial t}\langle\boldsymbol{p} \mid \psi(t)\rangle=\frac{\partial}{\partial} \bar{\psi}(\boldsymbol{p}, t)
$$

$$
\left\langle\boldsymbol{p}\left|\boldsymbol{P}^{2}\right| \psi(t)\right\rangle=\boldsymbol{p}^{2} \bar{\psi}(\boldsymbol{p}, t)
$$

$$
\langle\boldsymbol{p}|V(\boldsymbol{R})| \psi(t)\rangle=\int \mathrm{d}^{3} p^{\prime}\left\langle\boldsymbol{p}|V(\boldsymbol{R})| \boldsymbol{p}^{\prime}\right\rangle\left\langle\boldsymbol{p}^{\prime} \mid \psi(t)\right\rangle=(2 \pi \hbar)^{-3 / 2} \int \mathrm{d}^{3} p^{\prime} \bar{V}\left(\boldsymbol{p}-\boldsymbol{p}^{\prime}\right) \bar{\psi}\left(\boldsymbol{p}^{\prime}, t\right)
$$

$\bar{V}(\boldsymbol{p})$ 是 $V(\boldsymbol{r})$ 的傅里叶变换。则
$$
\mathrm{i} \hbar \frac{\partial}{\partial t} \bar{\psi}(\boldsymbol{p}, t)=\frac{\boldsymbol{p}^{2}}{2 m} \bar{\psi}(\boldsymbol{p}, t)+(2 \pi \hbar)^{-3 / 2} \int \mathrm{d}^{3} p^{\prime} \bar{V}\left(\boldsymbol{p}-\boldsymbol{p}^{\prime}\right) \bar{\psi}\left(\boldsymbol{p}^{\prime}, t\right)
$$
即为坐标表象中方程的傅里叶变换。

## 态空间的张量积

对于每一对矢量 $|\varphi(1)\rangle \in \mathscr{E}_{1},|\chi(2)\rangle \in \mathscr{E}_{2}$, 都有 $\mathscr{E}$ 空间中的一个矢量 与之对应. 我们将这个矢量记作 $|\varphi(1)\rangle \otimes|\chi(2)\rangle$，为其张量积，则矢量空间 $\mathscr{E}$ 叫做 $\mathscr{E}_{1}$ 和 $\mathscr{E}_{2}$ 的张量积。若$\mathscr{E}_{1}$ 和 $\mathscr{E}_{2}$ 的维度为有限的$N_1,N_2$，则$\mathscr{E}$的维度为$N_1N_2$。

> 一个张量积矢量的分量就是该乘积中的两个矢量的分量之积.

$$
|\varphi(1)\rangle \otimes|\chi(2)\rangle=\sum_{i, l} a_{i} b_{l}\left|u_{i}(1)\right\rangle \otimes\left|v_{l}(2)\right\rangle
$$

> 在 $\mathscr{E}$ 空间中, 存在着这样的矢量, 它们并不是 $\mathscr{E}_{1}$ 空间中的矢量和 $\mathscr{E}_{2}$ 空间 中的矢量的张量积.  但是 $\mathscr{E}$ 空间中的任意一个矢量总可以分解为张量积矢量的线性组合.

标量积
$$
\left\langle\varphi^{\prime}(1) \chi^{\prime}(2) \mid \varphi(1) \chi(2)\right\rangle=\left\langle\varphi^{\prime}(1) \mid \varphi(1)\right\rangle\left\langle\chi^{\prime}(2) \mid \chi(2)\right\rangle
$$

> 如果每一个基 $\left\{\left|u_{i}(1)\right\rangle\right\}$ 和 $\left\{\left|v_{l}(2)\right\rangle\right\}$ 都是正交归一的, 那么基 $\left\{\left|u_{i}(1) v_{l}(2)\right\rangle=\left|u_{i}(1)\right\rangle \otimes\left|v_{l}(2)\right\rangle\right\}$ 也是正交归一的

$$
\left\langle u_{i^{\prime}}(1) v_{l^{\prime}}(2) \mid u_{i}(1) v_{l}(2)\right\rangle =\left\langle u_{i^{\prime}}(1) \mid u_{i}(1)\right\rangle\left\langle v_{l^{\prime}}(2) \mid v_{l}(2)\right\rangle 
=\delta_{i i^{\prime}} \delta_{l l^{\prime}}
$$

$\widetilde{A}(1)$, 叫做 $A(1)$ 在 $\mathscr{E}$ 空间中的**延伸算符**,若
$$
\widetilde{A}(1)[|\varphi(1)\rangle \otimes|\chi(2)\rangle]=[A(1)|\varphi(1)\rangle] \otimes|\chi(2)\rangle
$$
$A,B$算符的张量积
$$
[A(1) \otimes B(2)][|\varphi(1)\rangle \otimes|\chi(2)\rangle]=[A(1)|\varphi(1)\rangle] \otimes[B(2) \chi(2)]
$$

> 延伸算符为原算符和恒等算符的张量积

> 不同空间的延伸算符在张量积空间中对易

> 张量积空间里的投影算符为生成空间投影算符的张量积

### 张量积空间的本征值方程

在$\mathscr{E}_1$中
$$
A(1)\left|\varphi_{n}^{i}(1)\right\rangle=a_{n}\left|\varphi_{n}^{i}(1)\right\rangle ; \quad i=1,2, \cdots, g_{n}
$$
则在$\mathscr{E}$中，
$$
A(1)\left|\varphi_{n}^{i}(1)\right\rangle|\chi(2)\rangle =\left[A(1)\left|\varphi_{n}^{i}(1)\right\rangle\right]|\chi(2)\rangle 
=a_{n}\left|\varphi_{n}^{i}(1)\right\rangle|\chi(2)\rangle
$$
$a_n$仍为其本征值，形如$\ket{\varphi_n^i(1)}\ket{\chi(2)}$的一切矢量均为其本征矢。取$\{\ket{v_l(2)}\}$为$\mathscr{E}_2$中的一组基，则$\left|\psi_{n}^{i, l}\right\rangle=\left|\varphi_{n}^{i}(1)\right\rangle\left|v_{l}(2)\right\rangle$构成一组基。

> 1. 若 $A(1)$ 是 $\mathscr{E}_{1}$ 空间中的一个观察算符, 则它也是 $\mathscr{E}$ 空间中的观察算符.
> 1.  $A(1)$ 在 $\mathscr{E}$ 空间中的谱和它在 $\mathscr{E}_{1}$ 空间中的谱一样;
> 1. 在 $\mathscr{E}_{1}$ 空间中 $g_{n}$ 度简并的本征值 $a_{n}$ 在 $\mathscr{E}$ 空间中的简并度为 $N_{2} \times g_{n}$.

### 延伸算符和的本征值方程

$C=A(1)+B(2)$，$A,B$为各种空间的观察算符，若其的谱均为非简并的
$$
A(1)\left|\varphi_{n}(1)\right\rangle=a_{n}\left|\varphi_{n}(1)\right\rangle ，
B(2)\left|\chi_{p}(2)\right\rangle=b_{p}\left|\chi_{p}(2)\right\rangle
$$

$$
A(1)\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle=a_{n}\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle
$$

$$
B(2)\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle=b_{p}\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle
$$

$A(1)$ 和 $B(2)$ 是可对易的，而且构成 $\mathscr{E}$ 空间的基的诸矢量 $\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle$ 是 $A(1)$ 和 $B(2)$ 的共同本征矢，同时也是$C$的本征矢：
$$
C\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle=\left(a_{n}+b_{p}\right)\left|\varphi_{n}(1)\right\rangle\left|\chi_{p}(2)\right\rangle
$$

> $C=A(1)+B(2)$ 的本征值是 $A(1)$ 的一个本征值与 $B(2)$ 的一个本征值 之和;由 $C$ 的本征矢构成的一个基, 其中的基矢是 $A(1)$ 的一个本征矢和 $B(2)$ 的一个本征矢的张量积.

若不存在$a_n+b_p=a_m+b_q$，则$C$的本征值是非简并的

若存在$a_n+b_p=a_m+b_q$则$C$的本征矢为张量积的线性组合，不一定是张量积。

### 张量积空间中的CSCO

不失一般性，假设 $\mathscr{E}_{1}$ 空间中的 $A(1)$ 本身就是一个 CSCO, 而 $\mathscr{E}_{2}$ 空间中的 CSCO 则包含两个观察算符 $B(2)$ 与 $C(2)$. 在$\mathscr{E}$中，$A(1)$的每一个本征值都是$N_2$重简并的，其不再构成一个CSCO，同理，$\{B(2),C(2)\}$也不是。但有
$$
A(1)\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle=a_{n}\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle
$$

$$
B(2)\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle=b_{p}\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle
$$

$$
C(2)\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle=c_{r}\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle
$$

由于 $\left\{\left|\varphi_{n}(1)\right\rangle\right\}$ 与 $\left\{\left|\chi_{p r}(2)\right\rangle\right\}$ 分别为 $\mathscr{E}_{1}$ 与 $\mathscr{E}_{2}$ 中的基, 因此, 集合 $\left\{\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle\right\}$ 构成 $\mathscr{E}$ 中的一个基. 此外, 如果取定本征值的一个数组 $\left\{a_{n}, b_{p}, c_{r}\right\}$, 那么与此 对应的只有一个矢量 $\left|\varphi_{n}(1) \chi_{p r}(2)\right\rangle$; 因此 $A(1) 、 B(2)$ 与 $C(2)$ 便构成 $\mathscr{E}$ 空间中 的一个 ECOC.

> 若在 $\mathscr{E}_{1}$ 与 $\mathscr{E}_{2}$ 中各有一个可对易观察算符的完全集 合, 则将此两集合合并起来便得到 $\mathscr{\varphi}$ 中的一个可对易观察算符的完全集合.

### 应用

#### 一维和三维空间中的态

$$
\mathscr{E}_{x y z}=\mathscr{E}_{x} \otimes \mathscr{E}_{y} \otimes \mathscr{E}_{z}
$$

三维空间为三个分量的一维空间的张量积。任意一维空间的CSCO的组合构成三维空间的一个CSCO。

设算符$H=H_{x}+H_{y}+H_{z}$,其本征值为$E_x^n,E_y^p,E_z^r$，则$H$的全体本征值形如$E^{n, p, r}=E_{x}^{n}+E_{y}^{p}+E_{z}^{r}$

#### 双粒子体系的态

$$
\mathscr{E}_{r_{1} r_{2}}=\mathscr{E}_{r_{1}} \otimes \mathscr{E}_{r_{2}}
$$

> 双粒子体系的态空间是对应于每个粒子的态 空间的张量积. 

假设体系的态可以用张量积右矢$|\psi\rangle=\left|\psi_{1}\right\rangle\left|\psi_{2}\right\rangle$描述，则波函数可分解为
$$
\psi\left(\boldsymbol{r}_{1}, \boldsymbol{r}_{2}\right)=\left\langle\boldsymbol{r}_{1}, \boldsymbol{r}_{2} \mid \psi\right\rangle=\left\langle\boldsymbol{r}_{1} \mid \psi_{1}\right\rangle\left\langle\boldsymbol{r}_{2} \mid \psi_{2}\right\rangle=\psi_{1}\left(\boldsymbol{r}_{1}\right) \psi_{2}\left(\boldsymbol{r}_{2}\right)
$$
此时两个粒子之间没有联系。

> 如果一个物理体系由两个或更多的简单体系 组合而成, 则它的态空间就是对应于每一个组分体系的态空间的张量积.

## 宇称算符

$$
\Pi|\boldsymbol{r}\rangle=|-\boldsymbol{r}\rangle
$$

在坐标表象中
$$
\left\langle\boldsymbol{r}|\Pi| \boldsymbol{r}^{\prime}\right\rangle=\left\langle\boldsymbol{r} \mid-\boldsymbol{r}^{\prime}\right\rangle=\delta\left(\boldsymbol{r}+\boldsymbol{r}^{\prime}\right)
$$

> $I I$ 在 $\{|r\rangle\}$ 表象中的作用就是将 $r$ 换成 $-r$ .

$$
\Pi^{2}=1
$$

$$
\Pi^{\dagger}=\Pi
$$

其为二米算符和幺正算符。

> $\Pi$ 的本征值只能为 1 或 $-1$，且均为简并的。

> $\mathscr{E}_{r}$ 中的一个任意右矢 $|\psi\rangle$ 可以分解为 $\Pi$ 的两个本征矢 $\left|\psi_{+}\right\rangle$ 与 $\left|\psi_{-}\right\rangle$之和, 这两个本征矢分别属于偶性子空间 $\mathscr{E}_{+}$及奇性子空间 $\mathscr{E}_{-}$. 因此 $\Pi$ 是一个观察算符.

$$
\widetilde{B}=\Pi B \Pi
$$

* 算符 $\widetilde{B}$ 叫做 $B$ 的宇称变换算符.
* 若 $\widetilde{B}=+B$, 则我们称 $B$ 为偶算符;
* 若 $\widetilde{B}=-B$, 则我们称 $B$ 为奇算符;

> $\left[\Pi, B_{+}\right]=0$偶算符和宇称算符对易。奇算符反对易。

> 一个偶算符在宇称相反的矢量之间的矩阵元为零.
>
> 一个奇算符在宇称相同的矢量之间的矩阵元为零.
>
> 一个奇算符矩阵的对角元在 $|\psi\rangle$ 具有确定的宇称时应为零.

> $R,P$为奇算符，$\Pi$为偶算符

> 一个偶算符的任意幂还是偶算符，其算符函数也是偶算符。

> 一个奇算符的偶次幂是一个偶算符, 奇次幂是一个奇算符. 再考虑 算符 $F\left(B_{-}\right)$; 当对应的函数 是偶函数时, 是一个偶算符, 是奇函数时, 是一个奇算符. 一般地说, 没有确定的宇称.

任意的偶性观察算符 $B_{+},\left|\varphi_{b}\right\rangle$ 是它的一个本征矢，本征值为$b$，则

* 若 $b$ 是非简并的本征值, 则 $\left|\varphi_{b}\right\rangle$ 一定是 $\Pi$ 的本征矢; 因此, 这个矢量或 是偶性的, 或是奇性的. 从而一切奇性观察算符 $B_{-}$(诸如 $\boldsymbol{R} 、 \boldsymbol{P}$ 等) 的平均值 $\left\langle\varphi_{b}\left|B_{-}\right| \varphi_{b}\right\rangle$ 都等于零.
* 若 $b$ 是简并的本征值, 对应本征子空间是 $\mathscr{E}_{b}$, 则空间 $\mathscr{E}_{b}$ 中的矢量不一 定都有确定的宇称. 但这个矢量仍属于同一本征值 $b$. 此外, 在每一个子空间 $\mathscr{E}_{b}$ 中都可以找到由 $\Pi$ 和 $B_{+}$的共同本征矢构成的一个基（因为两者对易）.

算符 $\boldsymbol{P}$ 是奇性的, 故 $\boldsymbol{P}^{2}$ 是偶性的, 因而, 若函数 $V(\boldsymbol{r})$ 也是偶性的 $[V(\boldsymbol{r})=$ $V(-r)]$, 则算符 $H$ 便是偶性的. 可以找到 $H$ 在偶 性态中或奇性态中的本征态, 这往往使计算大为简化.

假设 $H$ 是偶算符, 它的一个没有确定宇称的本征态为$\left|\varphi_{h}\right\rangle$ 。那么, 对应的本征值是简并的. 由于 $\Pi$ 可以和 $H$ 对易, 因此, $\Pi\left|\varphi_{h}\right\rangle$ 是 $H$ 的 本征矢, 与 $\left|\varphi_{h}\right\rangle$ 同属一个本征值.