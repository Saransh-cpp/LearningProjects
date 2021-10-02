import aiview_ocr
import easyocr
import cv2

# print(help(aiview_ocr.OCR))

ocr = aiview_ocr.OCR(
    True, # is_scanned
    "roof-500x500.jpg", # path
)
print(ocr.ocr_sign_board())

# languages = ['en', 'hi']
# path = "roof-500x500.jpg"
# ft = ""

# img = cv2.imread(path)
# reader = easyocr.Reader(
#     languages
# )  # slow for the first time (also depends upon CPU/GPU)
# result = reader.readtext(path)

# for text in result:

#     # extracting the coordinates to highlight the text
#     coords_lower = text[0][:2]
#     coords_upper = text[0][2:4]

#     coords_lower.sort(key=lambda x: x[0])
#     pt1 = [int(x) for x in coords_upper[-1]]

#     coords_lower.sort(key=lambda x: x[0])
#     pt2 = [int(x) for x in coords_lower[-1]]

#     cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)

#     ft = ft + " " + text[-2]

# cv2.imwrite("OCR.png", img)

# print(ft)


