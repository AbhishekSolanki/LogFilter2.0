import cgi, cgitb
import socket
import pymongo
from pymongo import MongoClient
from datetime import datetime
import mongoConnection as conn
import re

cgitb.enable()
list1=[]
data = cgi.FieldStorage()

website = str(data["option"].value)
k=1
dict1={}
if(website!=""):
    tstart = datetime.now()
    result = conn.db.aggregate([{'$match':{'method_url': {'$regex':website}}},{'$group':{'_id':{'website':"$method_url",'user':"$username", 'date':"$date"},'count':{'$sum':1}}},{'$sort':{'count':-1}}])
    tend = datetime.now()
    print "Content-Type: text/html\n"
    abc = result['result']
    if(len(abc) !=0):
        abc1="""<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example').dataTable( {
        "pagingType": "full_numbers"

		} );
		$('#example_length').remove();
	} );
</script>
<table id="example" class="display" cellspacing="0" width="10%">
        <thead>
            <tr>
                <th><center>User</center></th>
                <th><center>Date</center></th>
                <th><center>Click</center></th>
            </tr>
        </thead><tbody>"""
        print abc1
        diff = tend-tstart
        print "About <big><b>"+ str(len(abc)) +"</b></big> results (<big><b>" +str("%s.%s" % (diff.seconds, (diff.microseconds)/1000))+"</b></big> seconds)"                 
        for i in range(len(abc)):
            user=abc[i]['_id']['user']
            count=abc[i]['count']
            date=abc[i]['_id']['date']
            print """<tr><td><center>"""+str(user)+"""</center></td><td><center>"""+str(date)+"""</center></td><td><center>"""+str(count)+"""</center></td></tr>"""
    end="</tbody></table>"""
    print end
else:
        print """<h1 style="color:red"><center>Sorry !<b></h1>\n
            <center><h4>Your search <big><I>'"""+website+"""'</big></I> did not match any document.</h4></center> """

	
        
