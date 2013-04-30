import xml.etree.cElementTree as et
import nltk
import sys
import re
import pickle
from nltk import FreqDist
from nltk import tokenize
from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError

#helper function to remove html tags
def removeTags(html, *tags):
	try:
		soup = BeautifulSoup(html)
		for tag in tags:
			for tag in soup.findAll(tag):
				tag.replaceWith("")
		return str( soup )
	except (HTMLParseError, TypeError):
		return html

#matches stuff thats not punctuation
nonPunct = re.compile('.*[A-Za-z0-9].*')

tree = et.parse( "boingboing/bbpostsdump.xml" )

root = tree.getroot()

articles = []

for child in root.findall( "row" ):
	bodytext = child.find( "body" ).text
	
	if bodytext is None: 
		print "fail"
		continue
	
	bodytext = removeTags( bodytext, 'a', 'b', 'p', 'i', 'blockquote', 'param', 'br', 'img', 'script', 'body')
	
	#tokenize text into sentences, and then sentences into words
	
	#get the month as a string, ex: 2000-01 . the created_on tag looks like: 2000-03-01 11:14:13
	date = child.find( "created_on" ).text[:10]
	
	articles.append( [date, bodytext] )

f = open( 'boingboing/standardnews.pickle', 'w' )

pickle.dump( articles, f )

f.close()