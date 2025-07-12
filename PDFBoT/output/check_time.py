import subprocess
import time
from pathlib import Path

# Configuration
BASE_URL = "http://127.0.0.1:5000/pdftotextAuto/auto/output"
INPUT_DIR = Path("../../data/chemrxiv_papers_pdf")
OUTPUT_DIR = Path("all_cleaned_papers")
DELAY_SECONDS = 3  # Delay between requests

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

start_time = time.time()
count = 0

for pdf_path in INPUT_DIR.glob('*.pdf'):
    output_file = OUTPUT_DIR / f"{pdf_path.stem}_cleaned_pdfbot.txt"
    
    print(f"Processing {pdf_path.name}...")
    
    curl_command = [
        'curl',
        '-s',
        f"{BASE_URL}/{pdf_path}",
        '-o', str(output_file)
    ]
    
    try:
        subprocess.run(curl_command, check=True)
        print(f"Saved to {output_file}, count: {count}")
        count += 1
    except subprocess.CalledProcessError as e:
        print(f"Failed to process {pdf_path.name}: {e}")
        if output_file.exists():
            output_file.unlink()
    except Exception as e:
        print(f"Error with {pdf_path.name}: {e}")
    
    print(f"Waiting {DELAY_SECONDS} seconds before next request...")
    time.sleep(DELAY_SECONDS)

end_time = time.time()
print(f"Time taken: {end_time - start_time:.2f} seconds for processing all PDFs")
print("Processing complete.")
