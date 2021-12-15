# 顺磁性

每个偶极子都具有磁矩 $\mu$ 的 $N$ 个磁偶极子的系统. 
当存在外磁场 $H$ 时, 这些偶极子将受到一力矩, 这个力矩趋向于把偶极子顺着外磁场方向排列起来. 
如果没有任何其他作用力来阻止这种倾向的话, 这些偶极子自己将严格地按这个方向排列成行, 
得到一个完全磁化的系统. 

然而, 在事实上, 系统中的热扰动却对这种倾向产生了一个阻力, 因此, 在平衡吋我们得到的只是一个部分磁化的系统.

当 $T \rightarrow 0 \mathrm{~K}$ N.j, 热扰动将不起作用, 从而无论外加磁场的虽度多大, 
系统将表 现出偶极矩的完全相同的取向; 

当 $T \rightarrow \infty$ 时, 我们的偶极矩将趋向完全无规状态, 这意味着磁化消失. 

在中等温度下, 磁化情况由 $\left(\mu H / k T^{\prime}\right)$ 来决定.

对于这个研究所采用的模型是, 由 $N$ 个全同的、定域的 (因而 是可分辨的)、
几乎是静态的、彼此无相互作用的和自由取向的偶 极子所组成的系统. 
需要考虑的唯一能量就是 偶极子的势能, 该势能是由于外磁场 $\boldsymbol{H}$ 存在而引起的, 
并取决于 偶极子相对于外磁场的取向:

$$
E=\sum_{i=1}^{N} E_{i}=-\sum_{i=1}^{N} \mu_{i} \cdot \boldsymbol{H}=-\mu H \sum_{i=1}^{N} \cos \theta_{i} .
$$

$$
Q_{N}(\beta)=\left[Q_{1}(\beta)\right]^{N}
=(\sum_{\theta} \exp (\beta \mu H \cos \theta))^N
$$

$$
\begin{aligned}
M_{z} &=N\langle\mu \cos \theta\rangle=N \frac{\sum_{\theta} \mu \cos \theta \exp (\beta \mu H \cos \theta)}{\sum_{\theta} \exp (\beta \mu H \cos \theta)} \\
&=\frac{N}{\beta} \frac{\partial}{\partial H} \ln Q_{1}(\beta)=-\left(\frac{\partial A}{\partial H}\right)_{T}
\end{aligned}
$$

$$
Q_{1}(\beta)=\int_{0}^{2 \pi} \int_{0}^{\pi} e^{\beta \mu H \cos \theta} \sin \theta d \theta d \phi=4 \pi \frac{\sinh (\beta \mu H)}{\beta \mu H}
$$

$$
\bar{\mu}_{z} \equiv \frac{M_{z}}{N}=\mu\left\{\operatorname{coth}(\beta \mu H)-\frac{1}{\beta \mu H}\right\}=\mu L(\beta \mu H),
$$

$L(x)$为**郎之万函数**

$$
L(x)=\operatorname{coth} x-\frac{1}{x}
$$

![郎之万函数](https://s2.loli.net/2021/12/05/wM4xCoJiVRlXcdm.png)

若$H\gg T$，磁场很强或温度很低,$L(x)\rightarrow 1$

$$
\bar{\mu}_{z} \simeq \mu \quad \text { and } \quad M_{z 0} \simeq N_{0} \mu .
$$

若$H\ll T$，磁场很弱或温度很高，对泰勒展开取一阶项

$$
M_{z 0} \simeq \frac{N_{0} \mu^{2}}{3 k T} H
$$

$$
\chi_{T}=\operatorname{Lim}_{H \rightarrow 0}\left(\frac{\partial M_{z 0}}{\partial H}\right)_{T} \simeq \frac{N_{0} \mu^{2}}{3 k T}=\frac{C}{T}
$$

上式即为顺磁性的**居里定律**，$C$为**居里温度**

## 量子力学修正

$$
\mu=\left(g \frac{e}{2 m c}\right) l
$$

角动量是分立的

$$
l^{2}=J(J+1) \hbar^{2} ; \quad J=\frac{1}{2}, \frac{3}{2}, \frac{5}{2}, \ldots \quad \text { or } \quad 0,1,2, \ldots
$$

$g(e / 2 m c)$ 这个量称为偶极子的迴磁比, 而 $g$ 数即所谓的朗德 $g$ 因 子.
 一方面, 如果偶极子的净角动量仅来源于电子白旋, 则 $g=2$; 
 另一方面, 如果它仅来源于轨道运动, 则 $g=1$. 
 然而, 一般说来, 它来源于两者的混合作用, 于是, 

$$
g=\frac{3}{2}+\frac{S(S+1)-L(L+1)}{2 J(J+1)}
$$

$$
\mu^{2}=g^{2} \mu_{B}^{2} J(J+1)
$$

$$
\mu_{z}=g \mu_{B} m, \quad m=-J,-J+1, \ldots, J-1, J
$$

$$
Q_{1}(\beta)=\sum_{m=-J}^{J} \exp \left(\beta g \mu_{B} m H\right)
=\sinh \left\{\left(1+\frac{1}{2 J}\right) x\right\} / \sinh \left\{\frac{1}{2 J} x\right\}
$$

$$
x=\beta\left(g \mu_{B} J\right) H
$$

$$
\bar{\mu}_{z}=\frac{M_z}{N}=\frac{1}{\beta} \frac{\partial}{\partial H} \ln Q_{1}(\beta)=\left(g \mu_{B} J\right) B_{J}(x)
$$

$B_K(x)$未布里渊函数

$$
B_{J}(x)=\left(1+\frac{1}{2 J}\right) \operatorname{coth}\left\{\left(1+\frac{1}{2 J}\right) x\right\}-\frac{1}{2 J} \operatorname{coth}\left\{\frac{1}{2 J} x\right\} .
$$

![布里渊函数](https://s2.loli.net/2021/12/05/WFHiTJncohepauB.png)

若$H\gg T$，磁场很强或温度很低,$B_J(x)\rightarrow 1$,$\bar{\mu}_z=g\mu_BJ$

若$H\ll T$，磁场很弱或温度很高，对泰勒展开取一阶项

$$
\bar{\mu}_{z} \simeq \frac{\left(g \mu_{B} J\right)^{2}}{3 k T}\left(1+\frac{1}{J}\right) H=\frac{g^{2} \mu_{B}^{2} J(J+1)}{3 k T} H .
$$

同样遵循居里定律。

$$
C_{J}=\frac{N_{0} g^{2} \mu_{B}^{2} J(J+1)}{3 k}=\frac{N_{0} \mu^{2}}{3 k}
$$

> $J \rightarrow \infty$ 的情况, 
> 同时有 $g \rightarrow 0$, 此时乘积 $g J$ 将是一个常数, 
> 从而 $\mu$ 值也就是一个常数. 在此极限下, 布里渊函数 $B_{J}(x)$ 趋向于与 $J$ 无关,
> 且同 朗之万函数等同。在这个极限 情况下，一个磁偶极子所允许的取向数变成无限大, 
> 结果此问题实 质上退化为经典的对应问题 (其中我们允许所有可能的取向). 


>  $J=\frac{1}{2}$, 此时只允许两个取向. 
> 在这 种情况下的结果当然与 $J \gg 1$ 情况下的结果大不相同. 我们现在

$$
\bar{\mu}_{z}=\mu_{B} B_{1 / 2}(x)=\mu_{B} \tanh x .
$$

对于 $x \gg 1$ 的情形, $\bar{\mu}_{z}$ 几乎等于 $\mu$. 
当 $x \ll 1$ 时, $\bar{\mu}_{z}$ $\simeq \mu x$, 这时对应的居里常数为:

$$
C_{1 / 2}=\frac{N_{0} \mu_{B}^{2}}{k}
$$

为三倍的经典居里常数$C_\infty$

# 负温度

$J=1/2$时，仅两个取向，能量为$\pm\mu H$，记为$\pm \varepsilon$

$$
Q_{N}(\beta)=\left(e^{\beta \varepsilon}+e^{-\beta \varepsilon}\right)^{N}=\{2 \cosh (\beta \varepsilon)\}^{N}
$$

---

物理量

$$
A=-N k T \ln \{2 \cosh (\varepsilon / k T)\}
$$

$$
S=-\left(\frac{\partial A}{\partial T}\right)_{H}=N k\left[\ln \left\{2 \cosh \left(\frac{\varepsilon}{k T}\right)\right\}-\frac{\varepsilon}{k T} \tanh \left(\frac{\varepsilon}{k T}\right)\right]
$$

![20211207083004](https://s2.loli.net/2021/12/07/Ab9t3lVmWsd741w.png)

> 注意到, 当 $k T \ll \varepsilon$ 时, 系统的嫡很小, 接近于零; 当 $k T$ 为 $\varepsilon$ 的量级 时, 系统的樀迅速地升高; 而当 $k T \gg \&$ 时, 它接近于极限值 $N k \ln 2$.
> (完全随机，状态数为$2^N$)

$$
U=A+T S=-N \varepsilon \tanh \left(\frac{\varepsilon}{k T}\right)
$$

![20211207083033](https://s2.loli.net/2021/12/07/cqpdRb1GKHItE49.png)

> $T \rightarrow 0 \mathrm{~K}$ 时, 该系统的能量达到它的最小值 $-N \varepsilon$. 这显然对应于 磁饱和状态, 
> 也就是对应于系统的一个理想有序状态. 接近高温 时, 能量就趋向于零; 这意味着偶极子具有完全随机性的取向,

$$
M=-\left(\frac{\partial A}{\partial H}\right)_{T}=N \mu_{B} \tanh \left(\frac{\varepsilon}{k T}\right)
$$

![20211207083052](https://s2.loli.net/2021/12/07/1EjuMckIJt5Wh8a.png)

$$
C=\left(\frac{\partial U}{\partial T}\right)_{H}=N k\left(\frac{\varepsilon}{k T}\right)^{2} \operatorname{sech}^{2}\left(\frac{\varepsilon}{k T}\right)
$$

![20211207083206](https://s2.loli.net/2021/12/07/gC5Zdp1KJkyWsiV.png)

> 比热在低温及高温时变为零. 在 $T=\varepsilon / k$ 附近的某个地方, 
> 比热曲线呈现出一个最大值. 当我们把偶极子的两个允计状态之间的能量差写成 $\Delta$ 时, 比热公式可以写成:

$$
C=N k\left(\frac{\Delta}{k T}\right)^{2} e^{\Delta / k T}\left(1+e^{\Delta / k T}\right)^{-2}
$$

> 这种形式的比热通常称为**肖脱基比热**(*Schottky anomaly*); 其特征是有一个反常的峰值, 
> 这在具有激发能隙 $\Delta$ 的所有系统中都可观测到.


---

$$
E=\left(N_{+}-N_{-}\right) \varepsilon_{1}
$$

$$
N_{+}+N_{-}=N_{0}
$$

$$
N_{+}=\frac{1}{2}\left(N+\frac{E}{\varepsilon}\right)_{3} \quad N_{-}=\frac{1}{2}\left(N-\frac{E}{\varepsilon}\right)
$$

> 其对应一个随机游走问题。$N$个偶极子中，若$N_+$的位置确定了，那么$N_-$的分布也确定了
> 于是其一个排列问题，结果为

$$
\Omega(N, E)=C_N^{N_+}=\frac{N !}{N_{+} ! N_{-}!}=\frac{N!}{\left\{\frac{1}{2}\left(N+\frac{E}{\varepsilon}\right)\right\} !\left\{\frac{1}{2}\left(N-\frac{E}{\varepsilon}\right)\right\}!} .
$$

$$
S(N, E) =k \operatorname{In} \Omega 
 \simeq k\left[N \ln N-\frac{1}{2}\left(N+\frac{E}{\varepsilon}\right) \ln \left\{\frac{1}{2}\left(N+\frac{E}{\varepsilon}\right)\right\}\right.
\left.-\frac{1}{2}\left(N-\frac{E}{\varepsilon}\right) \ln \left\{\frac{1}{2}\left(N-\frac{E}{\varepsilon}\right)\right\}\right]
$$

$$
\frac{1}{T}=\left(\frac{\partial S}{\partial E}\right)_{N}=\frac{k}{2 \varepsilon} \ln \left\{\frac{N-E / \varepsilon}{N+E / \varepsilon}\right\}
$$

当$E\lt 0$,就有温度$T<0$

> $E>0$ 的区域 $($ 因而 $T<0)$ 确实是反常的, 因为它相应于在与外 场相反方向上的磁化：尽管如此, 这一反常现象能够在晶体核矩 系统中从实验上米实现, 只要晶体中核自旋间相互作用的弛豫时间 $t_{1}$ 跟自旋与点阵相互作用的弛豫时间 $t_{2}$ 比较起来非常之小. 
> 
> 让这样的晶体在强磁场中进行磁化, 然后将磁场迅速反向, 快得使自旋跟不上这种转向. 这将使系统处在非平衡态之中, 其能量高 于新的平衡态的能量值 $U$. 
> 在 $t_{1}$ 量级的期间, 核自旋子系统应该 徍㿟达到一种内部平衡状态; 此态将具有负磁化强度, 因而将对应 于一个负温度．点阵子系统 (其能量原则上是不受限制的), 确实 处于正温度. 在 $t_{2}$ 量级的剘间, 两个子系统将达到一个相互平衡 的状态, 此吋又具有正温度, 
> 
> 这类型的实验最早是由珀塞尔和 庞德任 1951 年用氟化锂 $(\mathrm{LiF})$ 晶体成功地做出的.

![反向磁化实验](https://s2.loli.net/2021/12/07/bLxD7N1suGYIAti.png)

> 只有当给定系统的能量存在上 限时, 才有可能开始出现负温度. 在大多数的物理系统中并不存 在这种情况, 因为大多数的物理系统具有显然不受限制的动能.同理, 开始出现正温度是与系统能量存在下限有关. 

处于负温度的系统比处于正温度的系统更热. 确实, 所有负温度是在 $+\infty$ 以 上, 而不是在零以下!