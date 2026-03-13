# Amazon Product Scraper using Selenium

This project is a **Python-based Amazon product scraper** that collects product information from Amazon search results and saves it to a CSV file.

The scraper extracts:

- Product Title
- Price
- Rating
- Product Link

The script can scrape multiple pages of Amazon search results automatically.

---

# Project Structure

```
Product-Scraper/
├── README.md
├── requirements.txt
└── scraper.py

```

- **scraper.py** → Main Python script for scraping Amazon
- **requirements.txt** → Python dependencies
- **README.md** → Project documentation

---

# Creating a Virtual Environment (venv)

Using a virtual environment keeps project dependencies isolated from your system Python.

## 1. Create a Virtual Environment

Run the following command inside the project folder:

```bash
python -m venv venv
```

This will create a folder named:

```
venv/
```

---

## 2. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

Once activated, the terminal will show:

```
(venv) your-path>
```

---

# Installing Dependencies

Install required packages using:

```bash
pip install -r requirements.txt
```

---

# Running the Scraper

Run the script using:

```bash
python scraper.py
```

You will be asked for:

```
Enter the product name :
Enter the number of pages to scrape :
```

Example:

```
Enter the product name : laptop
Enter the number of pages to scrape : 5
```

---

# Output

The program generates a CSV file containing scraped products.

Example output file:

```
laptop_amazon_products.csv
```

---

# Notes

- Amazon pages load dynamically, which is why Selenium is used instead of simple HTTP requests.
- If scraping fails due to blocking, increase the delay between requests.
- The scraper may stop working if Amazon changes its page structure.

---

# Deactivating the Virtual Environment

After finishing the work, deactivate the environment:

```bash
deactivate
```

---

# Disclaimer

This project is created for **educational purposes only**.  
Always follow the website's terms of service before scraping.
