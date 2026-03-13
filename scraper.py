# Selenium implementation for scraping Amazon
import csv
import time
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_amazon_selenium(search_query, pages=5):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment to run without a browser window
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    product_data = []

    try:
        for page in range(1, pages + 1):
            url = f"https://www.amazon.in/s?k={quote_plus(search_query)}&page={page}"
            print(f"Scraping page {page}...")
            driver.get(url)
            
            # Wait for products to load
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')))

            products = driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')

            for product in products:
                try:
                    # Title
                    try:
                        title_elem = product.find_element(By.CSS_SELECTOR, "h2 span")
                        title = title_elem.text.strip()
                    except:
                        title = "N/A"

                    # Price
                    try:
                        price_elem = product.find_element(By.CSS_SELECTOR, ".a-price-whole")
                        price = price_elem.text.strip()
                    except:
                        price = "N/A"

                    # Rating
                    try:
                        rating_elem = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt")
                        rating = rating_elem.get_attribute("innerHTML")
                    except:
                        rating = "N/A"

                    # Link
                    try:
                        link = product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                    except:
                        try:
                            asin = product.get_attribute("data-asin")
                            link = f"https://www.amazon.in/dp/{asin}"
                        except:
                            link = "N/A"

                    product_data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Link": link
                    })
                except Exception as e:
                    continue
            time.sleep(2)
    finally:
        driver.quit()
    return product_data

def save_to_csv(data, filename="amazon_products.csv"):
    if not data:
        print("No product data parsed.")
        return
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully saved {len(data)} items to '{filename}'.")

if __name__ == "__main__":
    results = scrape_amazon_selenium("wall clocks", pages=5)
    save_to_csv(results)