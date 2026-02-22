from bs4 import BeautifulSoup

import requests

url = input("Enter your url: ")

result = requests.get(url)
# tag1 = doc.title

# print(tag.String)



doc = BeautifulSoup(result.text,"html.parser")
# print(doc.prettify())

print(doc.title.string)
print(doc.body.get_text())



