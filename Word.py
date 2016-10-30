#!/usr/bin/python
# -*- coding: utf8 -*-
import sqlite3
import sys
import os
from urllib import quote,unquote

dbfile = 'word.db'

class Word:

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
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()
            
            query = "insert into wordTbl (word, proun, sentencelnTopic, meanlnDict,etc,viewCount,feedback) values(?,?,?,?,?,?,?)"

            cursor.execute(sql,(word, proun, sentencelnTopic, meanlnDict, etc, viewCount, feedback))
            self.id = cursor.lastrowid
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            return -1
        finally:
            connector.close()
        return self.id

    #select method
    def retriveWord(self,id):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "select id, word, proun, sentencelnTopic, meanlnDict,etc,viewCount,feedback from wordTbl where id=" + str(id)
            cursor.execute(query)
            if len(rs) == 0 or id != rs[0][0]:
                return None
            self.id = id
            self.word = rs[0][1]
            self.proun = rs[0][2]
            self.sentencelnTopic = rs[0][3]
            self.meanlnDict = rs[0][4]
            self.etc = rs[0][5]
            self.viewCount = rs[0][6]
            self.feedback = rs[0][7]
            return rs
        except:
            import traceback
            traceback.print_exc()
            return None
        finally:
            connector.close()

    #select method
    def retriveWordAll(self):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "select id, word, proun, sentencelnTopic, meanlnDict,etc,viewCount,feedback from wordTbl"
            cursor.execute(query)
            rs = cursor.fetchall()
            return rs
        except:
            import traceback
            traceback.print_exc()
            return None
        finally:
            connector.close()

    #update method
    def updateWord(self):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            if word != '':
                setQuery = "word = '" + self.word + "',"
            if proun != '':
                setQuery = setQuery + "proun ='" + self.proun + "',"
            if sentencelnTopic != '':
                setQuery = setQuery + "sentencelnTopic = '" + self.sentencelnTopic + "',"
            if meanlnDict != '':
                setQuery = setQuery + "meanlnDict = '" + self.meanlnDict + "',"
            if etc != '':
                setQuery = setQuery + "etc = '" + self.etc + "',"
            if viewCount != '':
                setQuery = setQuery + "viewCount = '" + self.viewCount + "',"
            if feedback != '':
                setQuery = setQuery + "feedback = '" + self.feedback + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            query = "update from wordTbl set " + setQuery + " where id=?"
            cursor.execute(query,(self.id))
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            print "update failure : " + query
            return False
        finally:
            connector.close()
        return True

    #delete method
    def deleteWord(self,id):
        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "delete from wordTbl where id=" + str(id)
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
