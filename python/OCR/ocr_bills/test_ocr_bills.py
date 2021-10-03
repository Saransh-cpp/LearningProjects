import cv2
import math
import numpy as np
import pytesseract
from scipy import ndimage
from skimage.filters import threshold_local
from aiview_ocr import Preprocessor

# img = cv2.imread("Bill3.jpg")


def noise_removal(image):

    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image


def thick_font(image):

    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image


pre = Preprocessor("Bill3.jpg")

img = pre.scan(save=True)
img = noise_removal(img)

img = thick_font(img)

img_edges = cv2.Canny(img, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(
    img_edges,
    rho=1,
    theta=np.pi / 180.0,
    threshold=160,
    minLineLength=100,
    maxLineGap=10,
)

# calculate all the angles:
angles = []
for [[x1, y1, x2, y2]] in lines:
    # drawing Hough lines
    angle = 90 + math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

# median angle
median_angle = np.median(angles)
print(median_angle)
# actual rotate
img = ndimage.rotate(img, median_angle)

cv2.imwrite("rotated.png", img)

tesseract_location = r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = tesseract_location

# reading the image
img = cv2.imread("rotated.png")

# extracting the text
text = pytesseract.image_to_string(img, config="-l eng --oem 1 --psm 11")
print(text)

# adding boxes around the words
boxes = pytesseract.image_to_data(img)
for z, box in enumerate(boxes.splitlines()):
    if z != 0:
        box = box.split()

        # if the data has a word
        if len(box) == 12:

            x, y = int(box[6]), int(box[7])
            h, w = int(box[8]), int(box[9])

            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 0, 255), 1)

cv2.imwrite("OCR.png", img)
