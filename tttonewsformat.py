import xml.etree.cElementTree as et
import nltk
import sys
import re
import pickle
from nltk import FreqDist
from nltk import tokenize
from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError

tree = et.parse( "texastrib/tt1.xml" )

root = tree.getroot()

articles = []

for child in root.findall( "article" ):
	bodytext = child.text
	
	if bodytext is None: 
		print "fail"
		continue
		
	#tokenize text into sentences, and then sentences into words
	
	#get the month as a string, ex: 2000-01 . the created_on tag looks like: 2000-03-01 11:14:13
	date = child.attrib['date'][:10]
	
	articles.append( [date, bodytext] )

f = open( 'texastrib/standardnews.pickle', 'w' )

pickle.dump( articles, f )

f.close()