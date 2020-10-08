import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image = Image.open(r'D:\open-cv\Image recognition1\b.png')
code = pytesseract.image_to_string(image)
print(code)