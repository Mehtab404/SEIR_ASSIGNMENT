from bs4 import BeautifulSoup

import requests

import sys 



url = sys.argv[1]

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



word_Dict = {}
def countBodyCharacter(body_content):
    for word_s in body_content.split():
        if word_s.lower() in word_Dict:
            word_Dict[word_s.lower()] = word_Dict[word_s.lower()] + 1
        else:
            word_Dict[word_s.lower()] = 1
    print(word_Dict)


res = countBodyCharacter(doc.body.get_text())
print(res)











