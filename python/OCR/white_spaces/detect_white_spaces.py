import cv2

image = cv2.imread("Page.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
dilated = cv2.dilate(thresh, kernel, iterations=13)  # dilate
contours, hierarchy = cv2.findContours(
    dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
)  # get contours


idx = 0
# for each contour found, draw a rectangle around it on original image
for contour in contours:

    idx += 1

    # get rectangle bounding contour
    [x, y, w, h] = cv2.boundingRect(contour)

    # discard areas that are too large
    if h > 300 and w > 300:
        continue

    # discard areas that are too small
    if h < 40 or w < 40:
        continue

    # draw rectangle around contour on original image
    # cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)

    roi = image[y : y + h, x : x + w]

    cv2.imwrite(str(idx) + ".jpg", roi)

    cv2.imshow("img", roi)
    cv2.waitKey(0)
