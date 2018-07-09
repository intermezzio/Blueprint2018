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
		self.defArray = self.wordApi.getDefinitions(self.wordName, limit="1")
		if self.defArray == None:
			print "None"
		self.defArray = self.defArray[0]

		self.definition = self.defArray.text
		return 0
	def setupWordnik(self):
		apiUrl = 'http://api.wordnik.com/v4'
		apiKey = 'f2269092144bc2689a0080d8f3702e7ae6d3d8e56c6a4a031'
		client = swagger.ApiClient(apiKey, apiUrl)
		return client
	def isImportant(self):
		return len(self.wordName) >= 9
	def getWikiSimple(self):
		print self.wordName
		self.string = self.wordName.replace(" ", "%20")
		self.inprocess = requests.get("https://simple.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=" + self.string).content
		self.inprocess = json.loads(self.inprocess)
		self.inprocess = self.inprocess["query"]["pages"]
		for key in self.inprocess:
			k = key
		self.inprocess = self.inprocess[k]
		print self.inprocess.keys()
		self.final = self.inprocess["extract"]

		if "extract" not in self.inprocess:
			self.definition = "nodef"
		else:
			self.definition = self.final
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
