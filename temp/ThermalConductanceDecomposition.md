热导的谱分解

# 理论推导

$$
G=\frac{Q}{A \Delta T}
$$

$$
Q=\int_{0}^{\infty} \frac{d \omega}{2 \pi} q(\omega)
$$

$q(\omega)$是频率$\omega$对应的时间平均热流（即热流在频域的分布）。不直接与涨落相关。
$$
Q_{j \rightarrow i}=\frac{1}{2}\left\langle\mathbf{F}_{i j} \cdot\left(\mathbf{v}_{i}+\mathbf{v}_{j}\right)\right\rangle
$$
两个原子之间的传导流（$Q_{j\rightarrow i}=-Q_{i\rightarrow j}?$

---

推导

对于粒子$i$，其哈密顿量为
$$
H_{i}=\frac{p_{i}^{2}}{2 m}+\frac{1}{2} \sum_{j \in A_{i}} V\left(z_{j}-z_{i}\right)
$$
动能+由其他粒子存在引起的相对势能

能流（即热流）为
$$
\dot{H}_i=-\sum J_{ij}\delta_{ij}
$$
而
$$
\dot{H}_i=\frac{p_i}{m}\dot{p_i}+\frac12\sum\limits_{j\in A_i}V^{\prime}(z_j-z_i)(\dot{z_j}-\dot{z_i})=\frac{p_i}{m}\dot{p_i}+\frac12\sum F_{ji}(\dot{z_j}-\dot{z_i})
$$
忽略其他高阶作用项，只考虑其他原子的作用，含噪项对时间的平均为0
$$
\frac{p_i}{m}\dot{p_i}=m\dot{z_i}\ddot{z_i}=\dot{z_i}\sum F_{ji}+[white\quad noise]
$$

$$
J_{ij}=\frac12\sum\mathbf{F_{ij}}\cdot(\mathbf{v}_j+\mathbf{v}_i)+[white\quad noise]
$$

$$
Q_{ij}=\lang J_{ij}\rang
$$

---

$$
Q=\sum\limits_{i,j}Q_{j\rightarrow i}
$$

$$
Q_{j \rightarrow i}=\int_{0}^{\infty} \frac{d \omega}{2 \pi} q_{j \rightarrow i}(\omega)
$$

$$
K_{i j}\left(t_{1}-t_{2}\right)=\frac{1}{2}\left\langle\mathbf{F}_{i j}\left(t_{1}\right) \cdot\left[\mathbf{v}_{i}\left(t_{2}\right)+\mathbf{v}_{j}\left(t_{2}\right)\right]\right\rangle
$$

$$
K_{ij}(\tau)=\mathscr{F}^{-1}[\hat{K}_{ij}(\omega)]=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{K}_{ij}(\omega)e^{i\omega\tau}d\omega
$$

$$
Q_{j \rightarrow i}\equiv K_{i j}(0) =\int_{-\infty}^{\infty} \frac{d \omega}{2 \pi} \hat{K}_{i j}(\omega) 
$$

---

也可以直接按傅里叶变换的性质推导。
$$
K_{i j}(0) \equiv Q_{j \rightarrow i}=\int_{-\infty}^{\infty} K_{ij}(\tau)\delta(\tau)d\tau
$$

$$
\delta(x)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i \omega x} d \omega
$$

$$
Q_{j \rightarrow i}=\int_{-\infty}^{\infty} K_{ij}(\tau)\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{i\omega\tau}d\omega d\tau
$$

将$K_{ij}$放到积分符号里并交换积分次序可得

---

按傅里叶变换的性质，**实函数的傅里叶变换关于原点共轭对称**。即其实部为偶函数，虚部为奇函数。
$$
Q_{j \rightarrow i}=2 \int_{0}^{\infty} \frac{d \omega}{2 \pi} \operatorname{Re}\left[\tilde{K}_{i j}(\omega)\right]
$$

$$
q_{j \rightarrow i}(\omega)=2 \operatorname{Re}\left[\tilde{K}_{i j}(\omega)\right]
$$

$$
q(\omega)=\sum\limits_{i,j}q_{j \rightarrow i}(\omega)=2\sum\limits_{i,j}\operatorname{Re}\left[\tilde{K}_{i j}(\omega)\right]
$$

