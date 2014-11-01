import cgi
import cgitb
form = cgi.FieldStorage()
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head><link rel='stylesheet' type='text/css' href='../combined.css' />"
print " <title> Settings Submitted </title></head><body><div class='header'> </div><div class='main'>"
print "<br> <br> <b>"
print "<h1>Your Settings have been Successfully saved :) !!! <br> <br>"
print "<a href='http://localhost:8000'> << Back</a> </h1> <b>"
with open ('conf.ini','w') as fileOutput:
	fileOutput.write("[report]")
	fileOutput.write("\r\n")
	fileOutput.write("log_file_location:")
	fileOutput.write(form.getvalue('log'))
	
