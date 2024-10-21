from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
# fraction = soup.find(name="span", class_="a-price-fraction").getText()

if price >= "100":
    print("Buy!")
else:
    print("Not Yet")
