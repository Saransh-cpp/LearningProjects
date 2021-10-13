import aiview_ocr


ocr = aiview_ocr.OCR(
    True,
    # "bills/1174-receipt.jpg",
    # "bills/1166-receipt.jpg",
    # "bills/1000-receipt.jpg",
    # "bills/1178-receipt.jpg",
    # "bills/1146-receipt.jpg",
    # "bills/1132-receipt.jpg",
    "Screenshot 2021-10-09 112620.png"
    # r"D:\Saransh\Softwares\Tesseract-OCR\tesseract.exe"
)

text = ocr.ocr_sparse_text()

print(text)

# print(ocr.process_extracted_text_from_invoice())
