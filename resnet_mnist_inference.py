import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

testset = datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform
)
testloader = DataLoader(testset, batch_size=64, shuffle=False)

# 使用预训练 ResNet18
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

# MNIST 是 10 类，替换最后一层；不训练，所以准确率会很低
model.fc = nn.Linear(model.fc.in_features, 10)

model = model.to(device)
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for images, labels in testloader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        preds = outputs.argmax(dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

acc = correct / total
print(f"Accuracy: {acc:.4f}")