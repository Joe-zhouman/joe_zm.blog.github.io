# 从MD中直接得到声子色散关系

## 允许波失

对$n\times n$的三斜晶胞，允许波失为将$\boldsymbol{b}_{1}, \boldsymbol{b}_2$各$n$等分。

### 六方晶胞的允许波失

![image-20220104162211084](https://s2.loli.net/2022/01/04/VLA1ORBUdYvZmEz.png)

![image-20220104190250149](https://s2.loli.net/2022/01/04/LOerzqHt3AGB9lh.png)
$$
\boldsymbol{a}_{1}=(a,0,0)
$$

$$
\boldsymbol{a}_{2}=\left( \frac{1}{2}a, \frac{\sqrt{3}}{2}a,0 \right)
$$

$$
\boldsymbol{a}_3=(0,0,1)
$$

$$
b_{1}=\frac{a_{2} \times a_{3}}{a_{1} \cdot\left(a_{2} \times a_{3}\right)}=\frac{1}{a}\left(1,-\frac{\sqrt3}{3},0\right)
$$

$$
\boldsymbol{b}_2=\frac{1}{a}\left(0,\frac{2}{\sqrt{3}},0\right)
$$

$$
\boldsymbol{b}_{3}=\left(0,0,1\right)
$$

固允许波失为
$$
\boldsymbol{k}=\frac{2\pi}{n}\left(l_{i}\boldsymbol{b_i}\right)=\frac{2\pi}{na}\left(l_{1},-\frac{l_{1}}{\sqrt{3}}+\frac{2l_{2}}{\sqrt{3}},l_{3}\right),l_{i}=1,2,\cdots,n
$$
高对称点（high-symmetry points）

* $\Gamma$ : Center of Brillouin zone
* M : Center of an edge
* K : Middle of an edge joining two hexagonal faces

$\Gamma-M$ 
$$
\Gamma M=\frac{1}{2}\left(\boldsymbol{b_1}+ \boldsymbol{b_{2}} \right)
$$

$$
l_{1}=l_{2},l_{i}\le \frac{n}{2}
$$

$\Gamma-K$ 
$$
\Gamma K=\frac{1}{3}\left(2 \boldsymbol{b_{1}}+ \boldsymbol{b_2}\right)
$$

$$
l_{1}=2l_{2},l_{1}\le \frac{2n}{3}
$$
$M-K$ 
$$
l_{1}+l_{2}=n,\frac{n}{2}\le l_{1} \le	\frac{2n}{3}
$$

### 正交晶胞的允许波失

![image-20220104201837670](https://s2.loli.net/2022/01/04/BWeC1xiYla5Qhrp.png)
$$
\boldsymbol{a_1}=(a,0,0)
$$

$$
\boldsymbol{a_{2}}=(0,b,0)
$$

$$
a_3=(0,0,c)
$$

$$
b_{1}=\left(\frac{1}{a},0,0\right)
$$

$$
b_{2}=\left(0,\frac{1}{b},0\right)
$$

$$
b_{3}=\left(0,0,\frac{1}{c}\right)
$$

固允许波失为
$$
\boldsymbol{k}=\frac{2\pi}{n}\left(l_{i}\boldsymbol{b_i}\right)=\frac{2\pi}{n}\left(\frac{l_{1}}{a}, \frac{l_2}{b}, \frac{l_{3}}{c}\right),l_{i}=1,2,\cdots,n
$$
$\Gamma-X$ 
$$
l_{1}\le \frac{n}{2},l_{2}=l_{3}=0
$$
$\Gamma-Y$ 
$$
l_{2}\le \frac{n}{2}, l_{1}=l_{3}=0
$$
$X-S$ 
$$
l_{1}=\frac{n}{2},l_{2}\le	\frac{n}{2},l_{3}=0
$$
$Y-S$
$$
l_{1}\le\frac{n}{2},l_{2}=\frac{n}{2},l_{3}=0
$$
