# 周期势场

我们将要考虑的函数不一定是严格意义下的周期函数, 只要它在 $O x$ 轴上一 段有限区间内具有周期函数的形状即可也就是说, 它可以是同一个 图案顺次重复出现 $N$ 次的结果 [仅在 $N$ 为无限大的极限情况下, $V(x)$ 才是真 正的周期函数].

![image-20211220150703090](https://s2.loli.net/2021/12/20/btVYyEFLupIUJxQ.png)
$$
\left\{\frac{\mathrm{d}^{2}}{\mathrm{~d} x^{2}}+\frac{2 m}{\hbar^{2}}[E-V(x)]\right\} \varphi_{\alpha}(x)=0，\alpha=\sqrt{\frac{2 m E}{\hbar^{2}}}
$$
在第N个势垒左侧，$V(x)=0$，
$$
\varphi_{\alpha}(x)=A_{0} \mathrm{e}^{\mathrm{i} \alpha x}+A_{0}^{\prime} \mathrm{e}^{-\mathrm{i} \alpha x},x\le-\frac{l}{2}
$$
在以$x=(n-1)l$为中心的第$n$个势垒的范围内
$$
\varphi_{\alpha}(x)=A_{n} v_{\alpha}[x-(n-1) l]+A_{n}^{\prime} v_{\alpha}^{\prime}[x-(n-1) l]
$$

$$
(n-1) l-\frac{l}{2} \leqslant x \leqslant(n-1) l+\frac{l}{2}
$$

在第N个势垒右侧，$V(x)=0$，
$$
\varphi_{\alpha}(x)=C_{0} \mathrm{e}^{\mathrm{i} \alpha[x-(N-1) l]}+C_{0}^{\prime} \mathrm{e}^{-\mathrm{i} \alpha[x-(N-1) l]}
$$

$$
x \geqslant(N-1) l+\frac{l}{2}
$$

$$
\left(\begin{array}{l}
\tilde{A}_{n} \\
\tilde{A}_{n}^{\prime}
\end{array}\right)=M(\alpha)\left(\begin{array}{l}
A_{n} \\
A_{n}^{\prime}
\end{array}\right)
$$

按照衔接条件有
$$
\left\{\begin{array}{l}
A_{0}=A_{1} \\
A_{0}^{\prime}=A_{1}^{\prime}
\end{array}\right.
$$

$$
\left\{\begin{array}{l}
A_{n+1}=\tilde{A}_{n} \mathrm{e}^{\mathrm{i} \alpha l} \\
A_{n+1}^{\prime}=\tilde{A}_{n}^{\prime} \mathrm{e}^{-\mathrm{i} \alpha l}
\end{array}\right.
$$

$$
\left\{\begin{array}{l}
C_{0}=\tilde{A}_{N} \\
C_{0}^{\prime}=\tilde{A}_{N}^{\prime}
\end{array}\right.
$$

定义矩阵
$$
D(\alpha)=\left(\begin{array}{cc}
\mathrm{e}^{\mathrm{i} \alpha l} & 0 \\
0 & \mathrm{e}^{-\mathrm{i} \alpha l}
\end{array}\right)
$$

$$
\left(\begin{array}{l}
A_{n+1} \\
A_{n+1}^{\prime}
\end{array}\right)=D(\alpha)\left(\begin{array}{c}
\tilde{A}_{n} \\
\tilde{A}_{n}^{\prime}
\end{array}\right)=D(\alpha) M(\alpha)\left(\begin{array}{c}
A_{n} \\
A_{n}^{\prime}
\end{array}\right)
$$

$$
\left(\begin{array}{c}
A_{n+1} \\
A_{n+1}^{\prime}
\end{array}\right) &=[D(\alpha) M(\alpha)]^{n}\left(\begin{array}{c}
A_{1} \\
A_{1}^{\prime}
\end{array}\right)
=[D(\alpha) M(\alpha)]^{n}\left(\begin{array}{c}
A_{0} \\
A_{0}^{\prime}
\end{array}\right)
$$

$$
\left(\begin{array}{l}
C_{0} \\
C_{0}^{\prime}
\end{array}\right)=M(\alpha)\left(\begin{array}{l}
A_{N} \\
A_{N}^{\prime}
\end{array}\right)=M(\alpha)[D(\alpha) M(\alpha)]^{N-1}\left(\begin{array}{l}
A_{0} \\
A_{0}^{\prime}
\end{array}\right)
$$

$$
Q(\alpha)=D(\alpha)M(\alpha)=\left(\begin{array}{cc}
\mathrm{e}^{\mathrm{i} \alpha l} F(\alpha) & \mathrm{e}^{\mathrm{i} \alpha l} G^{*}(\alpha) \\
\mathrm{e}^{-\mathrm{i} \alpha l} G(\alpha) & \mathrm{e}^{-\mathrm{i} \alpha l} F^{*}(\alpha)
\end{array}\right)
$$

称为迭代矩阵。

$\lambda$为$Q(\alpha)$的一个本征值，则本征方程为
$$
\left[\mathrm{e}^{\mathrm{i} \alpha l} F(\alpha)-\lambda\right]\left[\mathrm{e}^{-\mathrm{i} \alpha l} F^{*}(\alpha)-\lambda\right]-|G(\alpha)|^{2}=0
$$

$$
\lambda^{2}-2 \lambda X(\alpha)+1=0
$$

利用透射率加反射率为1。
$$
X(\alpha)=\operatorname{Re}\left[\mathrm{e}^{\mathrm{i} \alpha l} F(\alpha)\right]=\frac{1}{2} \operatorname{Tr} Q(\alpha)
$$
本征方程判别式为
$$
\Delta^{\prime}=[X(\alpha)]^{2}-1
$$
若$|X(\alpha)| \leqslant 1$

令$X(\alpha)=\cos [k(\alpha) l]$

则
$$
\lambda=\mathrm{e}^{\pm \mathrm{i} k(\alpha) l}，0\le k(\alpha)\le\frac\pi l
$$
$$
|\lambda|=1
$$



若$|X(\alpha)|>1$

令$X(\alpha)=\varepsilon \cosh [\rho(\alpha) l]$
$$
\lambda=sgn(X(\alpha))\mathrm{e}^{\pm \rho(\alpha) l}
$$

$$
\lambda_1\lambda_2=1,\lambda\in R
$$

## 允带和禁带

$Q(\alpha)$对应$\lambda_1,\lambda_2$的本征矢分别为$\Lambda_1(\alpha),\Lambda_2(\alpha)$
$$
\left(\begin{array}{l}
A_{1} \\
A_{1}^{\prime}
\end{array}\right)=c_{1}(\alpha) \Lambda_{1}(\alpha)+c_{2}(\alpha) \Lambda_{2}(\alpha)
$$

$$
\left(\begin{array}{l}
A_{n} \\
A_{n}^{\prime}
\end{array}\right)=\lambda_{1}^{n-1} c_{1}(\alpha) \Lambda_{1}(\alpha)+\lambda_{2}^{n-1} c_{2}(\alpha) \Lambda_{2}(\alpha)
$$

![](https://s2.loli.net/2021/12/21/3fvZ5u8xeQIXBVn.png)

> 复数 $\mathrm{e}^{\mathrm{i} \alpha l} F(\alpha)=X(\alpha)+\mathrm{i} Y(\alpha)$ 随 $\alpha$ 变化的情况. 由于 $|F(\alpha)|>1$, 所以在复平面 上作出的曲线应在以 $O$ 点为圆心的单位圆外. 正文中的讨论表明, 如果 $|X(\alpha)|$ 小于 1 , 也就是说, 如果由已选定的 $\alpha$ 值所确定的曲线上的点位于图中的两条垂直虚线之间, 那么, 对应的能量便落在 “容许能带" 内; 反之, 对应的能量便落在 “禁戒能带” 内.

$|X(\alpha)|\gt 1$,对于充分大的$n$，对小于1的特征值，该项可忽略不计。另一项趋于无穷大。
$$
\left(\begin{array}{l}
A_{n} \\
A_{n}^{\prime}
\end{array}\right) \simeq \varepsilon^{n-1} \mathrm{e}^{(n-1) \rho(\alpha) l} c_{1}(\alpha) \Lambda_{1}(\alpha)
$$
因而 $A_{n}$ 和 $A_{n}^{\prime}$ 是按指数律随 $n$ 增大的 $\left[c_{1}(\alpha)=0\right.$ 的特殊情况除外; 由此可见, 顺次通过一个一个的势垒, 波函数 $\varphi_{\alpha}(x)$ 的模将变得越来越大, 它的行为很像 实指数函数叠加结果的行为.

$|X(\alpha)|\le 1$ 通过 一连串势垒的效果表现为列矩阵 $\left(\begin{array}{l}A_{n} \\ A_{n}^{\prime}\end{array}\right)$ 的两个分量相对于 $\Lambda_{1}(\alpha)$ 和 $\Lambda_{2}(\alpha)$ 的相移. 这时 $\varphi_{\alpha}(x)$ 的行为类似于虚指数函数的叠加结果的行为. 

### 能量量子化

![image-20211221225130840](https://s2.loli.net/2021/12/21/iHyslcxekV2uGOr.png)

$[0, N l]$ 为 “昌格的内部”, 而称点 $x \simeq-\frac{l}{2}$ 附近和 $x \simeq N l+\frac{l}{2}$ 附近为 “晶格的端点(或边缘)“
$$
\begin{array}{l}
c_{1}(\alpha) \Lambda_{1}(\alpha)=\left(\begin{array}{l}
f_{1}(\alpha) \\
f_{1}^{\prime}(\alpha)
\end{array}\right) \\
c_{2}(\alpha) \Lambda_{2}(\alpha)=\left(\begin{array}{l}
f_{2}(\alpha) \\
f_{2}^{\prime}(\alpha)
\end{array}\right)
\end{array}
$$

$$
A_{n}=f_{1}(\alpha) \lambda_{1}^{n-1}+f_{2}(\alpha) \lambda_{2}^{n-1}
$$

$$
A_{n}^{\prime}=f_{1}^{\prime}(\alpha) \lambda_{1}^{n-1}+f_{2}^{\prime}(\alpha) \lambda_{2}^{n-1}
$$

舍去一个解 $e^{-\mu(\alpha) x}$, 因为它在 $x \rightarrow-\infty$ 时是发散的
$$
\varphi_{\alpha}(x)=B \mathrm{e}^{\mu(\alpha) x}
$$

$$
\mu(\alpha)=\sqrt{\frac{2 m}{\hbar^{2}}\left(V_{e}-E\right)}
$$

$$
\frac{A_{1}}{A_{1}^{\prime}}=\mathrm{e}^{\mathrm{i} \chi(\alpha)}
$$

式中 $\chi(\alpha)$ 是 $\alpha$ 的 (因而也是能量 $E$ 的) 实函数, 它依赖于 $V(x)$ 在晶格左端边缘处的 变化细节 

同样的推理显然也适用于右端 $(x \rightarrow+\infty)$
$$
\frac{A_{N+1}}{A_{N+1}^{\prime}}=e^{i \chi^{\prime}(\alpha)}
$$
由于 $\varphi_{\alpha}(x)$ 只能确定到差一个常数因子, 所以我们可以选择
$$
A_{1}=\mathrm{e}^{\mathrm{i} \chi(\alpha) / 2},A_{1}^{\prime}=\mathrm{e}^{-\mathrm{i} \chi(\alpha) / 2}
$$
计算 $A_{n}$ 和 $A_{n}^{\prime}$ 一定得到
$$
A_{n}^{\prime}=A_{n}^{*}
$$
比值 $A_{N+1}/A_{N+1}^{\prime}$ 必然是模等于 1 的复数;

### 允带

$$
A_{n}=f_{1}(\alpha) \mathrm{e}^{\mathrm{i}(n-1) k(\alpha) l}+f_{2}(\alpha) \mathrm{e}^{-\mathrm{i}(n-1) k(\alpha) l}
$$

$$
A_{n}^{\prime}=f_{1}^{\prime}(\alpha) \mathrm{e}^{\mathrm{i}(n-1) k(\alpha) l}+f_{2}^{\prime}(\alpha) \mathrm{e}^{-\mathrm{i}(n-1) k(\alpha) l}
$$

$$
f_{1}^{*}(\alpha)=f_{2}^{\prime}(\alpha)
$$

$$
f_{2}^{*}(\alpha)=f_{1}^{\prime}(\alpha)
$$

$$
\frac{f_{1}(\alpha) \mathrm{e}^{2 \mathrm{i} N k(\alpha) l}+f_{2}(\alpha)}{f_{2}^{*}(\alpha) \mathrm{e}^{2 \mathrm{i} N k(\alpha) l}+f_{1}^{*}(\alpha)}=\mathrm{e}^{\mathrm{i} \chi^{\prime}(\alpha)}
$$

$$
\Theta(\alpha)=\operatorname{Arg}\left\{\frac{f_{1}^{*}(\alpha) \mathrm{e}^{\mathrm{i} \chi^{\prime}(\alpha) / 2}-f_{2}(\alpha) \mathrm{e}^{-\mathrm{i} \chi^{\prime}(\alpha) / 2}}{f_{1}(\alpha) \mathrm{e}^{-\mathrm{i} \chi^{\prime}(\alpha) / 2}-f_{2}^{*}(\alpha) \mathrm{e}^{\mathrm{i} \chi^{\prime}(\alpha) / 2}}\right\}
$$

$$
\mathrm{e}^{2 \mathrm{i} N k(\alpha) l}=\mathrm{e}^{\mathrm{i} \theta(\alpha)}
$$

能级为
$$
k(\alpha)=\frac{\Theta(\alpha)}{2 N l}+p \frac{\pi}{N l}\quad
p=0,1,2, \cdots,(N-1)
$$
若$N$非常大，则
$$
k(\alpha) \simeq p \frac{\pi}{N l}
$$
![image-20211221234343967](https://s2.loli.net/2021/12/21/9SRK7hsHtqfny4I.png)

---

图解法

如果将 $k(\alpha)$的定义式代入 式中, 我们便得到关于 $\alpha$ 的一个方程, 由它 便可确定能量的容许值. 为了用图解法来解这个方程, 我们先作出表示函数 $X(\alpha)=$ $\operatorname{Re}\left[\mathrm{e}^{\mathrm{i} \alpha l} F(\alpha)\right]$ 的曲线; 由于这里含有虚指数函数 $\mathrm{e}^{\mathrm{i} \alpha l}$, 可以料到这曲线具有振荡特性. 由于 $|F(\alpha)|$ 比 1 大 , 故振荡的幅度比 1 大, 以至于曲线与两直线 $X(\alpha)=\pm 1$ 相交于很多点, 交点处的 $\alpha=\alpha_{0}, \alpha_{1}, \alpha_{2}, \cdots$ 在 $\alpha$ 轴上这些交点之间的区域内, 如果条件 $|X(\alpha)|<1$ 不成立, 我们便将这些区域一律舍 去; 这样便得到曲线 $X(\alpha)$ 上的很多弧段, 利用这些弧便可将函数 $k(\alpha)$ 表示为:
$$
k(\alpha)=\frac{1}{l} \text { Arc } \cos X(\alpha)
$$
 由这条曲线与曲线
$$
\frac{\Theta(\alpha)}{2 N l}+p \frac{\pi}{N l}
$$
若 $N \gg 1$, 这些曲线实际上是水平直线 
$$
y=p \frac{\pi}{N l}(p=0,1,2, \cdots, N-1)
$$
的交点便可以决定各能级.

---

![image-20211222203808812](https://s2.loli.net/2021/12/22/iFZru4gBSLckxnO.png)

> 能量随参变量 $k$ 变化的情况. 实曲线表示头两个容许能带中的能量 (确定各 能级的 $k$ 的值在 $0 \leqslant k \leqslant \frac{\pi}{l}$ 区间中是等间距的). 虚曲线对应于 $V(x)$ 为零 (自由粒子) 的 特例; 这时容许能带邻接, 禁戒能带不复存在.
>
> 给定 $k$ 的一个值, 便有 $\alpha$ 的若干个 (亦即能量的 若干个) 对应值; 因此, 在图中出现若干段弧线. 但是, 在某一指定的容许能 带内, 如果 $X(\alpha)$ 不断从 $-1$ 增加到 $+1$ (或不断从 $+1$ 减少到 $-1$ ), 那么, 在这个 能带中, 与 $k$ 的每一个值对应的能级只有一个, 因而, 这个能带包含 $N$ 个能级.
>
> 表示能量的曲线在点 $k=0$ 及 $k=\pi / l$ 处 (容许能带的边缘) 的方向趋于水平 方向. 与自由粒子的情况相反, 对于每一个能带而言, 都存在一个转折点, 在这里能量 随 $k$ 线性地变化.

可以看出很重要的一点: 通过函数 $\chi(\alpha)$, $\chi^{\prime}(\alpha)$ [或通过 $\Theta(\alpha)$ ] 才能引人的晶格边缘的效应, 当 $N$ 很大时不会产 生任何影响; 为了确定可能的能量值, 只有晶格内部的周期势的形状才是重要的.

#### 自由粒子

$$
\left\{\begin{array}{l}
F(\alpha)=1 \\
X(\alpha)=\cos \alpha l
\end{array}\right.
$$

$$
\left\{\begin{array}{ll}
 0 \leqslant \alpha \leqslant \pi / l: & k(\alpha)=\alpha \\
 \frac{\pi}{l} \leqslant \alpha \leqslant \frac{2 \pi}{l}: & k(\alpha)=\frac{2 \pi}{l}-\alpha
\end{array}\right.
$$

 $|X(\alpha)| \leqslant 1$ 是永远 具备的,  就自由粒子而言, 禁戒能带是不存在的.

#### 透射系数的影响

透射系数 $T(\alpha)$ 实际上等于零,
$$
\left\{\begin{array}{l}
|F(\alpha)| \gg 1 \\
|G(\alpha)| \gg 1
\end{array}\right.
$$
此时, 在透射系数为零的极限情况下, 这些能带就变成孤立势阱中 的一个个的能级. 反之, 只要粒子通过隧道效应从一个势阱进人下一个势阱, 那么, 势阱中的每一个分立能级都产生一个能带, 透射系数越大, 能带越宽.

### 禁带

$$
\left\{\begin{array}{l}
A_{n}=\varepsilon^{n-1}\left[f_{1}(\alpha) \mathrm{e}^{(n-1) \rho(\alpha) l}+f_{2}(\alpha) \mathrm{e}^{-(n-1) \rho(\alpha) l}\right] \\
A_{n}^{\prime}=\varepsilon^{n-1}\left[f_{1}^{\prime}(\alpha) \mathrm{e}^{(n-1) \rho(\alpha) l}+f_{2}^{\prime}(\alpha) \mathrm{e}^{-(n-1) \rho(\alpha) l}\right]
\end{array}\right.
$$

对任意的 $n, A_{n}^{\prime}=A_{n}^{*}$
$$
\left\{\begin{array}{l}
f_{1}^{\prime}(\alpha)=f_{1}^{*}(\alpha) \\
f_{2}^{\prime}(\alpha)=f_{2}^{*}(\alpha)
\end{array}\right.
$$

$$
\frac{A_{N+1}}{A_{N+1}^{\prime}}=\frac{f_{1}(\alpha)+f_{2}(\alpha) \mathrm{e}^{-2 N \rho(\alpha) l}}{f_{1}^{*}(\alpha)+f_{2}^{*}(\alpha) \mathrm{e}^{-2 N \rho(\alpha) l}}=\mathrm{e}^{\mathrm{i} \chi^{\prime}(\alpha)}
$$

令
$$
\mathrm{e}^{-2 N \rho(\alpha) l}=L(\alpha)
$$

$$
L(\alpha)=-\frac{f_{1}^{*}(\alpha) \mathrm{e}^{\mathrm{i} \chi^{\prime}(\alpha) / 2}-f_{1}(\alpha) \mathrm{e}^{-\mathrm{i} \chi^{\prime}(\alpha) / 2}}{f_{2}^{*}(\alpha) \mathrm{e}^{\mathrm{i} \chi^{\prime}(\alpha) / 2}-f_{2}(\alpha) \mathrm{e}^{-\mathrm{i} \chi^{\prime}(\alpha) / 2}}
$$

$N \gg 1$ 的情况; 这时 $\mathrm{e}^{-2 N \rho(\alpha) t} \simeq 0$,
$$
L(\alpha)=0
$$
禁戒能带中的能级决定于函数 $L(\alpha)$ 的零点 (参看图 3-36). 由于 $N$ 既不出现在式中,  所以这些能级的数目与 $N$ 无关 (这与容许能带中的 能级数相反). 因而, 当 $N \gg 1$ 时, 我们可以说, 实际上所有的能级都被纳人容许能带 之中.

![image-20211222220852243](https://s2.loli.net/2021/12/22/wNdqabj9F7t3pGe.png)

对于禁带, $N$ 这个数, 亦即晶格的 长度, 只要充分大, 是不起作用的; 而函数 $\chi(\alpha)$ 和 $\chi^{\prime}(\alpha)$ 起着重要作用. 这些函数与 $V(x)$ 在晶格边缘上的行为有关, 因此, 可以 预期得到定域在这些区域中的态.