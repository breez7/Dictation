import sys
sys.path.insert(0, '..')
import unittest

import TopicManager


class TestEnglishStudy(unittest.TestCase):
	title = 'testHello'
	genere = 'greeting'
	path = 'bbc.wav'
	#path = 'woman1_wb.wav'
	script = 'hello man'
	sttResult = "to administer medicine to animals is frequently a very difficult matter and yet sometimes it's necessary to do so "

	def setUp(self):
		self.topicManager = TopicManager.TopicManager()
	def tearDown(self):
		pass
	def testTopicManager(self):


		id = self.topicManager.addTopic(TestEnglishStudy.title, TestEnglishStudy.genere, TestEnglishStudy.path, TestEnglishStudy.script)
		self.assertTrue( id > 0)

		self.assertTrue(self.topicManager.getTopic(id) == (TestEnglishStudy.title, TestEnglishStudy.genere, TestEnglishStudy.path, TestEnglishStudy.script,''))

		self.assertTrue(self.topicManager.analyseTopic(id) == (TestEnglishStudy.title,TestEnglishStudy.genere,TestEnglishStudy.path,TestEnglishStudy.script,TestEnglishStudy.sttResult))

if __name__ == '__main__':
	unittest.main()