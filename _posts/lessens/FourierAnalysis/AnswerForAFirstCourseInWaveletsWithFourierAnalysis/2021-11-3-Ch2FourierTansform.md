---
layout: code
istop : true
book : true
title: 小波与傅里叶分析基础（第二版）第二章 傅里叶变换习题解答
category: knowledge
tags: 傅里叶分析 matlab
background-image: WaveSignal.png
date: 2021-3-9 17:54:39 + 0800

---
# Q1
考虑信号
$$
f(t)= \begin{cases}\cos (3 t) & -\pi \leqslant t \leqslant \pi \\ 0 & \text { else }\end{cases}
$$
证明:
$$
\int_{-\pi}^{\pi} \cos (m t) \cos (\lambda t) d t=-2 \frac{(-1)^{m} \lambda \sin (\pi \lambda)}{m^{2}-\lambda^{2}}
$$
并证明
$$
\widehat{f}(\lambda)=\frac{-\sqrt{2} \lambda \sin (\lambda \pi)}{\sqrt{\pi}\left(\lambda^{2}-9\right)}
$$
## ANS

$$
\int_{-\pi}^{\pi} \cos (m t) \cos (\lambda t) d t=
\int_{-\pi}^{\pi}\frac{1}{2}\left[\cos(m+\lambda)t+\cos(m-\lambda)t\right]dt
$$

$$
=[\frac{\sin(m+\lambda)t}{2(m+\lambda)}+
\left.\frac{\sin(m-\lambda)t}{2(m-\lambda)}]\right|_{-\pi}^{\pi}=./】

$$
