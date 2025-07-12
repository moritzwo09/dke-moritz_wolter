# clear tempOutput directory entirely
import os
import shutil
from pathlib import Path
import re


path = Path("pdf_dataset")  # Directory to clear

for item in path.iterdir():
    if item.is_file():
        # remove if the file ends with unlocked.pdf
        if item.name.endswith("unlocked.pdf"):
            item.unlink()  # Remove the file
    elif item.is_dir():
        shutil.rmtree(item)  # Remove the directory and its contents
import os
from pathlib import Path

def remove_empty_lines_between(text):
    """Removes extra empty lines between content while preserving single empty lines."""
    lines = text.splitlines()
    cleaned_lines = []
    
    for i, line in enumerate(lines):
        if line.strip():  # Keep non-empty lines
            cleaned_lines.append(line)
        elif (i > 0 and i < len(lines)-1 and 
              not lines[i-1].strip() and not lines[i+1].strip()):  # Preserve single empty lines
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

# Directory containing text files
input_dir = Path("extracted_texts_2")

# Process each .txt file
for txt_file in input_dir.glob("*.txt"):
    print(f"Processing: {txt_file.name}")
    
    # Read file
    with open(txt_file, 'r', encoding='utf-8') as f:
        original_text = f.read()
    
    # Clean text
    cleaned_text = remove_empty_lines_between(original_text)
    
    # Overwrite file
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)

print("All files processed!")