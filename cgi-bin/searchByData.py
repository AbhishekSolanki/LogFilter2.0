import cgi, cgitb
import socket
import pymongo
from pymongo import MongoClient
import mongoConnection as conn

cgitb.enable()
list1=[]
data = cgi.FieldStorage()

varFrom = (int(data["from"].value)*(1024*1024))
varTo = (int(data["to"].value)*(1024*1024))+1

result=conn.db.aggregate([{'$group':{'_id':"$username",'total':{'$sum':"$byte_transferred"}}},{'$match':{'total':{'$gte':varFrom,'$lte':varTo}}}])
total_data=conn.db.aggregate([{'$group':{'_id':'null','count':{'$sum':"$byte_transferred"}}}])
temp=total_data['result']
for i in temp:
    totalData=(int(i['count'])//(1024*1024))

print "Content-Type: text/html\n"
abc = result['result']
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
</script>"""
print """About <big><b>"""+str(totalData)+""" MB</b></big> data has been used till now"""

table="""<table id="example" class="display" cellspacing="0" width="10%">
        <thead>
            <tr>
                <th><center>Username</center></th>
                <th></center>Data Used</center></th>
                
            </tr>
        </thead><tbody>"""
print abc1
print table
for i in abc:
    total=(int(i['total'])/(1024*1024))
    print """<tr><td><center>"""+str(i['_id'])+"""</center></td><td><center>"""+str(total)+""" MB</center></td></tr>"""
    "</tbody></table>"""
