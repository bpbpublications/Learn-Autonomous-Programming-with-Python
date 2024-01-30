import requests
from bs4 import BeautifulSoup
x = requests.get('https://toscrape.com/')
if x.status_code == 200:
    objSoup = BeautifulSoup(x.content, 'html.parser')
    tbl = objSoup.findAll('table')[1]
    tbltr = tbl.findAll('tr')
    i=0
    for element in tbltr:
        if not i==0:
            print(element.findAll('td')[0].text)
        i=+1
