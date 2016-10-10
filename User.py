#!/usr/bin/python
# -*- coding: utf8 -*-
import MySQLdb

class User:

    #database connection info
    host="localhost"
    db="englishstudy"
    user="enlishstudy"
    passwd="englishstudy"
    charset="utf8"

    #init method
    def __init__(self):
        self.id = ""
        self.name = ""
        self.password = ""
        self.descripttion = ""
        self.email = ""

    #createUser method
    def createUser(self, name, password, description, email):

        query = ""
	try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            setValue = "name='" + name + "',password='" + password + "',description='" + description + "',script='" + script + "'" 

            query = "insert into userTbl (name, password, description, email) values(" + setValue +")"

            cursor.execute(sql)
            return cursor.last_insert_id()
        except:
            return -1

    #select method
    def retriveUser(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "select id, name, password, description, email from userTbl where id=" + id
	    cursor.execute(query)
            rs = cursor.fetchall()
            return rs
        except:
            return -1

    #update method
    def updateUser(self, id, name, password, description, email):
        query = ""
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            if name != '':
                setQuery = "name = '" + name + "',"
            if description != '':
                setQuery = setQuery + "description ='" + description + "',"
            if email != '':
                setQuery = setQuery + "email = '" + email + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            print "setQuery = " + setQuery + "\n"
            query = "update from  userTbl set " + setQuery + " where id="+id
            print "query = " + query + "\n"
	    cursor.execute(query)
        except:
            print "update failure : " + query

    #delete method
    def deleteUser(self,id):
        try:
            connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "delete from  userTbl where id=" + id
	    cursor.execute(query)
        except:
            print "delete failure : " + query


top = Topic()
top.retriveTopic(1)
