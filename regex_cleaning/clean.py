import re
from pathlib import Path
import time

DATA_DIR = Path("txt_dataset")
OUTPUT_DIR = Path("cleaned_papers")
OUTPUT_DIR.mkdir(exist_ok=True)

def clean_paper(prefix, paper, output_dir):
    with open(paper, "r") as file:
        content = file.read()

    normalized_content = content.replace('\f', '\n')

   # Remove everything after "Supporting Information", "Symbols and Notations, data availability", or "Conflicts of Interest"
    cleaned = re.split(
    r'(?i)(?<=\n\n)\s*(supporting information|symbols and notations|data availability|conflicts? of interest)(?!\))\s*:?.*$',
    normalized_content,
    maxsplit=1,
    flags=re.MULTILINE
    )[0]


    # For Acknowledgements
    cleaned = re.split(r'(?i)^\s*Acknowledg?ments?\s*:.*$', cleaned, maxsplit=1, flags=re.MULTILINE)[0]

    # Remove from "References" onward
    cleaned = re.split(r'(?i)^\s*References\b.*$', cleaned, maxsplit=1, flags=re.MULTILINE)[0]

    # Remove everything before abstract
    cleaned = re.sub(r'^.*?\bAbstract\b:?\s*\n', '', cleaned, flags=re.DOTALL | re.IGNORECASE)

    # Remove URLs and ChemRxiv links
    cleaned = re.sub(r'^.*(?:https://|ChemRxiv).*\n?', '', cleaned, flags=re.MULTILINE | re.IGNORECASE)

    # Remove email addresses
    cleaned = re.sub(r'^[^\n]*\b[\w\.-]+@[\w\.-]+\.\w+\b[^\n]*\n?', '', cleaned, flags=re.MULTILINE)

    # Remove standalone page numbers
    cleaned = re.sub(r'^\s*\d{1,3}\s*$\n?', '', cleaned, flags=re.MULTILINE)

    # Remove figure captions starting with "Figure" or "FIG"
    cleaned = re.sub(r'^(?:Figure|FIG|Fig\.)\s*\d+\..*?(?:\n\s*\n)', '', cleaned, flags=re.DOTALL | re.MULTILINE)

    # Remove Schemes and Tables (Captions))
    cleaned = re.sub(r'^(Scheme|Table)\b.*\n?', '', cleaned, flags=re.MULTILINE | re.IGNORECASE)

    # Remove standalone "Tel" or "Fax" lines
    cleaned = re.sub(r'^(Tel|Fax)\b.*\n?', '', cleaned, flags=re.MULTILINE | re.IGNORECASE)

    # Remove standalone numbers, single letters, or words at the start of lines
    cleaned = re.sub(r'^\s*([A-Za-z]{1}|[A-Za-z]+|\d+(\.\d+)?|\.\d+)\s*\n', '', cleaned, flags=re.MULTILINE)


    # Save to cleaned_papers directory
    out = prefix + "_cleaned.txt"
    output_path = output_dir / out
    with open(output_path, "w") as file:
        file.write(cleaned)

# Get the first 5 .txt files in the DATA_DIR
txt_files = sorted(DATA_DIR.glob("*.txt"))

s = time.time()
c = 0
# Apply cleaning to each paper
for paper in txt_files:
    prefix = paper.stem.split('_')[0] 
    clean_paper(prefix, paper, OUTPUT_DIR)
    c+=1
e = time.time()
print(f"Time taken: {e - s:.2f} seconds for {c} papers.")
