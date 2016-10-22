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
    def createUser(self, id, password, name, description, email):

        query = ""
        #connector = MySQLdb.connect(host, db, user, passwd, charset)
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")

	try:
            #connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = """insert into userTbl (loginId, loginPw, name, description, email) values(%s,%s,%s,%s,%s);"""

            cursor.execute(query,(id,password,name,description,email))
            connector.commit()
            #return cursor.last_insert_id()
            return 'success'

        except:
            import traceback
            traceback.print_exc()
            return -1
        finally:
            connector.close()
            


    #select method
    def retriveUser(self,id):
        #connector = MySQLdb.connect(host, db, user, passwd, charset)
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")

        try:
            cursor = connector.cursor()

            query = "select loginId, loginPw,name, description, email from userTbl where id=%s"  
	    cursor.execute(query, (id))
            connector.commit()
            rs = cursor.fetchall()
            print rs;
            #return rs
        except:
            import traceback
            traceback.print_exc()
            return -1
        finally:
            connector.close()

    #update method
    def updateUser(self, id, name, password, description, email):

        query = ""

        #connector = MySQLdb.connect(host, db, user, passwd, charset)
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")
        try:
            cursor = connector.cursor()

            if name != '':
                setQuery = "name = '" + name + "',"
            if description != '':
                setQuery = setQuery + "description ='" + description + "',"
            if email != '':
                setQuery = setQuery + "email = '" + email + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            query = "update userTbl set " + setQuery + " where id=%s"
	    cursor.execute(query,(id))
            connector.commit()
        except:
            import traceback
            traceback.print_exc()
            print "update failure : " + query
        finally:
            connector.close()

    #delete method
    def deleteUser(self,id):
        #connector = MySQLdb.connect(host, db, user, passwd, charset)
        connector = MySQLdb.connect(host="localhost", db="englishstudy", user="englishstudy", passwd="englishstudy", charset="utf8")
        query = ''

        try:
            cursor = connector.cursor()

            query = "delete from  userTbl where id=%s"
	    cursor.execute(query,(id))
            connector.commit()
            print "delete success"
        except:
            import traceback
            traceback.print_exc()
            print "delete failure : " + query
        finally:
            connector.close()


#test
#user = User()
#result=user.createUser('xiger8','1234','test','test description','xiger78@gmail.com');
#result=user.retriveUser('7');
#result=user.updateUser('7','nameupdate','1234','update description','xiger78@naver.com');
#result=user.deleteUser('1');
#print result
