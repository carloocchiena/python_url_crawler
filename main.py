from bs4 import BeautifulSoup as BS4
import requests as req

#globals

url = "https://www.ursite.com"

raw_data = []

temp_data = []

clean_data = []

limit = 10

#data cleaner: remove not-urls and external links. Also, append items to the main stack.
def cleaner(data):
    for items in data:
        if items[0:len(url)] == url:
            temp_data.append(items)
    global clean_data
    clean_data = set(temp_data)

#recursive crawling  function    
def crawler(url):
    
    count = 0
   
    source_code = req.get(url, "html.parser").content

    soup = BS4(source_code, 'lxml')

    links = soup.findAll("a", href=True)
    
    for link in links:
        raw_data.append(str(link.get("href")))
        
    cleaner(raw_data)
    
    while count < limit:

        for links in clean_data:
            temp = []
            source_code = req.get(links, "html.parser").content
            soup = BS4(source_code, 'lxml')
            bites = soup.findAll("a", href=True)
      
        for bite in bites:
            temp.append(str(bite.get("href")))  
        
        cleaner(temp)
            
        count += 1 
    
    return clean_data
