from Sentences import *
import re
class Reader():
	def __init__(self, text):
		self.sentences = re.split(".|!|;|?", text)
		self.sentenceArray = []
		self.makeSentences()
		self.masterDict = dict()

	def makeSentences(self):
		for sentence in self.sentences:
			self.sentenceArray.append(Sentence(sentence))

	def getMasterDictionary(self):
		
		for sentence in sentenceArray:
			sentenceDict = sentence.getDictionary()
			for word in sentenceDict.getKeys():
				self.masterDict[word] = sentenceDict[word]

		return self.masterDict


	def getCSV(self):
		csvFile = fopen("parsedSolution.csv", 'w')
		for vocab in self.getMasterDictionary.getKeys():
			pass

	def fileRead():
		pass		
