import requests
from lxml.html import fromstring
from bs4 import BeautifulSoup
import ast
from itertools import cycle
import traceback
import random
import os
import time



voteHead = [{ "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0", \
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
                "Accept-Language": "en-US,en;q=0.5",\
                "Accept-Encoding": "gzip, deflate",\
                "Connection": "close", \
                "Referer": "https://poll.fm/10400254" }, \
                { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", \
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
                    "Accept-Language": "en-US,en;q=0.5",\
                    "Accept-Encoding": "gzip, deflate",\
                    "Connection": "close", \
                    "Referer": "https://poll.fm/10400254" }, \
                { "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1", \
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", \
                    "Accept-Language": "en-US,en;q=0.5",\
                    "Accept-Encoding": "gzip, deflate",\
                    "Connection": "close", \
                    "Referer": "https://poll.fm/10400254" } \
                ]

s = requests.Session()
#'https://free-proxy-list.net/'
def get_proxies():
    url = 'https://www.us-proxy.org'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[5]/text()')[0] == 'anonymous':
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def getNonce():
    url = 'https://poll.fm/10400254'
    newHead = random.randint(0,2)
    s.headers = voteHead[newHead]
    response = s.get(url)
    text = response.text
    html = BeautifulSoup(text, 'html.parser')
    #Find the a tag that contains the info needed to submit the vote
    for a in html.select('a'):
        if a['href'] == 'vote':
            vote = a['data-vote']
            vote = ast.literal_eval(vote)
    #get the pz value from the hidden input field
    for i in html.select('input'):
        if i['name'] == 'pz':
            vote['pz'] = i['value']
    return vote


def vote(voteFor, proxy):
    info = getNonce()
    url = "https://poll.fm/vote?va=10&pt=0&r=1&p=10400254&a="
    url += voteFor + "%2c&o=&t=" + str(info['t']) + "&token=" + str(info['n']) + "&pz=" + str(info['pz'])
    s.proxies = {"http": proxy}
    responses = s.get(url)
    # response = requests.get(url)
    s.cookies.clear()
    return responses.status_code


# print(vote("48022565"))
proxies = get_proxies()
print(get_proxies())
t = 0
for p in proxies:
    i = 0
    while True:
        # if i % 2 == 0:
        vote("48022566", p)
        # else:
        #     vote("47965006", p)
        time.sleep(6)
        # if t % 50 == 1:
        #     os.chdir('C:\\Program Files\\Private Internet Access\\')
        #     os.system("taskkill /im pia-client.exe /f")
        #     os.startfile('pia-client.exe')
        i += 1
        t += 1
        print(t)

print(t)
#
# 48022565
# Dayan 48022566
# Chubba 47965006
