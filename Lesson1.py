from urllib import response
#pip install requests
import requests
#pip install bs4
from bs4 import BeautifulSoup

url_requests = "http://books.toscrape.com/"

response = requests.get(url_requests)
# print(response.text)

html = response.text

soup = BeautifulSoup(html, "html.parser")

soup.find_all("img")

print(soup.find_all("img"))

links = soup.find_all("img")
for link in links:
    print(url_requests + link.get("src"))