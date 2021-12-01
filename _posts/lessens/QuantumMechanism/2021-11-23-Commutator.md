---
layout: code
istop : true
book : true
title: 对易子及其性质
category: knowledge
tags: 量子力学
background-image: quantum.jpg
date: 2021-11-23 20:16:51 + 0800
---
量子力学中的对易子及其性质 <!-- more -->
# 定义

$$
[\hat{A}, \hat{B}] := \hat{A} \hat{B}-\hat{B} \hat{A}
$$

$$\{A, B\} \equiv \sum_{i}\left(\frac{\partial A}{\partial q_{i}} \frac{\partial B}{\partial p_{i}}-\frac{\partial A}{\partial p_{i}} \frac{\partial B}{\partial q_{i}}\right)$$

$$
\lim _{h \rightarrow 0} \frac{[A, B]}{i \hbar}=\{A, B\}
$$

# 性质

$$[\hat{A}, \hat{B}]=-[\hat{B}, \hat{A}]$$

$$[\hat{A}, \hat{A}]=0$$

$$[\hat{A}, c]=0$$

$$[\hat{A}, \hat{B}+\hat{C}]=[\hat{A}, \hat{B}]+[\hat{A}, \hat{C}]$$

$$[\hat{A}+\hat{B}, \hat{C}]=[\hat{A}, \hat{C}]+[\hat{B}, \hat{C}]$$

$$[\hat{A}, \hat{B} \hat{C}]=[\hat{A}, \hat{B}] \hat{C}+\hat{B}[\hat{A}, \hat{C}]$$

$$[\hat{A} \hat{B}, \hat{C}]=[\hat{A}, \hat{C}] \hat{B}+\hat{A}[\hat{B}, \hat{C}]$$

$$[\hat{A}, [\hat{B}, \hat{C}]]+[\hat{B}, [\hat{C}, \hat{A}]]+[\hat{C}, [\hat{A}, \hat{B}]]=0$$

$$[\hat{A}, \hat{B}]^{*}=[\hat{B}^*, \hat{A}^*]$$

$$
\left[\hat{A}^{m}, \hat{A}^{n}\right]=0
$$

$$
\left[\hat{A}^{m}, f(\hat{A})\right]=0
$$

$$\left[A, B^{n}\right]=\sum_{s=0}^{n-1} B^{s}[A, B] B^{n-x-1}$$

--- 

设算符 $A$ 和 $B$ 与它们的对易式 $[A, B]$ 都对易,则

$$\left[A, B^{n}\right]=n B^{n-1}[A, B]$$

$$\left[A^{n}, B\right]=n A^{n-1}[A, B]$$

---

若$[q, p]=i \hbar$，则在$q$表象中，

$$
p=-\mathrm{i} \hbar \frac{\partial}{\partial q}
$$

$$
\left[q, p^{n}\right]=n i \hbar p^{n-1}
$$

$$
\left[q, f(p)\right]=i\hbar f^\prime(p)
$$

---

# 常用对易式

$$
\left[x_{\alpha}, \hat{p}_{\beta}\right]=i \hbar \delta_{\alpha \beta}
$$

$$
\left[\hat{x}, \hat{p}_{x}^{n}\right]=\mathrm{i} \hbar n \hat{p}_{x}^{n-1}=\mathrm{i} \hbar \frac{\partial \hat{p}_{x}^{n}}{\partial \hat{p}_{x}}
$$

$$
[\hat{x}, \hat{F}(\boldsymbol{p})]=\mathrm{i} \hbar \frac{\partial \hat{F}}{\partial \hat{p}_{x}}
$$

$$
\left[\hat{p}_{x}, f(\boldsymbol{r})\right]=-\mathrm{i} \hbar \frac{\partial f}{\partial x}
$$

$$
\left[\hat{p}_{x}^{2}, f(x)\right]=-\hbar^{2} \frac{\partial^{2} f}{\partial x^{2}}-2 \mathrm{i} \hbar \frac{\partial f}{\partial x} \hat{p}_{x}
$$

---

`容易出现以下错误`

$$
\left[\hat{p}_{x}^{2}, f(x)\right]=\hat{p}_x[\hat{p}_x,f(x)]+[\hat{p}_x,f(x)]\hat{p}_x
$$

$$= -i\hbar\frac{\partial}{\partial x}(-i \hbar \frac{\partial f}{\partial x})-\mathrm{i} \hbar \frac{\partial f}{\partial x} \hat{p}_{x}$$

$$= -\hbar^{2} \frac{\partial^{2} f}{\partial x^{2}}- \mathrm{i} \hbar \frac{\partial f}{\partial x} \hat{p}_{x}$$

`问题出在最后一个等号处`

`按算符的定义`

$$
\hat{p}_x[\hat{p}_x,f(x)]\psi = -i\hbar\frac{\partial}{\partial x}(-i \hbar \frac{\partial f}{\partial x}\psi)=
 -\hbar^{2} \frac{\partial^{2} f}{\partial x^{2}}\psi+(-i \hbar \frac{\partial f}{\partial x})(-i \hbar \frac{\partial \psi}{\partial x})
$$

`故`

$$
\hat{p}_x[\hat{p}_x,f(x)]=-\hbar^{2} \frac{\partial^{2} f}{\partial x^{2}}- \mathrm{i} \hbar \frac{\partial f}{\partial x} \hat{p}_{x}
$$

---


$$
\left[\hat{l}_{\alpha}, x_{\beta}\right]=\varepsilon_{\alpha \beta \gamma} i \hbar x_{\gamma}
$$

$$\left[\hat{l}_{\alpha}, \hat{p}_{\beta}\right]=\varepsilon_{\alpha \beta \gamma} \mathrm{i} \hbar \hat{p}_{\gamma}$$

$$\left[\hat{l}_{\alpha}, \hat{l}_{\beta}\right]=\varepsilon_{\alpha \beta \gamma} \mathrm{i} \hbar \hat{l}_{\gamma}$$

$$
\left[\hat{\boldsymbol{L}}, \hat{\boldsymbol{L}}^{2}\right]=0
$$
