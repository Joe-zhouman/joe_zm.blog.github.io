# 计算机指令

![image-20230207225547820](C:/Users/Joe/AppData/Roaming/Typora/typora-user-images/image-20230207225547820.png)

![image-20230207225602843](C:/Users/Joe/AppData/Roaming/Typora/typora-user-images/image-20230207225602843.png)

![image-20230207225623454](C:/Users/Joe/AppData/Roaming/Typora/typora-user-images/image-20230207225623454.png)

设计原则：

* 简单源于规整
* 更少则更快
* 优秀设计需要折中

有符号数：
$$
-a_{63}2^63+\sum a_i2^i
$$
![image-20230209164404834](C:/Users/Joe/AppData/Roaming/Typora/typora-user-images/image-20230209164404834.png)

以下是RISC-V指令中每个字段名称的含义：

* opcode（操作码）：指令的基本操作，这个缩写是它的惯用名称
* rd：目的操作数寄存器，用来存放操作结果。
* funct3：一个另外的操作码字段
* rs1：第一个源操作数寄存器
* rs2：第二个源操作数寄存器
* funct7：一个另外的操作码字段