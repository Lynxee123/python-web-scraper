# Import libraries for web scraping
#   1) requests > allows to pull a website
#   2) BeautifulSoup > parse html 
import requests
from bs4 import BeautifulSoup

# Define website to scrape
url = "https://thehackernews.com/"


#print(doc.find_all("span", class_={"h-tags"}))

# 
def scrapeArticles():
    # 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 
    articles=[]
    
    # 
    for post in soup.find_all("div", class_={"body-post"}):
        title = post.find("h2", class_="home-title").text
        date = post.find("span", class_="h-datetime")
        link = post.find("a", class_="story-link")
        summary = post.find("div", class_="home-desc").text
        tags = post.find("span", class_="h-tags")

        print("title: " + title + "\n" + "description:" + summary + "\n")

scrapeArticles()
# Prints response code
#print(requests.get(url))