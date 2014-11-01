import cgi, cgitb
import socket
import pymongo
from pymongo import MongoClient
from datetime import datetime
import mongoConnection as conn

cgitb.enable()
list1=[]
data = cgi.FieldStorage()

search_str = str(data["option"].value)
k=1
dict1={}
if(search_str!=""):
    tstart = datetime.now()
    result = conn.db.aggregate([{'$match':{'method_url': {'$regex':search_str}}},{'$group':{'_id':'$method_url','count':{'$sum':1}}},{'$sort':{'count':-1}}])
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
                <th>Website</th>
                <th>Clicks</th>
                
            </tr>
        </thead><tbody>"""
        print abc1
        diff = tend-tstart
        print "About <big><b>"+ str(len(abc)) +"</b></big> results (<big><b>" +str("%s.%s" % (diff.seconds, (diff.microseconds)/1000))+"</b></big> seconds)"                 
        for i in abc:
            print """<tr><td>"""+str(i['_id'])+"""</td><td>"""+str(+i['count'])+"""</td></tr>        """
        end="</tbody></table>"""
        print end
    else:
        print """<h1 style="color:red"><center>Sorry !<b></h1>\n
            <center><h4>Your search <big><I>'"""+search_str+"""'</big></I> did not match any document.</h4></center> """

	
        
