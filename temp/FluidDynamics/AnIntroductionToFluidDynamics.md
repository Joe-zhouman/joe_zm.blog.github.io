# An Introduction to Fluid Dynamics

![image-20220619225839682](C:/Users/Joe/AppData/Roaming/Typora/typora-user-images/image-20220619225839682.png)

表面力
$$
\boldsymbol{F_s}= \Sigma(\mathbf{n}) \delta A+\Sigma(-\mathbf{a}) \delta A_{1}+\Sigma(-\mathbf{b}) \delta A_{2}+\Sigma(-\mathbf{c}) \delta A_{3}
$$

$$
\delta A_{1}=\mathbf{a} \cdot \mathbf{n} \delta A
$$

$$
F_{s,i}=\left[\Sigma_{i}(\mathbf{n})-\left\{a_{j} \Sigma_{i}(\mathbf{a})+b_{j} \Sigma_{i}(\mathbf{b})+c_{j} \Sigma_{i}(\mathbf{c})\right\} n_{j}\right] \delta A
$$

$$
\text { 质量 } \times \text { 加速度 }:=\text { 合体力 }+\text { 合面力 }
$$

质量，合体力为$\delta V$的等阶无穷小，即$o(\delta l^3)$，合面力为$\delta A$的等阶无穷小，即$o(\delta l^2)$，故而合面力的系数为0才能满足以上关系，即
$$
\Sigma_{i}(\mathbf{n})=\left\{a_{j} \Sigma_{i}(\mathbf{a})+b_{j} \Sigma_{i}(\mathbf{b})+c_{j} \Sigma_{i}(\mathbf{c})\right\} n_{j} .
$$
右侧为一个二阶张量的分量，记为$\boldsymbol{\sigma} $
$$
\Sigma_{i}(\mathbf{n})=\sigma_{i j} n_{j}
$$
表面力的力矩
$$
\int \epsilon_{i j k} r_{j} \sigma_{k l} n_{l} d A=
\int \epsilon_{i j k} \frac{\partial\left(r_{j} \sigma_{k l}\right)}{\partial r_{l}} d V=\int \epsilon_{i j k}\left(\sigma_{k j}+r_{j} \frac{\partial \sigma_{k l}}{\partial r_{l}}\right) d V
$$
（利用散度定理）

右侧第一项为$o(\delta l^3)$，第二项为$o(\delta l^4)$。体积力的力矩为也为$o(\delta l^4)$。故
$$
\epsilon_{i j k} \sigma_{k j}=0
$$
故$\boldsymbol{\sigma} $为一个对称张量。对于二阶张量，可以通过旋转使其的非对角元为0.