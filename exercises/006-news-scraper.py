import requests
from bs4 import BeautifulSoup
import sys


def scrape_news_headlines(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find and extract headlines (this may need to be adjusted based on the specific website structure)
        headlines = soup.find_all(
            "header", class_="ue-c-cover-content__headline-group"
        )  # Adjust the tag and class as needed

        # Print the headlines
        for headline in headlines:
            title = headline.text.strip()
            link = headline.find("a")["href"] if headline.find("a") else None
            print(f"Title: {title}")
            print(f"URL: {link}\n")

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    news_url = "https://www.elmundo.es/"  # Replace with the actual news website URL
    scrape_news_headlines(news_url)
