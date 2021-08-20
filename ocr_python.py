# from PIL import Image
# import pytesseract
# import numpy as np

# filename = 'C:\\Users\\himan\\Desktop\\my_programs\\python\\Telegram Bot\\file_5.jpg'
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)

# print(text)

import numpy as np
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


file = "file_5.jpg"

img = np.array(Image.open(file))

text = pytesseract.image_to_string(img)

print(text)
