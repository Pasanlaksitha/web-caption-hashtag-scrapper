import requests
from bs4 import BeautifulSoup
url = 'https://turbofuture.com/internet/Fashion-Quotes-and-Caption-Ideas/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

for tag in soup.find_all("li"):
    print(format(tag.text))