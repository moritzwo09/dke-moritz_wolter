import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
DOWNLOAD_DIR = os.path.abspath("../chemrxiv_papers")
SEARCH_URL = "https://chemrxiv.org/engage/chemrxiv/search-dashboard?categories=605c72ef153207001f6470da&sortBy=PUBLISHED_DATE_DESC"

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1200,1000")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    })
    service = Service(executable_path="/opt/homebrew/bin/chromedriver")
    return webdriver.Chrome(service=service, options=chrome_options)

def scroll_to_bottom(driver):
    """Scroll to bottom to load more papers"""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for loading
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def download_all_papers(driver):
    driver.get(SEARCH_URL)
    time.sleep(3)
    
    # Scroll to load ALL papers
    scroll_to_bottom(driver)
    
    papers = driver.find_elements(By.CSS_SELECTOR, "div.MatchResult")
    print(f"Found {len(papers)} papers total")
    
    for i, paper in enumerate(papers, 1):
        try:
            title = paper.find_element(By.CSS_SELECTOR, "span[data-v-6b49c87c]").text
            print(f"\nProcessing {i}/{len(papers)}: {title[:50]}...")
            
            download_btn = paper.find_element(
                By.XPATH, ".//button[contains(@aria-label, 'Download')]"
            )
            
            # Scroll and click with JavaScript
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", download_btn)
            driver.execute_script("arguments[0].click();", download_btn)
            time.sleep(2)  # Wait for download
            
        except Exception as e:
            print(f"Error on paper {i}: {str(e)}")

def main():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    driver = setup_driver()
    try:
        download_all_papers(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()