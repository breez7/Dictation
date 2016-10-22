<<<<<<< HEAD
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
=======
#!/usr/bin/python
# -*- coding: utf8 -*-
import MySQLdb

class Topic:

    #database connection info
    host="localhost"
    db="englishstudy"
    user="enlishstudy"
    passwd="englishstudy"
    charset="utf8"

    #init method
    def __init__(self):
        self.title = ""
        self.genere = ""
        self.mediaFilePath = ""
        self.script = ""
        self.sttResult = ""
        self.id = -1

    #createTopic method
    def createTopic(self, title, genere, mediaFilePath, script):

        query = ""
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")

	try:
            cursor = connector.cursor()

            query = "insert into topicTbl (title, genere, mediaFilePath, scriptContent) values(%s,%s,%s,%s)"

            cursor.execute(query, (title,genere,mediaFilePath,script))
            #return cursor.last_insert_id()
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            return false
        finally:
            connector.close()
#        return true

    #select method
    def retriveTopic(self,id):

    	query = ""
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")

        try:
            cursor = connector.cursor()

            query = "select id, title, genere, mediaFilePath, scriptContent from topicTbl where id=%s"
            cursor.execute(query, (id))
            rs = cursor.fetchall()
            return rs
        except:
            import traceback
            traceback.print_exc()
            return false
        finally:
            connector.close()

    #update method
    def updateTopic(self, id, title, genere, mediaFilePath, script):

        query = ""
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")

        try:
            cursor = connector.cursor()

            if title != '':
                setQuery = "title = '" + title + "',"
            if genere != '':
                setQuery = setQuery + "genere ='" + genere + "',"
            if mediaFilePath != '':
                setQuery = setQuery + "mediaFilePath = '" + mediaFilePath + "',"
            if script != '':
                setQuery = setQuery + "scriptContent = '" + script + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            print "setQuery = " + setQuery + "\n"
            query = "update topicTbl set " + setQuery + " where id="+id
            print "query = " + query + "\n"
            cursor.execute(query)
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            print "update failure : " + query
            return false
        finally:
            connector.close()
#        return true

    #delete method
    def deleteTopic(self,id):

        query = ""
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")

        try:
            cursor = connector.cursor()

            query = "delete from topicTbl where id=%s"
            cursor.execute(query,(id))
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            print "delete failure : " + query
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/master

    def loadDBValue(self, id):
        self.title = 'BBC English'
        self.genere = 'News'
        self.mediaFilePath = './UnitTest/bbc.mp3'
        self.script = "words in the news from BBC learning English dot com it's been a history in the making the people of Scotland have decided to continue their three hundred GA union with England so the U. K. survives pro independence campaign to say that disappointed but insist the high turnout shows there's an appetite for change few would disagree and accept the results doesn't mean Britain goes back to business as usual in the hours and days ahead the prime minister David Cameron and the other party leaders will now have to deliver on that promise in the last days of the campaign to give Scotland more powers and no one believes that can be done without a wide a shakeup of how the rest of the UK is governed"
        self.sttResult = None
=======
            return false
        finally:
            connector.close()
#        return true

#topic = Topic()
#result=topic.createTopic("topic title", "genere movie" , "move path", "script text")
#result=topic.retriveTopic('1')
#result=topic.updateTopic("2", "modified topic title", "modified movie" , "modified path", "modified script")
#result=topic.deleteTopic('1');
#print result
>>>>>>> refs/remotes/origin/master
