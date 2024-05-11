import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('./data/photo.jpg', 0)

# Уменьшение шума
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Бинаризация изображения
_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# Нахождение контуров
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Находим контур с максимальной площадью
max_area = 0
max_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_contour = contour

# Находим прямоугольник, описывающий этот контур
x, y, w, h = cv2.boundingRect(max_contour)

# Обрезаем изображение до этого прямоугольника
cropped = binary[y:y+h, x:x+w]

# Инвертируем обрезанное изображение
inverted = cv2.bitwise_not(cropped)

# Находим контуры на инвертированном изображении
contours, _ = cv2.findContours(inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Находим контур с максимальной площадью на инвертированном изображении
max_area = 0
max_contour = None
for contour in contours:
    area = cv2.contourArea(contour)
    if area > max_area:
        max_area = area
        max_contour = contour

# Находим прямоугольник, описывающий этот контур
x, y, w, h = cv2.boundingRect(max_contour)

# Обрезаем инвертированное изображение до этого прямоугольника
final_cropped = inverted[y:y+h, x:x+w]

# Инвертируем обрезанное изображение обратно
final_cropped = cv2.bitwise_not(final_cropped)

cv2.imshow('Final Cropped', final_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
