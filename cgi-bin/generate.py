#importing begins
from datetime import datetime
import re
import os
import glob
import cgi
import cgitb; cgitb.enable()
from datetime import datetime
import math
from math import log
from math import floor
import webbrowser
import ConfigParser
import fileinput
import mongoConnection as conn
import json
import bson
#import ends
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "</head>"
print "<body>"

form = cgi.FieldStorage() 
config = ConfigParser.ConfigParser()
location = form.getvalue('log')
if os.path.exists(location):
    logfile=open(location,'r')
    expr = re.compile('\"(?P<id1>([^-]*))[^ ]* (?P<elapsed_time>([\d]*)) (?P<client_ip>([.\d]*)) \"(?P<username>([^@]*))[^ ]*\" \"(?P<connection_id>([^ ]*))\" \[(?P<date>([^:]*))\:(?P<time>([^ ]*))] \"(?P<method_url>([^"]*))\" (?P<httpstatus>([\d]*)) (?P<byte_transferred>([\d]*)) \"(?P<referrer_url>([^"]*))\" \"(?P<user_agent>([^"]*))\" (?P<mime>([^ ]*)) \"(?P<filter_name>([^"]*))\" \"(?P<filter_profile>([^"]*))\" \"(?P<interface>([^"]*))')
    dict1={}
    k=1   
    tstart = datetime.now()
    
    for line in logfile:
        temp = expr.search(line)
        id1=temp.group("id1")
        elapsed_time=temp.group("elapsed_time")
        client_ip=temp.group("client_ip")
        username=temp.group("username")
        date=temp.group("date")
        time=temp.group("time")
        method_url=temp.group("method_url")
        httpstatus=temp.group("httpstatus")
        byte_transferred=temp.group("byte_transferred")
        #dict1["referrer_url"]=temp.group("referrer_url")
        user_agent=temp.group("user_agent")
        user_agent1=user_agent.decode('utf-8', 'ignore')
        mime=temp.group("mime")
        filter_name=temp.group("filter_name")
        filter_profile=temp.group("filter_profile")
        interface=temp.group("interface")
    
        conn.db.insert({'id1':id1,'elapsed_time':elapsed_time,'client_ip':client_ip,'username':username,'date':date,'time':time,'httpstatus':httpstatus,'byte_transferred':byte_transferred,'mime':mime,'filter_profile':filter_profile,'interface':interface,'method_url':method_url,'filter_name':filter_name,'user_agent':user_agent1})
        #'user_agent':user_agent
#print di
    tend = datetime.now()
    diff = tend-tstart
    print "Successfully parsed....Visit <a href='http://localhost:8000/view.html'> View </a> to see reports...<br>"
    print "Processing time: <b>"+str("%s.%s" % (diff.seconds, (diff.microseconds)/1000))+"</b> seconds" 
else:
	print "Please enter the correct file. Visit <a href='http://localhost:8000/settings1.html'>Settings</a> "
	
