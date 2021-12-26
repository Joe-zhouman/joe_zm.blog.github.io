# 规范不变性

## 简述

对于满足麦克斯韦方程组的电场和磁场，可以引入标势和矢势，使：
$$
\boldsymbol{E}(\boldsymbol{r}, t)=-\nabla U(\boldsymbol{r}, t)-\frac{\partial}{\partial t} \boldsymbol{A}(\boldsymbol{r}, t)
$$

$$
\boldsymbol{B}(\boldsymbol{r}, t)=\nabla \times \boldsymbol{A}(\boldsymbol{r}, t)
$$

但由电场和磁场不能唯一确定标势和矢势。如以下变换
$$
U^{\prime}(\boldsymbol{r}, t)=U(\boldsymbol{r}, t)-\frac{\partial}{\partial t} \chi(\boldsymbol{r}, t)
$$

$$
\boldsymbol{A}^{\prime}(\boldsymbol{r}, t)=\boldsymbol{A}(\boldsymbol{r}, t)+\nabla \chi(\boldsymbol{r}, t)
$$

不改变电场和磁场。

选用一组特定的势即选择了一种规范。规范不改变物理结果。

## 经典力学的规范不变性

洛伦茨力
$$
\boldsymbol{f}=q[\boldsymbol{E}(\boldsymbol{r}, t)+\boldsymbol{v} \times \boldsymbol{B}(\boldsymbol{r}, t)]
$$
牛顿力学的基本方程：
$$
m \frac{\mathrm{d}^{2}}{\mathrm{~d} t^{2}} \boldsymbol{r}(t)=\boldsymbol{f}
$$
单粒子的拉格朗日量
$$
\mathscr{L}(\boldsymbol{r}, \boldsymbol{v} ; t)=\frac{1}{2} m \boldsymbol{v}^{2}-q[U(\boldsymbol{r}, t)-\boldsymbol{v} \cdot \boldsymbol{A}(\boldsymbol{r}, t)]
$$

$$
\boldsymbol{p}=\nabla_{\boldsymbol{v}} \mathscr{L}(\boldsymbol{r}, \boldsymbol{v} ; t)=m \boldsymbol{v}+q \boldsymbol{A}(\boldsymbol{r}, t)
$$

哈密顿量：
$$
\mathscr{H}(\boldsymbol{r}, \boldsymbol{p}, t)=\frac{1}{2 m}[\boldsymbol{p}-q \boldsymbol{A}(\boldsymbol{r}, t)]^{2}+q U(\boldsymbol{r}, t)
$$
机械动量
$$
\boldsymbol{\pi}=m \boldsymbol{v}=\boldsymbol{p}-q\boldsymbol{A}(\boldsymbol{r},t)
$$
显然在不同规范下，有
$$
\boldsymbol{r}^{\prime}(t)=\boldsymbol{r}(t)
$$

$$
\pi^{\prime}(t)=\pi(t)
$$

但在不同规范下，
$$
\boldsymbol{p}^{\prime}(t)-q \boldsymbol{A}^{\prime}\left[\boldsymbol{r}^{\prime}(t), t\right]=\boldsymbol{p}(t)-q \boldsymbol{A}[\boldsymbol{r}(t), t]
$$
固有
$$
\boldsymbol{p}^{\prime}(t)=\boldsymbol{p}(t)+q \nabla \chi[\boldsymbol{r}(t), t]
$$

> 在哈密顿表述形式中, 描述某种运动的力学变量在任何时刻的值都依赖于我们所选用的规范 $\mathscr{J}$. 

### 真实物理量和非物理量

> 一所研究的体系的**真实物理量**是这样一些量, 它们在任意时刻的值 (就体 系的某一特定运动而言) 都不依赖于用以描述电磁场的规范.
>
> 一非物理量 则是这样一些量, 进行规范变换时, 它们的值要受到修正. 因此, 这一类量, 如同标势和矢势一样, 表现为一种计算工具, 而不是实际上可观 察的量.

规范 $\mathscr{J}^{\prime}$ 中的函数 $\mathscr{G}_{g^{\prime}}[r, p ; t]$, 如果将其中的 $p$ 换成 $p+$ $q \nabla \chi(\boldsymbol{r}, t)$ , 由此得到的 $r$ 和 $p$ 的新函数应该与 $\mathscr{G}_{g}[r, p ; t]$ 全同; 如若不然, 所考查的函数所对应 的量便不是一个真实的物理量.
$$
\mathscr{G}_{\mathscr{J}}[\boldsymbol{r}, \boldsymbol{p} ; t]=\mathscr{G}_{\mathscr{J}^{\prime}}[\boldsymbol{r}, \boldsymbol{p}+q \nabla \chi(\boldsymbol{r}, t) ; t]
$$
真实物理量：

---

机械动量
$$
\pi_{\mathscr{J}}(r, p ; t)=p-q A(r, t)
$$
动能
$$
\gamma_{\mathscr{J}}(\boldsymbol{r}, \boldsymbol{p}, t)=\frac{1}{2 m}[\boldsymbol{p}-q \boldsymbol{A}(\boldsymbol{r}, t)]^{2}
$$
具有以下形式的均为真实物理量：
$$
\mathscr{G}_{\mathscr{J}}(\boldsymbol{r}, \boldsymbol{p}, t)=F[\boldsymbol{r}, \boldsymbol{p}-q \boldsymbol{A}(\boldsymbol{r}, t)]
$$

---

非物理量：

---

$$
\mathscr{C}(\boldsymbol{p})=\frac{\boldsymbol{p}^{2}}{2 m}
$$

角动量
$$
\mathscr{L}(\boldsymbol{r}, \boldsymbol{p})=\boldsymbol{r} \times \boldsymbol{p}
$$
哈密顿量

---

## 量子力学的规范不变性

> 应该用一个随规范而变的数学的态矢量 $|\psi\rangle$ 去描述一个给 定的物理体系, 从一种规范 $\mathscr{J}$ 中的态矢量过渡到另一种规范 $\mathscr{J}^{\prime}$ 中的态矢量, 要由幺正变换来实现; 但薛定谔方程的形式则永远保持不变 。

位置算符和动量算符在任何规范下都一样。按量子化规则，由$R,P$算符组成的算符在任何规范中一样。

### 态矢量变换

$$
\left\langle\psi^{\prime}(t)\left|\boldsymbol{R}_{\mathscr{J}^{\prime}}\right| \psi^{\prime}(t)\right\rangle=\left\langle\psi(t)\left|\boldsymbol{R}_{\mathscr{g}}\right| \psi(t)\right\rangle
$$

$$
\left\langle\psi^{\prime}(t)\left|\boldsymbol{P}_{\mathscr{g}^{\prime}}\right| \psi^{\prime}(t)\right\rangle=\left\langle\psi(t)\left|\boldsymbol{P}_{\mathscr{J}}+q \nabla \chi(\boldsymbol{R}, t)\right| \psi(t)\right\rangle
$$

$$
T_{\chi}(t)=\mathrm{e}^{\mathrm{i} F(\boldsymbol{R}, t)}
$$

$$
\left[\boldsymbol{P}, T_{\chi}(t)\right]=\hbar \nabla\{F(\boldsymbol{R}, t)\} T_{\chi}(t)
$$

$$
\hbar \nabla\{F(\boldsymbol{R}, t)\}=q \nabla \chi(\boldsymbol{R}, t)
$$

$$
F(\boldsymbol{R}, t)=F_{0}(t)+\frac{q}{\hbar} \chi(\boldsymbol{R}, t)
$$

$$
T_{\chi}(t)=\mathrm{e}^{\mathrm{i} \frac{q}{\hbar} \chi(\boldsymbol{R}, t)}
$$

因此, 对于波函数来说, 规范变换并不对应于乘上一个总的相位因子, 而是表 现为随点而异的相位变化. 由此可见, 利用波函数 $\psi$ 或 $\psi^{\prime}$ 得到的物理预言 具有规范不变性, 这并非不证自明的.

时间演化
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t}|\psi(t)\rangle=H_{\mathscr{J}}(t)|\psi(t)\rangle
$$

$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t}\left|\psi^{\prime}(t)\right\rangle=H_{\mathscr{J}^\prime}(t)\left|\psi^{\prime}(t)\right\rangle
$$

$$
\widetilde{H}_{\mathscr{J}}=T_{\chi}(t) H_{\mathscr{J}}(t) T_{\chi}^{\dagger}(t)
$$

$$
H_{\mathscr{J} \prime}(t)=\widetilde{H}_{\mathscr{J}}(t)-q \frac{\partial}{\partial t} \chi(\boldsymbol{R}, t)
$$

对任何可观察量：
$$
\widetilde{K}=T_{\chi}(t) K T_{\chi}^{\dagger}(t)
$$

> 在量子力学中, 与任何真实物理量 相联系的算符 $G_{\mathscr{L}}(t)$ 都满足关系：

$$
\widetilde{G}_{\mathscr{J}}(t)=G_{\mathscr{J}^{\prime}}(t)
$$

除了 $\boldsymbol{R}$ 或只依赖于 $\boldsymbol{R}$ 的 函数这种特殊情况以外, 与真实物理量对应的算符都依赖于规范 $\mathscr{J}$。

### 真实物理量的概率

$$
G_{\mathscr{J}}\left|\varphi_{n}\right\rangle=g_{n}\left|\varphi_{n}\right\rangle
$$

$$
\mathscr{P}_{n}=\left|\left\langle\varphi_{n} \mid \psi\right\rangle\right|^{2}
$$

$$
\left|\varphi_{n}^{\prime}\right\rangle=T_{\chi}\left|\varphi_{n}\right\rangle
$$

$$

G_{g^{\prime}}\left|\varphi_{n}^{\prime}\right\rangle =T_{\chi} G_{\not g} T_{\chi}^{\dagger} T_{\chi}\left|\varphi_{n}\right\rangle =T_{\chi} g_{n}\left|\varphi_{n}\right\rangle 
=g_{n}\left|\varphi_{n}^{\prime}\right\rangle
$$

$$
\left\langle\varphi_{n}^{\prime} \mid \psi^{\prime}\right\rangle=\left\langle\varphi_{n}\left|T_{\chi}^{\dagger} T_{\chi}\right| \psi\right\rangle=\left\langle\varphi_{n} \mid \psi\right\rangle
$$

### 概率密度和概率流

$$
\rho(\boldsymbol{r}, t)=|\psi(\boldsymbol{r}, t)|^{2}
$$

$$
\boldsymbol{J}(\boldsymbol{r}, t)=\frac{1}{m} \operatorname{Re}\left\{\psi^{*}(\boldsymbol{r}, t)\left[\frac{\hbar}{\mathrm{i}} \nabla-q \boldsymbol{A}(\boldsymbol{r}, t)\right] \psi(\boldsymbol{r}, t)\right\}
$$

$$
\rho^{\prime}(\boldsymbol{r}, t)=\left|\psi^{\prime}(\boldsymbol{r}, t)\right|^{2}=\rho(\boldsymbol{r}, t)
$$

$$
\boldsymbol{J}^{\prime}(\boldsymbol{r}, t)=\boldsymbol{J}(\boldsymbol{r}, t)
$$

规范变换下，概率密度和概率流不变。