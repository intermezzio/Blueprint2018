from Sentences import *
import re
class Reader():
	def __init__(self, text):
		self.sentences = re.split(".", text)
		self.sentenceArray = []
		self.makeSentences()
		self.masterDict = dict()

	def makeSentences(self):
		for sentence in self.sentences:
			self.sentenceArray.append(Sentence(sentence))

	def getMasterDictionary(self):
		
		for sentence in self.sentenceArray:
			self.sentenceDict = sentence.getDictionary()
			for word in self.sentenceDict:
				self.masterDict[word] = self.sentenceDict[word]

		return self.masterDict


	def getCSV(self):
		csvFile = fopen("parsedSolution.csv", 'w')
		for vocab in self.getMasterDictionary.getKeys():
			pass

	def fileRead():
		pass		


reader = Reader("A simple pendulum consists of a relatively massive object hung by a string from a fixed support. It typically hangs vertically in its equilibrium position. The massive object is affectionately referred to as the pendulum bob. When the bob is displaced from equilibrium and then released, it begins its back and forth vibration about its fixed equilibrium position. The motion is regular and repeating, an example of periodic motion. Pendulum motion was introduced earlier in this lesson as we made an attempt to understand the nature of vibrating objects. Pendulum motion was discussed again as we looked at the mathematical properties of objects that are in periodic motion. Here we will investigate pendulum motion in even greater detail as we focus upon how a variety of quantities change over the course of time. Such quantities will include forces, position, velocity and energy - both kinetic and potential energy.")
print reader.getMasterDictionary()