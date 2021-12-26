# 绘景

## 薛定谔绘景

与体系的可观察量对应的,一般都是与 时间无关的算符. 例如, 粒子的位置算符、动量算符及 动能算符都是不依赖于时间的. 体系的演变完全包含在态矢量 $|\psi(t)\rangle$ 记作 $\left|\psi_{S}(t)\right\rangle$,的演变中, 而且这种演变可以用薛定谔方程求得. 称这种绘景为**薛定谔绘景**.
$$
\left|\psi_{S}(t)\right\rangle=U\left(t, t_{0}\right)\left|\psi_{S}\left(t_{0}\right)\right\rangle
$$

## 海森堡绘景

选择这样一种变换, 使得右矢 $\left|\psi_{S}(t)\right\rangle$ 的变换 式成为一个与时间无关的右矢; 可观察量经过这样的 变换将依赖于时间了. 这样我们便得到了**海森伯绘景**.
$$
\begin{aligned}
\left|\psi_{H}\right\rangle &=U^{\dagger}\left(t, t_{0}\right)\left|\psi_{S}(t)\right\rangle \\
&=U^{\dagger}\left(t, t_{0}\right) U\left(t, t_{0}\right)\left|\psi_{S}\left(t_{0}\right)\right\rangle \\
&=\left|\psi_{S}\left(t_{0}\right)\right\rangle
\end{aligned}
$$

$$
A_{H}(t)=U^{\dagger}\left(t, t_{0}\right) A_{S}(t) U\left(t, t_{0}\right)
$$

体系为保守系时，
$$
U\left(t, t_{0}\right)=\mathrm{e}^{-\mathrm{i} H_{S}\left(t-t_{0}\right) / \hbar}
$$

$$
A_{H}(t)=U^{\dagger}\left(t, t_{0}\right) U\left(t, t_{0}\right) A_{S}=A_{S}
$$

对任意$A_S(t)$
$$
\frac{\mathrm{d}}{\mathrm{d} t} A_{H}(t)=-\frac{1}{\mathrm{i} \hbar} U^{\dagger}\left(t, t_{0}\right) H_{S}(t) A_{S}(t) U\left(t, t_{0}\right)+U^{\dagger}\left(t, t_{0}\right) \frac{\mathrm{d} A_{S}(t)}{\mathrm{d} t} U\left(t, t_{0}\right) 
+\frac{1}{\mathrm{i} \hbar} U^{\dagger}\left(t, t_{0}\right) A_{S}(t) H_{S}(t) U\left(t, t_{0}\right)
$$
在$H_S(t)$和$A_S(t)$之间插入恒定算符$UU^\dagger$，则
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t} A_{H}(t)=\left[A_{H}(t), H_{H}(t)\right]+\mathrm{i} \hbar\left(\frac{\mathrm{d}}{\mathrm{d} t} A_{S}(t)\right)_{H}
$$
平均值
$$
\langle A\rangle(t)=\left\langle\psi_{H}\left|A_{H}(t)\right| \psi_{H}\right\rangle
$$