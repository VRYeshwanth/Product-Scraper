import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_amazon(search_query, pages=5):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.5"
    }
    
    product_data = []
    
    for page in range(1, pages + 1):
        url = f"https://www.amazon.in/s?k={search_query}&page={page}"
        print(f"Scraping page {page}...")
        
        try:
            response = requests.get(url, headers=headers)
            
            soup = BeautifulSoup(response.content, "html.parser")
            
            products = soup.find_all("div", {"data-component-type": "s-search-result"})
            
            for product in products:
                title_elem = product.find("span", {"class": "a-size-medium a-color-base a-text-normal"}) or \
                             product.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
                title = title_elem.text.strip() if title_elem else "N/A"
                
                price_elem = product.find("span", {"class": "a-price-whole"})
                price = price_elem.text.strip() if price_elem else "N/A"
                
                rating_elem = product.find("span", {"class": "a-icon-alt"})
                rating = rating_elem.text.strip() if rating_elem else "N/A"
                
                link_elem = product.find("a", {"class": "a-link-normal s-no-outline"})
                if not link_elem:
                    link_elem = product.find("a", {"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
                link = "https://www.amazon.in" + link_elem["href"] if link_elem and "href" in link_elem.attrs else "N/A"
                
                product_data.append({
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Link": link
                })
                
        except Exception as e:
            print(f"Error on page {page}: {e}")
            
        time.sleep(2)
        
    return product_data

def save_to_csv(data, filename="amazon_products.csv"):
    if not data:
        print("No product data parsed. Exiting without creating CSV.")
        return
        
    keys = data[0].keys()
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Successfully scraped {len(data)} items and saved to '{filename}'.")

if __name__ == "__main__":
    query = "belts"
    print(f"Initiating Amazon.in scrape for '{query}'...")
    
    results = scrape_amazon(query, pages=5)
    
    save_to_csv(results)