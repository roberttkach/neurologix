import torch
import torchvision
import torchvision.transforms as transforms
import pandas as pd
import numpy as np
import cv2

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([transforms.ToTensor()])  # Убираем шаг нормализации

# Загрузка набора данных для обучения и тестирования
trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# Объединение наборов данных для обучения и тестирования
full_dataset = trainset + testset

def convert_to_numpy(dataset):
    # Преобразование данных в numpy массивы
    images = np.array([np.array(image[0]).flatten() for image in dataset])
    labels = np.array([image[1] for image in dataset])
    return images, labels

images, labels = convert_to_numpy(full_dataset)

# Генерация дополнительных изображений
generated_images = []
for _ in range(len(full_dataset) // 11):  # Генерация 1/11 от общего количества изображений
    # Создание пустого холста 28x28
    canvas = np.zeros((28, 28), dtype=np.uint8)

    # Генерация случайной толщины линии
    thickness = np.random.randint(1, 5)

    # Рисование случайных линий
    for _ in range(5 - thickness):  # Чем больше толщина, тем меньше количество линий
        # Выбор случайных точек для линии
        x1, y1 = np.random.randint(0, 28, size=2)
        x2, y2 = np.random.randint(0, 28, size=2)

        # Выбор случайного цвета для линии
        color = np.random.randint(1, 256)

        # Рисование линии
        cv2.line(canvas, (x1, y1), (x2, y2), color, thickness)

    # Нормализация изображения
    canvas = canvas / 255.0

    # Добавление сгенерированного изображения в список
    generated_images.append(canvas.flatten())

# Добавление сгенерированных изображений и меток None в данные
images = np.concatenate((images, np.array(generated_images)))
labels = np.concatenate((labels, [10] * len(generated_images)))

# Создание DataFrame
df = pd.DataFrame(images)
df['label'] = labels

# Сохранение данных в CSV
df.to_csv('./data/mnist+.csv', index=False)
