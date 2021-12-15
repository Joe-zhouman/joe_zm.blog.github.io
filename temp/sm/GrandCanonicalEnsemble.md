# 巨正则系综

把 $N$ 和 $E$ 两者都看成是系统的变量, 并把它们的期望值 $\langle N\rangle$ 和 $\langle E\rangle$ 看成与相应的热力学量是等同的.

巨正则系综是由 这个给定系统 $A$ 及其大量的(思维)复本所组成的, 系综的成员之 
间可以互相进行能量的交换和粒子的交换: 必须固定两个强度参量, 
比如 $\alpha$ 和 $\beta$来描述系统

## 系统与粒子--能量库之间的平衡

$$
N_{r}+N_{r}^{\prime}=N^{(0)}=\text { const. }
$$

$$
E_{s}+E_{s}^{\prime}=E^{(0)}=\text { const. }
$$

$$
\frac{N_{r}}{N^{(0)}}=\left(1-\frac{N_{r}^{\prime}}{N^{(0)}}\right) \ll 1
$$

$$
\frac{E_{s}}{E^{(0)}}=\left(1-\frac{E_{s}^{\prime}}{E^{(0)}}\right) \ll 1
$$

$$
P_{r, s} \propto \Omega^{\prime}\left(N^{(0)}-N_{r}, E^{(0)}-E_{s}\right)
$$

$$
\begin{aligned}
\ln \Omega^{\prime}\left(N^{(0)}-N_{r}, E^{(0)}-E_{s}\right)=& \ln \Omega^{\prime}\left(N^{(0)}, E^{(0)}\right) +\left(\frac{\partial \ln \Omega^{\prime}}{\partial N^{\prime}}\right)_{N^{\prime}=N^{(0)}}\left(-N_{r}\right)+\left(\frac{\partial \ln \Omega^{\prime}}{\partial E^{\prime}}\right)_{E^{\prime}=E^{(0)}}\left(-E_{s}\right)+\cdots \\
& \simeq \ln \Omega^{\prime}\left(N^{(0)}, E^{(0)}\right)+\frac{\mu^{\prime}}{k T^{\prime}} N_{r}-\frac{1}{k T^{\prime}} E_{s} ;
\end{aligned}
$$

$$
P_{r, s} \propto \exp \left(-\alpha N_{r}-\beta E_{s}\right)
$$

$$
\alpha=-\frac{\mu}{k T} \quad \text { 和 } \quad \beta=\frac{1}{k T} \text {. }
$$

$$
P_{r, s}=\frac{\exp \left(-\alpha N_{r}-\beta E_{s}\right)}{\sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)}
$$

## 系综观点推导

$$
\sum_{r, s} n_{r, s}=\mathcal{N}
$$

$$
\sum_{r, s} n_{r, s} N_{r}=\mathcal{N} \bar{N}
$$

$$
\sum_{r, s} n_{r, s} E_{s}=\mathcal{N} \bar{E}
$$

$$
W\left\{n_{r, s}\right\}=\frac{\mathcal{N} !}{\prod_{r, s}\left(n_{r, s} !\right)}
$$

$$
\frac{n_{r, s}^{*}}{\mathcal{N}}=\frac{\exp \left(-\alpha N_{r}-\beta E_{s}\right)}{\sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)}
$$

### 最几可推导

利用拉格朗日算子法

$$
\ln W=\ln \left(\mathscr{N}！\right)-\sum_{r,s} \ln \left(n_{r,s}!\right)
$$

根据斯特林公式

$$
\ln W=\mathscr{N} \ln \mathscr{N}-\sum_{r,s} n_{r,s} \ln n_{r,s}
$$

同时要满足上面的约束方程，按拉格朗日算子法，即求以下方程$V(n,\alpha,\beta)$的极值：

$$
V=\ln W+\alpha\sum_{r,s}n_{r,s}N_r+\beta\sum_{r,s}n_{r,s}E_s+\gamma\sum_{r,s}n_{r,s}
$$

固有

$$
\frac{\partial V}{\partial n_r}=-(\ln n_{r,s}+1)+\alpha N_r+\beta E_s+\gamma=0
$$

$$
n_{r}^{*}=C \exp \left(-\alpha N_r-\beta E_{r}\right)
$$

$$
\bar{N}=\frac{\sum_{r, s} N_{r} \exp \left(-\alpha N_{r}-\beta E_{s}\right)}{\sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)} \equiv-\frac{\partial}{\partial \alpha}\left\{\ln \sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)\right\}
$$

$$
\bar{E}=\frac{\sum_{r, s} E_{s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)}{\sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)} \equiv-\frac{\partial}{\partial \beta}\left\{\ln \sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)\right\},
$$

# 物理量

$$
q \equiv \ln \left\{\sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)\right\}
$$

$$
d q=-\bar{N} d \alpha-\bar{E} d \beta-\frac{\beta}{\mathcal{N}} \sum_{r, s}\left\langle n_{r, s}\right\rangle d E_{s},
$$

$$
d(q+\alpha \bar{N}+\beta \bar{E})=\beta\left(\frac{\alpha}{\beta} d \bar{N}+d \bar{E}-\frac{1}{\mathcal{N}} \sum_{r, s}\left\langle n_{r, s}\right\rangle d E_{s}\right) .
$$

$$
\delta Q=d \bar{E}+\delta W-\mu d \bar{N}
$$

$$
\delta W=-\frac{1}{\mathcal{N}} \sum_{r, s}\left\langle n_{r, s}\right\rangle d E_{s}, \quad \mu=-\alpha / \beta,
$$

$$
d(q+\alpha \bar{N}+\beta \bar{E})=\beta \delta Q
$$

$$
q=\frac{S}{k}-\alpha \bar{N}-\beta \bar{E}=\frac{T S+\mu \bar{N}-\bar{E}}{k T} .
$$

$$
\mu\bar{N}=\bar{E}-TS+PV
$$

$$
q \equiv \ln \left\{\sum_{r, s} \exp \left(-\alpha N_{r}-\beta E_{s}\right)\right\}=\frac{P V}{k T}
$$

定义系统的**逸度**(*fugacity*)
$$
z \equiv e^{-\alpha}=e^{\mu / k T}
$$

$$
q  \equiv \ln \left\{\sum_{r, s} z^{N_{r}} e^{-\beta E_{s}}\right\} 
=\ln \left\{\sum_{N_{r}=0}^{\infty} z^{N_{r}} Q_{N_{r}}(V, T)\right\} \quad\left(\text { with } Q_{0} \equiv 1\right),
$$

$$
q(z, V, T) \equiv \ln \mathcal{Q}(z, V, T)
$$

**巨配分函数**
$$
\left.\mathcal{Q}(z, V, T) \equiv \sum_{N_{r}=0}^{\infty} z^{N_{r}} Q_{N_{r}}(V, T) \quad \text { (with } Q_{0} \equiv 1\right)
$$

$$
P(z, V, T)=\frac{k T}{V} q(z, V, T) \equiv \frac{k T}{V} \ln \mathcal{Q}(z, V, T)
$$

$$
N(z, V, T)=z\left[\frac{\partial}{\partial z} q(z, V, T)\right]_{V, T}=k T\left[\frac{\partial}{\partial \mu} q(\mu, V, T)\right]_{V, T}
$$

$$
U(z, V, T)=-\left[\frac{\partial}{\partial \beta} q(z, V, T)\right]_{z, V}=k T^{2}\left[\frac{\partial}{\partial T} q(z, V, T)\right]_{z, V} .
$$

# 与其他系综的关系

> 从表面上看来，巨正则系综与先前讨论的正则系综和微正则系综相比，有着很大的差别。然而，就其热力学而论，由巨正则系综所得的结果，与其他两个系综所得的结果是相同的。
>
> 因此，不管其表面上的差别如何显著，一个给定物理系统的整个行为，不论该系统是否属于这一类系综或另一类系综，实际上都是相同的，其根本的原因与以下事实有关，即**各个物理量随系综成员变化所引起的“相对涨落”实际上是可以忽略不计的**。因此，尽管不同的系综对一个给定物理系统所提供的环境并不相同，但是系统的总的行为特性并不会受到显著的影响

$$
\bar{N}=\frac{\sum_{r, s} N_{r} e^{-\alpha N_{r}-\beta E_{s}}}{\sum_{r, s} e^{-\alpha N_{r}-\beta E_{s}}}
$$

$$
\left(\frac{\partial \bar{N}}{\partial \alpha}\right)_{\beta, E_{s}}=-\overline{N^{2}}+\bar{N}^{2}
$$

$$
\overline{(\Delta N)^{2}} \equiv \overline{N^{2}}-\bar{N}^{2}=-\left(\frac{\partial \bar{N}}{\partial \alpha}\right)_{T, V}=k T\left(\frac{\partial \bar{N}}{\partial \mu}\right)_{T, V}
$$

$n=N/V$为粒子密度
$$
\frac{\overline{(\Delta n)^{2}}}{\bar{n}^{2}}=-\frac{k T}{V} \frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_{T}=\frac{k T}{V} \kappa_{T}
$$
$\kappa_T$为等温压缩系数。

> 因此, 该给定系统的粒子数密度的相对方均根涨落通常为 $O\left(N^{-1 / 2}\right)$, 因而是可以忽略不计的.
>
>  然而, 也可能会有例外的情 形, 如在伴随有相变的情形中就遇到这种例外. 在这种相变的情 况下, 一个给定系统的压缩系数可以变得异常地大, 如通过等温线 的几乎 “平化” 所显示的那样. 在这些情况下, 导数 $(\partial V / \partial P)_{r}$, 因 而 $\kappa_{T}$, 都可以正好是 $O(N)$. 因此, 粒子数密度 $n$ 的方均根张落 可以是 $O(1)$. 我们可望碰到在系统的粒子数密度中出现异常大的涨落. 确实存在这种涨落, 并可用来解释诸如[**临界乳光现象**](https://baike.baidu.com/item/%E4%B8%B4%E7%95%8C%E4%B9%B3%E5%85%89/3459185?fr=aladdin)  (*critical opalescence*)等. 
>
> 很显然, 在这样的情况下, 致使巨正则系综的表述形式给出的结 果, 与从正则系综的表述形式所得出的结果从原则上讲末必是相同的. 在这样的情况下, 我们将愿意用巨正则系综的表述形式, 因为只有它才能为实际物理状况提供正确图象.

$$
\left(\frac{\partial U}{\partial T}\right)_{z, V}=\left(\frac{\partial U}{\partial T}\right)_{N, V}+\left(\frac{\partial U}{\partial N}\right)_{T, V}\left(\frac{\partial N}{\partial T}\right)_{z, V}
$$

$$
\left(\frac{\partial N}{\partial \beta}\right)_{\alpha, V}=\left(\frac{\partial U}{\partial \alpha}\right)_{\beta, V}
$$

$$
\left(\frac{\partial N}{\partial T}\right)_{z, V}=\frac{1}{T}\left(\frac{\partial U}{\partial \mu}\right)_{T, V}
$$

$$
\overline{(\Delta E)^{2}}=k T^{2} C_{V}+k T\left(\frac{\partial U}{\partial N}\right)_{T, V}\left(\frac{\partial U}{\partial \mu}\right)_{T, V}
$$

$$
(\Delta E)^{2}=\left\langle(\Delta E)^{2}\right\rangle_{\text {can }}+\left\{\left(\frac{\partial U}{\partial N}\right)_{T, V}\right\}^{2} \overline{(\Delta N)^{2}}
$$

能量涨落为正则系统的涨落加上由粒子数变化引起的涨落。通常情况下，涨落可以忽略不计。但在诸如相变等情形，第二项涨落很大。