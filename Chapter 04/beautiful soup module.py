import requests
from bs4 import BeautifulSoup

x = requests.get('https://toscrape.com/')
if x.status_code == 200: #A status of 200 is returned whenever a request is OK.A status of 404 means not found.
    objSoup = BeautifulSoup(x.content, 'html.parser')
    print(objSoup.title) #This would print the title tag
    print(objSoup.title.name) #This would print the name of the tag

