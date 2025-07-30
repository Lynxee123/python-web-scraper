import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/"

scrape = requests.get(URL)
soup = BeautifulSoup(scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})

for quote in quotes:
    print(quote.text)
