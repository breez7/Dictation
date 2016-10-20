import sys
sys.path.insert(0, '..')
import unittest

from TopicManager import TopicManager


class TestEnglishStudy(unittest.TestCase):
	title = 'BBC English'
	genere = 'News'
	path = './UnitTest/bbc.mp3'
	script = "words in the news from BBC learning English dot com it's been a history in the making the people of Scotland have decided to continue their three hundred GA union with England so the U. K. survives pro independence campaign to say that disappointed but insist the high turnout shows there's an appetite for change few would disagree and accept the results doesn't mean Britain goes back to business as usual in the hours and days ahead the prime minister David Cameron and the other party leaders will now have to deliver on that promise in the last days of the campaign to give Scotland more powers and no one believes that can be done without a wide a shakeup of how the rest of the UK is governed"
	sttResult = "Not STT"
	
	def setUp(self):
		self.topicManager = TopicManager()
	def tearDown(self):
		pass
	def testTopicManager(self):


		topic = self.topicManager.addTopic(TestEnglishStudy.title, TestEnglishStudy.genere, TestEnglishStudy.path, TestEnglishStudy.script)
		self.assertTrue( topic.id > 0)

		getTopic = self.topicManager.getTopic(topic.id)
		self.assertTrue((getTopic.title, getTopic.genere, getTopic.mediaFilePath, getTopic.script) == (TestEnglishStudy.title, TestEnglishStudy.genere, TestEnglishStudy.path, TestEnglishStudy.script))

		self.topicManager.analyseTopic(topic)
		self.assertTrue(topic.sttResult == TestEnglishStudy.sttResult)

if __name__ == '__main__':
	unittest.main()