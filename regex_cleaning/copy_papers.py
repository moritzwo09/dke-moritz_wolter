from pathlib import Path
import shutil

SOURCE_DIR = Path("../data/chemrxiv_papers_txt")
DEST_DIR = Path("ground_truth")
DEST_DIR.mkdir(exist_ok=True) 

# Get first 5 .txt files and copy them
for file in sorted(SOURCE_DIR.glob("*.txt"))[:5]:
    shutil.copy(file, DEST_DIR / file.name)
