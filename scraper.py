from bs4 import BeautifulSoup

import requests

import sys 



url = sys.argv[1]
if not url.startswith(("https://","http://")):
    url = "https://" + url

headers = {
    'User-Agent': 'ScrapingBee/1.0 (https://www.scrapingbee.com; support@scrapingbee.com)'   
}

result = requests.get(url, headers=headers)

# result = requests.get(url)
# tag1 = doc.title

# print(tag.String)

doc = BeautifulSoup(result.text,"html.parser")
# print(doc.prettify())

if doc.title:
    print(doc.title.string)
else:
    pass
if doc.body:
    print(doc.body.get_text())
else:
    pass

for urls in doc.find_all("a"):
    href = urls.get("href")
    if href:
        print(href)












        


















