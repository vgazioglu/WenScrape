import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, "html.parser")

#print(soup.prettify())
xxx=list(soup.children)
for i in xxx:
    print(i , "\t" , type(i))
print(len(xxx))