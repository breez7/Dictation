import Topic

class TopicManager:
	def addTopic(self,title, genere, path, script):
		topic = Topic.Topic()
		id = topic.createTopic(title,genere,path,script)
		return id
	def getTopic(self, id):
		topic = Topic.Topic()
		return topic.retriveTopic(id)
	def analyseTopic(self, id):
		topic = Topic.Topic()
		topic.retriveTopic(id)
		
		#TODO
		sttResult = getSTTResult(path)
		topic.sttResult = sttResult
		topic.updateTopic()

	def getSTTResult(path):
		return ''

