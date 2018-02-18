"""
List of Words in a sentence

Credit to Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
	for the nltk Library (Natural Language Toolkit Python)

"""
from Word import *
from wordnik import *
from nltk import *
from collections import Counter

class Sentence:
    
    def __init__(self, sentence):
        self.words = nltk.word_tokenize(sentence)
        self.pos_words = None

    def partOfSpeech(self, word)
    	pass

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

    	for wordTuple in self.pos_words:
    		if wordTuple[1] not in ("NNP", ""):
    			pass