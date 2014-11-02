import cgi, cgitb
import socket
import pymongo
from pymongo import MongoClient
import mongoConnection as conn

cgitb.enable()
list1=[]
data = cgi.FieldStorage()
website="ganpat"
result = conn.db.aggregate([{'$match':{'method_url':{'$regex':website}}},{'$group':{'_id':{'website':"$method_url",'user':"$username",'date':"$date"},'count':{'$sum':1}}},{'$sort':{'count':-1}}])
abc=result['result']
print abc
for i in range(len(abc)):
    #print abc[i]['_id']['user']
    user=abc[i]['_id']['user']
    count=abc[i]['count']
    date=abc[i]['_id']['date']
    print user
    print count
    print date
