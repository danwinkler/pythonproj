import matplotlib.pyplot as plt
import nltk
import sys
import pickle

f = open( sys.argv[1] + '/wordfreqpermonth.pickle' )
dict = pickle.load( f )
f.close()

wordlist = ["kill", "love"]
for word in wordlist:
	keys = []
	vals = []
	for key in dict:
		keys.append( key )
		vals.append( dict[key].freq( word ) )
	p = plt.plot( vals )
	
plt.ylabel('word freq')
plt.xlabel('date')
plt.show()