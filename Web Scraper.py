import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print("\n Top News Headlines:\n")
    headlines = soup.find_all('h3')  # You can adjust based on site's structure

    count = 1
    for h in headlines[:10]:  # Print top 10 headlines
        text = h.get_text(strip=True)
        if text:
            print(f"{count}. {text}")
            count += 1

# Use any news site — here’s NDTV as an example:
news_url = 'https://www.ndtv.com/latest'
fetch_headlines(news_url)