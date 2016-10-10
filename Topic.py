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
	try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            setValue = "title='" + title + "',genere='" + genere + "',mediaFilePath='" + mediaFilePath + "',script='" + script + "'" 

            query = "insert into topicTbl (title, genere, mediaFilePath, script) values(" + setValue +")"

            cursor.execute(sql)
            return cursor.last_insert_id()
        except:
            return -1

    #select method
    def retriveTopic(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "select id, title, genere, mediaFilePath, script from topicTbl where id=" + id
	    cursor.execute(query)
            rs = cursor.fetchall()
            return rs
        except:
            return -1

    #update method
    def updateTopic(self, id, title, genere, mediaFilePath, script):
        query = ""
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            if title != '':
                setQuery = "title = '" + title + "',"
            if genere != '':
                setQuery = setQuery + "genere ='" + genere + "',"
            if mediaFilePath != '':
                setQuery = setQuery + "mediaFilePath = '" + mediaFilePath + "',"
            if script != '':
                setQuery = setQuery + "script = '" + script + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            print "setQuery = " + setQuery + "\n"
            query = "update from topicTbl set " + setQuery + " where id="+id
            print "query = " + query + "\n"
	    cursor.execute(query)
        except:
            print "update failure : " + query

    #delete method
    def deleteTopic(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "delete from topicTbl where id=" + id
	    cursor.execute(query)
        except:
            print "delete failure : " + query

	def loadDBValue(self,id):
		self.title = 'testHello'
		self.genere = 'greeting'
		self.mediaFilePath = 'hello.mp3'
		self.script = 'hello man'
