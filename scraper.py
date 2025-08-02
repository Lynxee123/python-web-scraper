# Import libraries for web scraping
#   1) requests > allows to pull a website
#   2) BeautifulSoup > parse html 
import requests
from bs4 import BeautifulSoup
# import pandas as pd

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
        title = post.find("h2", class_="home-title").text.strip()
        
        date = post.find("span", class_="h-datetime").text.strip()
        link = post.find("a", class_="story-link")['href']
        summary = post.find("div", class_="home-desc").text.strip()
        tag_elements = post.find("span", class_="h-tags")
        if tag_elements:
            tags = [tag.text.strip() for tag in tag_elements]
        else:
            tags = ""

        articles.append({
            "Title": title,
            "Date": date,
            "Link": link,
            "Summary": summary,
            "tags": tags
        })
        
        
        print(articles)


scrapeArticles()


# Prints response code
#print(requests.get(url))