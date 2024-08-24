---
layout: blog
istop : true
book : true
title: 动网格与UDF讲义
category: knowledge
tags: CFD fluent UDF
background-image: CFD.jpg
date: 2024-8-24 10:19:08 + 0800
---

关于有限体积法的一些认识<!-- more -->

# CFD从入门到入土「动网格与UDF」

| B站： | @satisfactions |
| :-: | :-: |
| 邮箱： | man.man.man.man.a@gmail.com |
| 个人主页： | www.joezhouman.com |

# 什么是UDF?

Fluent的SDK

# UDF

# UDF学习方法

如何变成UDF大佬

# 学习资料

Fluent UDF 源码

Fluent UDF文档 \(推荐\)

胡坤老师 ANSYS\-fluent 二次开发指南\(本质上是文档的翻译\)

# 开发环境

Vs code \+ C 语言插件 \+ Lingma

# 动网格方法

Move on \!

# Options

In\-Cylinder 模拟气缸内部的运动

Six DOF 六自由度求解器

Periodic Displacement 根据模态形状为叶片颤振分析指定周期性位移。

Implicit Update 在时间步长内更新动态网格\, 而非仅在时间步开始时更新 \(双向耦合\)

![](https://s2.loli.net/2024/08/24/1oU4wLfBWvism3t.png)

# Smoothing

当对具有移动和/或变形边界的区域进行smoothing处理以调整网格时，内部节点会随之移动，但节点的数量及其连接关系不会发生变化。

# Diffusion

默认情况下，共轭梯度法（CG）。在这种情况下，该方法比其他可用方法更快。

如果使用 CG 方法时检测到发散，则会使用广义最小残量法（GMRES）作为替代。

CG 方法可能会生成负体积单元，您可以通过将最大迭代次数从默认的 50 增加到 200\-500 的范围来避免此问题。

如果在增加迭代次数后，CG 方法继续生成负体积单元，或者看到控制台消息提示使用 GMRES。GMRES 方法比 CG 方法更稳健，尤其适用于高长宽比网格，但相应地，它对内存使用和求解时间的要求也更高。

BCGSTAB（双对角共轭梯度法）CG 方法一样，当检测到发散时，BCGSTAB 也会退回到 GMRES 方法进行迭代。

与spring\-based smoothing相比\, 计算 PDE 以实现网格平滑通常成本更高，但它通常能产生更高质量的网格，通常可以处理更大的边界变形。

![](https://s2.loli.net/2024/08/24/bJSvym15XhowEgD.png)

# Diffusivity Based on Boundary Distance

![](https://s2.loli.net/2024/08/24/ShqU4VZX67EwDdO.png)

_Diffusion Parameter = 0_

![](https://s2.loli.net/2024/08/24/CYO6ZbfgNh2nM3K.png)

_Diffusion Parameter = 1_

范围为0到2的值是有效的。值为0在整个网格中均匀扩散边界运动。

更高的值则保留了靠近移动边界的较大网格区域，并使得远离移动边界的区域吸收更多的运动。

对旋转\, 值为1\.5比较合适

距离指的是最近的wall类型边界的无量纲距离\.

Generalized Boundary Distance Method选型开启后\, 距离为最近的未设置为Deforming的边界\, 而不论边界的类型\.

# Diffusivity Based on Cell Volume

默认值为0表示整个网格中均匀扩散边界运动。较高的值使得较大的单元吸收的运动量比较小单元更多\(形变更大\)。

# Spring-based

![](https://s2.loli.net/2024/08/24/BKDMvqQeNU6OW7o.png)

![](https://s2.loli.net/2024/08/24/gE3fBD4SU2obcqy.png)

# Spring Constant Factor

![](https://s2.loli.net/2024/08/24/a2iBCj4zXwkxAeN.png)

_Spring Constant Factor = 0_

![](https://s2.loli.net/2024/08/24/7jlJXpnTHYK1eCA.png)

_Spring Constant Factor = 1_



值为0表示弹簧没有阻尼，边界节点的位移对内部节点的运动影响更大。

# Spring-based smoothing

* 在边界运动或变形的情况下，可以使用，尤其适用于非四面体单元区域和二维三角形区域，但需满足以下条件：
  * 单元区域的边界主要沿一个方向移动，即没有过度的各向异性拉伸或压缩。
  * 运动主要是垂直于边界区域的。
* 如果未满足以上条件，所生成的单元可能具有较高的偏斜度。多面体单元在基于弹簧的平滑处理中尤其容易出现高度偏斜\.
* 无论是否满足上述条件，通常建议对多面体单元使用diffusion\-based smoothing。
* 默认情况下，所有单元区域都启用。禁用除四面体或三角形单元组成的单元区域，可以选择在三维中选择“Tet in Tet Zones”（或在二维中选择“Tri in Tri Zones”）。
* 对混合单元区域，不想在所有单元类型上应用基于弹簧的平滑，可以通过在三维中选择“Tet in Mixed Zones”（或在二维中选择“Tri in Mixed Zones”）来仅对四面体或三角形单元启用弹簧平滑。
* 适用于对齐的变形周期边界

# Linearly Elastic Based Smoothing

* 性质与局限性与diffusion\-based smoothing类似，特别是在旋转运动导致网格质量下降的情况下。

* 计算上比基于扩散的平滑处理更为复杂，但在某些网格和网格运动情况下，它能够更好地保持网格质量。

* 在存在旋转边界运动和尖锐角的情况下，使用Radial Basis Function Smoothing更好。

* 适用于二维的所有单元类型（如三角形、四边形），以及三维的四面体、六面体、楔形和金字塔单元。如果变形单元区域包含多面体单元或悬挂节点，则无法应用此方法。在这种情况下，建议使用Diffusion\-based Smoothing。


# Radial Basis Function Smooth

* 与其他可用的平滑方法相比，它特别适用于旋转的运动

* 适用于所有类型的网格。

* 与扩散平滑方法不同，对于多面体单元，它具有更强的鲁棒性。

* 唯一一种支持在包含Deforming的一致性周期性边界方法。

* 当在集群上运行分布式内存时，性能不如其他平滑方法扩展得那么好。

* 与边界层  _smoothing_  方法不兼容。


# Smoothing from a Reference Position

在进行周期性或准周期性运动的多个循环时可能非常有用。确保平滑总是从相同的参考位置开始，可以使网格质量在每个循环之间保持更一致。

如果案例中包括Frame Motion 或 Mesh Motion，并定义为Deforming区域，则此选项在计算过程中默认启用。如果启用了Layering/Remeshing/Mesh Adaption\, 则该选项不可用。

# 比较

|  | Spring | diffusion | Elastic | Bias |
| :-: | :-: | :-: | :-: | :-: |
| 平移 | √ | √ | √ | × |
| 旋转 | × | 〇 | × | √ |

# Remeshing

* 当边界位移相对于局部单元大小较大时，仅使用smoothing可能导致单元质量下降或单元退化。这将使网格无效（如负体积），并且在更新到下一个时间步长时会导致收敛问题。

* remeshing根据偏斜度标准，对聚集的单元或面进行局部重网格化。如果新的单元或面满足偏斜度标准，则用新单元更新网格，并将解从旧单元插值到新单元中。否则，新的单元将被丢弃，旧的单元将继续保留。

* 在为动态区域定义重网格化设置时，建议使用unified remeshing（默认选项）在网格移动时试图保持初始网格大小分布。这简化了设置，并能提供更高的鲁棒性，特别是在并行仿真中。

* 统一重网格化适用于三角形或四面体单元，并且可以在三维边界层网格中生成楔形单元。

* 可以method\-based remeshing，对特定类型的单元进行更新


# Parameters

* 确定使用remeshing的网格：
  * Skewness > Maximum Cell Skewness
  * Element Size < Minimum Length Scale
  * Element Size > Maximum Length Scale
* 如果local remeshing不能降低整体的Skewness，将使用Zone remeshing自动remeshing所有网格。
* 对2D, Max = 1\.41 Max, Min = 0\.71 Min
* 对3D, Max = 1\.26 Max, Min = 0\.80 Min

![](https://s2.loli.net/2024/08/24/fmCEM9vT3WpUQA6.png)

# Remeshing

* Methods\-Based Remeshing
  * Local Cell：只影响三角形和四面体网格。
  * Local Face：仅3D模型使用，只影响四面体网格和边界层中的楔形网格
  * Cell Zone：将所有网格的类型替换为三角形或四面体。并在3D边界层区域生成楔形网格
  * Region Face：对2D模型，只影响三角形网格；对3D模型，只影响四面体网格和边界层中的楔形网格
  * 2\.5D：仅3D模型使用，只影响六面体网格和从三角形面网格延伸出来的楔形网格

![](https://s2.loli.net/2024/08/24/fmCEM9vT3WpUQA6.png)

# 小结

* 形变从大到小:
  * 整体变化小 smoothing
  * 整体变化大, 单步变化小 smoothing \+ remeshing
  * 整体变化大, 单步变化大 remeshing
* 运动类型:
  * 平动 : 均可
  * 旋转 : bias smoothing, remeshing\.
  * 旋转\+平动 : diffusion smoothing, remeshing

