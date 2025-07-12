# Extracting Body Text from ChemRxiv Preprints

by Moritz Wolter

---

This repository contains the code I used to write my paper. I just detail shortly how one can use the code


### Dependencies

All Dependencies can simply be installed using 

````
pip install -r requirements.txt
````

### Investigation

* I used the script `download papers` to download a set of 318 papers from ChemRxiv
* In `investigation.py` I experimented a bit with the dataset to see what the papers usually contain
* `pdf_to_text.sh` is the shell script I used to convert the PDF files into txt files

### PDFBoT

* PDF papers to be cleaned have to be in the folder `pdf_dataset`
* The Dockerfile I used to create the custom Docker image for the pdf2htmlEX utility can be foound in the folder PDFBoT/pdf2htmlEX-docker
* There is also the README from the project I used as inspiration
* Run the Flask App: `python main.py`
* Extraction script is: `output/extract.py`
* afterwards `output/clean.py` has to be executed to get rid of unnecessasary files created by PDFBoT

### Regex

* Papers to be cleaned have to be in the `txt_dataset` directory
* Clean the Papers: `python clean.py` inside the `regex_cleaning` directory

### Results

* Results regarding similarity can be viewed in the `similarity.ipynb` notebook
* further investigative results like section header counting can be found in the `investigation.ipynb` notebook 