# 爬取live2d脚本

## 🚴🏻 爬取步骤
![步骤](https://img.mynamecoder.com/20230310224059.png)
人生苦短，我用python写了一个脚本爬取，主要用到的库是`requests`、`os`，在写的过程中发现一个趣事：
```
# mkdirs竟然可以支持创建带有上级路径的文件夹
path = '/pic/../video'
os.path.mkdirs(path) # 会创建video的文件夹
# abspath可以计算绝对路径，比如输入`/pic/../video/xx.mp4`
path = '/pic/../video/xx.mp4'
print(os.path.abspath(path)) # 输出`/video/xx.mp4`
```

## 🌏 模型预览
* [我的网站⭐️](https://mynamecoder.com/)
* [完整功能](https://mi.js.org/live2d-widget/demo/demo.html)

这个仓库会更新一些平时写的脚本，老哥们感兴趣的话，欢迎star⭐️。

## 📷 预览图
![所有模型](https://github.com/WhenCoding/live2d_models/blob/main/all_model_preview.png)

## 🔧 配合框架使用
框架链接：[stevenjoezhang/live2d-widget](https://github.com/WhenCoding/live2d-widget)