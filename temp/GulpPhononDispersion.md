# GULP Phonon Dispersion curve

## scripts

```gulp
phon nofreq 
cell
   4.212000   4.212000   4.212000  90.000000  90.000000  90.000000
fractional
Mg   core  0.000000   0.000000   0.000000 
Mg   core  0.000000   0.500000   0.500000 
Mg   core  0.500000   0.000000   0.500000 
Mg   core  0.500000   0.500000   0.000000 
O    core  0.500000   0.500000   0.500000 
O    core  0.500000   0.000000   0.000000 
O    core  0.000000   0.500000   0.000000 
O    core  0.000000   0.000000   0.500000 
O    shel  0.500000   0.500000   0.500000 
O    shel  0.500000   0.000000   0.000000 
O    shel  0.000000   0.500000   0.000000 
O    shel  0.000000   0.000000   0.500000 
species
Mg core 2.0
O  core 0.86902
O  shel -2.86902
buck
O    shel Mg   core    1295.553402 0.300000    0.00000  0.000  8.000
buck
O    shel O    shel   22764.000000 0.149000   27.88000  0.000 12.000
spring
O 74.92
shrink
4 4 4
dispersion
0.0 0.0 0.0 to 0.5 0.5 0.5
output phon example5
```



## 解析

> phon nofreq 

关键词：

* phonon

Causes the phonon frequencies to be calculated for each structure with k points specified at the end of each run. If no k points are explicitly given the phonons are calculated at the gamma point. Note: For materials with charges it is important to consider the effect of the LO/TO splitting.

计算声子频率。

* nofreq

Causes the frequencies not to be output after a phonon calculation. This is useful when calculating phonon dispersion curves which can involve large numbers of k points and frequencies.

不输出频率。

> cell
>   			 4.212000   4.212000   4.212000  90.000000  90.000000  90.000000

晶体结构：晶格参数：$a\quad b\quad c\quad \alpha\quad \beta\quad \gamma\quad$

也可使用向量形式：

vectors

4.212 0.000 0.000

0.000 4.212 0.000

0.000 0.000 4.212  

> fractional
> Mg   core  0.000000   0.000000   0.000000 
> Mg   core  0.000000   0.500000   0.500000 
> Mg   core  0.500000   0.000000   0.500000 
> Mg   core  0.500000   0.500000   0.000000 
> O    core  0.500000   0.500000   0.500000 
> O    core  0.500000   0.000000   0.000000 
> O    core  0.000000   0.500000   0.000000 
> O    core  0.000000   0.000000   0.500000 
> O    shel  0.500000   0.500000   0.500000 
> O    shel  0.500000   0.000000   0.000000 
> O    shel  0.000000   0.500000   0.000000 
> O    shel  0.000000   0.000000   0.500000 

原子坐标：

1. fractional 分数形式
1. 

* core - represents the main part of an atom including all its mass

* shel - represents the mass-less component in a shell model

* bcor - a core, but with a spherical breathing radius

* bshe - a shell, but with a spherical breathing radius  