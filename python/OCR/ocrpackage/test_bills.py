import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import cv2
import pytesseract
import aiview_ocr


# ocr = aiview_ocr.OCR(
#     True, # is_scanned
#     r"CosmosOne.jpg", # path
#     r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe", # tesseract_location
# )

pre = aiview_ocr.Preprocessor("CosmosOne.jpg")
pre.rotate(save=True)


# match=re.findall(r'\d+[/.-]\d+[/.-]\d+', ocr.text)

# st=" "
# st=st.join(match)
# print(st)

# price=re.findall(r'[\$\£\€](\d+(?:\.\d{1,2})?)',ocr.text)
# price = list(map(float,price))
# print(price)
# print(max(price))
# x=max(price)
