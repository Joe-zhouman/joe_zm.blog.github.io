# 二能级系统

考虑这样一个物理体系, 它的态空间是二维的。选择哈密顿算符 $H_{0}$ 的分别属于本征值 $E_{1}$ 及 $E_{2}$ 的两个本征态 $\left|\varphi_{1}\right\rangle$ 及 $\left|\varphi_{2}\right\rangle$ 作为基:
$$
\begin{array}{l}
H_{0}\left|\varphi_{1}\right\rangle=E_{1}\left|\varphi_{1}\right\rangle \\
H_{0}\left|\varphi_{2}\right\rangle=E_{2}\left|\varphi_{2}\right\rangle
\end{array}
$$
这个基是正交归一的, 即
$$
\left\langle\varphi_{i} \mid \varphi_{j}\right\rangle=\delta_{i j} ; i, j=1,2
$$

## 微扰

考虑外界微扰或体系内部的相 互作用, 则哈密顿算符变为:
$$
H=H_{0}+W
$$

$$
\begin{array}{l}
H\left|\psi_{+}\right\rangle=E_{+}\left|\psi_{+}\right\rangle \\
H\left|\psi_{-}\right\rangle=E_{-}\left|\psi_{-}\right\rangle
\end{array}
$$

$H_{0}$ 通常叫做末微扰的哈密顿算符, $W$ 叫做微扰或耦合. 在这里, 我们假定 $W$ 不依赖于时间. 在由 $H_{0}$ 的本征态 (叫做末微扰的态) 组成的基 $\left\{\left|\varphi_{1}\right\rangle,\left|\varphi_{2}\right\rangle\right\}$ 中, $W$ 由一个厄米矩阵表示:
$$
(W)=\left(\begin{array}{ll}
W_{11} & W_{12} \\
W_{21} & W_{22}
\end{array}\right)
$$
一般说来, $\left|\varphi_{1}\right\rangle$ 和 $\left|\varphi_{2}\right\rangle$ 并不是总哈密顿算符 $H$ 的本征态, 因而也不再是 定态. 例如, 如果 $t=0$ 时体系处于态 $\left|\varphi_{1}\right\rangle$, 则这体系有一定的概率 $\mathscr{P}_{12}(t)$ 在 $t$ 时刻处于态 $\left|\varphi_{2}\right\rangle$; 这就是说, $W$ 引起两个末微扰的态之间的跃迁, 因此, 我们 称 $W$ 为 (态 $\left|\varphi_{1}\right\rangle$ 和态 $\left|\varphi_{2}\right\rangle$ 之间的) 耦合.
$$
(H)=\left(\begin{array}{cc}
E_{1}+W_{11} & W_{12} \\
W_{21} & E_{2}+W_{22}
\end{array}\right)
$$

$$
E_{+}=\frac{1}{2}\left(E_{1}+W_{11}+E_{2}+W_{22}\right)+\frac{1}{2} \sqrt{\left(E_{1}+W_{11}-E_{2}-W_{22}\right)^{2}+4\left|W_{12}\right|^{2}}
$$

$$
E_{-}=\frac{1}{2}\left(E_{1}+W_{11}+E_{2}+W_{22}\right)-\frac{1}{2} \sqrt{\left(E_{1}+W_{11}-E_{2}-W_{22}\right)^{2}+4\left|W_{12}\right|^{2}}
$$

$$
\left|\psi_{+}\right\rangle=\cos \frac{\theta}{2} \mathrm{e}^{-\mathrm{i} \varphi / 2}\left|\varphi_{1}\right\rangle+\sin \frac{\theta}{2} \mathrm{e}^{\mathrm{i} \varphi / 2}\left|\varphi_{2}\right\rangle
$$

$$
\left|\psi_{-}\right\rangle=-\sin \frac{\theta}{2} \mathrm{e}^{-\mathrm{i} \varphi / 2}\left|\varphi_{1}\right\rangle+\cos \frac{\theta}{2} \mathrm{e}^{\mathrm{i} \varphi / 2}\left|\varphi_{2}\right\rangle
$$

$$
\tan \theta=\frac{2\left|W_{12}\right|}{E_{1}+W_{11}-E_{2}-W_{22}}
$$

$$
W_{21}=\left|W_{21}\right| \mathrm{e}^{\mathrm{i} \varphi}
$$

## 耦合的作用

如果 $W_{11}$ 和 $W_{22}$ 不为零, 令 $\widetilde{E}_{1}=E_{1}+W_{11}, \widetilde{E}_{2}=E_{2}+W_{22}$ .故可假设$W_{11}=W_{22}=0$
$$
E_{+}=\frac{1}{2}\left(E_{1}+E_{2}\right)+\frac{1}{2} \sqrt{\left(E_{1}-E_{2}\right)^{2}+4\left|W_{12}\right|^{2}}
$$

$$
E_{-}=\frac{1}{2}\left(E_{1}+E_{2}\right)-\frac{1}{2} \sqrt{\left(E_{1}-E_{2}\right)^{2}+4\left|W_{12}\right|^{2}}
$$

令
$$
E_{m}=\frac{1}{2}\left(E_{1}+E_{2}\right)
$$

$$
\Delta=\frac{1}{2}\left(E_{1}-E_{2}\right)
$$

$$
E_{+}=E_{m}+\sqrt{\Delta^{2}+\left|W_{12}\right|^{2}}
$$

$$
E_{-}=E_{m}-\sqrt{\Delta^{2}+\left|W_{12}\right|^{2}}
$$

![image-20211223223556482](https://s2.loli.net/2021/12/23/yeVzMuqiHTsPKdU.png)

以$E_m$为原点，$\Delta$为横坐标，$E_{1}$ 和 $E_{2}$, 为两条直线, 其斜率为 $+1$ 和 $-1$。当 $\Delta$ 变化时, $E_{+}$和 $E_{-}$的值为相对于坐标轴为对称的双曲线的两支, 它 们的渐近线就是对应于末微扰能级的两条直线, 它们的顶点间的距离为 $2\left|W_{12}\right|$

没有耦合的时候, 两个能级的能量 $E_{1}$ 和 $E_{2}$ “相交” 于 $\Delta=0$ 处. 在耦合的影响下, 两个能级 “互相背离”, 也就是说, 两个能量 值的差异增大. 因此, 我们常称其为反相交图.

此外, 我们还可以看出, 不论 $\Delta$ 的值如何, 恒有:
$$
\left|E_{+}-E_{-}\right|>\left|E_{1}-E_{2}\right|
$$
于是我们得到在物理学其他领域中 (例如在电路理论中) 常见的一个规律: 

> 耦合使固有频率互相远离.

在靠近渐近线的区域中, 即在 $|\Delta| \gg\left|W_{12}\right|$ 的区域中, 我们可以将 $E_\pm$展开为 $\left|W_{12} / \Delta\right|$ 的幂级数:
$$
E_{+}=E_{m}+\Delta\left(1+\frac{1}{2}\left|\frac{W_{12}}{\Delta}\right|^{2}+\cdots\right)
$$

$$
E_{-}=E_{m}-\Delta\left(1+\frac{1}{2}\left|\frac{W_{12}}{\Delta}\right|^{2}+\cdots\right)
$$

反之, 在双曲线的中心, $E_{2}=E_{1}(\Delta=0)$, 由 (C-15) 式和 (C-16) 式得到:
$$
\begin{array}{l}
E_{+}=E_{m}+\left|W_{12}\right| \\
E_{-}=E_{m}-\left|W_{12}\right|
\end{array}
$$
由此可见, 当两个末微扰能级的能量相等时, 耦合的影响尤其重要, 在一级近似中这种影响就显露出来了; 但当 $\Delta \gg\left|W_{12}\right|$ 时, 在二级近似中才能看出这种影响.
$$
\tan \theta=\frac{\left|W_{12}\right|}{\Delta}
$$
由此可以看出, 若 $\Delta \ll\left|W_{12}\right|$ (强耦合), 则 $\theta \simeq \frac{\pi}{2}$; 反之, 若 $\Delta \gg\left|W_{12}\right|$ (弱耦合 则 $\theta \simeq 0$ (我们假设 $\Delta \geqslant 0$ ).

在双曲线的中心, $E_{2}=E_{1}(\Delta=0)$, 我们有:
$$
\left|\psi_{+}\right\rangle=\frac{1}{\sqrt{2}}\left[\mathrm{e}^{-\mathrm{i} \varphi / 2}\left|\varphi_{1}\right\rangle+\mathrm{e}^{\mathrm{i} \varphi / 2}\left|\varphi_{2}\right\rangle\right]
$$

$$
\left|\psi_{-}\right\rangle=\frac{1}{\sqrt{2}}\left[-\mathrm{e}^{-\mathrm{i} \varphi / 2}\left|\varphi_{1}\right\rangle+\mathrm{e}^{\mathrm{i} \varphi / 2}\left|\varphi_{2}\right\rangle\right]
$$

而在靠近渐近线的区域中 (即若 $\Delta \gg\left|W_{12}\right|$ ), 如果只写出 $\left|W_{12}\right| / \Delta$ 的一次幂, 则两个态变为:
$$
\left|\psi_{+}\right\rangle=\mathrm{e}^{-\mathrm{i} \varphi / 2}\left[\left|\varphi_{1}\right\rangle+\mathrm{e}^{\mathrm{i} \varphi} \frac{\left|W_{12}\right|}{2 \Delta}\left|\varphi_{2}\right\rangle+\cdots\right]
$$

$$
\left|\psi_{-}\right\rangle=\mathrm{e}^{\mathrm{i} \varphi / 2}\left[\left|\varphi_{2}\right\rangle-\mathrm{e}^{-\mathrm{i} \varphi} \frac{\left|W_{12}\right|}{2 \Delta}\left|\varphi_{1}\right\rangle+\cdots\right]
$$

对于弱耦合 $\left(\Delta \gg\left|W_{12}\right|\right)$, 微扰态与末微扰态的差异不大, 除了总的相位因子 $\mathrm{e}^{-\mathrm{i} \varphi / 2}$ 以外, $\left|\psi_{+}\right\rangle$几 乎等于 $\left|\varphi_{1}\right\rangle$, 因为态 $\left|\varphi_{2}\right\rangle$ 的微小贡献仅引起轻微的修正. 反之, 对于强耦合 $\left(\Delta \ll\left|W_{12}\right|\right)$, 态 $\left|\psi_{+}\right\rangle$和 $\left|\psi_{-}\right\rangle$完全不同于态 $\left|\varphi_{1}\right\rangle$ 和 $\left|\varphi_{2}\right\rangle$; 这是因为, 前者是后者的线性叠加, 其系数具有相同的模.

## 量子共振

当 $E_{1}=E_{2}=E_{m}$ 时, $H_{0}$ 对应的能量是二重简并的. 正如我们刚才所看 到的, 耦合 $W_{12}$ 将消除这种简并, 特别是, 出现了这样一个能级, 它的能量下降了 $\left|W_{12}\right|$. 换句话说, 如果一个物理体系的基态是二重简并的 (而且对应的能 级与其他所有能级相隔足够远), 那么, 这两个态之间的任何 (纯粹非对角的) 耦合都将降低体系基态的能量, 于是体系变得更加稳定.

### 苯分子

![image-20211224090027106](https://s2.loli.net/2021/12/24/ZShj67nVwLIJugx.png)

作为这种现象的第一个例子, 可以举出苯分子 $\mathrm{C}_{6} \mathrm{H}_{6}$ 如何因共振而达到 稳定. 实验表明, 六个碳原子的位置在正六角形的顶点上, 而且我们可以料到 基态包含相邻碳原子之间的三个双键. 由于核的质量很大, 在这里我们假设它们是固定的. 因此, 两种构型的电子态 $\left|\varphi_{1}\right\rangle$ 和 $\left|\varphi_{2}\right\rangle$ 是不同的. 如果(a)构 型是唯一可能的, 则电子体系的基态能量应为 $E_{m}=\left\langle\varphi_{1}|H| \varphi_{1}\right\rangle$, 其中 $H$ 是在 核的势场中电子的哈密顿算符. 但是, 键的配置也可能如(b)的那 样. 由于对称的缘故, 显然应有 $\left\langle\varphi_{2}|H| \varphi_{2}\right\rangle=\left\langle\varphi_{1}|H| \varphi_{1}\right\rangle$, 因而我们可以推想分 子的基态能级是二重简并的. 但是, 哈密顿算符 $H$ 的非对角矩阵元 $\left\langle\varphi_{2}|H| \varphi_{1}\right\rangle$ 并不等于零. 由于态 $\left|\varphi_{1}\right\rangle$ 和态 $\left|\varphi_{2}\right\rangle$ 之间存在耦合, 将会出现两个不同的能级, 其中一个能级的能量低于 $E_{m}$. 因此, 苯分子比我们所预期的要稳定得多. 此 外, 在实际的基态中, 分子的构型既不像(a), 也不像图 (b) 那样, 这 个态应是 $\left|\varphi_{1}\right\rangle$ 和 $\left|\varphi_{2}\right\rangle$ 的线性叠加 , 化学家所常用的双箭头就表示这个意思.

### 电离

![image-20211224090242707](https://s2.loli.net/2021/12/24/mBz3fwi1CdTIPvL.png)

电离分子 $\mathrm{H}_{2}^{+}$图 4-13 在 $\mathrm{H}_{2}^{+}$离子中, 电子或定域在质子 $p_{1}$ 周围 (图 a) 或定域在质子 $p_{2}$ 周围 (图 b). 在离子的基态中, 电子的波函数是对应于图 $\mathrm{a}$ 和图 $\mathrm{b}$ 的波函数的线性叠加. 电子出现 的概率相对于垂直平分 $p_{1} p_{2}$ 的平面是对称的.

含有两个质子 $p_{1} 、 p_{2}$ 和一个电子. 由于质 子的质量很大, 我们可以把它们看成是固定的. 我们把它们之间的距离记作 $R$, 而把电子定域在 $p_{1}$ 周围的态和定域在 $p_{2}$ 周围的态分别记作 $\left|\varphi_{1}\right\rangle$ 及 $\left|\varphi_{2}\right\rangle$, 对应的波函数就是以 $p_{1}$ 为核或以 $p_{2}$ 为核的氢原子的波函数. 和上 面的情况相似, 由于对称性, 哈密顿算符的对角元 $\left\langle\varphi_{1}|H| \varphi_{1}\right\rangle$ 和 $\left\langle\varphi_{2}|H| \varphi_{2}\right\rangle$ 是 相等的, 可将它们记作 $E_{m}(R)$. 但因矩阵元 $\left\langle\varphi_{1}|H| \varphi_{2}\right\rangle$ 不等于零, 故 $\left|\varphi_{1}\right\rangle,\left|\varphi_{2}\right\rangle$ 这两个态并非定态. 在这个例子中, 仍然有一个低于 $E_{m}(R)$ 的能级, 而且在基 态中, 电子的波函数是对应于a，b 的波函数的线性组合. 因 而, 电子不再仅仅定域在某一质子的周围; 这种离域性 (délocalization), 由于它 降低了电子的势能, 正是化学键的成因.

## 未微扰态的振荡

$$
|\psi(t)\rangle=a_{1}(t)\left|\varphi_{1}\right\rangle+a_{2}(t)\left|\varphi_{2}\right\rangle
$$

存在耦合$W$时
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t}|\psi(t)\rangle=\left(H_{0}+W\right)|\psi(t)\rangle
$$
我们将这个方程投影到基矢 $\left|\varphi_{1}\right\rangle 、\left|\varphi_{2}\right\rangle$ 上, 并利用  $\left.W_{11}=W_{22}=0\right]$, 便得到:
$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t} a_{1}(t)=E_{1} a_{1}(t)+W_{12} a_{2}(t)
$$

$$
\mathrm{i} \hbar \frac{\mathrm{d}}{\mathrm{d} t} a_{2}(t)=W_{21} a_{1}(t)+E_{2} a_{2}(t)
$$

解如上线性方程，即求算符$H=H_0+W$的本征矢。$\ket{\psi_\pm}$和本征值$E_\pm$。且有：
$$
|\psi(0)\rangle=\lambda\left|\psi_{+}\right\rangle+\mu\left|\psi_{-}\right\rangle
$$
$\lambda$ 和 $\mu$ 由初始条件确定
$$
|\psi(t)\rangle=\lambda \mathrm{e}^{-\mathrm{i} E_{+} t / \hbar}\left|\psi_{+}\right\rangle+\mu \mathrm{e}^{-\mathrm{i} E_{-} t / \hbar}\left|\psi_{-}\right\rangle
$$
假设在 $t=0$ 时体系处在态 $\left|\varphi_{1}\right\rangle:$
$$
|\psi(0)\rangle=\left|\varphi_{1}\right\rangle=\mathrm{e}^{\mathrm{i} \varphi / 2}\left[\cos \frac{\theta}{2}\left|\psi_{+}\right\rangle-\sin \frac{\theta}{2}\left|\psi_{-}\right\rangle\right]
$$

$$
|\psi(t)\rangle=\mathrm{e}^{\mathrm{i} \varphi / 2}\left[\cos \frac{\theta}{2} \mathrm{e}^{-\mathrm{i} E_{+} t / \hbar}\left|\psi_{+}\right\rangle-\sin \frac{\theta}{2} \mathrm{e}^{-\mathrm{i} E_{-} t / \hbar}\left|\psi_{-}\right\rangle\right]
$$

在 $t$ 时刻, 发现体系处于态 $\left|\varphi_{2}\right\rangle$ 的概率幅可以写作:
$$
\begin{aligned}
\left\langle\varphi_{2} \mid \psi(t)\right\rangle &=\mathrm{e}^{\mathrm{i} \varphi / 2}\left[\cos \frac{\theta}{2} \mathrm{e}^{-\mathrm{i} E_{+} t / \hbar}\left\langle\varphi_{2} \mid \psi_{+}\right\rangle-\sin \frac{\theta}{2} \mathrm{e}^{-\mathrm{i} E_{-} t / \hbar}\left\langle\varphi_{2} \mid \psi_{-}\right\rangle\right] \\
&=\mathrm{e}^{\mathrm{i} \varphi} \sin \frac{\theta}{2} \cos \frac{\theta}{2}\left[\mathrm{e}^{-\mathrm{i} E_{+} t / \hbar}-\mathrm{e}^{-\mathrm{i} E_{-} t / \hbar}\right]
\end{aligned}
$$
概率
$$
\begin{aligned}
\mathscr{P}_{12}(t) &=\frac{1}{2} \sin ^{2} \theta\left[1-\cos \left(\frac{E_{+}-E_{-}}{\hbar} t\right)\right] \\
&=\sin ^{2} \theta \sin ^{2}\left(\frac{E_{+}-E_{-}}{2 \hbar} t\right)
\end{aligned}
$$
用原始能级及耦合项表示
$$
\mathscr{P}_{12}(t)=\frac{4\left|W_{12}\right|^{2}}{4\left|W_{12}\right|^{2}+\left(E_{1}-E_{2}\right)^{2}} \sin ^{2}\left[\sqrt{4\left|W_{12}\right|^{2}+\left(E_{1}-E_{2}\right)^{2}} \frac{t}{2 \hbar}\right]
$$
$\mathscr{P}_{12}(t)$ 以 $\left(E_{+}-E_{-}\right) / h$ 为频率随着时间振荡, 这 个频率就是体系的唯一的玻尔频率. $\mathscr{P}_{12}(t)$ 在零和一个极大值之间变化, 极大值为 $\sin ^{2} \theta$, 达到这个值的时刻是 $t=(2 k+1) \pi \hbar /\left(E_{+}-E_{-}\right)$, 此 处 $k=0,1,2, \cdots$ 

![image-20211224093742082](https://s2.loli.net/2021/12/24/376wxv9AasuDzHt.png)

当 $E_{1}=E_{2}$ 时, $\left(E_{+}-E_{-}\right) / h$ 等于 $2\left|W_{12}\right| / h$, 而且 $\sin ^{2} \theta$ 也达到它的最大 可能值 (即 1), 即在 $t=(2 k+1) \pi \hbar / 2\left|W_{12}\right|$ 这些时刻, 体系的态从初态 $\left|\varphi_{1}\right\rangle$ 演 变到态 $\left|\varphi_{2}\right\rangle$. 因此, 两个能量相等的态之间的任何耦合总是使体系在这两个态之间以正比于耦合的频率进行完整的振荡.

当 $E_{1}-E_{2}$ 增大时, $\left(E_{+}-E_{-}\right) / h$ 也增大, 而 $\sin ^{2} \theta$ 却减小了. 对于弱耦合 $\left(E_{1}-E_{2} \gg W_{12}\right), E_{+}-E_{-}$和 $E_{1}-E_{2}$ 相差很小, $\sin ^{2} \theta$ 则变得很小. 因为在弱 耦合的情况下, 态 $\left|\varphi_{1}\right\rangle$ 非常接近定态 $\left|\psi_{+}\right\rangle$, 得到后一种结果 就不足为奇了: 从初态 $\left|\varphi_{1}\right\rangle$ 出发, 体系的态只有十分微小的变化.

我们再回到离子 $\mathrm{H}_{2}^{+}$的例子. 现在假设在某一时刻电子定域在质子 $p_{1}$ 周 围:  我们知道电子将 在两个质子之间振荡, 其频率就是与离子的两个定态 $\left|\psi_{+}\right\rangle$和 $\left|\varphi_{-}\right\rangle$相联系的 玻尔频率. 两个态之间的电子振荡对应着 分子的电偶极矩的平均值的振荡 (当电子定域在两个质子之一的周围时, 偶极 矩不等于零; 依所论的质子为 $p_{1}$ 或 $p_{2}$, 偶极矩有不同的符号). 于是我们具体 地看到, 当这离子的态并非定态时, 一个振荡的电偶极矩是怎样出现的. 我们 知道, 这样一个振荡的偶极子可以和同频率的电磁波交换能量; 因此, 这个频 率应该出现在 $\mathrm{H}_{2}^{+}$离子的吸收谱和发射谱中.

## 虚设自旋

$$
(H)=\left(\begin{array}{cc}
\frac{1}{2}\left(H_{11}-H_{22}\right) & H_{12} \\
H_{21} & -\frac{1}{2}\left(H_{11}-H_{22}\right)
\end{array}\right)
$$

虽然我们所要讨论的二能级体系不一定是自旋 $\frac{1}{2}$, 但我们总可以给它联 系上一个自旋 $\frac{1}{2}$, 在由这个自旋的分量 $S_{z}$ 的本征矢所构成的基 $\{|+\rangle,|-\rangle\}$ 中, 此自旋的哈密顿算符 $H$ 可用上面的矩阵 $(H)$ 来表示. 我们即将看到, 可以将总可以给它联 系上一个自旋 $\frac{1}{2}$, 在由这个自旋的分量 $S_{z}$ 的本征矢所构成的基 $\{|+\rangle,|-\rangle\}$ 中, 此自旋的哈密顿算符 $H$ 可用上面的矩阵 $(H)$ 来表示. 我们即将看到, 可以将算符 $H$ 可用上面的矩阵 $(H)$ 来表示. 

表示自旋 $\frac{1}{2}$ 和分量为 $B_{x} 、 B_{y} 、 B_{z}$ 的磁场 $\boldsymbol{B}$ 之间的耦合的哈密顿算符可以写作:
$$
\widetilde{H}=-\gamma \boldsymbol{B} \cdot \boldsymbol{S}=-\gamma\left(B_{x} S_{x}+B_{y} S_{y}+B_{z} S_{z}\right)
$$

$$
(\widetilde{H})=-\frac{\gamma \hbar}{2}\left(\begin{array}{cc}
B_{z} & B_{x}-\mathrm{i} B_{y} \\
B_{x}+\mathrm{i} B_{y} & -B_{z}
\end{array}\right)
$$

引入虚设磁场
$$
\left\{\begin{array}{l}
B_{x}=-\frac{2}{\gamma \hbar} \operatorname{Re} H_{12} \\
B_{y}=\frac{2}{\gamma \hbar} \operatorname{Im} H_{12} \\
B_{z}=\frac{1}{\gamma \hbar}\left(H_{22}-H_{11}\right)
\end{array}\right.
$$
注意 $\boldsymbol{B}$ 在 $x O y$ 平面上的投影 $\boldsymbol{B}_{\perp}$ 的模为
$$
B_{\perp}=\frac{2}{\hbar}\left|\frac{H_{12}}{\gamma}\right|
$$

$$
\left\{\begin{array}{ll}
\tan \theta=-\frac{\left|\gamma \beta_{\perp}\right|}{\gamma B_{z}} & 0 \leqslant \theta<\pi \\
-\gamma\left(B_{x}+\mathrm{i} B_{y}\right)=\left|\gamma B_{\perp}\right| \mathrm{e}^{\mathrm{i} \varphi} & 0 \leqslant \varphi<2 \pi
\end{array}\right.
$$

这里的旋磁比 $\gamma$ 不过是计算中的一个辅助量, 它事先可以取定任意值. 如果我 们约定 $\gamma$ 取负值, 那么, 与矩阵 $(H)$ 相联系的角 $\theta$ 和 $\varphi$ 实际上就 是磁场 $\boldsymbol{B}$ 的方向的极角 (如果假设 $\gamma$ 取正值, 则方向刚好反过来).

最后, 可以看出, 我们可以忘却作为出发点的那个二能级体系, 而认为在 $S_{z}$ 的本征态 $|+\rangle$ 和 $\ket{-}$ 构成的基中, 矩阵 $(H)$ 所表示的就是磁场 $\boldsymbol{B}$ 中的自旋 $\frac{1}{2}$ 的哈密顿算符 $\widetilde{H}$, 而 $\boldsymbol{B}$ 的分量则由 上面给出. 我们又可将 $\widetilde{H}$ 写作:
$$
\widetilde{H}=\omega S_{u}
$$
式中 $S_{u}$ 是算符 $\boldsymbol{S} \cdot \boldsymbol{u}$, 它是自旋在极角为 $\theta 、 \varphi$ 的方向 $\boldsymbol{u}$ 上的分量, $\omega$ 是拉莫尔 角频率:
$$
\omega=|\gamma||\boldsymbol{B}|
$$
![image-20211228084812470](https://s2.loli.net/2021/12/28/1rZSngXLBaCTwxo.png)

### 二能级系统的虚设磁场解释

令
$$
\left\{\begin{array}{l}
B_{0 z}=\frac{E_{2}-E_{1}}{\gamma \hbar} \\
B_{0 \perp}=0
\end{array}\right.
$$

$$
\left\{\begin{array}{l}
b_{z}=0 \\
b_{\perp}=\frac{2}{\hbar}\left|\frac{W_{12}}{\gamma}\right|
\end{array}\right.
$$

这就是说, $\boldsymbol{B}_{0}$ 平行于 $O z$ 轴并正比于 $\frac{1}{2}\left(E_{1}-E_{2}\right) ; \boldsymbol{b}$ 则垂直于 $O z$ 轴并正比于 $\left|W_{12}\right|$. 由于 $(H)=\left(H_{0}\right)+(W)$, 故与总哈密顿算符相联系的磁场 $\boldsymbol{B}$ 是 $\boldsymbol{B}_{0}$ 与 $\boldsymbol{b}$ 的矢量和:
$$
\boldsymbol{B}=\boldsymbol{B}_{0}+\boldsymbol{b}
$$
![image-20211228085246758](https://s2.loli.net/2021/12/28/tTi1N4jK7MaFsAU.png)

强耦合条件 $\left(\left|W_{12}\right| \gg\left|E_{1}-E_{2}\right|\right)$ 相当于 $|\boldsymbol{b}| \gg\left|\boldsymbol{B}_{0}\right|$; 弱耦合条件 $\left(\left|W_{12}\right| \ll\left|E_{1}-E_{2}\right|\right)$ 则相当于 $|b| \ll\left|B_{0}\right|$ 。

![image-20211228085613322](https://s2.loli.net/2021/12/28/jJBsPtYLgIeZfhq.png)

$E_{1}-E_{2}$ 和 $E_{+}-E_{-}$分别对应于磁场 $\boldsymbol{B}_{0}$ 和 $\boldsymbol{B}$ 中的拉莫尔角频率 $\omega_{0}=$ $|\gamma|\left|\boldsymbol{B}_{0}\right|$ 和 $\omega=|\gamma||\boldsymbol{B}|$. 我们看到, $\boldsymbol{B}_{0} 、 \boldsymbol{b}$ 及 $\boldsymbol{B}$ 构成一个直角三角 形, 其斜边为 $\boldsymbol{B}$; 因而永远有 $|\boldsymbol{B}| \geqslant\left|\boldsymbol{B}_{0}\right|$, 从而我们再次证明了 $E_{+}-E_{-}$永远 大于 $\left|E_{1}-E_{2}\right|$.

在弱耦合的情况下 $|\boldsymbol{B}|$ 与 $\left|\boldsymbol{B}_{0}\right|$ 之差的相对数值很小, 属于 $|\boldsymbol{b}| /\left|\boldsymbol{B}_{0}\right|$ 的二级小量. 由此我们立即推知, 就相对数值而言, $E_{+}-E_{-}$与 $E_{1}-E_{2}$ 之差属于 $\left|W_{12}\right| /\left(E_{1}-E_{2}\right)$ 的二级小量. 反之, 在强耦合情况下, $|\boldsymbol{B}|$ 甚大于 $\left|\boldsymbol{B}_{0}\right|$, 几乎等于 $|\boldsymbol{b}|$; 因而 $E_{+}-E_{-}$也甚大于 $\left|E_{1}-E_{2}\right|$, 实际上正比于 $\left|W_{12}\right|$. 这样我们就再次证明了全部结果.

利用虚设自旋的概念可将问题陈述如下: 在 $t=0$ 时, 与二能级体系相联系的虚设自旋处于 $S_{z}$ 的本征态 $|+\rangle$; 给 $\boldsymbol{B}_{0}$ 加上 ，$\boldsymbol{b}$在时刻 $t$ 发现该自旋处于态 $|-\rangle$ 的概率 $\mathscr{P}_{+-}(t)$ 是多大? 根据表中 列出的对应关系, $\mathscr{P}_{12}(t)$ 应该全同于 $\mathscr{P}_{+-}(t)$.

![image-20211231083225504](https://s2.loli.net/2021/12/31/h4v5SyJElPmOUxD.png)

由于自旋随时间的演变归结为绕 $B$ 的拉莫尔进动 , 于是 $\mathscr{P}_{+-}(t)$ 的计算就非常简单. 在进动过程中, 自旋与 $B$ 的方向 $O u$ 之间的夹角 $\theta$ 保持 不变. 在 $t$ 时刻, 自旋指向方向 $O n$, 而与 $O z$ 构成一个角 $\alpha$; 平面 $(O z, O u)$ 与平 面 $(O u, O n)$ 之间的二面角则等于 $\omega t$. 根据球面三角学中的经典公式, 我们可 以写出:
$$
\cos \alpha=\cos ^{2} \theta+\sin ^{2} \theta \cos \omega t
$$
而当自旋的方向与 $O z$ 轴的夹角为 $\alpha$ 时, 发现该自旋处于 $S_{z}$ 的本征态 $|-\rangle$ 的 概率等于 $\sin ^{2} \frac{\alpha}{2}=(1-\cos \alpha) / 2$ . 由此, 便 可推知:
$$
\mathscr{P}_{+-}(t)=\sin ^{2} \frac{\alpha}{2}=\frac{1}{2} \sin ^{2} \theta(1-\cos \omega t)
$$
$\omega$ 换成 $\left(E_{+}-E_{-}\right) / \hbar$,

## 两个自旋体系

态空间 $\mathscr{E}_{S}(1)$ 中的普遍的右矢写作:
$$
|\varphi(1)\rangle=\alpha_{1}|1:+\rangle+\beta_{1}|1:-\rangle
$$
在态空间 $\mathscr{E}_{S}(2)$ 中则有:
$$
|\chi(2)\rangle=\alpha_{2}|2:+\rangle+\beta_{2}|2:-\rangle
$$
如果使这两个粒子结合成一个体系, 则该体系的态空间 $\mathscr{E}_{S}$ 应为上列两 个态空间的张量积:
$$
\mathscr{E}_{S}=\mathscr{E}_{S}(1) \otimes \mathscr{E}_{S}(2)
$$

$$
\begin{array}{l}
|++\rangle=|1:+\rangle|2:+\rangle \\
|+-\rangle=|1:+\rangle|2:-\rangle \\
|-+\rangle=|1:-\rangle|2:+\rangle \\
|--\rangle=|1:-\rangle|2:-\rangle
\end{array}
$$

孹如, 在态 $|+-\rangle$ 中, 粒子 (1) 的自旋在 $O z$ 轴上的分量确定地是 $+\frac{\hbar}{2}$, 粒子 (2) 的自旋在 $O z$ 轴上的分量确定地是 $-\frac{\hbar}{2}$. 现在我们约定用 $\langle+-|$ 来表示右矢 $1+-\rangle$ 的共轭左矢; 第一个符号总是对应于粒子 (1), 第二个符号总是对应于 粒子 (2).
$$
\left\langle\varepsilon_{1} \varepsilon_{2} \mid \varepsilon_{1}^{\prime} \varepsilon_{2}^{\prime}\right\rangle=\delta_{\varepsilon_{1} \varepsilon_{1}^{\prime}} \delta_{\varepsilon_{2} \varepsilon_{2}^{\prime}}
$$

$$
\sum_{\varepsilon_{1}, \varepsilon_{2}}\left|\varepsilon_{1} \varepsilon_{2}\right\rangle\left\langle\varepsilon_{1} \varepsilon_{2}|=|++\right\rangle\langle++|+|+-\rangle\langle+-|+|-+\rangle\langle-+|+|--\rangle\langle--|=\mathbb{1}
$$

空间 $\mathscr{E}_{S}$ 中的一个右矢:
$$
|\varphi(1)\rangle|\chi(2)\rangle=\alpha_{1} \alpha_{2}|++\rangle+\alpha_{1} \beta_{2}|+-\rangle+\alpha_{2} \beta_{1}|-+\rangle+\beta_{1} \beta_{2}|--\rangle
$$
但是, 空间 $\mathscr{E}_{S}$ 中的右矢并不都是张量积. 空间 $\mathscr{E}_{S}$ 中的最一般的右矢是基 矢的任意的线性组合:
$$
|\psi\rangle=\alpha|++\rangle+\beta|+-\rangle+\gamma|-+\rangle+\delta|--\rangle
$$

$$
|\alpha|^{2}+|\beta|^{2}+|\gamma|^{2}+|\delta|^{2}=1
$$
