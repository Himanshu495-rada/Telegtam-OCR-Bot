import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


file = "file.jpg"

img = np.array(Image.open(file))

text = pytesseract.image_to_string(img)

print(text)
