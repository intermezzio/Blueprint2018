import requests
from wordnik import *

class Word:
	def __init__(self, word):
		self.wordName = word
		self.partOfSpeech = None
		self.etymology = None
		self.lettersIn = []
		self.definition = None
		self.wordApi = WordApi.WordApi(self.setupWordnik())
	def getWordInfo(self):
		defArray = self.wordApi.getDefinitions(self.wordName)
		defArray = defArray[0]
		self.definition = defArray.text
		return 0
	def setupWordnik(self):
		apiUrl = 'http://api.wordnik.com/v4'
		apiKey = 'f2269092144bc2689a0080d8f3702e7ae6d3d8e56c6a4a031'
		client = swagger.ApiClient(apiKey, apiUrl)
		return client
	def getWord(self):
		return self.wordName
word = Word("plant")
word.getWordInfo()
print word.definition


