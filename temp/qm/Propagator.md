# 传播函数

$$
\psi\left(\boldsymbol{r}_{2}, t_{2}\right)=\int \mathrm{d}^{3} r_{1} K\left(\boldsymbol{r}_{2}, t_{2} ; \boldsymbol{r}_{1}, t_{1}\right) \psi\left(\boldsymbol{r}_{1}, t_{1}\right)
$$

![image-20211219190041876](https://s2.loli.net/2021/12/19/g57ISthJ2R8HEmT.png)

于时刻 $t_{2}$ 在点 $\boldsymbol{r}_{2}$ 处找到粒子的概率幅, 等于在空-时 中的曲面 $t=t_{1}$ 上的各个 “子波源” $\left(\boldsymbol{r}_{1}, t\right),\left(\boldsymbol{r}_{1}^{\prime}, t_{1}\right), \cdots$ 所 “辐射” 的所有振幅的 总和, 各个子波源的贡献分别正比于 $\psi\left(\boldsymbol{r}_{1}, t_{1}\right), \psi\left(\boldsymbol{r}_{1}^{\prime}, t_{1}\right), \cdots$  将 $K$ 称为薛定谔方程的`传播函数`。

## 传播函数的性质

### $K(2,1)$

$$
\left|\psi\left(t_{2}\right)\right\rangle=U\left(t_{2}, t_{1}\right)\left|\psi\left(t_{1}\right)\right\rangle
$$

$$
\psi\left(\boldsymbol{r}_{2}, t_{2}\right)=\left\langle\boldsymbol{r}_{2} \mid \psi\left(t_{2}\right)\right\rangle
$$

$$
\begin{aligned}
\psi\left(\boldsymbol{r}_{2}, t_{2}\right) &=\int \mathrm{d}^{3} r_{1}\left\langle\boldsymbol{r}_{2}\left|U\left(t_{2}, t_{1}\right)\right| \boldsymbol{r}_{1}\right\rangle\left\langle\boldsymbol{r}_{1} \mid \psi\left(t_{1}\right)\right\rangle \\
&=\int \mathrm{d}^{3} r_{1}\left\langle\boldsymbol{r}_{2}\left|U\left(t_{2}, t_{1}\right)\right| \boldsymbol{r}_{1}\right\rangle \psi\left(\boldsymbol{r}_{1}, t_{1}\right)
\end{aligned}
$$

$$
K\left(\boldsymbol{r}_{2}, t_{2} ; \boldsymbol{r}_{1}, t_{1}\right)=\left\langle\boldsymbol{r}_{2}\left|U\left(t_{2}, t_{1}\right)\right| \boldsymbol{r}_{1}\right\rangle \theta\left(t_{2}-t_{1}\right)
$$

$\theta$为阶跃函数。

 $K(2,1)$ 的物理解释: 它表示在时刻 $t_{1}$ 从点 $\boldsymbol{r}_{1}$ 出发的粒子在此后的某时刻 $t_{2}$ 到达点 $\boldsymbol{r}_{2}$ 的概率幅. 

若$H$不显含时间，则
$$
H\left|\varphi_{n}\right\rangle=E_{n}\left|\varphi_{n}\right\rangle
$$

$$
U\left(t_{2}, t_{1}\right)=\mathrm{e}^{-\mathrm{i} H\left(t_{2}-t_{1}\right) / \hbar}
$$

$$
U\left(t_{2}, t_{1}\right)=\mathrm{e}^{-\mathrm{i} H\left(t_{2}-t_{1}\right) / \hbar} \sum_{n}\left|\varphi_{n}\right\rangle\left\langle\varphi_{n}\right|
$$

$$
U\left(t_{2}-t_{1}\right)=\sum_{n} \mathrm{e}^{-\mathrm{i} E_{n}\left(t_{2}-t_{1}\right) / \hbar}\left|\varphi_{n}\right\rangle\left\langle\varphi_{n}\right|
$$

$$
\left\langle\boldsymbol{r}_{2} \mid \varphi_{n}\right\rangle=\varphi_{n}\left(\boldsymbol{r}_{2}\right)
$$

$$
\left\langle\varphi_{n} \mid \boldsymbol{r}_{1}\right\rangle=\varphi_{n}^{*}\left(\boldsymbol{r}_{1}\right)
$$

$$
K\left(\boldsymbol{r}_{2}, t_{2} ; \boldsymbol{r}_{1}, t_{1}\right)=\theta\left(t_{2}-t_{1}\right) \sum_{n} \varphi_{n}^{*}\left(\boldsymbol{r}_{1}\right) \varphi_{n}\left(\boldsymbol{r}_{2}\right) \mathrm{e}^{-\mathrm{i} E_{n}\left(t_{2}-t_{1}\right) / \hbar}
$$

$$
\left[\mathrm{i} \hbar \frac{\partial}{\partial t_{2}}-H\left(r_{2}, \frac{h}{\mathrm{i}} \nabla_{2}\right)\right] \varphi_{n}\left(r_{2}\right) \mathrm{e}^{-\mathrm{i} E_{n} t_{2} / \hbar}=0
$$

$$

\left[\mathrm{i} \hbar \frac{\partial}{\partial t_{2}}-H\left(r_{2}, \frac{\hbar}{\mathrm{i}} \nabla_{2}\right)\right] K\left(r_{2}, t_{2} ; r_{1}, t_{1}\right) 
= \mathrm{i} \hbar \delta\left(t_{2}-t_{1}\right) \sum_{n} \varphi_{n}^{*}\left(r_{1}\right) \varphi_{n}\left(r_{2}\right) \mathrm{e}^{-\mathrm{i} E_{n}\left(t_{2}-t_{1}\right) / \hbar}
$$

$$
\left[\mathrm{i} \hbar \frac{\partial}{\partial t_{2}}-H\left(r_{2}, \frac{\hbar}{\mathrm{i}} \nabla_{2}\right)\right] K\left(r_{2}, t_{2} ; r_{1}, t_{1}\right)=\mathrm{i} \hbar \delta\left(t_{2}-t_{1}\right) \delta\left(r_{2}-r_{1}\right)
$$

上述方程的解为**格林函数**

## 拉格朗日表述

![image-20211219193415223](https://s2.loli.net/2021/12/19/NBt7LGbwPIgSmko.png)

 $\boldsymbol{r}(t)$ 确定了 $\left(\boldsymbol{r}_{1}, t_{1}\right)$ 和 $\left(\boldsymbol{r}_{2}, t_{2}\right)$ 之间的一条空-时路径. 我们不妨将它看 作质点于时刻 $t_{1}$ 从点 $r_{1}$ 出发于时刻 $t_{2}$ 到达点 $r_{2}$ 所走过的路径.
$$
\begin{aligned}
K(2,1)=& \int \mathrm{d}^{3} r_{\alpha_{N}} \int \mathrm{d}^{3} r_{\alpha_{N-1}} \cdots \int \mathrm{d}^{3} r_{\alpha_{2}} \int \mathrm{d}^{3} r_{\alpha_{1}} K\left(2, \alpha_{N}\right) \\
& \times K\left(\alpha_{N}, \alpha_{N-1}\right) \cdots K\left(\alpha_{2}, \alpha_{1}\right) K\left(\alpha_{1}, 1\right)
\end{aligned}
$$
这个乘积为粒子从点 $1\left(\boldsymbol{r}_{1}, t_{1}\right)$ 出 发, 顺次通过图 中诸点 $\alpha_{i}\left(r_{\alpha_{i}}, t_{\alpha_{i}}\right)$ 而到达点 $2\left(r_{2}, t_{2}\right)$ 的概率幅. 上述积分要对一切中间可能位置求积分。

* (空-时中的点 $\left(r_{1}, t_{1}\right)$ 和点 $\left(r_{2}, t_{2}\right)$ 之间的每一条路径都有一个对应的 部分幅, $K(2,1)$ 就是这无限多个部分幅的总和.

* 对应于某一条路径 $\boldsymbol{\Gamma}$ 的部分幅 $K_{\Gamma}(2,1)$ 可按下述方式求得: 假设 $S_{\boldsymbol{\Gamma}}$ 是沿路径 $\boldsymbol{r}$ 计算出来的经典作用量, 即

$$
S_{\boldsymbol{\Gamma}}=\int_{(\boldsymbol{\Gamma})} \mathscr{L}(\boldsymbol{r}, \boldsymbol{p}, t) \mathrm{d} t
$$

$$
K_{\Gamma}(2,1)=N \mathrm{e}^{\frac{i}{\hbar} S_{r}}
$$

若$S_\Gamma \gg \hbar$，但两条路径之间的改变量一般来说$\Delta S_{\Gamma}\ll \hbar$，此时$K$的相位变化很快，绝大多数路径的贡献因相干而相互抵消。

 如果存在这样一条路径 $\boldsymbol{\Gamma}_{0}$, 与它 对应的作用量是稳定的 (意思是说, 从 $\Gamma_{0}$ 过渡到一条无限邻近的路径时, 在一 级近似下, 作用量没有变化), 那么, 幅度 $K_{\Gamma_{0}}(2,1)$ 将与靠近 $\Gamma_{0}$ 的那些路径的 幅度相长地相干, 这是因为现在它们的相位实际上是保持一致的. 因此, 如果 作用量 $S_{\Gamma}$ 甚大于 $\hbar$, 那么, 我们遇到的便是 “准经典的” 情况, 这时, 要得到$K(2,1)$, 我们只需考虑 $\boldsymbol{\Gamma}_{0}$ 和与它无限邻近的路径, 其他路径都可忽略; 而且我 们可以说, 在点 1 和点 2 之间粒子通过的路径就是 $\boldsymbol{\Gamma}_{0}$. 

这些假设为最小作用量原理提供一个假想的解释: 与粒子相联系的波, “试探” 了各条可能的路径, 终于选出在其上作用量为最小的那条路径.