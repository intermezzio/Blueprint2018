"""
List of Words in a sentence

	for the nltk Library (Natural Language Toolkit Python)

"""
#from Word import *
from wordnik import *
import nltk
from collections import Counter

class Sentence:
    
    def __init__(self, sentence):
        self.words = nltk.word_tokenize(sentence)
        self.pos_words = None

    

    def countOccurrences(self, word):
    	try:
    		return Counter(words)[word]
    	except KeyError:
    		return 0
    
    def getPartOfSpeech(self):
    	self.pos_words = nltk.pos_tag(self.words)

    def combinePropers(self):
    	if self.pos_words is None:
    		self.getPartOfSpeech()
    	print self.pos_words
    	newSentence = []
    	currWord = ""
    	prevpos = ""
    	for word, pos in self.pos_words:
    		print word + " " + pos
    		if pos in ("NNP",):
    			if prevpos in ("NNP",):
    				currWord += " " + word
    			#elif i == len(self.pos_words) - 1:
    			#	newSentence += [(word, pos)]
    			#	currWord = word
    			#	currWord = ""
    			else:
    				currWord = word
    		else:
    			if prevpos in ("NNP",):
    				newSentence += [(currWord, "NNP")]
    				newSentence	+= [(word, pos)]
    				currWord = ""
    			else:
    				newSentence += [(word, pos)]
    		prevpos = pos
    	if currWord	!= "":
    		newSentence.append( (currWord, pos) );
    	print newSentence

firstSentence = Sentence("I didn't know Tom Brady and Nick Foles threw two touchdown passes")
firstSentence.getPartOfSpeech()
firstSentence.combinePropers()