import torch
import torchvision
import torchvision.transforms as transforms
import pandas as pd
import numpy as np
import cv2

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose([transforms.ToTensor()])

trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

full_dataset = trainset + testset

def convert_to_numpy(dataset):
    images = np.array([np.array(image[0]).flatten() for image in dataset])
    labels = np.array([image[1] for image in dataset])
    return images, labels

images, labels = convert_to_numpy(full_dataset)

generated_images = []
for _ in range(len(full_dataset) // 11):

    canvas = np.zeros((28, 28), dtype=np.uint8)

    thickness = np.random.randint(1, 5)

    for _ in range(5 - thickness):
        x1, y1 = np.random.randint(0, 28, size=2)
        x2, y2 = np.random.randint(0, 28, size=2)

        color = np.random.randint(1, 256)
        cv2.line(canvas, (x1, y1), (x2, y2), color, thickness)

    canvas = canvas / 255.0
    generated_images.append(canvas.flatten())

images = np.concatenate((images, np.array(generated_images)))
labels = np.concatenate((labels, [10] * len(generated_images)))

df = pd.DataFrame(images)
df['label'] = labels

df.to_csv('./data/mnist+.csv', index=False)
