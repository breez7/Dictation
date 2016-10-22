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
