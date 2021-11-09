---
layout: blog
istop : true
book : true
title: LAMMPS安装
category: knowledge
tags: 分子动力学 LAMMPS
background-image: Lammps.jpg
date: 2021-3-5 16:37:23 + 0800
---

记录LAMMPS的编译过程，方便自己使用。<!-- more -->

# 基本需求

* gcc, g++, gfortran, make
* [fftw](http://www.fftw.org/download.html)
* [mpich](https://www.mpich.org/downloads/)
* [lammps](https://lammps.sandia.gov/download.html)

建议使用最新版本，新版本会修复很多bug，没有什么某个特定版本最好用一说。

# 安装编译环境

我一般用的Ubuntu，所以直接
```shell
sudo apt-get install gcc g++ gfortran make
```

# 安装fftw

## 准备
下载`*.tar.gz`文件至服务器上，解压并进入解压后的文件夹
```shell
tar -zvxf fftw*.tar.gz
cd fftw*
```
## 配置安装位置及安装

一般用户的库最好放在`/usr/local`目录里，我喜欢按库名及版本号分别命名下级文件夹，方便版本管理，即放在`/usr/local/库名/版本号`下，
比如这次放在`/usr/local/fftw/3.3.8`

```shell
sudo ./configure --prefix=/usr/local/fftw/3.3.8 --enable-shared=yes
sudo make -j4 #(这是并行编译，4为编译的线程数，可以加快编译速度)
sudo make install
```
等待安装完成。

## 配置路径

修改`~/.bashrc`文件，将类库安装文件夹下的`bin`和`lib`文件夹加入路径中。


```shell
#My Path
export PATH=$PATH:/usr/local/fftw/3.3.8/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/fftw/3.3.8/lib
```

在`PATH`和`LD_LIBRARY_PATH`添加相应路径，如果没有，则把以上内容都加上去。

修改完后，使用
```shell
source ~/.bashrc
```
使路径生效

# 安装mpich

## 准备

下载`*.tar.gz`文件至服务器上，解压并进入解压后的文件夹
```shell
tar -zvxf mpich*.tar.gz
cd mpich*
```
## 配置安装位置及安装

基本思想与上面一样，这里只列出命令
```shell
sudo ./configure --prefix=/usr/local/mpich/3.3.2 --enable-shared=yes
sudo make -j4 #(这是并行编译，4为编译的线程数，可以加快编译速度)
sudo make install
```
## 配置路径

```shell
#My Path
export PATH=$PATH:/usr/local/fftw/3.3.8/bin:/usr/local/mpich/3.3.2/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/fftw/3.3.8/lib:/usr/local/mpich/3.3.2/lib
```

修改完后，使用
```shell
source ~/.bashrc
```
使路径生效

用
```shell
which mpirun
```
检查一下，如果给出的是刚才路径下的`bin`文件夹，则修改成功。

# 安装lammps

## 准备

下载`*.tar.gz`文件至服务器上，解压并进入解压后的文件夹
```shell
tar -zvxf lammps*.tar.gz
cd lammps/src/MAKE*
```
## 安装配置

在上面进入的路径下寻找`Makefile.mpi`文件，对其进行修改。如果该路径下没有这一文件，就去下一级的`MACHIES`里复制一个过来。

在对于位置填上`fftw`和`mpich`的相关路径，最终效果如下

```Makefile
# MPICH
MPI_INC =   -DMPICH_SKIP_MPICXX -DOMPI_SKIP_MPICXX=1 -I/usr/local/mpich/3.3.2/include
MPI_PATH = -L/usr/local/mpich/3.3.2/lib
MPI_LIB =	-lmpi -lmpl -lpthread

# FFTW
FFT_INC =    -DFFT_FFTW3 -I/usr/local/fftw/3.3.8/include
FFT_PATH =  -L/usr/local/fftw/3.3.8/lib
FFT_LIB =	-lfftw3

# JPEG一般用不到，直接注释掉
#JPG_INC =       
#JPG_PATH = 	
#JPG_LIB =
```
## 切换用户
lammps 需要使用root用户进行安装
```shell
sudo su
```
切换至root用户。
将上面的`fftw`及·`mpich`的路径同样添加在`/root/.bashrc`中，方法同上。
>安装时出现`mpicxx:cammond not found`错误的可能是没做这一步。

## 编译
修改完后，返回`src`文件夹，进行编译
```shell
cd ..
make yes-all #安装所有包
make no-lib #取消安装需要外链的包
make mpi -j40
```
成功的话`src`路径下会有一个`lmp_mpi`可执行文件

## 版本管理
执行到上一步其实`lammps`已经可以用了，但为了我们使用的方便，有时需要多个编译版本同时存在，这就需要我们对可执行文件进行版本管理。

我的方法是将`lammps`可执行文件放到同一个文件夹下，我习惯放在`/opt/lammps`里。

然后按`lmp_LAMMPS版本号_编译版本说明`重命名

如此次
```shell
sudo cp ./lmp_mpi /opt/lammps/lmp_3Mar20_std #std 在我这里指没有任何附加文件，按yes-all+no-lib编译出来的版本
```
然后把对应的路径加入环境变量中
```shell
export PATH=$PATH:/usr/local/fftw/3.3.8/bin:/usr/local/mpich/3.3.2/bin:/opt/lammps
```
大功告成

## 可能出现的问题及解决
`mpicxx:cammond not found`

1. 见上方``切换用户``部分
2. 在安装`fftw`及`mpich`时加上配置`--enable-shared=yes`
3. 将`fftw`及`mpich`安装至`lammps`的默认目录，即`/usr/local/`