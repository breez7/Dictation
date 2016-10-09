#!/usr/bin/python
# -*- coding: utf8 -*-
import MySQLdb

class Word:

    #database connection info
    host="localhost"
    db="englishstudy"
    user="enlishstudy"
    passwd="englishstudy"
    charset="utf8"

    #init method
    def __init__(self):
        self.id = ""
        self.word = ""
        self.proun = ""
        self.sentencelnTopic = ""
        self.meanlnDict = ""
        self.etc = ""
        self.viewCount = ""
        self.feedback = ""

    #create method
    def createWord(self, word, proun, sentencelnTopic, meanlnDict, etc, viewCount, feedback):

        query = ""
	try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            setValue = "word='" + word + "',proun='" + proun + "',sentencelnTopic='" + sentencelnTopic + "',meanlnDict='" + meanlnDict + "',etc='" + etc +"',viewCount='" + viewCount + "',feedback='" + feedback + "'"  

            query = "insert into userTbl (word, proun, sentencelnTopic, meanlnDict,etc,viewCount,feedback) values(" + setValue +")"

            cursor.execute(sql)
            return cursor.last_insert_id()
        except:
            return -1

    #select method
    def retriveWord(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "select id, word, proun, sentencelnTopic, meanlnDict,etc,viewCount,feedback from  userTbl where id=" + id
	    cursor.execute(query)
            rs = cursor.fetchall()
            return rs
        except:
            return -1

    #update method
    def updateWord(self, id, word, proun, sentencelnTopic, meanlnDict,etc,viewCount, feedback):
        query = ""
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            if word != '':
                setQuery = "word = '" + word + "',"
            if proun != '':
                setQuery = setQuery + "proun ='" + proun + "',"
            if sentencelnTopic != '':
                setQuery = setQuery + "sentencelnTopic = '" + sentencelnTopic + "',"
            if meanlnDict != '':
                setQuery = setQuery + "meanlnDict = '" + meanlnDict + "',"
            if etc != '':
                setQuery = setQuery + "etc = '" + etc + "',"
            if viewCount != '':
                setQuery = setQuery + "viewCount = '" + viewCount + "',"
            if feedback != '':
                setQuery = setQuery + "feedback = '" + feedback + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            print "setQuery = " + setQuery + "\n"
            query = "update from  wordTbl set " + setQuery + " where id="+id
            print "query = " + query + "\n"
	    cursor.execute(query)
        except:
            print "update failure : " + query

    #delete method
    def deleteWord(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "delete from  wordTbl where id=" + id
	    cursor.execute(query)
        except:
            print "delete failure : " + query


top = Topic()
top.retriveTopic(1)
