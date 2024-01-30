#run each of these pieces separately

#conventional method
import requests
from bs4 import BeautifulSoup
x = requests.get('https://toscrape.com/')
if x.status_code == 200:
      objSoup = BeautifulSoup(x.content, 'html.parser')
      print(objSoup.find('div',class_="container") \
      .findAll('div',class_="row")[2] \
      .find('div',class_="col-md-10") \
      .findAll('div',class_="col-md-6")[1] \
      .find('table',class_="table table-hover" \
            ).findAll('tr')[1].findAll('td')[1].text)

    
    

#faster method
import requests
from bs4 import BeautifulSoup
x = requests.get('https://toscrape.com/')
if x.status_code == 200:
      objSoup = BeautifulSoup(x.content, 'html.parser')
      print(objSoup.findAll('table')[1].findAll('tr')[1].findAll('td')[1].text)
