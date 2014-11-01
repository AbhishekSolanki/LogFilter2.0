#!/usr/bin/python
# -*- coding: cp1252 -*-

import cgi, cgitb
import socket
import pymongo
from pymongo import MongoClient
import mongoConnection as conn

cgitb.enable()
list1=[]
data = cgi.FieldStorage()

search_str = str(data["option"].value)
k=1
dict1={}
if(search_str!=""):
    result = conn.db.aggregate([{'$match':{'method_url': {'$regex':search_str}}},{'$group':{'_id':'$method_url','count':{'$sum':1}}},{'$sort':{'count':-1}}])
    print "Content-Type: text/html\n"
    abc = result['result']
    if(len(abc) !=0):
        for i in abc:
            print """<br data-linkify="br, .plain-text">"""
            print i['_id']
            print " -----------------------"
            print i['count']
            print "</br>"
    else:
        print """<h1 style="color:red"><center>Sorry !<b></h1>\n
            <center><h4>Your search <big><I>'"""+search_str+"""'</big></I> did not match any document.</h4></center> """
    
        
