---
layout: blog
istop : true
book : true
title: vasp安装
category: knowledge
tags: 分子动力学 VASP
background-image: vasp.png
date: 2024-8-4 17:39:42 + 0800
---

记录VASP的编译过程，方便自己使用。<!-- more -->
# 在linux中安装vasp6.3.2 intel并行版本 (包括py4vasp)

## 安装intel-oneapi以及hpc

这里直接通过包管理安装.

> 注意, 需要有`root`权限

以下为基于`Debian`系的apt的安装方法. 由于`CentOS`已经放弃支持, 建议使用`Ubuntu`作为`linux`发行版, 比较简单.

可以通过以下网址查看官方安装教程[intel oneapi base toolkit installation guide](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-download.html)

1. 安装依赖

```bash
sudo apt update
sudo apt install -y gpg-agent wget
```

2. 添加秘钥, 设置存储库

```bash
wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null
```

3. 添加存储库

```bash
echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | sudo tee /etc/apt/sources.list.d/oneAPI.list
```

4. 更新源

```bash
sudo apt update
```

5. 下载安装`intel oneapi base toolkit`

```bash
sudo apt install intel-basekit
```

6. 下载安装`intel HPC toolkit`

可以通过以下网址查看官方安装教程[intel oneapi HPC toolkit installation guide](https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html)

> 这里存储库已经设置过了, 可以跳过前面的步骤, 直接apt就可以了

```bash
 sudo apt install intel-hpckit
```

7. 设置环境变量

   `intel oneapi`的默认安装位置在`/opt/intel/oneapi`

```bash
source /opt/intel/oneapi/setvars.sh
```

> 注意: 以上设置的环境变量是临时的, 想让他永久生效, 将上面这句话加入到自己的环境里.
>
> ```bash
> vim ~/.bashrc
> # 把source /opt/intel/oneapi/setvars.sh加入到文件中, 退出vim
> source ~/.bashrc
> ```

## (可选)安装`hdf5`库 

> `hdf5`不是编译`vasp`必须的, 但是要使用`py4vasp`必须使用这个库. 建议编译两版, 一般不含`hdf5`库, 一版含`hdf5`库.

1. 下载

   [Release HDF5 Release 1.14.4.3 · HDFGroup/hdf5 (github.com)](https://github.com/HDFGroup/hdf5/releases/tag/hdf5_1.14.4.3)

   在以上网址下载`hdf5-X.Y.Z-T.tar.gz`

2. 解压

上传文件至服务器

```bash
tar -zvxf hdf5*.tar.gz
```

3. 安装

```bash
cd hdf5*
sudo mkdir /opt/local/hdf5
sudo mkdir /opt/local/hdf5/1.14.4.3 #按照自己的版本设置
CC=icx FC=ifx CXX=icpx ./configure --prefix=/opt/local/hdf5/1.14.4.3 --enable-fortran --enable-cxx
 # 我的习惯安装在/opt, 并且前面加上版本号方便多版本共存和切换
 # 这里用之前安装的intel套件进行编译
make -j40 #根据计算机线程数改变数值
make check -j40
make install -j40
make check-install -j40
```

> 注意: 如果make过程中出现错误, 先执行
>
> ```bash
> make clean
> ```
>
> 再重新尝试.

> 编译过程中出现权限问题, 给自己加上`/opt/local/hdf5/1.14.4.3`文件夹的权限, 或者切换到`root`用户进行编译.

## 编译VASP

1. 切换到root用户

```bash
sudo su root
```

2. 设置环境变量

   此时变成了`root`用户,需要重新设置环境变量, 这里最好临时设置.

```bash
source /opt/intel/oneapi/setvars.sh
```

3. 设置makefile

   (假设已经进入`vasp`源码的根目录)

```bash
cp ./arch/makefile.include.intel ./makefile.include
vim makefile.include
```

> 注意: 新版本oneapi已经移除了`icc`等套件, 所以需要在`makefile.include`中进行如下修改: 
>
> * icc -> icx
> * icpc -> icpx
> * mpiifort -> mpiifx

将`MKLROOT    ?= /path/to/your/mkl/installation`修改为之前安装的位置

```bash
MKLROOT    ?= /opt/intel/oneapi/mkl
```

(可选, 在编译hdf5版本时需要)将

```bash
# HDF5-support (optional but strongly recommended)
#CPP_OPTIONS+= -DVASP_HDF5
#HDF5_ROOT  ?= /path/to/your/hdf5/installation
#LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
#INCS       += -I$(HDF5_ROOT)/include
```

修改为

```bash
# HDF5-support (optional but strongly recommended)
CPP_OPTIONS+= -DVASP_HDF5
HDF5_ROOT  ?= /opt/local/hdf5/1.14.4.3
LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
INCS       += -I$(HDF5_ROOT)/include
```

最后文件长这样

```bash
# Default precompiler options
CPP_OPTIONS = -DHOST=\"LinuxIFC\" \
              -DMPI -DMPI_BLOCK=8000 -Duse_collective \
              -DscaLAPACK \
              -DCACHE_SIZE=4000 \
              -Davoidalloc \
              -Dvasp6 \
              -Duse_bse_te \
              -Dtbdyn \
              -Dfock_dblbuf

CPP         = fpp -f_com=no -free -w0  $*$(FUFFIX) $*$(SUFFIX) $(CPP_OPTIONS)

FC          = mpiifx
FCL         = mpiifx

FREE        = -free -names lowercase

FFLAGS      = -assume byterecl -w

OFLAG       = -O2
OFLAG_IN    = $(OFLAG)
DEBUG       = -O0

OBJECTS     = fftmpiw.o fftmpi_map.o fftw3d.o fft3dlib.o
OBJECTS_O1 += fftw3d.o fftmpi.o fftmpiw.o
OBJECTS_O2 += fft3dlib.o

# For what used to be vasp.5.lib
CPP_LIB     = $(CPP)
FC_LIB      = $(FC)
CC_LIB      = icx
CFLAGS_LIB  = -O
FFLAGS_LIB  = -O1
FREE_LIB    = $(FREE)

OBJECTS_LIB = linpack_double.o

# For the parser library
CXX_PARS    = icpx
LLIBS       = -lstdc++

##
## Customize as of this point! Of course you may change the preceding
## part of this file as well if you like, but it should rarely be
## necessary ...
##

# When compiling on the target machine itself, change this to the
# relevant target when cross-compiling for another architecture
VASP_TARGET_CPU ?= -xHOST
FFLAGS     += $(VASP_TARGET_CPU)

# Intel MKL (FFTW, BLAS, LAPACK, and scaLAPACK)
# (Note: for Intel Parallel Studio's MKL use -mkl instead of -qmkl)
FCL        += -qmkl=sequential
MKLROOT    ?= /opt/intel/oneapi/mkl
LLIBS      += -L$(MKLROOT)/lib/intel64 -lmkl_scalapack_lp64 -lmkl_blacs_intelmpi_lp64
INCS        =-I$(MKLROOT)/include/fftw

# HDF5-support (optional but strongly recommended)
CPP_OPTIONS+= -DVASP_HDF5
HDF5_ROOT  ?= /opt/local/hdf5/1.14.4.3
LLIBS      += -L$(HDF5_ROOT)/lib -lhdf5_fortran
INCS       += -I$(HDF5_ROOT)/include

# For the VASP-2-Wannier90 interface (optional)
#CPP_OPTIONS    += -DVASP2WANNIER90
#WANNIER90_ROOT ?= /path/to/your/wannier90/installation
#LLIBS          += -L$(WANNIER90_ROOT)/lib -lwannier

```

> 注意: 编译非`hdf5`版本时把`HDF5`那几行注释掉

4. 编译

```bash
make all
```

> 注意: 这里不要加`-j`,会出错

> 注意: 编译出错时先执行`make veryclean`清理之前的编译中间文件

5. (可选)版本管理

> 注意: 以下操作是个人习惯, 也可以不做.

对于非`hdf5`版本

```bash
cd bin
cp vasp_gam /opt/bin/vasp/vasp_gam
cp vasp_std /opt/bin/vasp/vasp_std
cp vasp_ncl /opt/bin/vasp/vasp_ncl
```

对于`hdf5`版本

```bash
cd bin
cp vasp_gam /opt/bin/vasp/vasp_gam_h5
cp vasp_std /opt/bin/vasp/vasp_std_h5
cp vasp_ncl /opt/bin/vasp/vasp_ncl_h5
```

这样就能同时使用两个版本的`vasp`了

6. 设置路径

把`vasp`可执行文件所在位置加入`.bashrc`里

```bash
echo 'export PATH=/opt/bin/vasp/:$PATH' >> ~/.bashrc
source ~/.bashrc
```

(可选)把`hdf5`要使用的链接库加入`.bashrc`里

```bash
echo 'export LD_LIBRARY_PATH=/opt/local/hdf5/1.14.4.3/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

对于有经验的人, 直接修改`.bashrc`文件就行了

## (可选)安装`py4vasp`

1. 安装`conda`

图省事直接装`anaconda`

[Download Anaconda Distribution | Anaconda](https://www.anaconda.com/download)

旁边要注册, 直接`skip registration`

下载对应版本, 应该是一个`sh`文件. 上传到服务器上, 然后

```bash
bash *.sh
```

等待安装完毕.

> 注意: 具体的安装过程这里就不做了, 下次自己在安装时再写详细攻略~

2. 新建环境

```bash
conda create -n vasp python=3.11 #pyrhon版本大于等于3.9比较好
```

等命令执行完

```bash
conda activate vasp
```

3. 安装

```bash
pip install py4vasp
conda install -c conda-forge mdtraj
pip install py4vasp
```

4. 测试

```bash
python -c "import py4vasp; print(py4vasp.__version__)"
```

如果正确输出版本则说明安装成功