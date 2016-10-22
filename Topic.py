import sys


class Topic():
    def __init__(self):
        self.id = -1
        self.title = ''
        self.genere = ''
        self.mediaFilePath = ''
        self.script = ''
        self.sttResult = None

    def createTopic(self, title, genere, mediaFilePath, script):
        self.id = 1
        self.title = title
        self.genere = genere
        self.mediaFilePath = mediaFilePath
        self.script = script
        return self.id

    def updateTopic(self):
        pass

    def deleteTopic(self, id):
        pass

    def retriveTopic(self, id):
        self.id = id
        self.loadDBValue(id)
        return self.title, self.genere, self.mediaFilePath, self.script, self.sttResult

    def loadDBValue(self, id):
        self.title = 'BBC English'
        self.genere = 'News'
        self.mediaFilePath = './UnitTest/bbc.mp3'
        self.script = "words in the news from BBC learning English dot com it's been a history in the making the people of Scotland have decided to continue their three hundred GA union with England so the U. K. survives pro independence campaign to say that disappointed but insist the high turnout shows there's an appetite for change few would disagree and accept the results doesn't mean Britain goes back to business as usual in the hours and days ahead the prime minister David Cameron and the other party leaders will now have to deliver on that promise in the last days of the campaign to give Scotland more powers and no one believes that can be done without a wide a shakeup of how the rest of the UK is governed"
        self.sttResult = None