import cv2

img = cv2.imread("ChemBookTwo.jpg")

inv_img = cv2.bitwise_not(img)
cv2.imwrite("inv.jpg", inv_img)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return (image)


gray_image = grayscale(img)
cv2.imwrite("gray.jpg", gray_image)

thresh, im_bw = cv2.threshold(gray_image, 130, 245, cv2.THRESH_BINARY)
cv2.imwrite("bw_image.jpg", im_bw)

# no_noise = noise_removal(im_bw)
# cv2.imwrite("no_noise.jpg", no_noise)
