from bs4 import BeautifulSoup

import requests

import sys 
url1 = sys.argv[1]
url2 = sys.argv[2]

headers = {
    'User-Agent': 'ScrapingBee/1.0 (https://www.scrapingbee.com; support@scrapingbee.com)'   
}

result1 = requests.get(url1, headers=headers)
result2 = requests.get(url2,headers=headers)

doc1 = BeautifulSoup(result1.text,"html.parser")
doc2 = BeautifulSoup(result2.text,"html.parser")



# res = countBodyCharacter(doc.body.get_text())
# print(res)

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
    for i in range(64):
        if sim[i] > 0:
            fingerprint = fingerprint | (1 << i)

    return fingerprint


def hashCode(words):
    p = 53
    m = 2**64

    s = 0
    final  =0
    for i in words:
        final = (final + ord(i)*(p**s))%m
        s+=1
    return final



def countBodyCharacter(body_content):
    word_Dict = {}
    for word_s in body_content.split():
        stop_words = ["is","am","are","the","not","in","on","or","but","if","while","at","for","by"]
        if word_s in stop_words: continue
        if word_s.lower() in word_Dict:
            word_Dict[word_s.lower()] = word_Dict[word_s.lower()] + 1
        else:
            word_Dict[word_s.lower()] = 1
    return word_Dict





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


if doc1.body and doc2.body:

    dict1 = countBodyCharacter(doc1.body.get_text())
    dict2 = countBodyCharacter(doc2.body.get_text())

    fingerprint1 = simhash(dict1)
    fingerprint2 = simhash(dict2)

    common_bits = findcommonbits(fingerprint1, fingerprint2)

    print(common_bits)