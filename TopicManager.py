import requests
from Topic import Topic
from pydub import AudioSegment

import json

class TopicManager:
	def __init__(self):
		self.stt = IBMSTT()

	def addTopic(self,title, genere, path, script):
		topic = Topic()
		topic.createTopic(title,genere,path,script)
		return topic
	def getTopic(self, id):
		topic = Topic()
		topic.retriveTopic(id)
		return topic
	def analyseTopic(self, topic):
		sttResult = self.stt.translate(topic.mediaFilePath)
		topic.sttResult = sttResult
		topic.updateTopic()
		return topic
	def getAllTopics(self):
		return None

class IBMSTT:
	URL = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true&continuous=true'	
	USERNAME = "12dd2d69-9bb7-45c7-8bc9-c193bd2dba63"
	PASSWORD = "rnAnWqvZvHzt"
	HEADERS = {"Content-Type":"audio/wav","X-Waston-Learning-Opt-Out":"true"}
	def translate(self, filePath):
		#data = open("woman1_wb.wav", "rb")
		filePath = self.convertToWav(filePath)
		data = open(filePath, "rb")
		res = requests.post(IBMSTT.URL, data=data, auth=(IBMSTT.USERNAME, IBMSTT.PASSWORD), headers=IBMSTT.HEADERS)
		data.close()
		return self.parseSTTResult(res.text)

	def convertToWav(self,src):
		if src.lower().endswith('mp3'):

			sound = AudioSegment.from_mp3(src)
			src = src[:-3] + 'wav'
			sound.export(src, format="wav")
		return src

	def parseSTTResult(self, sttResult):
		sttResult = json.loads(sttResult)
		sentences = []
		result = sttResult['results']
		for sentence in result:
			transcript = sentence['alternatives'][0]['transcript']
			words = sentence['alternatives'][0]['timestamps']
			sentences.append([transcript, words])
		return sentences	