import cv2
import math
import numpy as np
import pytesseract
from scipy import ndimage
import aiview_ocr

# img = cv2.imread("Bill3.jpg")

ocr = aiview_ocr.OCR(
    False,
    "Bill4.jpg",
    # r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"
)

text = ocr.ocr_sign_board()
print(text)

# pre = Preprocessor("CosmosTwo.jpg")

# img = pre.scan(save=True)

# orig = img.copy()
# noise_free = pre.remove_noise(img)
# thickened = pre.thicken_font(noise_free)

# _, median_angle = pre.rotate(thickened)

# preprocessed = ndimage.rotate(orig, median_angle)
# preprocessed = pre.remove_noise(preprocessed)
# cv2.imwrite("preprocessed.png", preprocessed)

# img = thin_font(img)

# cv2.imwrite("processed.png", img)

# tesseract_location = r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"

