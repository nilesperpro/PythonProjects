import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup

# need to setup and test login from within python to see if Cookie is returned
loginUrl = "https://api.eliteguardtraining.com/auth/login"
creds = {"username":"wotesab628@wmail1.com","password":"password"}

response = requests.post(loginUrl, data=creds)
text = response.text
html = BeautifulSoup(text, 'html.parser')
print(text)
