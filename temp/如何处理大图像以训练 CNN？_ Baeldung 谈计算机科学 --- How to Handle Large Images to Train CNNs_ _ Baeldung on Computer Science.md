  

1\. Overview1.概述[](#overview)
-----------------------------

In this tutorial, **we’ll talk about how to handle large images to train Convolutional Neural Networks (CNNs)**. First, we’ll introduce CNNs and the difficulties of using large images as input to CNNs. Then, we’ll describe three ways to handle large images: resize the image, increase the model size or process the images in batches.  
在本教程中，我们将讨论如何处理大图像以训练卷积神经网络（CNN）。首先，我们将介绍卷积神经网络以及将大尺寸图像作为卷积神经网络输入的困难。然后，我们将介绍处理大图像的三种方法：调整图像大小、增大模型大小或批量处理图像。

2\. Introduction to CNNs  
2.CNN 简介[](#introduction-to-cnns)
------------------------------------------------------------

**One of the most successful architectures in deep learning is the [Convolutional Neural Networks (CNNs)](https://www.baeldung.com/cs/ai-convolutional-neural-networks) which consists of one or more convolutional layers followed by some feed-forward layers.** In a [previous article](https://www.baeldung.com/cs/neural-networks-conv-fc-layers), we discussed the differences between these types of layers.  
卷积神经网络（CNN）是深度学习领域最成功的架构之一，它由一个或多个卷积层和一些前馈层组成。在上一篇文章中，我们讨论了这些层类型之间的区别。

CNNs are primarily used in visual tasks like image classification, image segmentation, and reconstruction. However, during the last years, CNNs are also employed in other tasks like speech recognition and natural language processing. In this article, we’ll focus on the use of CNNs in visual tasks where the input of the model is an image.  
CNN 主要用于图像分类、图像分割和重建等视觉任务。不过，在过去几年中，CNN 也被用于语音识别和自然语言处理等其他任务。本文将重点讨论 CNN 在视觉任务中的应用，其中模型的输入是图像。

3\. The Problem of Large Images  
3.大图像问题[](#the-problem-of-large-images)
-------------------------------------------------------------------------

**A crucial characteristic of CNNs is the fact the input image should be fixed in size.  
CNN 的一个重要特征是输入图像的大小必须固定。** 

Specifically, the total number of parameters in a CNN depends on the input size. During training, the total number of parameters should be stable. That’s why the input size should be stable as well.  
具体来说，CNN 的参数总数取决于输入大小。在训练过程中，参数总数应保持稳定。因此，输入大小也应保持稳定。

Also, a common practice in computer vision is to use already trained CNNs for pretraining. This practice facilitates the training of a model since we use some prior knowledge about the image distribution we want to learn. However, the pretrained CNNs have been trained using a specific input size.  
此外，计算机视觉领域的一个常见做法是使用已经训练过的 CNN 进行预训练。这种做法有利于模型的训练，因为我们使用了一些关于要学习的图像分布的先验知识。不过，预训练的 CNN 是使用特定的输入大小进行训练的。

We can easily understand that the fixed input size creates a problem in training CNNs since we are restricted to using a predefined input size that may not be equal to the size of our images. Below, we will discuss three solutions for using large images in CNN architectures that take as input smaller images.  
我们不难理解，固定的输入尺寸会给 CNN 的训练带来问题，因为我们只能使用预定义的输入尺寸，而该尺寸可能与我们的图像尺寸不相等。下面，我们将讨论在将较小图像作为输入的 CNN 架构中使用大图像的三种解决方案。

4\. Resize4.调整大小[](#resize)
---------------------------

**One solution is to resize the input image so that it has the same size as the required input size of the CNN.** There are many ways to resize an input image. In this article, we’ll focus on two of them.  
一种解决方案是调整输入图像的大小，使其与 CNN 所需的输入大小相同。调整输入图像大小的方法有很多。本文将重点介绍其中两种。

### 4.1. Downsample the Image  
4.1.对图像进行降采样[](#1-downsample-the-image)

**When we downsample an image, our goal is to reduce the spatial resolution of the image while keeping the same two-dimensional representation.** The simplest way to downsample an image is to skip some pixels. For example, in order to reduce an image to half of its size, we can skip one every two pixels.  
对图像进行降采样时，我们的目标是降低图像的空间分辨率，同时保持相同的二维表现形式。对图像进行降采样的最简单方法就是跳过一些像素。例如，为了将图像缩小到其大小的一半，我们可以跳过每两个像素中的一个。

However, the well-known problem of aliasing appears in this case, where high-frequency changes (like changing light and dark colors) will convert to low-frequency changes (like constant dark and light).  
不过，在这种情况下会出现众所周知的混叠问题，即高频变化（如明暗颜色变化）会转换为低频变化（如明暗不变）。

**A better downsampling technique that prevents aliasing is averaging, where we average ![](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-2f24fb7fb627da49dd5e446c9afdfd6c_l3.svg)
 pixels into a single pixel.  
更好的防止混叠的下采样技术是平均法，即把 ![](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-2f24fb7fb627da49dd5e446c9afdfd6c_l3.svg)
 像素平均为一个像素。** 

### 4.2. Crop the Image  
4.2.裁剪图像[](#2-crop-the-image)

**If we don’t want to keep the whole content of the image, we can reduce its size by cropping down the image to the size we want.** Usually, we crop the image from the center part so as to keep the central content that is usually more useful and significant for the image.  
如果我们不想保留图像的全部内容，可以通过裁剪图像来缩小图像大小。通常，我们会从中心部分开始裁剪图像，以保留中心内容，因为中心内容通常对图像更有用、更重要。

In the diagram below, we can see an example of using the above methods:  
在下图中，我们可以看到一个使用上述方法的示例：

![](https://www.baeldung.com/wp-content/uploads/sites/4/2022/08/resize_image.png)

5\. Increase Model Size  
5.增大模型尺寸[](#increase-model-size)
----------------------------------------------------------

Until now, we dealt with the problem of large input images to CNNs by reducing the size of the input image. **Another possible way could be to keep the size of the input stable and modify the CNN architecture accordingly.** Specifically, we can make use of the fact that convolutional layers can reduce the size of an input image. So, we can add some additional convolutional layers before the convolutional layers of the CNN architecture and end up with an architecture that can handle larger images.  
迄今为止，我们通过减小输入图像的大小来解决 CNN 输入图像过大的问题。另一种可能的方法是保持输入图像的大小稳定，并相应地修改 CNN 架构。具体来说，我们可以利用卷积层可以缩小输入图像大小这一事实。因此，我们可以在 CNN 架构的卷积层之前添加一些额外的卷积层，最终得到一个可以处理更大图像的架构。

In the image below, we can see an example of using a large image to a CNN by adding an extra convolutional layer. Specifically, the convolutional layer decreases the input size by a factor of 4:  
在下图中，我们可以看到通过增加一个额外的卷积层将大图像用于 CNN 的例子。具体来说，卷积层将输入大小减少了 4 倍：

![](https://www.baeldung.com/wp-content/uploads/sites/4/2022/08/increase_arch.png)

6\. Process Images in Batches  
6.分批处理图像[](#process-images-in-batches)
----------------------------------------------------------------------

**The third solution to our problem is to process the large input images in batches and reduce the overall memory load.** Specifically, a problem when using large images is that the whole training set can’t fit into our memory. The solution comes with [Mini-Batch Gradient Descent](https://www.baeldung.com/cs/epoch-vs-batch-vs-mini-batch), where we iterate through the dataset and process a group of images each time. So, we can adjust the size of this group (batch) to fit the large images into our memory.  
第三个解决方案是分批处理大型输入图像，以减少整体内存负荷。具体来说，使用大型图像时的一个问题是，我们的内存无法容纳整个训练集。迷你批量梯度下降法可以解决这个问题，我们可以遍历数据集，每次处理一组图像。因此，我们可以调整这组图像（批次）的大小，以便将大图像放入内存中。

7\. Conclusion7.结论[](#conclusion)
---------------------------------

In this article, we presented three ways of using large images as input to CNNs. First, we introduced the problem of using large images to these architectures, and then we described the three solutions along with detailed examples.  
在本文中，我们介绍了将大型图像作为 CNN 输入的三种方法。首先，我们向这些架构介绍了使用大图像的问题，然后通过详细示例介绍了这三种解决方案。

Comments are open for 30 days after publishing a post. For any issues past this date, use the Contact form on the site.  
帖子发布后 30 天内可发表评论。超过此日期的任何问题，请使用网站上的联系表。