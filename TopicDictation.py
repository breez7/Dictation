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
        self.dateAt = ""
        self.userWrittenScript = ""
        self.id = -1

    #create method
    def createTopicDictation(self, title, dateAt, userWrittenScript):

        query = ""
	try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            setValue = "title='" + title + "',dateAt='" + dateAt+ "',userWrittenScript='" + userWrittenScript + "'" 

            query = "insert into topicDictationTbl (title, dateAt, userWrittenScript) values(" + setValue +")"

            cursor.execute(sql)
            return cursor.last_insert_id()
        except:
            return -1

    #select method
    def retriveTopicDictation(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "select id, title, dateAt, userWrittenScript from topicDictationTbl where id=" + id
	    cursor.execute(query)
            rs = cursor.fetchall()
            return rs
        except:
            return -1

    #update method
    def updateTopic(self, id, title, dateAt, userWrittenScript):
        query = ""
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            if title != '':
                setQuery = "title = '" + title + "',"
            if dateAt != '':
                setQuery = setQuery + "dateAt ='" + dateAt + "',"
            if userWrittenScript != '':
                setQuery = setQuery + "userWrittenScript = '" + userWrittenScript + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            print "setQuery = " + setQuery + "\n"
            query = "update from topicDictationTbl set " + setQuery + " where id="+id
            print "query = " + query + "\n"
	    cursor.execute(query)
        except:
            print "update failure : " + query

    #delete method
    def deleteTopicDictation(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "delete from topicDictationTbl where id=" + id
	    cursor.execute(query)
        except:
            print "delete failure : " + query
