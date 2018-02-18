from wordnik import *
class Word:
	def __init__(self, word, partOfSpeech):
		self.wordName = word
		self.partOfSpeech = None
		self.etymology = None
		self.lettersIn = self.wordName.split()
		self.definition = None
		self.wordApi = WordApi.WordApi(self.setupWordnik())
		self.vocabTypes = {"JJ":"adjective", "JJR":"adjective","JJS":"adjective","NN":"noun","NNP":"noun","NNS":"noun","RB":"adverb","RBR":"adverb","RBS":"adverb","VB":"verb","VBD":"verb","VBG":"verb","VBN":"verb","VBP":"verb","VBZ":"verb"}
	def getWordDefinition(self):
		defArray = self.wordApi.getDefinitions(self.wordName, partOfSpeech=self.partOfSpeech, limit="3")
		defArray = defArray[0]
		self.definition = defArray.text
		return 0
	def setupWordnik(self):
		apiUrl = 'http://api.wordnik.com/v4'
		apiKey = 'f2269092144bc2689a0080d8f3702e7ae6d3d8e56c6a4a031'
		client = swagger.ApiClient(apiKey, apiUrl)
		return client
	def nltkPosHandler():
		if self.partOfSpeech in self.vocabTypes and len(self.wordName) > 8:
			self.partOfSpeech = self.vocabtypes[self.partOfSpeech]
			self.getWordDefinition()
		else:
			self.definition = None
	def getWord(self):
		return self.wordName


