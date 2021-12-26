# 演化算符

$$
|\psi(t)\rangle=U\left(t, t_{0}\right)\left|\psi\left(t_{0}\right)\right\rangle
$$

$U\left(t, t_{0}\right)$ 叫做体系的演变算符。
$$
U\left(t_0, t_{0}\right)=\mathbb{1}
$$
由薛定谔方程
$$
\mathrm{i} \hbar \frac{\partial}{\partial t} U\left(t, t_{0}\right)\left|\psi\left(t_{0}\right)\right\rangle=H(t) U\left(t, t_{0}\right)\left|\psi\left(t_{0}\right)\right\rangle
$$

$$
\mathrm{i} \hbar \frac{\partial}{\partial t} U\left(t, t_{0}\right)=H(t) U\left(t, t_{0}\right)
$$

$$
U\left(t, t_{0}\right)=\mathbb{1}-\frac{\mathrm{i}}{\hbar} \int_{t_{0}}^{t} H\left(t^{\prime}\right) U\left(t^{\prime}, t_{0}\right) \mathrm{d} t^{\prime}
$$

演化关系：
$$
U\left(t_{n}, t_{1}\right)=U\left(t_{n}, t_{n-1}\right) \cdots U\left(t_{3}, t_{2}\right) U\left(t_{2}, t_{1}\right)
$$

$$
U\left(t^{\prime}, t\right)=U^{-1}\left(t, t^{\prime}\right)
$$

## 无限小演化算符

薛定谔方程：
$$

\mathrm{d}|\psi(t)\rangle =|\psi(t+\mathrm{d} t)\rangle-|\psi(t)\rangle
=-\frac{\mathrm{i}}{\hbar} H(t)|\psi(t)\rangle \mathrm{d} t
$$

$$
|\psi(t+\mathrm{d} t)\rangle=\left[\mathbb{1}-\frac{\mathrm{i}}{\hbar} H(t) \mathrm{d} t\right]|\psi(t)\rangle
$$

$$
U(t+\mathrm{d} t, t)=\mathbb{1}-\frac{\mathrm{i}}{\hbar} H(t) \mathrm{d} t
$$

$H(t)$为厄密算符，故$U(t+dt,t)$为幺正算符。按演化关系，$U(t^\prime,t)$也是幺正算符。
$$
U^{\dagger}\left(t, t^{\prime}\right)=U^{-1}\left(t, t^{\prime}\right)=U\left(t^{\prime}, t\right)
$$
变换不改变态矢量的模。即态矢量的模不随时间变化。

## 保守系

$H$与时间无关，则
$$
U\left(t, t_{0}\right)=\mathrm{e}^{-\mathrm{i} H\left(t-t_{0}\right) / \hbar}
$$

$$
\mathscr{P}_{a}(c)=\left|\left\langle v_{c}\left|U\left(t_{2}, t_{0}\right)\right| u_{a}\right\rangle\right|^{2}
$$

$$
\mathscr{P}_{a}(b, c)=\left|\left\langle v_{c}\left|U\left(t_{2}, t_{1}\right)\right| w_{b}\right\rangle\right|^{2}\left|\left\langle w_{b}\left|U\left(t_{1}, t_{0}\right)\right| u_{a}\right\rangle\right|^{2}
$$

$$

\left\langle v_{c}\left|U\left(t_{2}, t_{0}\right)\right| u_{a}\right\rangle =\left\langle v_{c}\left|U\left(t_{2}, t_{1}\right) U\left(t_{1}, t_{0}\right)\right| u_{a}\right\rangle =\sum_{b}\left\langle v_{c}\left|U\left(t_{2}, t_{1}\right)\right| w_{b}\right\rangle\left\langle w_{b}\left|U\left(t_{1}, t_{0}\right)\right| u_{a}\right\rangle
$$

故
$$
\mathscr{P}_a(c)\ne\sum_b \mathscr{P}_a(b,c)
$$
