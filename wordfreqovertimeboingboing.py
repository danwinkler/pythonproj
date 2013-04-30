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

tree = et.parse( "bbpostsdump.xml" )

root = tree.getroot()

#dictionary has format of {monthasstring: [FreqDist]} hopefully that makes sense haha
wordfreqpermonth = {}

for child in root.findall( "row" ):
	bodytext = child.find( "body" ).text
	
	if bodytext is None: 
		print "fail"
		continue
	
	bodytext = removeTags( bodytext, 'a', 'b', 'p', 'i', 'blockquote', 'param', 'br', 'img')
	
	#tokenize text into sentences, and then sentences into words
	l1 = [tokenize.word_tokenize( sent ) for sent in tokenize.sent_tokenize( bodytext )]
	
	#flatten list of sentences, which are lists of words
	words = [item for sublist in l1 for item in sublist]
	
	#remove punctuation
	words = [w for w in words if nonPunct.match( w )]
	
	#get the month as a string, ex: 2000-01 . the created_on tag looks like: 2000-03-01 11:14:13
	month = child.find( "created_on" ).text[:7]
	
	print month
	
	#init the freqdist if we have to
	if not month in wordfreqpermonth:
		wordfreqpermonth[month] = FreqDist()
	
	#add the words into the freqdist forwhatever month it is
	fd = wordfreqpermonth[month]
	for word in words:
		fd.inc( word.lower() )

f = open( 'wordfreqpermonth.pickle', 'w' )

pickle.dump( wordfreqpermonth, f )

f.close()