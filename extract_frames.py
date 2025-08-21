import cv2
import os

# Path to your video
video_path = "C:\\Users\\Akash Kalakonda\\Desktop\\video-text-extraction\\test video 1.mp4"  # Replace with your actual video file path

# Output folder for frames
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# Open the video
cap = cv2.VideoCapture(video_path)

frame_rate = 1 # Capture 2 frames per second
count = 0
frame_id = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Save every (FPS / frame_rate)th frame
    if int(cap.get(1)) % int(cap.get(cv2.CAP_PROP_FPS) / frame_rate) == 0:
        frame_filename = os.path.join(output_folder, f"frame_{frame_id:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_id += 1

    count += 1

cap.release()
print(f"Extracted {frame_id} frames to '{output_folder}' folder.")
