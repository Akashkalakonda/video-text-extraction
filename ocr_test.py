from PIL import Image
import pytesseract

# Point pytesseract to your local tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\Akash Kalakonda\Desktop\\video-text-extraction\\tesseract\\tesseract.exe"  #replace with your actual tessaract file path

# Load a test image (make sure it's in the same folder or give full path)
img_path = "C:\\Users\\Akash Kalakonda\\Desktop\\video-text-extraction\\test image 1.webp"  # Replace with an actual testing image file path
img = Image.open(img_path)

# Run OCR
text = pytesseract.image_to_string(img, lang='eng')

print("----- OCR OUTPUT -----")
print(text)
