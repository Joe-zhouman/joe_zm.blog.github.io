---
layout: code
istop : true
book : true
title: 手写文本生成
category: code
tags: php
background-image: hacker.jpg
date: 2021-12-4 14:30:19 + 0800
---
老要交手写作业，整了个手写文本生成的脚本。

# 安装

1. 下载安装`php`
2. 解压文件。
3. 把`font`文件夹里的字体安装上
4. ojbk了

# 使用

1. 打开程序所在文件夹
2. 把要生成的文字放在`text.txt`文件夹里
3. `shift `+鼠标，选择`在此处打开powershell窗口`win7用户可能是`cmd`
4. 在命令行里输入`php process.php`，回车运行。生成的文本文档就在文件夹里的`output.docx`里了
5. 在`word`里调调页边距，行间距之类的，调到自己满意为止。有的字，手写字体显现不出来，删掉或者留个空自己补上。

# 下载

[百度网盘](https://pan.baidu.com/s/1smxI015kdivOlVySrJ5xJg) 提取码: rgrg

# 原理

> 首先十分感谢[zjsxwc](https://github.com/zjsxwc/handwrite-text)。本脚本是在他的工作基础上改过来了。主要是适配了`windows`，统一了标点符号，数字等的字体（因为这个不一样还是有点令人怀疑的QAQ）。


本脚本的原理很简单，就是对每个字，随机指定它的字体和字号。


# 代码

```php
<?php


require_once __DIR__ . '/vendor/autoload.php';


function getFontName()
{
    $fontNames = [
        //"陈静的字完整版",
        "李国夫手写体",
        "萌妹子体"
    ];
    return $fontNames[rand(0, count($fontNames) - 1)];
}

function getFontSize()
{
    $sizeNames = ["20","21", "21.5", "22", "22.5", "23","24"];
    return $sizeNames[rand(0, count($sizeNames) - 1)];
}

function getParagraphSpace()
{
    $paragraphSpaces = ["12", "13", "20", "7", "14"];
    return $paragraphSpaces[rand(0, count($paragraphSpaces) - 1)];
}


$text = file_get_contents(__DIR__ . "/text.txt");


// Creating the new document...
$phpWord = new \PhpOffice\PhpWord\PhpWord();

/* Note: any element you append to a document must reside inside of a Section. */

// Adding an empty Section to the document...
$section = $phpWord->addSection();
$textrun = $section->addTextRun();
$textrun->setParagraphStyle(array('spaceAfter' => rand(100,105)));
// Adding Text element with font customized using explicitly created font style object...
$i = 0;
while ($i < mb_strlen($text)) {
    $char = mb_substr($text, $i, 1);
    $i++;
    if ($char == "\n") {
        $section->addTextBreak();

        $textrun = $section->addTextRun();
        $myTextElement = $textrun->addText(" ");
        $textrun->setParagraphStyle(array('spaceAfter' => rand(100,105)));

        $textrun = $section->addTextRun();
        $textrun->setParagraphStyle(array('spaceAfter' => rand(100,105)));
        continue;
    }
    $myTextElement = $textrun->addText($char);
    $fontStyle = new \PhpOffice\PhpWord\Style\Font();
    if($char=="["||$char=="]"||$char=="0"||$char=="1"||($char>"2"&&$char<="9")){
        $fontStyle->setName("萌妹子体");
    }
    elseif($char=="，"||$char=="。"||$char=="."||$char==","||$char=="2"){
        $fontStyle->setName("李国夫手写体");
    }
    else{
        $fontStyle->setName(getFontName());
    }
    $fontStyle->setSize(getFontSize());
    $fontStyle->setPosition(rand(1,3));
    $myTextElement->setFontStyle($fontStyle);
}

// Saving the document as OOXML file...
$objWriter = \PhpOffice\PhpWord\IOFactory::createWriter($phpWord, 'Word2007');
$objWriter->save('output.docx');

// Saving the document as ODF file...
$objWriter = \PhpOffice\PhpWord\IOFactory::createWriter($phpWord, 'ODText');
$objWriter->save('output.odt');

// Saving the document as HTML file...
$objWriter = \PhpOffice\PhpWord\IOFactory::createWriter($phpWord, 'HTML');
$objWriter->save('output.html');
```

看得懂代码的自己修改就好了。
