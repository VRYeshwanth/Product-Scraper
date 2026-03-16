# Amazon Product Scraper using Selenium

This project is a **Python-based Amazon product scraper with a Tkinter GUI**.  
It allows users to search for products on Amazon and automatically extract product data from multiple pages of search results.

The scraped data is saved into a **CSV file** for easy analysis.

---

# Features

- Scrapes Amazon search results automatically
- Extracts the following product details:
    - Product Title
    - Price
    - Rating
    - Product Link
- Allows scraping **multiple pages**
- **Simple Tkinter GUI** for user interaction
- Saves results to a **CSV file**

---

# Project Structure

```
Directory structure:
└── Product-Scraper/
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── scraper.py
```

**File descriptions**

- **scraper.py** → Program containing the Selenium scraper
- **main.py** → Main program containing the Tkinter GUI
- **requirements.txt** → Python libraries required for the project
- **README.md** → Project documentation

---

# Prerequisites

- Python 3.8 or higher
- Google Chrome

# 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Product-Scraper.git
cd Product-Scraper
```

---

# 2. Create a Virtual Environment

Using a virtual environment keeps project dependencies isolated from the system Python.

Run the following command inside the project directory:

```bash
python -m venv venv
```

This will create a folder:

```
venv/
```

---

# 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

Once activated, the terminal should display something similar to:

```
(venv) your-path>
```

---

# 4. Install Required Libraries

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

This will install all dependencies required for the scraper.

---

# 5. Setting Up Chrome WebDriver

Selenium requires **ChromeDriver** to control the Chrome browser.

## Step 1: Check Your Chrome Version

Open Chrome and navigate to:

```
chrome://settings/help
```

Note the Chrome version installed on your system.

---

## Step 2: Download ChromeDriver

Download the matching ChromeDriver version from:

https://chromedriver.chromium.org/downloads

---

## Step 3: Extract ChromeDriver

After downloading:

- Extract the ZIP file
- You will get the executable:

```
chromedriver.exe
```

---

## Step 4: Place ChromeDriver

Add ChromeDriver to your **system PATH**.

---

# 6. Running the Program

Run the scraper using:

```bash
python main.py
```

This will open the **Tkinter GUI application**.

---

# Output

The program generates a CSV file containing the scraped product information.

Example output file:

```
laptop_amazon_products.csv
```

Example contents of the CSV file:

| Title               | Price   | Rating | Link                  |
| ------------------- | ------- | ------ | --------------------- |
| HP Laptop 15s       | ₹45,990 | 4.2    | https://amazon.in/... |
| Lenovo IdeaPad Slim | ₹52,990 | 4.1    | https://amazon.in/... |

---

# Deactivating the Virtual Environment

After finishing your work, deactivate the environment:

```bash
deactivate
```

---

# Notes

- Amazon pages load **dynamic content**, which is why **Selenium** is used instead of simple HTTP requests.
- Scraping too quickly may result in temporary blocking.
- If the scraper stops working, Amazon may have **changed their page structure**.

---

# Disclaimer

This project is created for **educational purposes only**.

Always follow the **terms of service of the website** before scraping.
