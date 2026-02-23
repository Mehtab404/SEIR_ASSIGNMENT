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
        stop_words = ["is","am","are","the","not","in","on","or","but","if","while","at","for","by"]
        if word_s in stop_words: continue
        if word_s.lower() in word_Dict:
            word_Dict[word_s.lower()] = word_Dict[word_s.lower()] + 1
        else:
            word_Dict[word_s.lower()] = 1
    print(word_Dict)


res = countBodyCharacter(doc.body.get_text())
print(res)



def hashCode(words):
    p = 53
    m = 2**64

    s = 0
    final  =0
    for i in words:
        final = (final + ord(i)*(p**s))%m
        s+=1
    return final



def simhash(word_list):
    sim = [0]*64
    for j in word_list:
        hash = hashCode(j)
        for i in range(64):
            if (hash >> i) & 1:
                sim[i] += word_list[j]
            else:
                sim[i] -= word_list[j]
    
    fingerprint = 0
    for i, v in enumerate(sim):
        if v > 0:
            fingerprint = fingerprint | (1 << i)

    return fingerprint

def findcommonbits(fingerprint1, fingerprint2):
    temp = fingerprint1 ^ fingerprint2
    count = 0
    while temp:
        bit = temp & 1
        if bit == 1:
            count += 1
        temp >>= 1
    diff = 64 - count
    return diff


"""
url1 -> html1 -> body1 -> fingerprint1
url2 -> html2 -> body2 -> fingerprint2
common -> 
"""


















