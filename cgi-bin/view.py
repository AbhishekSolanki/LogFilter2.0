import cgi
import cgitb; cgitb.enable()
import datetime
import ConfigParser
import os
print "Content-type:text/html\r\n\r\n"
def view(datelist1,loc):
	print "<html>"
	print """<head> <title>View</title>	<link rel="stylesheet" type="text/css" href="../../css/combined.css" />"""
	print """<script src="../../js/combined.js"></script></head><body><div class="header"> </div>"""
	print """<div class="tab-container"><br> <br><div class="example25">"""

	if not datelist1:
		print "No Log Reports Found. Go to localhost:8000/ and generate a Report first"
	else:
		print "<b style:color>Report available for the following Day/s</b><br>"
		print "<ul>"
		for date in datelist1:
			print "<li><a href=../"+loc+"/"+date+">"+date+"</a></li>" #niche badhu perfect che? mostly haan 
		print "</ul>"

filename="conf.ini"
config = ConfigParser.ConfigParser()
if os.path.exists(filename):
	config.read("conf.ini")
	loc=config.get("report", "output_location")
datelist1=[]
if not os.path.exists(loc+'/'):
	print "No Log Reports Found. Go to localhost:8000/ and generate a Report first"
else:
	datelist1=os.listdir(loc+'/')
	view(datelist1,loc)