import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL and the page range
url = "http://books.toscrape.com/catalogue/page-{}.html"
startPage = 1
endPage = 5  # Change this to the number of pages you want to scrape
data = [] # list to store the extracted data

for page in range(startPage, endPage + 1): # Looping through each page
    print(f"Scraping page {page}...")
    req_response = requests.get(url.format(page)) # Request response
    soup = BeautifulSoup(req_response.text, 'html.parser')

# Data extraction from each book
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        bookTitle = book.find("h3").text.strip()
        bookPrice = book.find("p", class_='price_color').text.strip()
        bookRating = book.find("p", class_='star-rating').get('class')[1]
        bookAvailability = book.find("p", class_='availability').text.strip()
# Adding the extracted data to the list
        data.append({
            "Book Title": bookTitle,
            "Price": bookPrice,
            "Rating": bookRating,
            "Availability": bookAvailability
        })

    print(f"Page {page} scraped successfully!")
df = pd.DataFrame(data)
df.to_csv('book_data.csv', index=False, encoding='utf-8')
print("Data extraction complete!")
print("CSV file saved to book_data.csv")