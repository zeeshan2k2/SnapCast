import subprocess
from datetime import datetime
import os

DESKTOP_PATH = "/Users/zeeshanwaheed/Desktop"


def take_screenshot():
    # create unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    filepath = os.path.join(DESKTOP_PATH, filename)

    try:
        subprocess.run(["screencapture", "-x", filepath], check=True)
        print(f"[Screenshot] Captured: {filepath}")
        return filepath

    except subprocess.CalledProcessError as e:
        print("[Screenshot] Screenshot failed:", e)
        return None


# test run
if __name__ == "__main__":
    take_screenshot()