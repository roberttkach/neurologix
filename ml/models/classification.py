import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.optim.lr_scheduler import StepLR
import random
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class MNISTPlusDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image = self.data.iloc[idx, :-1].values.astype('float32').reshape((28, 28))
        label = self.data.iloc[idx, -1]
        if self.transform:
            image = self.transform(image)
        return image, label

transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])

trainset = MNISTPlusDataset(csv_file='./data/mnist+.csv', transform=transform)
trainloader = DataLoader(trainset, batch_size=128, shuffle=True)

testset = MNISTPlusDataset(csv_file='./data/mnist+.csv', transform=transform)
testloader = DataLoader(testset, batch_size=128, shuffle=True)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(1, 32, 3, 1),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, 1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Dropout(0.25),
            nn.Flatten(),
            nn.Linear(9216, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 11),  # Изменено на 11 классов
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        return self.model(x)


net = Net()
net.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
scheduler = StepLR(optimizer, step_size=1, gamma=0.7)


for epoch in range(10):
    net.train()
    running_loss = 0.0
    correct_train = 0
    total_train = 0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()

    scheduler.step()

    net.eval()
    correct_test = 0
    total_test = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data[0].to(device), data[1].to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total_test += labels.size(0)
            correct_test += (predicted == labels).sum().item()

    accuracy_train = correct_train / total_train
    accuracy_test = correct_test / total_test
    torch.save(net.state_dict(), f'./saves/classification-{round(accuracy_test * 100, 2)}.pth')
    print(
        f'Epoch {epoch + 1} completed, loss: {round(running_loss / len(trainloader), 5)}, '
        f'accuracy-train: {round(accuracy_train, 3)}%, accuracy-test: {round(accuracy_test, 3)}%')

    # Выводим случайные 9 изображений из тестового набора данных
    dataiter = iter(testloader)
    images, labels = next(iter(dataiter))

    # Выбираем случайные 9 индексов из диапазона размера батча
    indices = random.sample(range(images.size(0)), 9)

    # Используем эти индексы для выбора изображений и меток
    images = images[indices]
    labels = labels[indices]

    outputs = net(images.to(device))
    _, predicted = torch.max(outputs.data, 1)

    # Переносим тензоры обратно на CPU перед использованием в matplotlib
    images = images.cpu()
    predicted = predicted.cpu()

    fig, axs = plt.subplots(3, 3)
    for i, ax in enumerate(axs.flat):
        ax.imshow(images[i].squeeze(), cmap='gray')
        ax.set_title(f"True: {labels[i]}, Predicted: {predicted[i]}")
        ax.axis('off')

    plt.tight_layout()
    plt.show()



