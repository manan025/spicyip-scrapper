import requests
from bs4 import BeautifulSoup

req = requests.get('https://spicyip.com/2024/07/yakshini-is-here-analysing-the-pocket-fm-v-novi-digital-judgement.html')
# print(req.text)
soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.prettify())
## print the class entry-header
print(soup.find_all("h1", class_='entry-title'))

# print(soup.p)

