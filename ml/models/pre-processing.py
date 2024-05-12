from PIL import Image, ImageDraw
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open('./data/text.png')

text = pytesseract.image_to_string(image, lang='rus')
print(text)

boxes = pytesseract.image_to_boxes(image, lang='rus')

draw = ImageDraw.Draw(image)
h = image.height
for b in boxes.splitlines():
    b = b.split(' ')
    draw.rectangle([int(b[1]), h - int(b[4]), int(b[3]), h - int(b[2])], outline='green')

image.show()
