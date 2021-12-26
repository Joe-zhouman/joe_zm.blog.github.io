# 密度算符

## 态的统计混合

量子力学中，$\ket{\psi_i}$的概率为$p_i$，则
$$
p_{1}+p_{2}+\cdots=\sum_{k} p_{k}=1
$$
以上各态组成一个**统计混合态**

> * 各种态 $\left|\psi_{1}\right\rangle,\left|\psi_{2}\right\rangle, \cdots$ 不一定是正交的; 但是我们总可以将它们取 作归一化的. 
> * 概率出在两个阶段：初态和测量。在两个阶段都必须引人概率 的理由是完全不同的: 一种理由是关于体系的态的初始知识不完备 (在经 典统计力学中也考虑过这种情况). 另一种理由是与测量过程有关的 (特 别是量子力学的) 不确定性.
> * **初态的概率**和**态的线性叠加**是两种概念。线性叠加态不能看成处于各**基矢**状态概率为对应数值的态的叠加。统计混合态不能用平均态矢量描述，会丢失态之间的干涉项。

## 密度算符

对于**纯态**，除一个态的概率$p_k$为1以外，其他的态概率为0.

---

态矢量描述
$$
|\psi(t)\rangle=\sum_{n} c_{n}(t)\left|u_{n}\right\rangle
$$
对观察量$A$，矩阵元为
$$
\left\langle u_{n}|A| u_{p}\right\rangle=A_{n p}
$$
平均值
$$
\langle A\rangle(t)=\langle\psi(t)|A| \psi(t)\rangle=\sum_{n, p} c_{n}^{*}(t) c_{p}(t) A_{n p}
$$
演化方程：
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t}|\psi(t)\rangle=H(t)|\psi(t)\rangle
$$

---

密度算符描述
$$
\rho(t)=|\psi(t)\rangle\langle\psi(t)|
$$

$$
\rho_{p n}(t)=\left\langle u_{p}|\rho(t)| u_{n}\right\rangle=c_{n}^{*}(t) c_{p}(t)
$$

归一化：
$$
\sum_{n}\left|c_{n}(t)\right|^{2}=\sum_{n} \rho_{n n}(t)=\operatorname{Tr} \rho(t)=1
$$

$$
\begin{aligned}
\langle A\rangle(t) &=\sum_{n, p}\left\langle u_{p}|\rho(t)| u_{n}\right\rangle\left\langle u_{n}|A| u_{p}\right\rangle \\
&=\sum_{p}\left\langle u_{p}|\rho(t) A| u_{p}\right\rangle \\
&=\operatorname{Tr}\{\rho(t) A\}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d} t} \rho(t) &=\left(\frac{\mathrm{d}}{\mathrm{d} t}|\psi(t)\rangle\right)\langle\psi(t)|+| \psi(t)\rangle\left(\frac{\mathrm{d}}{\mathrm{d} t}\langle\psi(t)|\right) \\
&=\frac{1}{\mathrm{i} \hbar} H(t)|\psi(t)\rangle\left\langle\psi(t)\left|+\frac{1}{(-\mathrm{i} \hbar)}\right| \psi(t)\right\rangle\langle\psi(t)| H(t) \\
&=\frac{1}{\mathrm{i} \hbar}[H(t), \rho(t)]
\end{aligned}
$$

概率守恒：
$$
\operatorname{Tr} \rho(t)=1
$$
平均值：
$$
\langle A\rangle(t)=\operatorname{Tr}\{A \rho(t)\}=\operatorname{Tr}\{\rho(t) A\}
$$
演化方程：
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t} \rho(t)=[H(t), \rho(t)]
$$

---

## 态的统计混合

假设态矢量为 $\left|\psi_{k}\right\rangle$ 时, 得到测量结果 $a_{n}$ 的概率是:
$$
\mathscr{P}_{k}\left(a_{n}\right)=\left\langle\psi_{k}\left|P_{n}\right| \psi_{k}\right\rangle
$$

$$
\mathscr{P}\left(a_{n}\right)=\sum_{k} p_{k} \mathscr{P}_{k}\left(a_{n}\right)
$$

$$
\mathscr{P}_{k}\left(a_{n}\right)=\operatorname{Tr}\left\{\rho_{k} P_{n}\right\}
$$

$$
\mathscr{P}\left(a_{n}\right)=\operatorname{Tr}\left\{\rho P_{n}\right\}
$$

$$
\rho=\sum_{k} p_{k} \rho_{k}
$$

### 密度算符的性质

$$
\operatorname{Tr} \rho=\sum_{k} p_{k}=1
$$

$$

\langle A\rangle =\sum_{n} a_{n} \mathscr{P}\left(a_{n}\right)=\operatorname{Tr}\left\{\rho \sum_{n} a_{n} P_{n}\right\} 
=\operatorname{Tr}\{\rho A\}
$$

时间演化：
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t} \rho(t)=[H(t), \rho(t)]
$$
正算符：
$$
\langle u|\rho| u\rangle \geqslant 0
$$

### 布居数和相干元

$$
\rho_{n n}=\sum_{k} p_{k}\left[\rho_{k}\right]_{n n}
$$

$$
c_{n}^{(k)}=\left\langle u_{n} \mid \psi_{k}\right\rangle
$$

$$
\rho_{n n}=\sum_{k} p_{k}\left|c_{n}^{(k)}\right|^{2}
$$

> 看出 $\rho_{n n}$ 表示发现体系处于态 $\left|u_{n}\right\rangle$ 的平均概率. 因 此, 我们称 $\rho_{n n}$ 为态 $\left|u_{n}\right\rangle$ 的**布居数**, 也就是说, 如果在同样的初始条件下, 进行 极多次 $\left(N\right.$ 次) 同样的测量, 那么我们将会发现共有 $N \rho_{n n}$ 个体系处于态 $\left|u_{n}\right\rangle$.

非对角元
$$
\rho_{n p}=\sum_{k} p_{k} c_{n}^{(k)} c_{p}^{(k) *}
$$
表示态$\ket{u_n}$和$\ket{u_p}$之间的干涉效应。$\rho_{np}$为0表示干涉项的平均值相互抵消，不为零表示具有相干性。

> 布居数与相干元之间的差异依赖于态空间中基 $\left\{\left|u_{n}\right\rangle\right\}$ 的选 择. 由于 $\rho$ 是厄米算符, 我们总可以找到一个正交归一基 $\left\{\left|\chi_{l}\right\rangle\right\}$, 使 $\rho$ 在其 中成为对角的.因此, 我们可以认为, $\rho$ 所描述的是概率为 $\pi_{l}$ 的诸 $\left|\chi_{l}\right\rangle$ 态的统计混合 (诸 $\left|\chi_{l}\right\rangle$ 态之间没有相干元).

>布居数为常数，相干元以体系的波尔频率震荡。

