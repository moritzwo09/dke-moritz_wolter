from pathlib import Path

DATA_DIR = Path("../data/chemrxiv_papers_txt") 


def count_empty_files(DATA_DIR):
    empty_count = 0
    for paper in Path(DATA_DIR).iterdir():
        if paper.is_file():
            if paper.stat().st_size <= 5:
                empty_count += 1
    print(f"Number of empty text files: {empty_count}")
    return empty_count


def count_files(DATA_DIR):
    count = 0
    for paper in Path(DATA_DIR).iterdir():
        if paper.is_file():
            count += 1
    return count


def get_section_percentage(DATA_DIR, section):
    count = 0
    for paper in Path(DATA_DIR).iterdir():
        with open(paper, "r", encoding="utf-8") as f:
            # write refgular expression to find abstract and count it
            content = f.read()
            if section in content.lower():
                count += 1
    num_files = count_files(DATA_DIR)
    percentage = count / num_files * 100 if num_files > 0 else 0
    print(f"Total number of files: {num_files}")
    print(f"Number of papers with abstracts: {count}")
    return percentage



abstract_percentage = get_section_percentage(DATA_DIR, "abstract")
print(f"Percentage of papers with abstracts: {abstract_percentage:.2f}%")
print("--------------------------------------------------"*2)

references_percentage = get_section_percentage(DATA_DIR, "references")
print(f"Percentage of papers with references: {references_percentage:.2f}%")
print("--------------------------------------------------"*2)

introduction_percentage = get_section_percentage(DATA_DIR, "introduction")
print(f"Percentage of papers with introductions: {introduction_percentage:.2f}%")
print("--------------------------------------------------"*2)

acknowledgements_percentage = get_section_percentage(DATA_DIR, "acknowledgements")
print(f"Percentage of papers with acknowledgements: {acknowledgements_percentage:.2f}%")
print("--------------------------------------------------"*2)
count_empty_files(DATA_DIR)






