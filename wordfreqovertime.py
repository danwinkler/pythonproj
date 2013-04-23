import xml.etree.cElementTree as et
import nltk
import sys
import re
from nltk import FreqDist
from nltk import tokenize
from bs4 import BeautifulSoup

def removeTags(html, *tags):
    soup = BeautifulSoup(html)
    for tag in tags:
        for tag in soup.findAll(tag):
            tag.replaceWith("")
    return str( soup )

nonPunct = re.compile('.*[A-Za-z0-9].*')

tree = et.parse( "bbpostsmini.xml" )

root = tree.getroot()

i = 0
for child in root.findall( "row" ):
    l1 = [tokenize.word_tokenize( sent ) for sent in tokenize.sent_tokenize( removeTags( child.find( "body" ).text, 'a', 'b', 'p') )]
    fd = FreqDist( [item for sublist in l1 for item in sublist] )
    v = fd.items()
    v = [w for w in v if nonPunct.match( w[0] )]
    print v[:10]
    
    i += 1
    if( i > 100 ):
        break
