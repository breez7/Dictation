#!/usr/bin/python
# -*- coding: utf8 -*-
import sqlite3
import sys
import os
from urllib import quote,unquote

dbfile = 'topic.db'


class Topic:

    # init method
    def __init__(self):
        self.title = ""
        self.genere = ""
        self.mediaFilePath = ""
        self.script = ""
        self.sttResult = ""
        self.id = -1

        if not os.path.isfile(dbfile):
            try:
                print 'creating table'
                connector = sqlite3.connect(dbfile)
                query = "CREATE TABLE IF NOT EXISTS topicTbl (id integer primary key autoincrement, title text not null,genere text not null ,mediaFilePath text not null,scriptContent text not null,sttResult text not null)"
                #query = "CREATE TABLE IF NOT EXISTS topicTbl (id int(11) NOT NULL AUTO_INCREMENT,title varchar(100) NOT NULL,genere varchar(50) NOT NULL,mediaFilePath varchar(255) NOT NULL,scriptContent text NOT NULL,sttResult text,  PRIMARY KEY (id))"
                cursor = connector.cursor()

                print 'creating table2'
                cursor.execute(query)
                connector.commit()
                print 'creating table3'

            except:
                import traceback
                traceback.print_exc()
                return -1
            finally:
                connector.close()

    # createTopic method
    def createTopic(self, title, genere, mediaFilePath, script):

        self.title = title
        self.genere = genere
        self.mediaFilePath = mediaFilePath
        self.script = script

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "insert into topicTbl (title, genere, mediaFilePath, scriptContent, sttResult) values(?,?,?,?,?)"

            cursor.execute(
                query, (title, genere, mediaFilePath, script, "None"))
            self.id = cursor.lastrowid
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            return -1
        finally:
            connector.close()
        return self.id

    # select method
    def retriveTopic(self, id):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "select id, title, genere, mediaFilePath, scriptContent, sttResult from topicTbl where id=" + \
                str(id)
            cursor.execute(query)
            rs = cursor.fetchall()
            if len(rs) == 0 or id != rs[0][0]:
                return None
            self.id = id
            self.title = rs[0][1]
            self.genere = rs[0][2]
            self.mediaFilePath = rs[0][3]
            self.script = rs[0][4]
            self.sttResult = unquote(rs[0][5])
            return rs
        except:
            import traceback
            traceback.print_exc()
            return None
        finally:
            connector.close()

  # select method
    def retriveTopicAll(self):

        query = ""
        connector = sqlite3.connect(dbfile)
        try:
            cursor = connector.cursor()

            query = "select id, title, genere, mediaFilePath, scriptContent, sttResult from topicTbl"
            cursor.execute(query)
            rs = cursor.fetchall()
            return rs
        except:
            import traceback
            traceback.print_exc()
            return None
        finally:
            connector.close()

    # update method
    def updateTopic(self):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            if self.title != '':
                setQuery = "title = '" + self.title + "',"
            if self.genere != '':
                setQuery = setQuery + "genere ='" + self.genere + "',"
            if self.mediaFilePath != '':
                setQuery = setQuery + "mediaFilePath = '" + self.mediaFilePath + "',"
            if self.script != '':
                setQuery = setQuery + "scriptContent = '" + self.script + "',"
            if self.sttResult != '':
                setQuery = setQuery + "sttResult = '" + quote(self.sttResult) + "',"

            # last of comma delete
            setQuery = setQuery[0:len(setQuery) - 1]

            print "setQuery = " + setQuery + "\n"
            query = "update topicTbl set " + \
                setQuery + " where id=" + str(self.id)
            print "query = " + query + "\n"
            cursor.execute(query)
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            print "update failure : " + query
            return False
        finally:
            connector.close()
        return True

    # delete method
    def deleteTopic(self, id):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "delete from topicTbl where id=" + str(id)
            cursor.execute(query)
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            print "delete failure : " + query

            return False
        finally:
            connector.close()
        return True

if __name__ == '__main__':
    topic = Topic()
    # if not os.path.isfile(dbfile):
    #     print 'fail create topic'
    # else:
    #     print 'create result id : ' + str(topic.createTopic(
    #         "topic title", "genere movie", "move path", "script text"))
    #     print 'before update: ' + topic.sttResult
    #     topic.retriveTopic(topic.id)
    #     print 'retrive reslt : ' + topic.title + topic.genere + str(topic.id)
    #     topic.sttResult = " good"
    #     topic.updateTopic()
        
    #     topic2 = Topic()
    #     topic2.retriveTopic(topic.id)
    #     print 'after update:' + topic2.sttResult
    #     rs = topic.retriveTopicAll()
    #     topic.deleteTopic(topic.id)
    #    print topic.retriveTopic(topic.id)
    #rs = topic.retriveTopicAll()
    topic.retriveTopic(1)
    print 'id:' + str(topic.id)
    print topic.sttResult
    


# class Topic():
#     def __init__(self):
#         self.id = -1
#         self.title = ''
#         self.genere = ''
#         self.mediaFilePath = ''
#         self.script = ''
#         self.sttResult = None

#     def createTopic(self, title, genere, mediaFilePath, script):
#         self.id = 1
#         self.title = title
#         self.genere = genere
#         self.mediaFilePath = mediaFilePath
#         self.script = script
#         return self.id

#     def updateTopic(self):
#         pass

#     def deleteTopic(self, id):
#         pass

#     def retriveTopic(self, id):
#         self.id = id
#         self.loadDBValue(id)
# return self.title, self.genere, self.mediaFilePath, self.script,
# self.sttResult

#     def loadDBValue(self, id):
#         self.title = 'BBC English'
#         self.genere = 'News'
#         self.mediaFilePath = './UnitTest/bbc.mp3'
#         self.script = "words in the news from BBC learning English dot com it's been a history in the making the people of Scotland have decided to continue their three hundred GA union with England so the U. K. survives pro independence campaign to say that disappointed but insist the high turnout shows there's an appetite for change few would disagree and accept the results doesn't mean Britain goes back to business as usual in the hours and days ahead the prime minister David Cameron and the other party leaders will now have to deliver on that promise in the last days of the campaign to give Scotland more powers and no one believes that can be done without a wide a shakeup of how the rest of the UK is governed"
#         self.sttResult = None
