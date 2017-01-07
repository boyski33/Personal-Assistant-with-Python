import json, requests, re, urllib2
from bs4 import BeautifulSoup
from google_search import *

#not tested
def get_wiki_title(voice_input):
    wikiUrl = None
    for url in search('%s wikipedia' % voice_input, stop=1):
        wikiUrl = url
        break
    soup = BeautifulSoup(urllib2.urlopen(wikiUrl))
    title_raw = soup.title.string
    title = title_raw.split(' - Wikipedia')
    return title[0]

def get_5_sentences(title):
    #url points to a JSON file
    url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles={}".format(title)
    url = url.replace(" ", "%20")

    response = urllib2.urlopen(url)
    response = requests.get(url)
    data = json.loads(response.text)

    ID = str(data["query"]["pages"].keys()[0])
    text = data["query"]["pages"][ID]["extract"]

    #regex for removing parentheses
    text = re.sub(r'(\([^)]*\))', '', text)
    #regex for removing pronunciation
    text = re.sub(r'(\/[^/\s]+\/\s*)', '', text)
    sentences = text.split(". ")
    sentences =  [x + "." for x in sentences]

    return sentences[:5]
