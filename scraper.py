# Import necessary libraries
import requests                 # For sending HTTP requests for websites
from bs4 import BeautifulSoup   # For parsing HTML content
import pandas as pd             # For handling data and exporting to CSV
import os                       # For interacting with the file system

# Define the URL of the website to scrape
url = "https://thehackernews.com/"

# Function that scrapes article data from the website
def scrapeArticles():
    # Send a GET request to the website and get HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Create an empty list to store article info
    articles=[]
    
    # Loop through each post block on the homepage
    for post in soup.find_all("div", class_={"body-post"}):
        # Extract article title and remove leading/trailing whitespace
        title = post.find("h2", class_="home-title").text.strip()
        # Extract publication date
        date = post.find("span", class_="h-datetime").text.strip()
        # Extract the URL link to the full article
        link = post.find("a", class_="story-link")['href']
        # Extract short summary
        summary = post.find("div", class_="home-desc").text.strip()
        # Extract category/topic > handle scenarios where tags are n/a
        tag_elements = post.find("span", class_="h-tags")
        if tag_elements:
            tags = [tag.text.strip() for tag in tag_elements]
        else:
            tags = ""

        # Append all extracted data as a dictionary to article list
        articles.append({
            "Title": title,
            "Date": date,
            "Link": link,
            "Summary": summary,
            "tags": tags
        })
        
    return articles

# Call the scraping function and store the results
scrapedData = scrapeArticles()

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(scrapedData)


# Ensure the 'output' directory exists before saving the file
os.makedirs("output", exist_ok=True)

# Save the DataFrame to a CSV file in the output folder
df.to_csv("output/scrapedData.csv", index=False)

# Hooray!
print("Saved CSV file!")

