# 密度矩阵

共$\mathcal{N}$个系统,$\ket{k}$表示第$k$个系统的态矢量。$\mathcal{N}\gg1$
$$
\ket{K}=\sum_n\bra{n}\ket{K}\Ket{n}
$$
$\ket{n}$为第$n$个基矢量。系数$\bra{n}\ket{K}$为表象中的基函数。

任意力学量对第$k$个体系的平均值为
$$
A_k=\bra{K}\hat{A}\ket{K}
$$
在整个系综上的平均
$$
\lang\hat{A}\rang=\frac1N\sum_K\bra{K}\hat{A}\ket{K}=\frac1N\sum_K\sum_{m,n}\bra{K}\ket{m}\bra{m}\hat{A}\ket{n}\bra{n}\ket{K}
$$
$\bra{m}\hat{A}\ket{n}$为算符在$n$表象中的矩阵元

定义矩阵$\hat{\rho}$,其矩阵元为
$$
\rho_{mn}:=\frac1N\sum_K\bra{m}\ket{K}\bra{K}\ket{n}
$$

$$
\langle\hat{A}\rangle=\sum_{m, n} A_{m n} \rho_{n m}=\operatorname{Tr}(\hat{\rho} \hat{A})
$$

该平均为两次平均，先对量子态做平均，再对
$$
\hat{\rho} \equiv \frac{1}{N} \sum_{K}\ket{K}\bra{K}
$$

1. 密度矩阵是厄米矩阵$\rho_{m n}=\rho_{n m}^{*}$
1. $\langle\hat{I}\rangle=\operatorname{Tr}(\hat{\rho} \hat{I})=\operatorname{Tr}(\hat{\rho})=1$
1. 对角元素为实数，且$\sum_{n} \rho_{n n}=1 ;, 0 \leqslant \rho_{n n} \leqslant 1$

对角元素
$$
\rho_{n n}=\frac{1}{N} \sum_{K}\langle n \mid K\rangle\langle K \mid n\rangle=\frac{1}{N} \sum_{K}|\langle n \mid K\rangle|^{2}
$$
由量子力学可知, $|\langle n \mid K\rangle|^{2}$ 是表示系综中第 $K$ 个体系处在状态 $|n\rangle$ 的概率; 平 均来说, 系综中任何一个体系处在状态 $|n\rangle$ 的概率为 $\rho_{nn}$。
$$
\mathrm{i} \hbar \frac{\partial}{\partial t} \hat{\rho} =\mathrm{i} \hbar \frac{\partial}{\partial t}\left(\frac{1}{N} \sum_{K}|K\rangle\langle K|\right) 
=\sum_{K} \frac{1}{N} \hat{H}\ket{K}\bra{K}-\sum_{K} \frac{1}{N} \ket{K}\bra{K}\hat{H} 
=[\hat{H},\hat{\rho}] .
$$
其为量子力学中的刘维尔定理。

平衡态中，$\dot{\rho}_{mn}=0$，则

1. $\hat{\rho}$为$\hat{H}$的显函数，$\hat{\rho}=\hat{\rho}(\hat{H})$，二者对易，具有共同本征态。
1. $\hat{H}$不显含$t$，$\dot{\hat{H}}=0$

# 量子系综

## 微正则系综

在能量表象中
$$
\rho_{m n}=\rho_{n} \delta_{m n}
$$

$$
\rho_{n}=\left\{\begin{array}{ll}
1 / \Gamma & \text { for each of the accessible states } \\
0 & \text { for all other states; }
\end{array}\right.
$$

## 正则系综

$$
\rho_{m n}=\rho_{n} \delta_{m n}
$$

$$
\rho_{n}=C \exp \left(-\beta E_{n}\right)
$$

$$
C=\frac{1}{\sum_{n} \exp \left(-\beta E_{n}\right)}=\frac{1}{Q_{N}(\beta)}
$$

$$
\begin{aligned}
\hat{\rho} &=\sum_{n}\left|\phi_{n}\right\rangle \frac{1}{Q_{N}(\beta)} e^{-\beta E_{n}}\left\langle\phi_{n}\right| \\
&=\frac{1}{Q_{N}(\beta)} e^{-\beta \hat{H}} \sum_{n}\left|\phi_{n}\right\rangle\left\langle\phi_{n}\right| \\
&=\frac{1}{Q_{N}(\beta)} e^{-\beta \hat{H}}=\frac{e^{-\beta \hat{H}}}{\operatorname{Tr}\left(e^{-\beta \hat{H}}\right)},
\end{aligned}
$$

$$

\langle G\rangle =\operatorname{Tr}(\hat{\rho} \hat{G})=\frac{1}{Q_{N}(\beta)} \operatorname{Tr}\left(\hat{G} e^{-\beta \hat{H}}\right) =\frac{\operatorname{Tr}\left(\hat{G} e^{-\beta \hat{H}}\right)}{\operatorname{Tr}\left(e^{-\beta \hat{H}}\right)} ;
$$

坐标表象中
$$

\rho\left(\boldsymbol{r}^{N}, \boldsymbol{r}^{N^{\prime}}\right) =\left\langle\boldsymbol{r}^{N}|\hat{\rho}| \boldsymbol{r}^{N^{\prime}}\right\rangle
=\sum_{n} \mathrm{e}^{-\psi-\beta E_{n}}\left\langle\boldsymbol{r}^{N} \mid E_{n}\right\rangle\left\langle E_{n} \mid \boldsymbol{r}^{N^{\prime}}\right\rangle
$$

## 巨正则系综

$$
\hat{\rho}=\frac{1}{\mathcal{Q}(\mu, V, T)} e^{-\beta(\hat{H}-\mu \hat{n})}
$$

$$
\mathcal{Q}(\mu, V, T)=\sum_{r, s} e^{-\beta\left(E_{r}-\mu N_{s}\right)}=\operatorname{Tr}\left\{e^{-\beta(\hat{H}-\mu \hat{n})}\right\}
$$

$$
\begin{aligned}
\langle G\rangle &=\frac{1}{\mathcal{Q}(\mu, V, T)} \operatorname{Tr}\left(\hat{G} e^{-\beta \hat{H}} e^{\beta \mu \hat{n}}\right) \\
&=\frac{\sum_{N=0}^{\infty} z^{N}\langle G\rangle_{N} Q_{N}(\beta)}{\sum_{N=0}^{\infty} z^{N} Q_{N}(\beta)}
\end{aligned}
$$

# 实例

## 磁场中的一个电子

$$
\hat{H}=-\mu_{B}(\hat{\sigma} \cdot \boldsymbol{B})=-\mu_{B} B \hat{\sigma}_{z}
$$

$\hat{\sigma}$为自旋算符。

