import cv2
import os
import shutil
from pathlib import Path
from tqdm import tqdm

PROJECT_ROOT = Path("/blue/egn6933/mulakav/depth-capstone")
INPUT_DIR = PROJECT_ROOT / "data/frames"
OUTPUT_DIR = PROJECT_ROOT / "data/filtered_frames"
BLUR_THRESHOLD = 100.0  # adjust if too strict/loose

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def blur_score(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

kept, dropped = 0, 0
images = sorted([p for p in INPUT_DIR.iterdir() if p.suffix.lower() in [".jpg", ".png", ".jpeg"]])

for img_path in tqdm(images, desc="Filtering blur"):
    img = cv2.imread(str(img_path))
    if img is None:
        dropped += 1
        continue

    score = blur_score(img)
    if score >= BLUR_THRESHOLD:
        shutil.copy(str(img_path), str(OUTPUT_DIR / img_path.name))
        kept += 1
    else:
        dropped += 1

print(f" Kept {kept} frames, dropped {dropped}. Output: {OUTPUT_DIR}")
