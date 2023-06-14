# author rahmanralei
# https://t.me/rahmanralei

import requests
import cloudscraper
import os
import random
from nagooglesearch import nagooglesearch
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
linux = 'clear'
windows = 'cls'
os.system([linux, windows][os.name == 'nt'])

print("""
+---------[ Grabber Domain By Dorking ]---------+
+ Author          : Rahman Ralei                +
+ Telegram        : t.me/rahmanralei            +
+-----------------------------------------------+
""")

dork = input('[?] input dork: ')
extdom = input('[?] extension domain *(.com, ac.id, .go.id, dll): ')
page = input('[?] page on google: ')
use_proxy = input('[?] Use proxy? (Y/N): ')

print('')

max_results = 100

url = f'https://www.google.com/search?q={dork}%20site:{extdom}+-inurl:*+-site:google.com+-site:google.co.id&num={max_results}&start={page}'

headers = {
    'User-Agent': nagooglesearch.get_random_user_agent()
}

proxies = {}

if use_proxy.lower() == 'y':
    proxy_type = input('[?] Proxy type (http/https): ')
    proxy_host = input('[?] Proxy host/IP: ')
    proxy_port = input('[?] Proxy port: ')
    
    proxies = {
        proxy_type.lower(): f'{proxy_host}:{proxy_port}'
    }

response = scraper.get(url, headers=headers, proxies=proxies).text
soup = BeautifulSoup(response, 'html.parser')
results = soup.find_all('a', href=True)
domains = set()

for result in results:
    url = result['href']
    if url.startswith('http') and not url.startswith('https://webcache.googleusercontent.com'):
        dork = url.split('/')[2]
        if dork.endswith(extdom):
            domains.add(dork)
            
for domain in domains:
    print(f"• {domain}")
    
with open('dorker.txt', 'a') as file:
    for domain in domains:
        file.write(f"{domain}\n")

with open('dorker.txt') as ff:
    rescount = ff.readlines()
    print(f"\n- Total: {len(set(rescount))} Domains")
    print(f"- Saved -> dorker.txt")
