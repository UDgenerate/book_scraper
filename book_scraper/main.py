import requests
from bs4 import BeautifulSoup

def books_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://books.toscrape.com/catalogue/category/books_1/page-' + str(page) + '.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll(lambda tag: len(tag.name) == 1 and len(tag.attrs) == 2):
            href = "http://books.toscrape.com/catalogue"  + link.get('href')[5:]
            title = link.get('title')
            print(title)
            print(href)
        page += 1

books_spider(1)

