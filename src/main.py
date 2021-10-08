import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        pass

    def get(self, currency_name):
        page = requests.get(
            "https://google.com/search?q=site%3Acoinmarketcap.com+" + currency_name + "&ie=utf-8&oe=utf-8")
        soup = BeautifulSoup(page.content, 'html.parser')
        r = soup.find_all("h3")
        return r


scrapper = Scrapper()
list = scrapper.get("bitcoin")

for el in list:
    print(el.find("div").get_text())
