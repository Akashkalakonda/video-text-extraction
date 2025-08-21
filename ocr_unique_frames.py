import os
from PIL import Image
import pytesseract

# Tell pytesseract where tesseract.exe is
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\Akash Kalakonda\\Desktop\\video-text-extraction\\tesseract\\tesseract.exe" # repalce with your actual tessaract file path

frames_folder = "unique_frames"
output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as f_out:
    for frame_file in sorted(os.listdir(frames_folder)):
        frame_path = os.path.join(frames_folder, frame_file)

        # Open image and run OCR
        img = Image.open(frame_path)
        text = pytesseract.image_to_string(img, lang='eng')

        # Write to file
        f_out.write(f"\n--- Page: {frame_file} ---\n")
        f_out.write(text.strip())
        f_out.write("\n")

print(f"OCR complete. Results saved to '{output_file}'.")
