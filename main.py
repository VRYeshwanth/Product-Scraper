import tkinter as tk
from tkinter import ttk, messagebox
import threading

# Import functions from scraper file
from scraper import scrape_amazon_selenium, save_to_csv


def start_scraping():

    product = product_entry.get().strip()
    pages = pages_entry.get().strip()

    if product == "":
        messagebox.showerror("Error", "Please enter a product name")
        return

    try:
        pages = int(pages)
        if pages <= 0:
            pages = 1
    except:
        messagebox.showerror("Error", "Pages must be a number")
        return

    status_label.config(text="Scraping started... Please wait")

    # Run scraper in separate thread so GUI doesn't freeze
    threading.Thread(target=run_scraper, args=(product, pages), daemon=True).start()


def run_scraper(product, pages):

    try:

        results = scrape_amazon_selenium(product, pages)

        filename = f"{product.replace(' ', '_')}_amazon_products.csv"
        save_to_csv(results, filename)

        status_label.config(
            text=f"Scraping finished! {len(results)} products saved."
        )

    except Exception as e:

        status_label.config(text="Error occurred")
        messagebox.showerror("Error", str(e))


# Main window
root = tk.Tk()
root.title("Amazon Product Scraper")
root.geometry("400x250")

# Title
title = tk.Label(
    root,
    text="Amazon Scraper",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Product input
product_label = tk.Label(root, text="Product Name")
product_label.pack()

product_entry = ttk.Entry(root, width=35)
product_entry.pack(pady=5)

# Pages input
pages_label = tk.Label(root, text="Number of Pages")
pages_label.pack()

pages_entry = ttk.Entry(root, width=10)
pages_entry.insert(0, "3")
pages_entry.pack(pady=5)

# Start button
scrape_button = ttk.Button(
    root,
    text="Start Scraping",
    command=start_scraping
)
scrape_button.pack(pady=15)

# Status
status_label = tk.Label(
    root,
    text="Waiting for input...",
    fg="blue"
)
status_label.pack()

root.mainloop()