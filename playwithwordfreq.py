import nltk
import sys
import re
import pickle
from nltk import FreqDist
from nltk import tokenize

f = open( 'wordfreqpermonth.pickle' )
dict = pickle.load( f )
f.close()

f = open( "wordplot.csv", "w" )

wordlist = ["the","a","internet","weather","government"]

f.write( "month," + ",".join(wordlist) + "\n" )
for key in dict:
	f.write( key + "," )
	for word in wordlist:
		f.write( str( dict[key].freq( word ) ) + "," )
	f.write( "\n" )
	
f.close()