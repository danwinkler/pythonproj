import xml.etree.cElementTree as et
import nltk
import sys
import re
import pickle
from nltk import FreqDist
from nltk import tokenize
from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError

f = open( sys.argv[1] + '/standardnews.pickle' )
articles = pickle.load( f )
f.close()

#matches stuff thats not punctuation
nonPunct = re.compile('.*[A-Za-z0-9].*')

#dictionary has format of {monthasstring: [FreqDist]} hopefully that makes sense haha
wordfreqpermonth = {}

for article in articles:
	bodytext = article[1]
	
	if bodytext is None: 
		print "fail"
		continue
		
	#tokenize text into sentences, and then sentences into words
	l1 = [tokenize.word_tokenize( sent ) for sent in tokenize.sent_tokenize( bodytext )]
	
	#flatten list of sentences, which are lists of words
	words = [item for sublist in l1 for item in sublist]
	
	#remove punctuation
	words = [w for w in words if nonPunct.match( w )]
	
	#get the month as a string, ex: 2000-01 . the created_on tag looks like: 2000-03-01 11:14:13
	month = article[0][:7]
	
	print month
	
	#init the freqdist if we have to
	if not month in wordfreqpermonth:
		wordfreqpermonth[month] = FreqDist()
	
	#add the words into the freqdist forwhatever month it is
	fd = wordfreqpermonth[month]
	for word in words:
		fd.inc( word.lower() )

f = open( sys.argv[1] + 'wordfreqpermonth.pickle', 'w' )

pickle.dump( wordfreqpermonth, f )

f.close()