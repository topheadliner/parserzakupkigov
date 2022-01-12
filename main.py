import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep

FILE_NAME = "test.csv"

data = []
for p in range(1, 5):
    print(p)
    url = f"https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=&morphology=on&search-filter=Дате+размещения&pageNumber={p}&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&savedSearchSettingsIdHidden=&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&placingWayList=&selectedLaws=&priceFromGeneral=&priceFromGWS=&priceFromUnitGWS=&priceToGeneral=&priceToGWS=&priceToUnitGWS=&currencyIdGeneral=-1&publishDateFrom=&publishDateTo=&applSubmissionCloseDateFrom=&applSubmissionCloseDateTo=&customerIdOrg=&customerFz94id=&customerTitle=&okpd2Ids=&okpd2IdsCodes=&gws="
    r = requests.get(url)
    soup = bs(r.text, 'lxml')
    cards = soup.findAll('div', class_="registry-entry__header-mid__number")

    for card in cards:
        link = card.find('a').get('href')
        data.append([link])

header = ['link']
df = pd.DataFrame(data, columns=header)
df.to_csv(FILE_NAME)