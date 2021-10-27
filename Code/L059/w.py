import requests
from bs4 import BeautifulSoup
html = requests.get('http://localhost:8080/animals.txt')
soup = BeautifulSoup(html.text)
print(soup.prettify())