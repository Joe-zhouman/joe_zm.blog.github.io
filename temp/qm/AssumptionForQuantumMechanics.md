# 假定

> 在确定的时刻 $t_{0}, 一 个$ 物理体系的态由态空间 $\mathscr{E}$ 中一个特定 的右矢 $\left|\psi\left(t_{0}\right)\right\rangle$ 来确定.

> 每一个可以测量的物理量 $\mathscr{A}$ 都可以用在 $\mathscr{E}$ 空间中起作用的 一个算符 $A$ 来描述; 这个算符是一个观察算符.

> 每次测量物理量 $\mathscr{A}$, 可能得到的结果, 只能是对应的观察算符 $A$ 的本征值之一.

> 若体系处于已归一化的态 $|\psi\rangle$ 中, 则测量物理量 $\mathscr{A}$ 得到的结果为对应观察算符 $A$ 的非简并本征值 $a_{n}$ 的概率 $\mathscr{P}\left(a_{n}\right)$ 是:$\left|\left\langle u_{n} \mid \psi\right\rangle\right|^{2}$，$\ket{u_n}$为$A$的属于$a_n$的本征矢。对应观察算符 $A$ 的简并本征值 $a_{n}$ 的概率 $\mathscr{P}\left(a_{n}\right)$ 是:$\sum_{i=1}^{g_{n}}\left|\left\langle u_{n}^{i} \mid \psi\right\rangle\right|^{2}$
>
> 对连续谱，介于$(\alpha,\alpha+d\alpha)$之间的概率为$\mathrm{d} \mathscr{P}(\alpha)=\left|\left\langle v_{\alpha} \mid \psi\right\rangle\right|^{2} \mathrm{~d} \alpha$

一些推论

* 互成比例的两个态矢量表示同一个物理状态.
* $|\varphi\rangle=\lambda_{1} \mathrm{e}^{\mathrm{i} \theta_{1}}\left|\psi_{1}\right\rangle+\lambda_{2} \mathrm{e}^{\mathrm{i} \theta_{2}}\left|\psi_{2}\right\rangle$并不描述与 $|\psi\rangle$ 相同的态。
* 总的相位因子对于物理预言没有影响, 但展开式中各系数的相对相位则有影响。

> 如果对处于 $|\psi\rangle$ 态的体系测量物理量 $\mathscr{A}$ 得到的结果是 $a_{n}$, 则 刚测量之后体系的态是 $|\psi\rangle$ 在属于 $a_{n}$ 的本征子空间上的归一化的投影 ${P_{n}|\psi\rangle}/{\sqrt{\left\langle\psi\left|P_{n}\right| \psi\right\rangle}} .$

## 波函数的坍塌

假设我们希望在指定的时刻测量物理量 $\mathscr{A}$, 如果我们已知刚要测量时描 述体系状态的右矢 $|\psi\rangle$, 那么 就可以按预言得到各种可能结果 的概率. 但是在实际进行一次测量时, 我们所得到的结果显然只是这些可能结果中的一个. 刚测量之后, 就不能说 “得到这个结果或得到那个结果的概率” 了, 这是因为我们已经知道实际上得到的是哪一个结果了. 刚测量之后体系所处的状态与 $|\psi\rangle$ 态是不同的.

如果紧接着第一次测量 (即在体系的态还来不及演变时) 再对 $\mathscr{A}$ 进行第二次测量, 那么,一定得到同样的结果 $a_{n}$, 这是因为刚要进行第二 次测量时, 体系的态不是 $|\psi\rangle$ 而是 $\left|u_{n}\right\rangle$.

> 态矢量 $|\psi(t)\rangle$ 随时间的演变遵从薛定谔方程:

$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t}|\psi(t)\rangle=H(t)|\psi(t)\rangle
$$

## 量子化

要得到描述一个已有经典定义的物理量 $\mathscr{A}$ 的观察算符 $A$, 只需在 $\mathscr{A}$ 的经 过适当对称化的表达式中, 将 $\boldsymbol{r}$ 与 $\boldsymbol{p}$ 分别换成观察算符 $\boldsymbol{R}$ 与 $\boldsymbol{P}$.在涉及到$\boldsymbol{r} , \boldsymbol{p}$的非线性项是, 我们要加上一条对称化规则. 例如, 和 $\boldsymbol{r} \cdot \boldsymbol{p}$ 相联系的 观察算符将是
$$
\frac{1}{2}(\boldsymbol{R} \cdot \boldsymbol{P}+\boldsymbol{P} \cdot \boldsymbol{R})
$$

---

标量场中，哈密顿函数为
$$
\mathscr{H}(\boldsymbol{r} \cdot \boldsymbol{p})=\frac{\boldsymbol{p}^{2}}{2 m}+V(\boldsymbol{r})
$$
则
$$
H=\frac{\boldsymbol{P}^{2}}{2 m}+V(\boldsymbol{R})
$$
电磁场中
$$
\mathscr{H}(\boldsymbol{r}, \boldsymbol{p})=\frac{1}{2 m}[\boldsymbol{p}-q \boldsymbol{A}(\boldsymbol{r}, t)]^{2}+q U(\boldsymbol{r}, t)
$$

$$
H(t)=\frac{1}{2 m}[\boldsymbol{P}-q \boldsymbol{A}(\boldsymbol{R}, t)]^{2}+V(\boldsymbol{R}, t)
$$

---

## 物理量的平均值

在$\ket{\psi}$态中，可观察量$A$的平均值
$$
\langle A\rangle_{\psi}=\langle\psi|A| \psi\rangle
$$

* $\langle A\rangle$ 是多次全同测量的全部结果的平均值, 在涉及与时间有关的 现象时, 我们有时还要计算对时间的平均值; 切勿混淆这两类平均值.
* 如果表示体系状态的右矢 $|\psi\rangle$ 末归一化,则

$$
\langle A\rangle_{\psi}=\frac{\langle\psi|A| \psi\rangle}{\langle\psi \mid \psi\rangle}
$$

## 物理量的方均根偏差

$$
\lang A-\lang A\rang\rang=\bra{\psi}A-\lang A\rang\ket{\psi}=\bra{\psi}A\ket{\psi}-\bra{\psi}\lang A\rang\ket{\psi}= 0
$$

$$
\Delta A=\sqrt{\left\langle(A-\langle A\rangle)^{2}\right\rangle}=\sqrt{\left\langle A^{2}\right\rangle-\langle A\rangle^{2}}
$$

连续谱
$$
(\Delta A)^{2} =\int_{-\infty}^{+\infty}[\alpha-\langle A\rangle]^{2} \rho(\alpha) \mathrm{d} \alpha 
=\int_{-\infty}^{+\infty} \alpha^{2} \rho(\alpha) \mathrm{d} \alpha-\left[\int_{-\infty}^{+\infty} \alpha \rho(\alpha) \mathrm{d} \alpha\right]^{2}
$$

## 可观察量的相容性

对易的算符$A 、 B$ 这样可以同时完全确定的可观察量, 叫做相容的可观察量.

不对易则一般无法同时确定，则不相容。

如果两个可观察量是相容的, 那么, 不论测量这两个量的先后顺序如何, 物理上的预言都一样 (假设两次测量之间的时间间隔充分小). 
$$
\mathscr{P}\left(a_{n}, b_{p}\right)=\mathscr{P}\left(b_{p}, a_{n}\right)=\sum_{i}\left|c_{n, p, i}\right|^{2}=\sum_{i}\left|\left\langle a_{n}, b_{p}, i \mid \psi\right\rangle\right|^{2}
$$
体系的态
$$
\left|\psi_{n, p}^{\prime \prime}\right\rangle=\left|\varphi_{p, n}^{\prime \prime}\right\rangle=\frac{1}{\sqrt{\sum_{i}\left|c_{n, p, i}\right|^{2}}} \sum_{i} c_{n, p, i}\left|a_{n}, b_{p}, i\right\rangle
$$
以后再测$A,B$必然得到与之前相同的结果。

对不相容的两个观察算符

![image-20211209002924761](https://s2.loli.net/2021/12/09/XmkYnut3q7b6aR2.png)

不同的测量顺序为
$$
|\psi\rangle \stackrel{\left(a_{1}\right)}{\Longrightarrow}\left|u_{1}\right\rangle \stackrel{\left(b_{2}\right)}{\Longrightarrow}\left|v_{2}\right\rangle
$$

$$
|\psi\rangle \stackrel{\left(b_{2}\right)}{\longrightarrow}\left|v_{2}\right\rangle \stackrel{\left(a_{1}\right)}{\longrightarrow}\left|u_{1}\right\rangle
$$

$$
\mathscr{P}\left(a_{1}, b_{2}\right)=\left|O H_{1}\right|^{2} \times\left|O K_{2}\right|^{2}
$$

$$
\mathscr{P}\left(b_{2}, a_{1}\right)=\left|O H_{2}\right|^{2} \times\left|O K_{1}\right|^{2}
$$

一般来说，二者并不相等。则

由此可见, 不相容的两个可观察量是不能同时测量的. 第二次测量会使第一次测量所得信息失去. 例如, 对$B$测量后, 我们重新测量 $A$, 结果将是不确定的, 因为 $\left|v_{2}\right\rangle$ 并不是 $A$ 的本征矢. 可见第一次测量 $A$ 所得的一切都消失了.

## 态的制备

> 为使体系在测量之后的态毫无例外地由测量 结果唯一地确定, 所测量的那些量必须是对易可观察量的完全集合。

# 薛定谔方程的物理意义

> 在物理体系随时间演变的过程中, 没有任何不 确定性. 不确定性只出现在测量某个物理量的时候. 这时态矢量发生不可预 料的跃变 . 但是, 在两次测量之间, 态矢量是按完全确定的 方式, 即按薛定谔方程演变.

> 设 $\left|\psi_{1}(t)\right\rangle$ 和 $\left|\psi_{2}(t)\right\rangle$ 是薛定谔方程  的两个解. 如果体系的初态是 $\left|\psi\left(t_{0}\right)\right\rangle=$ $\lambda_{1}\left|\psi_{1}\left(t_{0}\right)\right\rangle+\lambda_{2}\left|\psi_{2}\left(t_{0}\right)\right\rangle\left(\lambda_{1}, \lambda_{2}\right.$ 都是复常数), 与此对应的 $t$ 时刻的态为: $|\psi(t)\rangle=$ $\lambda_{1}\left|\psi_{1}(t)\right\rangle+\lambda_{2}\left|\psi_{2}(t)\right\rangle$. 则 $\left|\psi\left(t_{0}\right)\right\rangle$ 和 $|\psi(t)\rangle$ 之间的对应关系是线性的. 

> 态随时间的演 变并不会改变在整个空间找到粒子的总概率, 其值永远等于 1 . 因此, $|\psi(\boldsymbol{r}, t)|^{2}$可 解释为概率密度.

> 概率流局部守恒。

$$
\frac{\mathrm{d}}{\mathrm{d} t}\langle A\rangle=\frac{1}{\mathrm{i} \hbar}\langle[A, H(t)]\rangle+\left\langle\frac{\partial A}{\partial t}\right\rangle
$$

$$
\frac{\mathrm{d}}{\mathrm{d} t}\langle\boldsymbol{R}\rangle=\frac{1}{m}\langle\boldsymbol{P}\rangle
$$

$$
\frac{\mathrm{d}}{\mathrm{d} t}\langle\boldsymbol{P}\rangle=-\langle\nabla V(\boldsymbol{R})\rangle
$$

以上即为**埃伦费斯特定理**

对比经典的**哈密顿--雅各比**方程
$$
\frac{\mathrm{d}}{\mathrm{d} t} \boldsymbol{r}=\frac{1}{m} \boldsymbol{p}
$$

$$
\frac{\mathrm{d}}{\mathrm{d} t} \boldsymbol{p}=-\nabla V(\boldsymbol{r})
$$

## 方程的解

哈密顿函数$H$不显含t的体系为保守体系。对保守体系，其能量守恒。

知道了 $\left|\psi\left(t_{0}\right)\right\rangle$, 要求 $|\psi(t)\rangle$, 可按下列步骤进行:

1. 在由 $H$ 的本征态构成的基中, 展开 $\left|\psi\left(t_{0}\right)\right\rangle$ :

$$
\left|\psi\left(t_{0}\right)\right\rangle=\sum_{n} \sum_{\tau} c_{n, \tau}\left(t_{0}\right)\left|\varphi_{n, \tau}\right\rangle
$$

$$
c_{n, \tau}\left(t_{0}\right)=\left\langle\varphi_{n, \tau} \mid \psi\left(t_{0}\right)\right\rangle
$$

2. 对于任意的 $t$, 用 $\mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar}$ 去乘展开式中的每一个系数 $c_{n, \tau}\left(t_{0}\right)$, 便得到 $|\psi(t)\rangle$ :

$$
\psi(t)=\sum_{n} \sum_{\tau} c_{n, \tau}\left(t_{0}\right) \mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar}\left|\varphi_{n, \tau}\right\rangle
$$

* 对连续谱

$$
|\psi(t)\rangle=\sum_{\tau} \int \mathrm{d} E c_{\tau}\left(E, t_{0}\right) \mathrm{e}^{-\mathrm{i} E\left(t-t_{0}\right) / \hbar}\left|\varphi_{E, \tau}\right\rangle
$$

对于定态$\left|\psi\left(t_{0}\right)\right\rangle$ 本身就是 $H$ 的本征态.
$$
\left|\psi\left(t_{0}\right)\right\rangle=\sum_{\tau} c_{n, \tau}\left(t_{0}\right)\left|\varphi_{n, \tau}\right\rangle
$$

$$
\begin{aligned}
|\psi(t)\rangle &=\sum_{\tau} c_{n, \tau}\left(t_{0}\right) \mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar}\left|\varphi_{n, \tau}\right\rangle \\
&=\mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar} \sum_{\tau} c_{n, \tau}\left(t_{0}\right)\left|\varphi_{n, \tau}\right\rangle \\
&=\mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar}\left|\psi\left(t_{0}\right)\right\rangle
\end{aligned}
$$

因此, $|\psi(t)\rangle$ 和 $\left|\psi\left(t_{0}\right)\right\rangle$ 的差别只在于一个总的相位因子 $\mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar}$. 这两个态 在物理上是不可区分的. 由此, 我们得到一个结论: 处在$H$的本征态中的体系的一切物理性质, 都不随时间而变; 由于这个原因, 我 们称 $H$ 的本征态为定态.

假设在时刻 $t_{0}$. 我们测量这个体系的能量, 譬如得到的结果是 $E_{k}$. 刚测量之后, 体系处于 $H$ 的属于本征值 $E_{k}$ 的一个本征态 . 刚才我们看到, $H$ 的本征态都是定态, 因此, 在第一次测量之后, 体系的态不再 演变而总是保持在 $H$ 的属于本征值 $E_{k}$ 的本征态. 由此可以推知, 在以后的任一时刻 $t$, 第二次测量体系的能量, 必将总是得到和第一次相同的结果 $E_{k}$.以上即为量子力学中保守体系的能量守恒。

### 运动常量

**运动常量**是这样一个可观察量 $A$, 它不明显地依赖于时间, 并且 可以和 $H$ 对易。

对运动常量
$$
\frac{\mathrm{d}}{\mathrm{d} t}\langle A\rangle=\frac{\mathrm{d}}{\mathrm{d} t}\langle\psi(t)|A| \psi(t)\rangle=0
$$
即平均值不随时间变化。

 当 $A$ 为运动常量 时, 物理体系便有这样一些定态 (即态 $\left.\left|\varphi_{n, p, \tau}\right\rangle\right)$, 在任何时刻 $t$, 这些态都保持 为 $A$ 的属于同一本征值 $\left(a_{p}\right)$ 的本征态. 称 $A$ 的本征值 为好量子数.

在任意态 $|\psi(t)\rangle$ 中测量运动常量 $A$, 得到本征值 $a_{p}$ 的概率 是不随时间而变的. 

在基 $\left\{\left|\varphi_{n, p, \tau}\right\rangle\right\}$ 中展开
$$
\left|\psi\left(t_{0}\right)\right\rangle=\sum_{n} \sum_{p} \sum_{\tau} c_{n, p, \tau}\left(t_{0}\right)\left|\varphi_{n, p, \tau}\right\rangle
$$

$$
|\psi(t)\rangle=\sum_{n} \sum_{p} \sum_{\tau} c_{n, p, \tau}(t)\left|\varphi_{n, p, \tau}\right\rangle
$$

$$
c_{n, p, \tau}(t)=c_{n, p, \tau}\left(t_{0}\right) \mathrm{e}^{-\mathrm{i} E_{n}\left(t-t_{0}\right) / \hbar}
$$

$$
\mathscr{P}\left(a_{p}, t_{0}\right)=\sum_{n} \sum_{\tau}\left|c_{n, p, \tau}\left(t_{0}\right)\right|^{2}
$$

$$
\mathscr{P}\left(a_{p}, t\right)=\sum_{n} \sum_{\tau}\left|c_{n, p, \tau}(t)\right|^{2}
$$

二者相等。

### 波尔频率

对任意算符
$$
\langle\psi(t)|=\sum_{n^{\prime}} \sum_{\tau^{\prime}} c_{n^{\prime}, \tau^{\prime}}^{*}\left(t_{0}\right) \mathrm{e}^{\mathrm{i} E_{n^{\prime}}\left(t-t_{0}\right) / \hbar}\left\langle\varphi_{n^{\prime}, \tau^{\prime}}\right|
$$

$$
\langle\psi(t)|B| \psi(t)\rangle =\langle B\rangle(t) 
=\sum_{n} \sum_{\tau} \sum_{n^{\prime}} \sum_{\tau^{\prime}} c_{n^{\prime}, \tau^{\prime}}^{*}\left(t_{0}\right) c_{n, \tau}\left(t_{0}\right)\left\langle\varphi_{n^{\prime}, \tau^{\prime}}|B| \varphi_{n, \tau}\right\rangle \mathrm{e}^{\mathrm{i}\left(E_{n^{\prime}}-E_{n}\right)\left(t-t_{0}\right) / \hbar}
$$

若$B$不显含时间，则矩阵元为常数。$B$的平均值随时间的演化由上述级数决定，级数各项均为震荡型，震荡频率为
$$
\frac{1}{2 \pi} \frac{\left|E_{n^{\prime}}-E_{n}\right|}{\hbar}=\left|\frac{E_{n^{\prime}}-E_{n}}{h}\right|=\nu_{n^\prime n}
$$
其值与$B$及系统的初态无关。称其为**波尔频率**。

对一个原子，其各物理量的平均值均按该频率震荡。不妨设想，原子只能吸收和发射这些频率的辐射。

各频率与$B$无关，但权重由矩阵元决定，与其有关。某些矩阵元可以为0，此时，对应频率从展开式中消失。

波尔频率的权重还通过表达式中的系数依赖于初态。若初态为本征值$E_k$的定态，则仅$n=n^\prime=k$时，系数不为零，此时$\lang B\rang$与时间无关。

### 时间--能量不确定度

$$
\Delta t \cdot \Delta E \gtrsim h
$$

$$
\left|\psi\left(t_{0}\right)\right\rangle=c_{1}\left|\varphi_{1}\right\rangle+c_{2}\left|\varphi_{2}\right\rangle
$$

$$
|\psi(t)\rangle=c_{1} \mathrm{e}^{-\mathrm{i} E_{1}\left(t-t_{0}\right) / \hbar}\left|\varphi_{1}\right\rangle+c_{2} \mathrm{e}^{-\mathrm{i} E_{2}\left(t-t_{0}\right) / \hbar}\left|\varphi_{2}\right\rangle
$$

如果测量能量, 则得到的结果或是 $E_{1}$, 或是 $E_{2}$. 因而 $E$ 的不确定度的数量级
$$
\Delta E \simeq\left|E_{2}-E_{1}\right|
$$
$B$ 是一个任意的可观察量, 它与 $H$ 不可对易.
$$
\begin{aligned}
\mathscr{P}\left(b_{m}, t\right)=&\left|\left\langle u_{m} \mid \psi(t)\right\rangle\right|^{2}=\left|c_{1}\right|^{2}\left|\left\langle u_{m} \mid \varphi_{1}\right\rangle\right|^{2}+\left|c_{2}\right|^{2}\left|\left\langle u_{m} \mid \varphi_{2}\right\rangle\right|^{2} \\
&+2 \operatorname{Re}\left[c_{2}^{*} c_{1} \mathrm{e}^{\mathrm{i}\left(E_{2}-E_{1}\right)\left(t-t_{0}\right) / \hbar}\left\langle u_{m} \mid \varphi_{2}\right\rangle^{*}\left\langle u_{m} \mid \varphi_{1}\right\rangle\right]
\end{aligned}
$$
$\mathscr{P}\left(b_{m}, t\right)$ 以玻尔频率 $\nu_{21}=|E_{2}-E_{1}|/h$ 在两个极值之间振荡.
$$
\Delta t \simeq \frac{h}{\left|E_{2}-E_{1}\right|}
$$

# 叠加原理

假设 $\left|\psi_{1}\right\rangle$ 和 $\left|\psi_{2}\right\rangle$ 是两个正交归一的态:
$$
\mathscr{P}_{1}\left(a_{n}\right)=\left|\left\langle u_{n} \mid \psi_{1}\right\rangle\right|^{2}
$$

$$
\mathscr{P}_{2}\left(a_{n}\right)=\left|\left\langle u_{n} \mid \psi_{2}\right\rangle\right|^{2}
$$

考虑一个态
$$
|\psi\rangle=\lambda_{1}\left|\psi_{1}\right\rangle+\lambda_{2}\left|\psi_{2}\right\rangle
$$

$$
\left|\lambda_{1}\right|^{2}+\left|\lambda_{2}\right|^{2}=1
$$

 如果体系处于态 $|\psi\rangle$, 那么, 我们发现它处于态 $\left|\psi_{1}\right\rangle$ 的概率是 $\left|\lambda_{1}\right|^{2}$, 发现它处在态 $\left|\psi_{2}\right\rangle$ 的概率是 $\left|\lambda_{2}\right|^{2}$.

这不等同于**由 $N$ 个 ( $N$ 甚大) 处于 (E-4) 式表示的态的全同体系构 成的集合完全等价于由 $N\left|\lambda_{1}\right|^{2}$ 个处于态 $\left|\psi_{1}\right\rangle 、 N\left|\lambda_{2}\right|^{2}$ 个处于态 $\left|\psi_{2}\right\rangle$ 的 $N$ 个 全同体系构成的集合. **
$$
\mathscr{P}\left(a_{n}\right)=\left.\left\langle\left|u_{n}\right| \psi\right\rangle\right|^{2}=\left|\lambda_{1}\right|^{2}\left|\left\langle u_{n} \mid \psi_{1}\right\rangle\right|^{2}+\left|\lambda_{2}\right|^{2}\left|\left\langle u_{n} \mid \psi_{2}\right\rangle\right|^{2}
+2 \operatorname{Re}\left\{\lambda_{1} \lambda_{2}^{*}\left\langle u_{n} \mid \psi_{1}\right\rangle\left\langle u_{n} \mid \psi_{2}\right\rangle^{*}\right\}
$$
还包括有干涉项，并且起作用的不仅为模，还有其相位。

如果我们没有用实验来决定体系通过的是哪个 中间态, 则应对概率幅求和, 而不是对概率求和.
$$
\mathscr{P}_{a}(c)=\left|\left\langle v_{c} \mid u_{a}\right\rangle\right|^{2}
$$

$$
\mathscr{P}_{a}(b, c)=\left|\left\langle v_{c} \mid w_{b}\right\rangle\right|^{2}\left|\left\langle w_{b} \mid u_{a}\right\rangle\right|^{2}
$$

$$
\mathscr{P}_{a}(c) \ne \sum_{b} \mathscr{P}_{a}(b, c)
$$

其忽略了干涉项。

认为物理体系 “通过了诸态 $\left|w_{b}\right\rangle$ 中的这一个或那一个", 则是完全错误的; 比较正确的说法应该 是体系同时通过了所有诸态 $\left|w_{b}\right\rangle$.

1.  量子理论中的概率型预言一概得自概率幅, 计算时要取它的模的平方.
1. 在一个确定的实验中, 如果没有进行中间阶段的测量, 那么, 我们绝不 能根据中间测量可能得到的各种结果的概率, 而应根据它们的概率幅来分析 问题.
1. 一个物理体系的态可以线性叠加, 这意味着:一个概率幅往往表现为 若干部分幅之和. 因而对应的概率等于若干项之和的模的平方, 而且那些部分幅 是彼此相干的.