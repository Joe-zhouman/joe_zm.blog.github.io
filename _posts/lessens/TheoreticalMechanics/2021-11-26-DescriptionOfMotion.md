---
layout: code
istop : true
book : true
title: 运动的描述
category: knowledge
tags: 理论力学 运动
background-image: EulerAngles.jpg
date: 2021-11-26 21:23:18 + 0800
---
运动的描述 <!-- more -->
# 坐标系
## 直角坐标系

$$
\boldsymbol{r}=x \boldsymbol{i}+y \boldsymbol{j}+z \boldsymbol{k}
$$

$$
\boldsymbol{v} =\frac{\mathrm{d} \boldsymbol{r}}{\mathrm{d} t}=\dot{x} \boldsymbol{i}+
\dot{y} \boldsymbol{j}+\dot{z} \boldsymbol{k} 
=v_{x} \boldsymbol{i}+v_{y} \boldsymbol{j}+v_{z} \boldsymbol{k}
$$

$$
\boldsymbol{a}=\frac{\mathrm{d} \boldsymbol{v}}{\mathrm{d} t}=\ddot{x} \boldsymbol{i}+\ddot{y} \boldsymbol{j}+\ddot{z} \boldsymbol{k}=a_{x} \boldsymbol{i}+a_{y} \boldsymbol{j}+a_{z} \boldsymbol{k}
$$

## 平面极坐标系

$$\frac{\mathrm{d} \boldsymbol{i}}{\mathrm{d} t}=\frac{\mathrm{d} i}{\mathrm{~d} \theta} \frac{\mathrm{d} \theta}{\mathrm{d} t}=\dot{\theta} \boldsymbol{j}$$

$$\frac{\mathrm{d} \boldsymbol{j}}{\mathrm{d} t}=\frac{\mathrm{d} \boldsymbol{j}}{\mathrm{d} \theta} \frac{\mathrm{d} \theta}{\mathrm{d} t}=-\dot{\theta} \boldsymbol{i}$$

$$
\boldsymbol{v}=\dot{r} \boldsymbol{i}+r \dot{\boldsymbol{\theta}} \boldsymbol{j}
$$

$$
\boldsymbol{a}=\left(\ddot{r}-r \dot{\theta}^{2}\right) \boldsymbol{i}+(r \ddot{\theta}+2 \dot{r} \dot{\theta}) \boldsymbol{j}=\left(\ddot{r}-r \dot{\theta}^{2}\right) i+\frac{1}{r} \frac{\mathrm{d}}{\mathrm{d} t}\left(r^{2} \dot{\theta}\right) \boldsymbol{j}
$$

## 径向与切向加速度

$$
\boldsymbol{v}=v \boldsymbol{i}=\frac{\mathrm{d} s}{\mathrm{~d} t} \boldsymbol{i}
$$

$$
a=\frac{\mathrm{d} v}{\mathrm{~d} t} i+\frac{v^{2}}{\rho} j
$$

$$
\rho = \frac{\mathrm{d} s}{\mathrm{~d} \theta}
$$

## 任意曲线坐标系

$$
\boldsymbol{e}_{i}=\frac{1}{H_{i}} \frac{\partial \boldsymbol{r}}{\partial q_{i}}, \quad \frac{\partial \boldsymbol{r}}{\partial q_{i}}=\frac{\partial x}{\partial q_{i}} \boldsymbol{i}+\frac{\partial y}{\partial q_{i}} \boldsymbol{j}+\frac{\partial z}{\partial q_{i}} \boldsymbol{k}
$$

$$
H_{i}=\left|\frac{\partial \boldsymbol{r}}{\partial q_{i}}\right|=\sqrt{\left(\frac{\partial x}{\partial q_{i}}\right)^{2}+\left(\frac{\partial y}{\partial q_{i}}\right)^{2}+\left(\frac{\partial z}{\partial q_{i}}\right)^{2}}
$$

H为拉梅系数

$$
\boldsymbol{v}=\frac{\mathrm{d} \boldsymbol{r}}{\mathrm{d} t}=\frac{\partial \boldsymbol{r}}{\partial q_{1}} \dot{q}_{1}+\frac{\partial \boldsymbol{r}}{\partial q_{2}} \dot{q}_{2}+\frac{\partial \boldsymbol{r}}{\partial q_{3}} \dot{q}_{3}=v_{q_{1}} \boldsymbol{e}_{1}+v_{q_{2}} \boldsymbol{e}_{2}+v_{q_{3}} \boldsymbol{e}_{3}
$$

$$
v_{q_{i}}=H_{i} \dot{q}_{i}
$$

$$
a_{q_{i}}=\frac{\mathrm{d} \boldsymbol{v}}{\mathrm{d} t} \cdot 
\boldsymbol{e}_{i}=\frac{1}{H_{i}}\left(\frac{\mathrm{d} 
\boldsymbol{v}}{\mathrm{d} t} \cdot \frac{\partial 
\boldsymbol{r}}{\partial q_{i}}\right)=\frac{1}{H_{i}}
\left[\frac{\mathrm{d}}{\mathrm{d} t}\left(\boldsymbol{v} 
\cdot \frac{\partial \boldsymbol{r}}{\partial q_{i}}\right)-
\boldsymbol{v} \cdot \frac{\mathrm{d}}{\mathrm{d} t}
\left(\frac{\partial \boldsymbol{r}}{\partial q_{i}}\right)\right]
$$

而

$$
\frac{\mathrm{d}}{\mathrm{d} t}\left(\frac{\partial \boldsymbol{r}}{\partial q_{i}}\right)=\frac{\partial^{2} \boldsymbol{r}}{\partial q_{i} \partial q_{1}} \dot{q}_{1}+\frac{\partial^{2} \boldsymbol{r}}{\partial q_{i} \partial q_{2}} \dot{q}_{2}+\frac{\partial^{2} \boldsymbol{r}}{\partial q_{i} \partial q_{3}} \dot{q}_{3}
$$

$$
\frac{\partial \boldsymbol{v}}{\partial q_{i}}=\frac{\partial^{2} \boldsymbol{r}}{\partial q_{1} \partial q_{i}} \dot{q}_{1}+\frac{\partial^{2} \boldsymbol{r}}{\partial q_{2} \partial q_{i}} \dot{q}_{2}+\frac{\partial^{2} \boldsymbol{r}}{\partial q_{3} \partial q_{i}} \dot{q}_{3}
$$

故

$$
\frac{\mathrm{d}}{\mathrm{d} t}\left(\frac{\partial \boldsymbol{r}}{\partial q_{i}}\right)=\frac{\partial \boldsymbol{v}}{\partial q_{i}}
$$

$$
\frac{\partial \boldsymbol{r}}{\partial q_{i}}=\frac{\partial \boldsymbol{v}}{\partial \dot{q}_{i}}
$$

$$
a_{q_{i}}=\frac{1}{H_{i}}\left[\frac{\mathrm{d}}{\mathrm{d} t}\left(\boldsymbol{v} \cdot \frac{\partial \boldsymbol{v}}{\partial \dot{q}_{i}}\right)-\boldsymbol{v} \cdot \frac{\partial \boldsymbol{v}}{\partial q_{i}}\right]
$$

设$T=v^{2} / 2$为动能，则

$$
a_{q_{i}}=\frac{1}{H_{i}}\left(\frac{\mathrm{d}}{\mathrm{d} t} \frac{\partial T}{\partial \dot{q}_{i}}-\frac{\partial T}{\partial q_{i}}\right)
$$
# 参考系
## 平动参考系
### 绝对速度, 相对速度与牵连速度

有两个参考系 , 前者是静止不动的, 后者相对于前者作直线运动。

* **绝对运动** 物体相对于静止参考系的运动
* **相对速度** 物体相对于运动参考系的运动
* **牵连速度** 物体随运动参考系一道运动而具有相对于静止参考系的运动

$$
\boldsymbol{v}=\boldsymbol{v}_{0}+\boldsymbol{v}^{\prime}
$$

### 绝对加速度，相对加速度与牵连加速度

$$
a=a_{0}+a^{\prime}
$$

> 惯性平动系：$a_0=0$; 非惯性平动系$a_0\ne 0$

# 运动方程

$$
m \ddot{\boldsymbol{r}}=\boldsymbol{F}(\boldsymbol{r}, \dot{\boldsymbol{r}}, t)
$$

## 直角坐标系

$$m \ddot{x}=F_{x}(x, y, z ; \dot{x}, \dot{y}, \dot{z} ; t)$$

$$m \ddot{y}=F_{y}(x, y, z ; \dot{x}, \dot{y}, \dot{z} ; t)$$

$$m \ddot{z}=F_{z}(x, y, z ; \dot{x}, \dot{y}, \dot{z} ; t)$$

## 平面极坐标系

$$m\left(\ddot{r}-\dot{\theta}^{2}\right)=F_{r}(r, \theta ; \dot{r}, \dot{\theta} ; t)$$

$$m(r \ddot{\theta}+2 \dot{r} \quad \dot{\theta})=F_{\theta}(r, \theta ; \dot{r}, \dot{\theta} ; t)$$

## 约束与自然坐标系

> * 解非自由质点的运动（或称约束运动）问题，一般都是将约束去掉，而代之>以约束反作用力，从而把它当成自由质点
> * 约束反作用力，一般都是未知的,与作用在质点上的其它力及质点本身运动状态等有关；
> * 约束反作用力本身，并不能引起质点的任何运动
> * 约束反作用力通常作用在质点和曲线或曲面的接触点上。在无摩擦的情况下，它沿着曲线或曲面的法线，而在有摩擦的情况下，则和法线成一定角度的倾角

令$R$表约束反力，则

$$
m \ddot{\boldsymbol{r}}=\boldsymbol{F}(\boldsymbol{r}, \dot{\boldsymbol{r}}, t)+\boldsymbol{R}
$$

$$m \frac{\mathrm{d} v}{\mathrm{~d} t}=F_{t}+\mu\sqrt{R_n^2+R_b^2}$$

$$m \frac{v^{2}}{\rho}=F_{n}+R_{n}$$

$$0=F_{\mathrm{b}}+R_{\mathrm{b}}$$

约束用关系式 $f\left(\boldsymbol{r}_{\nu}, \boldsymbol{v}_{\nu}, t\right)$ 给出
> * **几何约束** 约束方程不含点的速度分量 $f\left(\boldsymbol{r}_{\nu}, t\right)=0$
> * **微分约束** 含速度分量
> * **

# 解题步骤

1. 理解题意
2. 作草图
3. 适当选取坐标系并规定质点的坐标
4. 标出已知及未知的力和加速度
5. 写出微分方程
6. 解方程
7. 讨论

# 有心力

$$
\boldsymbol{F}=\boldsymbol{F}(r) \frac{\boldsymbol{r}}{r}
$$

## 直角坐标系

$$m \ddot{x}=F(r) \frac{x}{r}$$

$$m \ddot{y}=F(r) \frac{y}{r}$$

## 极坐标系

$$m\left(\ddot{r}-r \dot{\theta}^{2}\right)=F(r)$$

$$r^{2} \dot{\theta}=h$$

## 比耐公式

$$h^{2} u^{2}\left(\frac{\mathrm{d}^{2} u}{\mathrm{~d} \theta^{2}}+u\right)=-\frac{F}{m}$$

$$u = \frac1r$$

