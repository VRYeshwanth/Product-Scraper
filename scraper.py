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
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()

    product_data = []
    seen_asins = set()

    try:

        url = f"https://www.amazon.in/s?k={quote_plus(search_query)}"
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        for page in range(pages):

            print(f"Scraping page {page+1}")

            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
                )
            )

            # Scroll to load lazy products
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            products = driver.find_elements(
                By.CSS_SELECTOR,
                'div[data-component-type="s-search-result"]'
            )

            for product in products:

                try:

                    asin = product.get_attribute("data-asin")

                    if asin in seen_asins or asin == "":
                        continue

                    seen_asins.add(asin)

                    # Title
                    try:
                        title = product.find_element(By.CSS_SELECTOR, "h2 span").text.strip()
                    except:
                        title = "N/A"

                    # Price
                    try:
                        price = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text.strip()
                    except:
                        price = "N/A"

                    # Rating
                    try:
                        rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
                    except:
                        rating = "N/A"

                    # Product link
                    try:
                        link = product.find_element(By.CSS_SELECTOR, "h2 a").get_attribute("href")
                    except:
                        link = f"https://www.amazon.in/dp/{asin}"

                    product_data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Link": link
                    })

                except:
                    continue

            time.sleep(3)

            # Find next button
            try:

                next_button = driver.find_element(By.CSS_SELECTOR, ".s-pagination-next")

                # Stop if last page
                if "s-pagination-disabled" in next_button.get_attribute("class"):
                    print("Last page reached.")
                    break

                driver.execute_script("arguments[0].click();", next_button)

                time.sleep(3)

            except:
                print("Next button not found.")
                break

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
    product_name = input("Enter the product name : ")
    try:
        no_of_pages = int(input("Enter the number of pages to scrape : "))
        pages = no_of_pages if no_of_pages > 0 else 1
    except ValueError:
        print("Invalid input. Please enter a valid number of pages.")
        exit()
    

    results = scrape_amazon_selenium(product_name, pages=pages)
    save_to_csv(results, filename=f"{product_name.replace(' ', '_')}_amazon_products.csv")