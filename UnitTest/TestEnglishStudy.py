import sys

import unittest

sys.path.insert(0, '..')
import TopicManager


class TestEnglishStudy(unittest.TestCase):
	def setUp(self):
		self.topicManager = TopicManager.TopicManager()
	def tearDown(self):
		pass

	def testTopicManager(self):
		title = 'testHello'
		genere = 'greeting'
		path = 'hello.mp3'
		script = 'hello man'
		sttResult = 'hello man'

		self.assertTrue(id = self.topicManager.addTopic(title, genere, path, script) > 0)
		self.assertTrue(self.topicManager.getTopic(id) == (title,genere,path,script,''))

		self.topicManager.analyseTopic(id)
		self.assertTrue(self.topicManager.getTopic(id) == (title,genere,path,script,sttResult))

if __name__ == '__main__':
	unittest.main()