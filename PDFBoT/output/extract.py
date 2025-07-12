import os
import subprocess
import re
import time  # Added for sleep functionality
from pathlib import Path

# Configuration
BASE_URL = "http://127.0.0.1:5000/pdftotextAuto/auto/output"
INPUT_DIR = Path("pdf_dataset")  # Using Path object
OUTPUT_DIR = Path("extracted_texts")
DELAY_SECONDS = 1  # Delay between requests

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

s = time.time()

# Process each PDF file
for pdf_path in INPUT_DIR.glob('*.pdf'):
    # Extract the number X from X_original.pdf filename
    match = re.match(r'^(\d+)_original\.pdf$', pdf_path.name, re.IGNORECASE)
    if not match:
        print(f"Skipping {pdf_path.name} - doesn't match expected pattern")
        continue
        
    file_number = match.group(1)
    output_file = OUTPUT_DIR / f"{file_number}_cleaned_pdfbot.txt"
    
    print(f"Processing {pdf_path}...")
    
    # Construct curl command with full path (converted to string for subprocess)
    curl_command = [
        'curl',
        '-s',  # Silent mode
        f"{BASE_URL}/{pdf_path}",
        '-o', str(output_file)
    ]
    
    # Execute curl
    try:
        subprocess.run(curl_command, check=True)
        print(f"Saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to process {pdf_path}: {e}")
        # Clean up failed output file if it was created
        if output_file.exists():
            output_file.unlink()
    except Exception as e:
        print(f"Error with {pdf_path}: {str(e)}")
    
    # Add delay after each request
    print(f"Waiting {DELAY_SECONDS} seconds before next request...")
    time.sleep(DELAY_SECONDS)


e = time.time()
print(f"Total processing time: {e - s:.2f} seconds")
print("Processing complete.")