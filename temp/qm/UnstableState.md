# 不稳定态与寿命

* 一个孤立的严格保守系的初态如果是若干定态的组合, 则体系的 态将随时间演变, 因而它不会总是停留在同一个态. 但它的哈密顿函数是 一个运动常量, 能量的任何一个值出现的概率, 如同能量的平均值一样, 是与时间无关的. 反之, 在非稳态的情况下, 在一 个态和另一个态之间会发生不可逆的过渡, 同时体系的能量有所损失, 这 部分能量被发射出去的光子所带走.
* 原子的激发态的不稳定性起因于光子的自发发射; 基态是稳定的, 因为没有比它更低的能态. 可是, 我们要注意, 原子也可能吸收光的能量, 而过渡到更高的能态.

## 寿命

 如果我们使体系在 $t=0$ 时处 于非稳态 $\left|\varphi_{n}\right\rangle$, 那么, 可以验证: 在以后的某时刻 $t$, 体系仍然停留在这个态的 概率 $\mathscr{P}(t)$ 应为:
$$
\mathscr{P}(t)=\mathrm{e}^{-t / \tau}
$$
$\tau$为态的寿命。

在时刻 $t$ 到 $t+\mathrm{d} t$ 之间, 脱离了这个非稳定态的体系的数目为:
$$
\mathrm{d} n(t)=N(t)-N(t+\mathrm{d} t)=-\frac{\mathrm{d} N(t)}{\mathrm{d} t} \mathrm{~d} t=N(t) \frac{\mathrm{d} t}{\tau}
$$

$$
\mathrm{d} w(t)=\frac{\mathrm{d} n(t)}{N(t)}=\frac{\mathrm{d} t}{\tau}
$$

1. 每单位时间内体系脱离非稳态的概率是 $1 / \tau$.

$$
\int_{0}^{\infty} t \mathrm{e}^{-t / \tau} \frac{\mathrm{d} t}{\tau}=\tau
$$

可见 $\tau$ 就是体系在态 $\left|\varphi_{n}\right\rangle$ 中度过的平均时间

2. 寿命 $\tau$ 有一个很值得注意的性质, 就是它与我们使体系进人非稳 态的方法无关, 也就是说, 它与体系过去的 “历史” 无关. 因此, 寿命是非稳 态本身的一个特征.

3. 根据时间-能量不确定度关系式, 表征非稳态演 变的时间 $\tau$, 与一能量不确定度 $\Delta E$ 相联系, 它由下式给出:

$$
\Delta E \simeq \frac{\hbar}{\tau}
$$

实际上, 我们发现不能以任意高的精确度去稳定非稳态的能量, 至少要带 有数量级为 $\Delta E$ 的不确定度. 因此, 我们称 $\Delta E$ 为该能级的自然宽度. 就氢 原子而言, 各能级的自然宽度和各能级间的间隔相比, 小到可以忽略, 因 此在一级近似下我们可以把它们当作是稳定的.

## 非稳定态的唯象描述

$$
|\psi(t)\rangle=\mathrm{e}^{-\mathrm{i} E_{n} t / \hbar}\left|\varphi_{n}\right\rangle
$$

在 $t$ 时刻进行观测, 发现体系处于态 $\left|\varphi_{n}\right\rangle$ 的概率 $\mathscr{P}_{n}(t)$ 为:
$$
\mathscr{P}_{n}(t)=\left|\mathrm{e}^{-\mathrm{i} E_{n} t / \hbar}\right|^{2}
$$
若
$$
E_{n}^{\prime}=E_{n}-\mathrm{i} \hbar \frac{\gamma_{n}}{2}
$$

$$
\mathscr{P}_{n}^{\prime}(t)=\left|\mathrm{e}^{-\mathrm{i}\left(E_{n}-\frac{1}{2} \mathrm{i} \hbar \gamma_{n}\right) t / \hbar}\right|^{2}=\mathrm{e}^{-\gamma_{n} t}
$$

在这种情况下,, 我们发现体系处于态 $\left|\varphi_{n}\right\rangle$ 的概率按指 数规律随时间衰减. 因此, 为了唯象地考虑寿命为 $\tau_{n}$ 的态 $\left|\varphi_{n}\right\rangle$ 的不稳定性, 只需在这个态的能量上附加一个虚部, 并令
$$
\gamma_{n}=\frac{1}{\tau_{n}}
$$

---

注：

态矢量 的模之所以不变化, 是因为哈密顿算符具有厄米性; 但是, 本征值为复数 $\left(\right.$ 如 $\left.E_{n}^{\prime}\right)$ 的算符不可能是厄米算符. 

我们所研究的体系是更大的体系的一部分 (该体系与电磁场有相 互作用), 而且严格说来, 我们不可能用哈密顿算符来描述它的演变. 引人 一个具有复本征值的 “哈密顿算符”, 就能简单地说明这种体系的演变, 这 是颇为引人注意的.

---

