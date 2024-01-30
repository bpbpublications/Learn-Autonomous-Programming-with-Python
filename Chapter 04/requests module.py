import requests

x = requests.get('https://toscrape.com/')
if x.status_code == 200:  #A status of 200 is returned whenever a request is OK.A status of 404 means not found.
    print(x.text)
