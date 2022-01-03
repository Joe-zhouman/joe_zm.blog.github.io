## 狄拉克符号，对易子，本征矢与本征值

### Q

我们用 $\left|\varphi_{n}\right\rangle$ 表示厄米算符 $H$ 的本征态 (憵如, $H$ 可以是任何物理体系 的哈密顿算符), 假设全体 $\left|\varphi_{n}\right\rangle$ 构成一个离散的正交归一基. 算符 $U(m, n)$ 的 定义是
$$
U(m, n)=\left|\varphi_{m}\right\rangle\left\langle\varphi_{n}\right|
$$
a. 计算 $U(m, n)$ 的伴随算符 $U^{\dagger}(m, n)$
$$
\begin{align}
&\bra{\psi}U(m,n)^{\dagger}\ket{\varphi}=\bra{\varphi}U(m,n)\ket{\psi}^*= (\bra{\varphi}\ket{\varphi_m}\bra{\varphi_n}\ket{\psi})^*\\
=&(a_{m}^*b_{n})^*	=b_{n}^{*}a_{m}=\bra{\psi} \ket{\varphi_{n}} \bra{\varphi_m} \ket{\varphi}
\end{align}
$$

$$
U^\dagger(m,n)=\ket{\varphi_n}\bra{\varphi_m}
$$

b. 计算对易子 $[H, U(m, n)]$
$$
[H,U(m,n)]\ket{\psi}=HU(m,n)\ket{\psi}-U(m,n)H\ket{\psi}
$$

$$
=b_{n}H \ket{\varphi_m}-U(m,n) \sum\limits_{i=0}^{\infty}E_{i} \ket{\varphi_i}=b_{n}E_{m}\ket{\varphi_m}-b_{n}E_{n}\ket{\varphi_m}
$$

$$
=H (\ket{\varphi_m} - \ket{\varphi_n}) \bra{\varphi_n} \ket{\psi}=H(U(m,n)-U(n,n))
$$



c. 证明:
$$
U(m, n) U^{\dagger}(p, q)=\delta_{n, q} U(m, p)
$$
$$
\ket{\varphi_m} \bra{\varphi_n} \ket{\varphi_q} \bra{\varphi_p}=\delta_{n,p}\ket{\varphi_m} \bra{\varphi_p}=\delta_{n,p}U(m,n)
$$



d. 计算算符 $U(m, n)$ 的迹 $\operatorname{Tr}\{U(m, n)\}$
$$
TrU(m,n)=\sum\limits_{i=_\infty}^{\infty} \bra{\varphi_i} U(m,n)\ket{\varphi_i}=\sum\limits_{i=-\infty}^{\infty} \bra{\varphi_i} \ket{\varphi_m} \bra{\varphi_n} \ket{\varphi_i}= \sum\limits_{i=-\infty}^{\infty} \delta_{im}\delta_{ni}=\delta_{mn}
$$


e. 设 $A$ 是一个算符, 它的矩阵元是 $A_{m n}=\left\langle\varphi_{m}|A| \varphi_{n}\right\rangle$; 试证:
$$
A=\sum_{m, n} A_{m, n} U(m, n)
$$
$$
A= \sum\limits_{m} \ket{\varphi_m} \bra{\varphi_m} A\sum\limits_{n} \ket{\varphi_n} \bra{\varphi_n}= \sum\limits_{m} \ket{\varphi_m} \sum\limits_{n} \bra{\varphi_m} A \ket{\varphi_n} \bra{\varphi_n}
$$

$$
= \sum\limits_{m} \ket{\varphi_m} \sum\limits_{n} A_{m,n} \bra{\varphi_n} = \sum\limits_{m,n} A_{m,n}U(m,n)
$$

f. 试证: $A_{p q}=\operatorname{Tr}\left\{A U^{\dagger}(p, q)\right\}$
$$
TrAU^{\dagger}(p,q)=\sum\limits_{i=-\infty}^{\infty} \bra{\varphi_i} AU^{\dagger}(p,q)\ket{\varphi_i} = \sum\limits_{i} \bra{\varphi_i}A \ket{\varphi_q} \bra{\varphi_p} \ket{\varphi_i}
$$

$$
= \sum\limits_{i}A_{i,q}\delta_{pi}=A_{pq}
$$

### Q

在一个二维矢量空间中, 考虑这样一个算符, 它在正交归一基 $\{|1\rangle,|2\rangle\}$ 中的矩阵为:
$$
\sigma_{y}=\left[\begin{array}{cc}
0 & -\mathrm{i} \\
\mathrm{i} & 0
\end{array}\right]
$$
a. $\sigma_{y}$ 是厄米算符吗? 试计算它的本征值和本征矢 (要给出它们在基 $\{|1\rangle,|2\rangle\}$ 中的已归一化的展开式).
$$
\sigma_{y}^{\dagger}=\sigma_{y}
$$
故为厄密算符。
$$
\lambda=\pm1
$$

对于$\lambda=1$
$$
\ket{\psi_1}= \frac{1}{\sqrt2}\ket{1} +\frac{i}{\sqrt2} \ket{2}
$$
对于$\lambda=-1$
$$
\ket{\psi_1}= \frac{1}{\sqrt2}\ket{1} -\frac{i}{\sqrt2} \ket{2}
$$


b. 计算在这些本征矢上的投影算符的矩阵, 然后证明它们满足正交归一 关系式和封闭性关系式.
$$

$$


c. 同样是上面这些问题, 但矩阵为
$$
M=\left[\begin{array}{cc}
2 & \mathrm{i} \sqrt{2} \\
-\mathrm{i} \sqrt{2} & 3
\end{array}\right]
$$
及三维空间的矩阵
$$
L_{y}=\frac{\hbar}{2 \mathrm{i}}\left[\begin{array}{ccc}
0 & \sqrt{2} & 0 \\
-\sqrt{2} & 0 & \sqrt{2} \\
0 & -\sqrt{2} & 0
\end{array}\right]
$$