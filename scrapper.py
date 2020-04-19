# scrapper untuk projects.co.id

from requests import get
from bs4 import BeautifulSoup

url = "https://projects.co.id/public/browse_projects/listing?search=Web+Scrapping"
webpage = get(url)
soup = BeautifulSoup(webpage.text)
for row in soup.find_all("div", {"class": "col-md-10 align-left"}):
    res = row.find_all("div", {"class": "col-md-6 align-left"})[0]
    print(res.text)
    print()
