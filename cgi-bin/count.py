#!/usr/bin/python

import cgi, cgitb
import mongoConnection as conn
cgitb.enable()

data = cgi.FieldStorage()

print "Content-Type: text/html\n"
print "Currently we are serving <big><b>"+str(conn.db.count())+"</big><b> logs"

