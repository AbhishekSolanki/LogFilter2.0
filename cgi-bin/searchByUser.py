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
    result = conn.db.aggregate([{'$match':{'username': {'$regex':search_str}}},{'$group':{'_id':'$method_url','count':{'$sum':1}}},{'$sort':{'count':-1}}])
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
</script>
<table id="example" class="display" cellspacing="0" width="10%">
        <thead>
            <tr>
                <th>Website</th>
                <th>Clicks</th>
                
            </tr>
        </thead><tbody>"""
    print abc1
    for i in abc:
        print """<tr><td>"""+str(i['_id'])+"""</td><td>"""+str(+i['count'])+"""</td></tr>        """
    end="</tbody></table>"""
    print end
	
        
