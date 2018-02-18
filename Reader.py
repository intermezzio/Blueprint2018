from Sentences import *
import re
class Reader():
	def __init__(self, text):
		self.sentences = re.split(".|!|;|?", text)
		self.sentenceArray = None
		i = 0
		for sentence in self.sentences:
			self.sentenceArray[i] = Sentence(sentence)
			i+=1
	def fileRead():
		
