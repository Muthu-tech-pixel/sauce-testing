from pathlib import Path
from datetime import datetime

def save_failure_screenshot(page, nodeid: str, output_dir="screenshots"):
    folder = Path(output_dir)
    folder.mkdir(parents=True, exist_ok=True)
    safe_name = "".join(c if c.isalnum() or c in "-_" else "_" for c in nodeid)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = folder / f"{safe_name}_{stamp}.png"
    page.screenshot(path=str(path), full_page=True)
    return path
