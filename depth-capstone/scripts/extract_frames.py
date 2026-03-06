import cv2
import os
from pathlib import Path
from tqdm import tqdm

PROJECT_ROOT = Path("/blue/egn6933/mulakav/depth-capstone")
VIDEO_PATH = PROJECT_ROOT / "data/raw_videos/video.mp4"   # rename video.mp4 if needed
OUTPUT_DIR = PROJECT_ROOT / "data/frames"

FRAME_INTERVAL = 1  # 1=every frame, 10=every 10th frame, etc.

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

cap = cv2.VideoCapture(str(VIDEO_PATH))
if not cap.isOpened():
    raise FileNotFoundError(f"Could not open video: {VIDEO_PATH}")

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
saved = 0
idx = 0

with tqdm(total=total_frames, desc="Extracting frames") as pbar:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if idx % FRAME_INTERVAL == 0:
            out_path = OUTPUT_DIR / f"frame_{saved:06d}.jpg"
            cv2.imwrite(str(out_path), frame)
            saved += 1

        idx += 1
        pbar.update(1)

cap.release()
print(f" Saved {saved} frames to: {OUTPUT_DIR}")

