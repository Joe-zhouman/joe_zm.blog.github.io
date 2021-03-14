---
layout: code
istop : true
book : true
title: 由NaN引起的错误
category: code
tags: C#
background-image: CSharpDotNet.png
date: 时间

---
由NaN引发的错误。<!-- more -->

# 简述

以下是出错的代码

```CSharp
public double Temp { get=>_temp;
            set {
                if(value == double.NaN){
                    throw new ValOutOfRangeException();
                }
                _temp = value;               
            }
        }
```
原意是在属性`Temp`上添加`setter`，如果要将`Temp`设为`NaN`则抛出异常。

结果任然可以将`Temp`设为`NaN`。

# 原因

造成这一错误的原因是`double.NaN`不能用`==`判等

运行如下代码

```CSharp
Console.WriteLine($"{double.NaN==double.NaN}");
```
其结果是`False`。

# 解决

用`double.IsNaN`判断

```CSharp
public double Temp { get=>_temp;
            set {
                if(double.IsNaN(value)){
                    throw new ValOutOfRangeException();
                }
                _temp = value;               
            }
        }
```

# 延伸

除了`NaN`以外，其他的`浮点数`也最好不用`==`判断。

`Math.Net`有相关的解决方案。

[查看 Precision.cs](https://github.com/mathnet/mathnet-numerics/blob/master/src/Numerics/Precision.cs)