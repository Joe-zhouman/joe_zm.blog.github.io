# Optimizer in pytorch

## Adam

> Adam optimizer is an optimization algorithm used in deep learning models. It is an extended version of stochastic gradient descent which could be implemented in various deep learning applications such as computer vision and natural language processing in the future years[[1]](https://optimization.cbe.cornell.edu/index.php?title=Adam). The optimizer is called Adam because it uses estimations of the first and second moments of the gradient to adapt the learning rate for each weight of the neural network[[1]](https://optimization.cbe.cornell.edu/index.php?title=Adam). Adam combines the best properties of the AdaGrad and RMSProp algorithms to provide an optimization algorithm that can handle sparse gradients on noisy problems[[3]](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/).

Adam优化器是深度学习模型中使用的优化算法。它是随机梯度下降的扩展版本，在未来的计算机视觉和自然语言处理等各种深度学习应用中都可以实现[[1\]](https://optimization.cbe.cornell.edu/index.php?title=Adam)。该优化器被称为Adam，因为它使用梯度的一阶和二阶矩的估计来适应神经网络每个权重的学习率[[1\]](https://optimization.cbe.cornell.edu/index.php?title=Adam)。Adam结合了AdaGrad和RMSProp算法的最佳特性，提供了一个能够处理嘈杂问题上稀疏梯度的优化算法[[3\]](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/)。

[[1412.6980\] Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

## SGD

> Stochastic Gradient Descent (SGD) is a variant of the Gradient Descent algorithm that is used for optimizing machine learning models. It addresses the computational inefficiency of traditional Gradient Descent methods when dealing with large datasets in machine learning projects[[1\]](https://www.geeksforgeeks.org/ml-stochastic-gradient-descent-sgd/). SGD is often referred to as the cornerstone for deep learning and is an algorithm for training a wide range of models in machine learning[[2\]](https://optimization.cbe.cornell.edu/index.php?title=Stochastic_gradient_descent).
>
> In deep learning, SGD is an iterative method often used for machine learning, optimizing the gradient descent during each search once a random weight vector is picked[[2\]](https://optimization.cbe.cornell.edu/index.php?title=Stochastic_gradient_descent).
>
> In PyTorch, SGD class implements stochastic gradient descent (optionally with momentum)[[3\]](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html). In Keras, SGD is a gradient descent (with momentum) optimizer[[4\]](https://keras.io/api/optimizers/sgd/).

随机梯度下降（SGD）是梯度下降算法的一种变体，用于优化机器学习模型。它解决了传统梯度下降方法在处理机器学习项目中的大型数据集时的计算效率问题[1]。 SGD通常被称为深度学习的基石，是用于训练各种机器学习模型的算法[2]。

在深度学习中，SGD是一种迭代方法，通常用于机器学习，优化每次搜索时选择随机权重向量时的梯度下降[2]。

在PyTorch中，SGD类实现了随机梯度下降（可选带动量）[3]。在Keras中，SGD是一种带动量的梯度下降优化器[4]。