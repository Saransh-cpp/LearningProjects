import aiview_ocr
import easyocr
reader = easyocr.Reader(['en', 'hi']) # this needs to run only once to load the model into memory
result = reader.readtext('roof-500x500.jpg')

print(result)
for _ in result:

    print(_[1])

