import requests
from bs4 import BeautifulSoup
import re
import time

url = 'https://www.google.com/'

source_code = requests.get(url)
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []
limit = 10

def remove_duplicates(array): # remove duplicates and unURL string
    for item in array:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))

for link in soup.find_all('a', href=True):
    data.append(str(link.get('href')))
flag = True
remove_duplicates(data)
while flag:
    try:
        for link in links:
            for i in soup.find_all('a', href=True):
                temp = []
                source_code = requests.get(link)
                soup = BeautifulSoup(source_code.content, 'lxml')
                temp.append(str(i.get('href')))
                remove_duplicates(temp)

                if len(links) > limit:
                    break
            if len(links) > limit:
                break
        if len(links) > limit:
            break
    except Exception as e:
        print(e)
        if len(links) > limit:
            break

links = set(links)
            
for url in links:
    print(url)
