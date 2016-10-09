class Topic():
	def __init__(self):
		self.title = ''
		self.genere = ''
		self.mediaFilePath = ''
		self.script = ''
		self.sttResult = ''

	def createTopic(self, title, genere, mediaFilePath, script):
		self.id = 1
		self.title = title
		self.genere = genere
		self.mediaFilePath = mediaFilePath
		self.script= script
		return self.id
	def updateTopic(self):
		pass
	def deleteTopic(self, id):
		pass
	def retriveTopic(self, id):
		self.id = id
		self.loadDBValue(id)
		return self.title, self.genere, self.mediaFilePath, self.script, self.sttResult

	def loadDBValue(self,id):
		self.title = 'testHello'
		self.genere = 'greeting'
		self.mediaFilePath = 'hello.mp3'
		self.script = 'hello man'
