import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

quotes = soup.find_all("div", class_="quote")

print("***Quotes***")
for quote in quotes:
    text_element = quote.find("span", class_="text")
    author_element = quote.find("small", class_="author")

    print("Quote:", text_element.text.strip())
    print("Author:", author_element.text.strip())
    print()

print("***END***")