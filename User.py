#!/usr/bin/python
# -*- coding: utf8 -*-
import sqlite3
import sys
import os
from urllib import quote,unquote

dbfile = 'user.db'


class User:

    #init method
    def __init__(self):
        self.id = -1
        self.loginId = ""
        self.loginPw = ""
        self.name = ""
        self.description = ""
        self.email = ""

        if not os.path.isfile(dbfile):
            try:
                print 'creating table'
                connector = sqlite3.connect(dbfile)
                query = "CREATE TABLE IF NOT EXISTS userTbl (id integer primary key autoincrement, loginId text not null,loginPw text not null,name text not null ,description text not null,email text not null)"
                
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

    #createUser method
    def createUser(self, loginId, loginPw, name, description, email):

        query = ""
        connector = sqlite3.connect(dbfile)

	    try:
            #connector = MySQLdb.connect(host, db, user, passwd, charset)
            cursor = connector.cursor()

            query = "insert into userTbl (loginId, loginPw, name, description, email) values(?,?,?,?,?);"

            cursor.execute(query,(loginId,loginPw,name,description,email))
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
    def retriveUser(self,id):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "select id,loginId, loginPw,name, description, email from userTbl where id=" + \
                str(id)  
            cursor.execute(query)
            connector.commit()
            rs = cursor.fetchall()
            if len(rs) == 0 or id != rs[0][0]:
                return None
            self.id = id
            self.loginId = rs[0][1]
            self.loginPw = rs[0][2]
            self.name = rs[0][3]
            self.description = rs[0][4]
            self.email = rs[0][5]
            return rs
        except:
            import traceback
            traceback.print_exc()
            return None
        finally:
            connector.close()

  # select method
    def retriveUserAll(self):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "select id, loginId, loginPw,name, description, email from userTbl"
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
    def updateUser(self):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            if name != '':
                setQuery = "name = '" + self.name + "',"
            if description != '':
                setQuery = setQuery + "description ='" + self.description + "',"
            if email != '':
                setQuery = setQuery + "email = '" + self.email + "',"
        
            #last of comma delete
            setQuery = setQuery[0:len(setQuery)-1]

            query = "update userTbl set " + setQuery + " where id=?"
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
    def deleteUser(self,id):

        query = ""
        connector = sqlite3.connect(dbfile)

        try:
            cursor = connector.cursor()

            query = "delete from  userTbl where id=" + str(id)
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
    user = User()
    if not os.path.isfile(dbfile):
        print 'fail create user'
    else:
        print 'create result id : ' + str(createUser('xiger','1234','NTJ,'test description','xiger78@gmail.com'))
        user.retriveUser(user.id)
        print 'retrive reslt : ' + user.loginId + user.name
        user.name='Nam Taekjin'
        user.updateUser()
      
        user2 = User()
        user2.retriveUser(user.id)
        print 'user loginid:' + user2.loginId
        rs = user.retriveUserAll()
        user.deleteUser(user.id)
        print user.retriveUser(user.id)
    rs = user.retriveUserAll()
    user.retriveUser(1)
    print 'id:' + str(user.id)
    print user.sttResult
    

#test
#user = User()
#result=user.createUser('xiger8','1234','test','test description','xiger78@gmail.com');
#result=user.retriveUser('7');
#result=user.updateUser('7','nameupdate','1234','update description','xiger78@naver.com');
#result=user.deleteUser('1');
#print result
