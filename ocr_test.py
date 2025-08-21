# from PIL import Image
# import pytesseract

# # Windows users: uncomment if pytesseract can't find Tesseract automatically
# # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# img_path = "C:\\Users\\Akash Kalakonda\\Desktop\\video-text-extraction\\test image 1.webp"  # put your image file here
# img = Image.open(img_path)

# text = pytesseract.image_to_string(img, lang='eng')
# print("----- OCR OUTPUT -----")
# print(text)

from PIL import Image
import pytesseract

# Point pytesseract to your local tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\Akash Kalakonda\Desktop\\video-text-extraction\\tesseract\\tesseract.exe"

# Load a test image (make sure it's in the same folder or give full path)
img_path = "C:\\Users\\Akash Kalakonda\\Desktop\\video-text-extraction\\test image 1.webp"  # Replace with an actual image file path
img = Image.open(img_path)

# Run OCR
text = pytesseract.image_to_string(img, lang='eng')

print("----- OCR OUTPUT -----")
print(text)
