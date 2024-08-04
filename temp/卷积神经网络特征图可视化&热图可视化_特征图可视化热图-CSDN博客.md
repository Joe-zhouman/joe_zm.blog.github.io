* * *

前言
--

使用pytorch中的钩子将[特征图](https://so.csdn.net/so/search?q=%E7%89%B9%E5%BE%81%E5%9B%BE&spm=1001.2101.3001.7020)和梯度勾出来，从而达到可视化特征图（featuremap）和可视化热图（heatmap）的目的。

* * *

`提示：以下是本篇文章正文内容，下面案例可供参考`

一、可视化特征图
--------

```python
`import torch.nn as nn
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
import torchvision.utils as vutils
from torch.utils.tensorboard import SummaryWriter
import torchvision.models as models
import torch
import torch.nn.functional as F
from ipdb import set_trace
 

 
writer = SummaryWriter(comment='test_your_comment', filename_suffix="_test_your_filename_suffix")
 

path_img = "./dog.jpg"     
normMean = [0.49139968, 0.48215827, 0.44653124]
normStd = [0.24703233, 0.24348505, 0.26158768]
 
norm_transform = transforms.Normalize(normMean, normStd)
img_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    norm_transform])
img_pil = Image.open(path_img).convert('RGB')
if img_transforms is not None:
    img_tensor = img_transforms(img_pil)
    img_tensor.unsqueeze_(0)    
 

vggnet = models.vgg16_bn(pretrained=False)
pthfile = './pretrained/vgg16_bn-6c64b313.pth'
vggnet.load_state_dict(torch.load(pthfile))
 
 

fmap_dict = dict()
n = 0
 
def hook_func(m, i, o):
    key_name = str(m.weight.shape)
    fmap_dict[key_name].append(o)
 
for name, sub_module in vggnet.named_modules():  
    if isinstance(sub_module, nn.Conv2d):
        n += 1
        key_name = str(sub_module.weight.shape)
        fmap_dict.setdefault(key_name, list())
        n1, n2 = name.split(".")
        vggnet._modules[n1]._modules[n2].register_forward_hook(hook_func)
 

output = vggnet(img_tensor)
print(fmap_dict['torch.Size([128, 64, 3, 3])'][0].shape)

for layer_name, fmap_list in fmap_dict.items():
    fmap = fmap_list[0]
    
    fmap.transpose_(0, 1)
    
 
    nrow = int(np.sqrt(fmap.shape[0]))
    
    
    fmap = F.interpolate(fmap, size=[112, 112], mode="bilinear")
    fmap_grid = vutils.make_grid(fmap, normalize=True, scale_each=True, nrow=nrow)
    print(type(fmap_grid),fmap_grid.shape)
    writer.add_image('feature map in {}'.format(layer_name), fmap_grid, global_step=322)` 
```

![](https://img-blog.csdnimg.cn/8e7718ed24054f128118a74c3b173f88.png)

![](https://img-blog.csdnimg.cn/e836d58b85304c068405b1f1dd59545a.png)

![](https://img-blog.csdnimg.cn/ee46be34805546b6b26191e293e8c8bf.png)

![](https://img-blog.csdnimg.cn/65a0928112f04ab3a39d26d9d3eef97a.png)

![](https://img-blog.csdnimg.cn/bb24b12315b949f39b017902d42be8c5.png)

![](https://img-blog.csdnimg.cn/e14a37cc6fcf4042923fa0ba844035d3.png)

![](https://img-blog.csdnimg.cn/67b9573dbf6849d794632982b42212a2.png)

![](https://img-blog.csdnimg.cn/f99e3d72a2684a3fb5c2e1d7971c6c72.png)

二、[热力图](https://so.csdn.net/so/search?q=%E7%83%AD%E5%8A%9B%E5%9B%BE&spm=1001.2101.3001.7020)可视化（图像分类）
-----------------------------------------------------------------------------------------------------

```python
import cv2
import os
import numpy as np
import torch
import torchvision.transforms as transforms
from torchvision import models
import json
from ipdb import set_trace
 
def img_preprocess(img_in):
    img = img_in.copy()						
    img = img[:, :, ::-1]   				
    img = np.ascontiguousarray(img)			
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.4948052, 0.48568845, 0.44682974], [0.24580306, 0.24236229, 0.2603115])
    ])
    img = transform(img)
    img = img.unsqueeze(0)					
    return img

def backward_hook(module, grad_in, grad_out):
    grad_block.append(grad_out[0].detach())
 
def farward_hook(module, input, output):
    fmap_block.append(output)

def cam_show_img(img, feature_map, grads, out_dir):
    H, W, _ = img.shape
    cam = np.zeros(feature_map.shape[1:], dtype=np.float32)		
    grads = grads.reshape([grads.shape[0],-1])					
    weights = np.mean(grads, axis=1)							
    for i, w in enumerate(weights):
        cam += w * feature_map[i, :, :]							
    cam = np.maximum(cam, 0)
    cam = cam / cam.max()
    cam = cv2.resize(cam, (W, H))
 
    heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
    cam_img = 0.3 * heatmap + 0.7 * img
 
    path_cam_img = os.path.join(out_dir, "cam.jpg")
    cv2.imwrite(path_cam_img, cam_img)
 
 
if __name__ == '__main__':
    
    path_img = './cam/test.png'
    json_path = './cam/labels.json'
    output_dir = './cam'
 
    with open(json_path, 'r') as load_f:
        load_json = json.load(load_f)
    classes = {int(key): value for (key, value)
               in load_json.items()}

    classes = list(classes.get(key) for key in range(1000))
    
    fmap_block = list()
    grad_block = list()
  
    img = cv2.imread(path_img, 1)
    img_input = img_preprocess(img)
  
    net = models.resnet.resnet50(pretrained=True)
   
    net.eval()														
    print(net)

    net.layer4[-1].register_forward_hook(farward_hook)	
    net.layer4[-1].register_backward_hook(backward_hook)
 
    output = net(img_input)
    idx = np.argmax(output.cpu().data.numpy())
    print("predict: {}".format(classes[idx]))
 
    
    net.zero_grad()
    class_loss = output[0,idx]
    class_loss.backward()
 
    
    grads_val = grad_block[0].cpu().data.numpy().squeeze()
    fmap = fmap_block[0].cpu().data.numpy().squeeze()
 
    
    cam_show_img(img, fmap, grads_val, output_dir)` 

```

![](https://img-blog.csdnimg.cn/c07ef958594e4de4a5918da21229f44f.png)

![](https://img-blog.csdnimg.cn/f34e5449336949d3ab9b5e0747daf23c.png)

* * *

总结
--

以上通过pytorch中的钩子进行特征图可视化和热图可视化，均是针对[图像分类](https://so.csdn.net/so/search?q=%E5%9B%BE%E5%83%8F%E5%88%86%E7%B1%BB&spm=1001.2101.3001.7020)的。其中特征图可视化可以直接迁移到目标检测，语义分割等其他目标，但是热图却不能直接转换，未来会增加对目标检测热图的可视化相关工作。