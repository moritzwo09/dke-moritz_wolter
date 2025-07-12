#!/bin/bash

# Directory containing PDFs
PDF_DIR="pdf_dataset"

# Output directory for raw text files
TXT_DIR="txt_dataset"

# Create output directory if it doesn't exist
mkdir -p "$TXT_DIR"

# Loop through all PDFs in the directory
for pdf_file in "$PDF_DIR"/*.pdf; do
    # Get the base filename (without extension)
    filename=$(basename "$pdf_file" .pdf)

    # Extract raw text using pdftotext and save to .txt file
    echo "Extracting text from: $pdf_file"
    pdftotext "$pdf_file" "$TXT_DIR/$filename.txt"
done

echo "Done! Raw text files saved to: $TXT_DIR"