import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

base_url = "https://books.toscrape.com/catalogue/"
page_url = "https://books.toscrape.com/catalogue/page-1.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

books = []

for page in range(1, 6):  # On scrape 5 pages (100 livres)
    print(f"Scraping page {page}...")

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select("article.product_pod")

    for item in items:
        title = item.h3.a["title"]
        price = item.select_one(".price_color").text.strip()
        availability = item.select_one(".availability").text.strip()
        rating = item.p["class"][1]  # ex: "One", "Two"
        product_url = base_url + item.h3.a["href"]

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "product_url": product_url
        })

    # Pause aléatoire pour respecter le scraping éthique
    time.sleep(random.uniform(1.1, 2.6))

df = pd.DataFrame(books)
df.to_csv("books_dataset.csv", index=False)

print("Scraping terminé ! Fichier créé : books_dataset.csv")

