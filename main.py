import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading

from scraper import scrape_amazon_selenium, save_to_csv


def log(message):
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)
    root.update_idletasks()


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

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save Scraped Data",
        initialfile=f"{product.replace(' ', '_')}_amazon_products.csv"
    )

    if not file_path:
        return

    log_box.delete("1.0", tk.END)

    log("Starting scraper...")
    log(f"Product: {product}")
    log(f"Pages: {pages}")
    log("Launching browser...\n")

    threading.Thread(
        target=run_scraper,
        args=(product, pages, file_path),
        daemon=True
    ).start()


def run_scraper(product, pages, file_path):

    try:

        results = scrape_amazon_selenium(
            product,
            pages,
            log_callback=log
        )

        log("\nSaving data to CSV...")
        save_to_csv(results, file_path)

        log("File saved successfully.")
        log(f"Total products: {len(results)}")
        log("Scraping completed.")

    except Exception as e:

        log("Error occurred.")
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Amazon Product Scraper")
root.geometry("520x420")


title = tk.Label(
    root,
    text="Amazon Product Scraper",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)


tk.Label(root, text="Product Name").pack()
product_entry = ttk.Entry(root, width=40)
product_entry.pack(pady=5)


tk.Label(root, text="Number of Pages").pack()
pages_entry = ttk.Entry(root, width=10)
pages_entry.insert(0, "3")
pages_entry.pack(pady=5)


ttk.Button(
    root,
    text="Start Scraping",
    command=start_scraping
).pack(pady=10)


tk.Label(root, text="Live Log").pack()


log_box = tk.Text(
    root,
    height=15,
    width=65,
    bg="black",
    fg="lime",
    font=("Consolas", 9)
)
log_box.pack()


scrollbar = ttk.Scrollbar(root, command=log_box.yview)
scrollbar.pack(side="right", fill="y")

log_box.config(yscrollcommand=scrollbar.set)


root.mainloop()