import cv2
import os
from skimage.metrics import structural_similarity as ssim

frames_folder = "frames"
unique_folder = "unique_frames"
os.makedirs(unique_folder, exist_ok=True)

frame_files = sorted(os.listdir(frames_folder))

prev_frame = None
unique_count = 0
threshold = 0.80  # Lower threshold for page change detection

for frame_file in frame_files:
    frame_path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)

    # Resize to speed up comparison & reduce small differences
    frame_small = cv2.resize(frame, (500, 500))

    if prev_frame is None:
        cv2.imwrite(os.path.join(unique_folder, frame_file), frame)
        prev_frame = frame_small
        unique_count += 1
    else:
        score, _ = ssim(prev_frame, frame_small, full=True)
        if score < threshold:
            cv2.imwrite(os.path.join(unique_folder, frame_file), frame)
            prev_frame = frame_small
            unique_count += 1

print(f"Filtered {unique_count} unique frames into '{unique_folder}'.")
