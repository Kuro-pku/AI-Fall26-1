aloha



我学到了什么



一、Git 和 GitHub 基础



通过这次作业，我学会了 Git 的基本工作流程：用 `git clone` 把远程仓库克隆到本地，用 `git add` 把修改加入暂存区，用 `git commit` 提交到本地历史，再用 `git push` 推送到 GitHub 远程仓库。我还学会了创建分支，用 `git checkout -b for\_fun main` 从 main 分支创建 for\_fun 分支，并在两个分支之间切换。

在把 for\_fun 合并回 main 时，因为两个分支都修改了 `readme.md`，所以产生了冲突。我学会了查看冲突标记，手动把文件改成只保留 `aloha`，删除 `<<`、`==`、`>>` 这些标记，然后用 `git add` 和 `git commit` 完成合并。



&#x20;二、Huggingface 环境和预训练模型推理



我安装了 Miniconda，创建了 `py310` 环境，并安装了 PyTorch、torchvision、datasets、transformers 和 huggingface\_hub。然后使用预训练的 ResNet18 模型在 MNIST 数据集上做推理。

因为 ResNet18 默认输入是 224x224 的 RGB 图像，而 MNIST 是 28x28 的灰度图，所以我用 `transforms.Resize((224, 224))` 调整大小，用 `transforms.Grayscale(num\_output\_channels=3)` 转成三通道，并做了归一化，将 ResNet18 最后的全连接层改成输出 10 类，对应 MNIST 的 0 到 9。



三、项目实践

我学会了用 `.gitignore` 避免把数据集、`\_\_pycache\_\_` 和模型权重提交到仓库。由于数据集等无需提交，所以在 `.gitignore` 里加入了 `data/`、`\*.pth`、`\*.pt`、`\*.bin`、`\*.safetensors` 等规则，这样仓库不会被大文件污染。

我还学会了写有意义的 commit message，比如在推理提交里包含准确率。



这些步骤让我理解了 Git 不只是保存代码，还能记录整个开发过程。

