# Video Text Extraction

This project extracts text from videos by breaking them into frames, filtering unique frames, and applying Optical Character Recognition (OCR). It’s useful for analyzing lecture videos, extracting subtitles from recordings, or any case where you need text hidden inside a video.

## 🚀 Features

Extracts frames from a video file.

Filters unique frames to avoid duplicate text extraction.

Performs OCR (Optical Character Recognition) using Tesseract.

Saves extracted text into an output file.

Lightweight and modular Python scripts.

## 🛠️ Technologies Used

Python 3.8+

OpenCV → for frame extraction.

ImageHash / PIL → for detecting unique frames.

Tesseract OCR → for text extraction.

pytesseract → Python wrapper for Tesseract.

## 📂 Project Structure
video-text-extraction/
│
├── extract_frames.py         # Extracts frames from input video
├── filter_unique_frames.py   # Filters unique frames from extracted frames
├── ocr_test.py               # Tests OCR on a single frame
├── ocr_unique_frames.py      # Runs OCR on unique frames
├── .gitignore                # Git ignore file
│
├── frames/                   # Stores all extracted frames
├── unique_frames/            # Stores unique frames only
├── output.txt                # Final text extracted from video

Folder & File Explanation

frames/ → Created after running extract_frames.py. Contains all frames extracted from the video (might include duplicates).

unique_frames/ → Created after running filter_unique_frames.py. Contains only distinct frames (removes near-duplicates).

output.txt → Generated after running ocr_unique_frames.py. Contains all recognized text from the video.

## ⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/<your-username>/video-text-extraction.git
cd video-text-extraction

2. Create Virtual Environment (Recommended)
python -m venv video-text-venv
source video-text-venv/bin/activate   # Linux/Mac
video-text-venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Install Tesseract OCR

Windows: Download installer → Tesseract at UB Mannheim

⚠️ After installation, make sure Tesseract is added to your PATH. Example for Windows:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

## ▶️ How to Run
Step 1: Extract Frames from Video
python extract_frames.py --input video.mp4 --output frames/

Step 2: Filter Unique Frames
python filter_unique_frames.py --input frames/ --output unique_frames/

Step 3: Run OCR on Unique Frames
python ocr_unique_frames.py --input unique_frames/ --output output.txt

Step 4: View Extracted Text

Open output.txt to see the extracted text.

## 📝 Example Workflow

Place your video (video.mp4) inside the project folder.

Run scripts in the above order.

You’ll get:

frames/ → individual frames from video.

unique_frames/ → smaller set of meaningful frames.

output.txt → extracted subtitles/text.

## 📌 Future Improvements

Improve OCR accuracy with preprocessing (grayscale, thresholding).

Add support for multi-language OCR.

Automate entire pipeline with a single script.

Export text in structured formats (CSV, JSON).
