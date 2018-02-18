from wordnik import *
import requests
import json
import re
class Word:
	def __init__(self, word, partOfSpeech):
		self.wordName = word
		self.partOfSpeech = partOfSpeech
		self.lettersIn = self.wordName.split()
		self.definition = None
		self.wordApi = WordApi.WordApi(self.setupWordnik())
		self.vocabTypes = {"JJ":"adjective", "JJR":"adjective","JJS":"adjective","NN":"noun","NNP":"pnoun","NNS":"noun","RB":"adverb","RBR":"adverb","RBS":"adverb","VB":"verb","VBD":"verb","VBG":"verb","VBN":"verb","VBP":"verb","VBZ":"verb"}
	def getWordDefinition(self):
		defArray = self.wordApi.getDefinitions(self.wordName, partOfSpeech=self.partOfSpeech, limit="1")
		defArray = defArray[0]
		self.definition = defArray.text
		return 0
	def setupWordnik(self):
		apiUrl = 'http://api.wordnik.com/v4'
		apiKey = 'f2269092144bc2689a0080d8f3702e7ae6d3d8e56c6a4a031'
		client = swagger.ApiClient(apiKey, apiUrl)
		return client
	def isImportant(self):
		return len(self.wordName) >= 9
	def getWikiSimple(self):
		string = self.wordName.replace(" ", "%20")
		inprocess = requests.get("https://simple.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + string)
		inprocess = inprocess.content
		inprocess = json.loads(inprocess)
		inprocess = inprocess["query"]["pages"]
		for key in inprocess:
			k = key
		inprocess = inprocess[k]
		if "extract" not in inprocess:
			print "xyz"
			self.definition = "nodef"
			return 0
		inprocess = inprocess["extract"]
		self.definition = inprocess
		return 0
	def nltkPosHandler(self):
		if self.partOfSpeech in self.vocabTypes and self.isImportant():
			if self.partOfSpeech != "NNP":
				self.partOfSpeech = self.vocabTypes[self.partOfSpeech]
				self.getWordDefinition()
			elif self.partOfSpeech == "NNP":
				self.getWikiSimple()
			else:
				self.definition = "nodef"
	def getWord(self):
		return self.wordName
word = Word("John Adams", "NNP")
word.nltkPosHandler()
print word.definition