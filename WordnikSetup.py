from wordnik import *
class WordnikSetup():
	def __init__(self):
		self.apiUrl = 'http://api.wordnik.com/v4'
		self.apiKey = 'f2269092144bc2689a0080d8f3702e7ae6d3d8e56c6a4a031'
		self.client = swagger.ApiClient(apiKey, apiUrl)
	def getApiThing(self):
		return self.client
