import time
import subprocess
import cv2
import numpy as np
from pathlib import Path
from datetime import datetime

SNAPSHOT_DIR = Path.home() / "aiuto_cam" / "snapshots"
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

LOW_RES_FILE = "/tmp/lowres.jpg"

THRESH_DIFF = 12      # sensibilità (più alto = meno sensibile)
MIN_PIXELS = 5000     # quantità di pixel cambiati
COOLDOWN = 20         # secondi tra snapshot HD

last_hd = 0
prev_gray = None

def capture_lowres():
    subprocess.run([
        "rpicam-still",
        "--nopreview",
        "--timeout", "1",
        "--width", "320",
        "--height", "240",
        "-o", LOW_RES_FILE
    ], check=True)

def capture_hd():
    filename = SNAPSHOT_DIR / f"snap_{datetime.now():%Y%m%d_%H%M%S}.jpg"
    subprocess.run([
        "rpicam-still",
        "--nopreview",
        "--timeout", "1",
        "--width", "1280",
        "--height", "720",
        "-o", str(filename)
    ], check=True)
    print("📸 HD Snapshot:", filename)

print("🟢 Diff-based motion detection started")

while True:
    capture_lowres()

    img = cv2.imread(LOW_RES_FILE, cv2.IMREAD_GRAYSCALE)
    if img is None:
        time.sleep(1)
        continue

    img = cv2.GaussianBlur(img, (9, 9), 0)

    if prev_gray is None:
        prev_gray = img
        time.sleep(1)
        continue

    diff = cv2.absdiff(prev_gray, img)
    _, thresh = cv2.threshold(diff, THRESH_DIFF, 255, cv2.THRESH_BINARY)
    changed = cv2.countNonZero(thresh)

    now = time.time()
    if changed > MIN_PIXELS and (now - last_hd) > COOLDOWN:
        capture_hd()
        last_hd = now

    prev_gray = img
    time.sleep(1)
