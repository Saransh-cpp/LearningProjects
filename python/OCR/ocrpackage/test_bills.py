import aiview_ocr

# help(aiview_ocr.OCR)
ocr = aiview_ocr.OCR(
    is_scanned=False,
    path="IMG_20210925_195026.jpg",
    tesseract_location=r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"
)

ocr.ocr()