#!/usr/bin/python
import cgi, cgitb
import mongoConnection as conn
cgitb.enable()
def users_graph(opt):
    result=conn.db.aggregate([{'$group':{'_id':'$username','count':{'$sum':1}}},{'$sort':{'count':-1}},{'$limit':opt}])
    abc=result['result']
    table_data=""
    bar_data=""
    donut_chart=""
    for i in abc:
        ids=str(i['_id'])
        count=str(i['count'])
        table_data+="<tr><td>"+ids+"</td><td>"+count+"</td></tr>"
        bar_data+="{ y:'"+ids+"', a:"+count+"},"
        donut_chart+="{ label:'"+ids+"', value:"+count+"},"
    response = """
<div id= "users_graph">
	<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example').dataTable( {
        "pagingType": "full_numbers"

		} );
		$('#example_length').remove();
		$('#example_info').remove();
		$('#example_filter').css("margin-top","-18px");
		$('#example_filter').css("margin-bottom","-25px");
		$('#example_paginate').css("margin-left","-25px");
		$('#example_first').css("margin-lef",-20);
$("input[type='search']").css('width',255);
$("input[type='search']").css('height',25);

		
	} );
</script>


<script type="text/javascript">
jQuery(document).ready(function($) 
{
	// Line Charts
	var line_chart_user = $("#line-chart-user");
	
	var line_charts_user = Morris.Bar({
		element: 'line-chart-user',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Hits'],
		redraw: true
		
	});
	
	line_chart_user.parent().attr('style', '');
	
	
	// Donut Chart
	var donut_chart_user = $("#donut-chart-user");
	
	donut_chart_user.parent().show();
	
	var donut_charts_user = Morris.Donut({
		element: 'donut-chart-user',
		data: [
        
			"""+donut_chart+"""
		],
		colors: ['#707f9b', '#455064', '#242d3c']
	});
	
	donut_chart_user.parent().attr('style', '');
	
	
	// Area Chart
	var area_chart_user = $("#area-chart-user");
	
	area_chart_user.parent().show();
	
	var area_charts_user = Morris.Area({
		element: 'area-chart-user',
		data: [
			"""+bar_data+"""
			
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Hits'],
		lineColors: ['#303641', '#576277'],
		parseTime: false
	});
	
	area_chart_user.parent().attr('style', '');
	
	// Rickshaw
	var seriesData = [ [], [] ];
	
	var random = new Rickshaw.Fixtures.RandomData(50);
	
	for (var i = 0; i < 50; i++) 
	{
		random.addData(seriesData);
	}

	setInterval( function() {
		random.removeData(seriesData);
		random.addData(seriesData);
		//graph.update();
	
	}, 500 );
});


function getRandomInt(min, max) 
{
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
</script>
<div class="row">
	<div class="col-sm-8">
	
		<div class="panel panel-primary" id="charts_env1">
		
			<div class="panel-heading">
				<div class="panel-title">Users</div>
				
				<div class="panel-options">
					<ul class="nav nav-tabs">
						<li class=""><a href="#area-user" data-toggle="tab">Area Chart</a></li>
						<li class="active"><a href="#line-user" data-toggle="tab">Bar Charts</a></li>
						<li class=""><a href="#pie-user" data-toggle="tab">Pie Chart</a></li>
					</ul>
				</div>
			</div>
	
			<div class="panel-body">
			
				<div class="tab-content">
				
					<div class="tab-pane" id="area-user">							
						<div id="area-chart-user" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane active" id="line-user">
						<div id="line-chart-user" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane" id="pie-user">
						<div id="donut-chart-user" class="morrischart" style="height: 300px;"></div>
					</div>
					
				</div>
				
			</div>

			
		</div>	


	</div>

	<div class="col-sm-4">
<table id="example" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>User</th>
                <th>Hits</th>
            </tr>
        </thead>
 
 
    <tbody>"""+table_data+"""</tbody>
            </table>
        </div>
    </div>
</div>"""
    
  
    
    print response

def mime_graph(opt):
    result1=conn.db.aggregate([{'$group':{'_id':'$mime','count':{'$sum':1}}},{'$sort':{'count':-1}},{'$limit':opt}])
    abc1=result1['result']
    table_data=""
    bar_data=""
    donut_chart=""
    for i in abc1:
        ids=str(i['_id'])
        count=str(i['count'])
        table_data+="<tr><td>"+ids+"</td><td>"+count+"</td></tr>"
        bar_data+="{ y:'"+ids+"', a:"+count+"},"
        donut_chart+="{ label:'"+ids+"', value:"+count+"},"
    response = """
<div id= "mime_graph">

<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example1').dataTable( {
        "pagingType": "full_numbers"

		} );
                $('#example1_length').remove();
		$('#example1_info').remove();
		$('#example1_filter').css("margin-top","0px");
		$('#example1_filter').css("margin-bottom","-25px");
		$('#example1_paginate').css("margin-left","-25px");
		$('#example1_first').css("margin-lef",-20);
		$('#mime_graph').css("margin-top",20);
		$("input[type='search']").css('width',255);
$("input[type='search']").css('height',25);

		
	} );
</script>


<script type="text/javascript">





jQuery(document).ready(function($) 
{
	// Line Charts
	var line_chart_mime = $("#line-chart-mime");
	
	var line_charts_mime = Morris.Bar({
		element: 'line-chart-mime',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		redraw: true
	});
	
	line_chart_mime.parent().attr('style', '');
	
	
	// Donut Chart
	var donut_chart_mime = $("#donut-chart-mime");
	
	donut_chart_mime.parent().show();
	
	var donut_charts_mime = Morris.Donut({
		element: 'donut-chart-mime',
		data: [
			"""+donut_chart+"""
		],
		colors: ['#707f9b', '#455064', '#242d3c']
	});
	
	donut_chart_mime.parent().attr('style', '');
	
	
	// Area Chart
	var area_chart_mime = $("#area-chart-mime");
	
	area_chart_mime.parent().show();
	
	var area_charts_mime = Morris.Area({
		element: 'area-chart-mime',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		lineColors: ['#303641'],
		parseTime: false
	});
	
	area_chart_mime.parent().attr('style', '');
	
	// Rickshaw
	var seriesData = [ [], [] ];
	
	var random = new Rickshaw.Fixtures.RandomData(50);
	
	for (var i = 0; i < 50; i++) 
	{
		random.addData(seriesData);
	}

	setInterval( function() {
		random.removeData(seriesData);
		random.addData(seriesData);
		//graph.update();
	
	}, 500 );
});


function getRandomInt(min, max) 
{
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
</script>
<div class="row">
	<div class="col-sm-8">
	
		<div class="panel panel-primary" id="charts_env1">
		
			<div class="panel-heading">
				<div class="panel-title">MIMEs</div>
				
				<div class="panel-options">
					<ul class="nav nav-tabs">
						<li class=""><a href="#area-mime" data-toggle="tab">Area Chart</a></li>
						<li class="active"><a href="#line-mime" data-toggle="tab">Bar Charts</a></li>
						<li class=""><a href="#pie-mime" data-toggle="tab">Pie Chart</a></li>
					</ul>
				</div>
			</div>
	
			<div class="panel-body">
			
				<div class="tab-content">
				
					<div class="tab-pane" id="area-mime">							
						<div id="area-chart-mime" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane active" id="line-mime">
						<div id="line-chart-mime" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane" id="pie-mime">
						<div id="donut-chart-mime" class="morrischart" style="height: 300px;"></div>
					</div>
					
				</div>
				
			</div>

			
		</div>	


	</div>

	<div class="col-sm-4">
<table id="example1" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Mime</th>
                <th>Count</th>
            </tr>
        </thead>
 
 
        <tbody>
           """+table_data+"""
        </tbody>
    </table>
		

	</div>
</div>
</div>
"""
    print response


def profiles_graph(opt):
    result2=conn.db.aggregate([{'$group':{'_id':'$filter_profile','count':{'$sum':1}}},{'$sort':{'count':-1}},{'$limit':opt}])
    abc2=result2['result']
    table_data=""
    bar_data=""
    donut_chart=""
    for i in abc2:
        ids=str(i['_id'])
        count=str(i['count'])
        table_data+="<tr><td>"+ids+"</td><td>"+count+"</td></tr>"
        bar_data+="{ y:'"+ids+"', a:"+count+"},"
        donut_chart+="{ label:'"+ids+"', value:"+count+"},"
    response = """
<div id= "profiles_graph">

<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example2').dataTable( {
        "pagingType": "full_numbers"

		} );
                $('#example2_length').remove();
		$('#example2_info').remove();
		$('#example2_filter').css("margin-top","0px");
		$('#example2_filter').css("margin-bottom","-25px");
		$('#example2_paginate').css("margin-left","-25px");
		$('#example2_first').css("margin-lef",-20);
		$('#profiles_graph').css("margin-top",20);
		$("input[type='search']").css('width',255);
$("input[type='search']").css('height',25);

		
	} );
</script>

<script type="text/javascript">
jQuery(document).ready(function($) 
{
	// Line Charts
	var line_chart_profile = $("#line-chart-profile");
	
	var line_charts_profile = Morris.Bar({
		element: 'line-chart-profile',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		redraw: true
	});
	
	line_chart_profile.parent().attr('style', '');
	
	
	// Donut Chart
	var donut_chart_profile = $("#donut-chart-profile");
	
	donut_chart_profile.parent().show();
	
	var donut_charts_profile = Morris.Donut({
		element: 'donut-chart-profile',
		data: [
			"""+donut_chart+"""
		],
		colors: ['#707f9b', '#455064', '#242d3c']
	});
	
	donut_chart_profile.parent().attr('style', '');
	
	
	// Area Chart
	var area_chart_profile = $("#area-chart-profile");
	
	area_chart_profile.parent().show();
	
	var area_charts_profile = Morris.Area({
		element: 'area-chart-profile',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		lineColors: ['#303641'],
		parseTime:false
	});
	
	area_chart_profile.parent().attr('style', '');
	
	// Rickshaw
	var seriesData = [ [], [] ];
	
	var random = new Rickshaw.Fixtures.RandomData(50);
	
	for (var i = 0; i < 50; i++) 
	{
		random.addData(seriesData);
	}

	setInterval( function() {
		random.removeData(seriesData);
		random.addData(seriesData);
		//graph.update();
	
	}, 500 );
});


function getRandomInt(min, max) 
{
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
</script>
<div class="row">
	<div class="col-sm-8">
	
		<div class="panel panel-primary" id="charts_env1">
		
			<div class="panel-heading">
				<div class="panel-title">Profiles</div>
				
				<div class="panel-options">
					<ul class="nav nav-tabs">
						<li class=""><a href="#area-profile" data-toggle="tab">Area Chart</a></li>
						<li class="active"><a href="#line-profile" data-toggle="tab">Bar Charts</a></li>
						<li class=""><a href="#pie-profile" data-toggle="tab">Pie Chart</a></li>
					</ul>
				</div>
			</div>
	
			<div class="panel-body">
			
				<div class="tab-content">
				
					<div class="tab-pane" id="area-profile">							
						<div id="area-chart-profile" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane active" id="line-profile">
						<div id="line-chart-profile" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane" id="pie-profile">
						<div id="donut-chart-profile" class="morrischart" style="height: 300px;"></div>
					</div>
					
				</div>
				
			</div>

			
		</div>	


	</div>

	<div class="col-sm-4">
<table id="example2" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Profile</th>
                <th>Count</th>
            </tr>
        </thead>
 
 
        <tbody>
            """+table_data+"""
        </tbody>
    </table>
		

	</div>
</div>
</div>
"""
    print response


def status_graph(opt):
    result3=conn.db.aggregate([{'$group':{'_id':'$httpstatus','count':{'$sum':1}}},{'$sort':{'count':-1}},{'$limit':opt}])
    abc3=result3['result']
    table_data=""
    bar_data=""
    donut_chart=""
    for i in abc3:
        ids=str(i['_id'])
        count=str(i['count'])
        table_data+="<tr><td>"+ids+"</td><td>"+count+"</td></tr>"
        bar_data+="{ y:'"+ids+"', a:"+count+"},"
        donut_chart+="{ label:'"+ids+"', value:"+count+"},"
    response = """
<div id= "status_graph">

<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example3').dataTable( {
        "pagingType": "full_numbers"

		} );
                $('#example3_length').remove();
		$('#example3_info').remove();
		$('#example3_filter').css("margin-top","0px");
		$('#example3_filter').css("margin-bottom","-25px");
		$('#example3_paginate').css("margin-left","-25px");
		$('#example3_first').css("margin-lef",-20);
		$('#status_graph').css("margin-top",20);
		$("input[type='search']").css('width',255);
$("input[type='search']").css('height',25);

		
	} );
</script>


<script type="text/javascript">
jQuery(document).ready(function($) 
{
	// Line Charts
	var line_chart_status = $("#line-chart-status");
	
	var line_charts_status = Morris.Bar({
		element: 'line-chart-status',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		redraw: true
	});
	
	line_chart_status.parent().attr('style', '');
	
	
	// Donut Chart
	var donut_chart_status = $("#donut-chart-status");
	
	donut_chart_status.parent().show();
	
	var donut_charts_status = Morris.Donut({
		element: 'donut-chart-status',
		data: [
			"""+donut_chart+"""
		],
		colors: ['#707f9b', '#455064', '#242d3c']
	});
	
	donut_chart_status.parent().attr('style', '');
	
	
	// Area Chart
	var area_chart_status = $("#area-chart-status");
	
	area_chart_status.parent().show();
	
	var area_charts_status = Morris.Area({
		element: 'area-chart-status',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		lineColors: ['#303641', '#576277'],
		parseTime: false
	});
	
	area_chart_status.parent().attr('style', '');
	
	// Rickshaw
	var seriesData = [ [], [] ];
	
	var random = new Rickshaw.Fixtures.RandomData(50);
	
	for (var i = 0; i < 50; i++) 
	{
		random.addData(seriesData);
	}

	setInterval( function() {
		random.removeData(seriesData);
		random.addData(seriesData);
		//graph.update();
	
	}, 500 );
});


function getRandomInt(min, max) 
{
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
</script>
<div class="row">
	<div class="col-sm-8">
	
		<div class="panel panel-primary" id="charts_env1">
		
			<div class="panel-heading">
				<div class="panel-title">Status</div>
				
				<div class="panel-options">
					<ul class="nav nav-tabs">
						<li class=""><a href="#area-status" data-toggle="tab">Area Chart</a></li>
						<li class="active"><a href="#line-status" data-toggle="tab">Bar Charts</a></li>
						<li class=""><a href="#pie-status" data-toggle="tab">Pie Chart</a></li>
					</ul>
				</div>
			</div>
	
			<div class="panel-body">
			
				<div class="tab-content">
				
					<div class="tab-pane" id="area-status">							
						<div id="area-chart-status" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane active" id="line-status">
						<div id="line-chart-status" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane" id="pie-status">
						<div id="donut-chart-status" class="morrischart" style="height: 300px;"></div>
					</div>
					
				</div>
				
			</div>

			
		</div>	


	</div>

	<div class="col-sm-4">
<table id="example3" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Status</th>
                <th>Count</th>
            </tr>
        </thead>
 
 
        <tbody>
           """+table_data+"""
        </tbody>
    </table>

		

	</div>
</div>
</div>
"""
    print response

def filters_graph(opt):
    result4=conn.db.aggregate([{'$group':{'_id':'$filter_name','count':{'$sum':1}}},{'$sort':{'count':-1}},{'$limit':opt}])
    abc4=result4['result']
    table_data=""
    bar_data=""
    donut_chart=""
    for i in abc4:
        ids=str(i['_id'])
        count=str(i['count'])
        table_data+="<tr><td>"+ids+"</td><td>"+count+"</td></tr>"
        bar_data+="{ y:'"+ids+"', a:"+count+"},"
        donut_chart+="{ label:'"+ids+"', value:"+count+"},"
    response = """
<div id= "filters_graph">
<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example4').dataTable( {
        "pagingType": "full_numbers"

		} );
                $('#example4_length').remove();
		$('#example4_info').remove();
		$('#example4_filter').css("margin-top","0px");
		$('#example4_filter').css("margin-bottom","-25px");
		$('#example4_paginate').css("margin-left","-25px");
		$('#example4_first').css("margin-lef",-20);
		$('#filters_graph').css("margin-top",20);
		$("input[type='search']").css('width',255);
$("input[type='search']").css('height',25);

		
	} );
</script>


<script type="text/javascript">
jQuery(document).ready(function($) 
{
	// Line Charts
	var line_chart_filter = $("#line-chart-filter");
	
	var line_charts_filter = Morris.Bar({
		element: 'line-chart-filter',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		redraw: true
	});
	
	line_chart_filter.parent().attr('style', '');
	
	
	// Donut Chart
	var donut_chart_filter = $("#donut-chart-filter");
	
	donut_chart_filter.parent().show();
	
	var donut_chart3 = Morris.Donut({
		element: 'donut-chart-filter',
		data: [
			"""+donut_chart+"""
		],
		colors: ['#707f9b', '#455064', '#242d3c']
	});
	
	donut_chart_filter.parent().attr('style', '');
	
	
	// Area Chart
	var area_chart_filter = $("#area-chart-filter");
	
	area_chart_filter.parent().show();
	
	var area_charts_filter = Morris.Area({
		element: 'area-chart-filter',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		lineColors: ['#303641'],
		parseTime: false
	});
	
	area_chart_filter.parent().attr('style', '');
	
	// Rickshaw
	var seriesData = [ [], [] ];
	
	var random = new Rickshaw.Fixtures.RandomData(50);
	
	for (var i = 0; i < 50; i++) 
	{
		random.addData(seriesData);
	}

	setInterval( function() {
		random.removeData(seriesData);
		random.addData(seriesData);
		//graph.update();
	
	}, 500 );
});


function getRandomInt(min, max) 
{
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
</script>
<div class="row">
	<div class="col-sm-8">
	
		<div class="panel panel-primary" id="charts_env1">
		
			<div class="panel-heading">
				<div class="panel-title">Filters</div>
				
				<div class="panel-options">
					<ul class="nav nav-tabs">
						<li class=""><a href="#area-filter" data-toggle="tab">Area Chart</a></li>
						<li class="active"><a href="#line-filter" data-toggle="tab">Bar Charts</a></li>
						<li class=""><a href="#pie-filter" data-toggle="tab">Pie Chart</a></li>
					</ul>
				</div>
			</div>
	
			<div class="panel-body">
			
				<div class="tab-content">
				
					<div class="tab-pane" id="area-filter">							
						<div id="area-chart-filter" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane active" id="line-filter">
						<div id="line-chart-filter" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane" id="pie-filter">
						<div id="donut-chart-filter" class="morrischart" style="height: 300px;"></div>
					</div>
					
				</div>
				
			</div>

			
		</div>	


	</div>

	<div class="col-sm-4">
<table id="example4" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Filter</th>
                <th>Count</th>
            </tr>
        </thead>
 
 
        <tbody>
            """+table_data+"""
         
        </tbody>
    </table>

		

	</div>
</div>
</div>
"""
    print response

def websites_graph(opt):
    result5=conn.db.aggregate([{'$group':{'_id':'$method_url','count':{'$sum':1}}},{'$sort':{'count':-1}},{'$limit':opt}])
    abc5=result5['result']
    table_data=""
    bar_data=""
    donut_chart=""
    for i in abc5:
        ids=str(i['_id'])
        count=str(i['count'])
        table_data+="<tr><td>"+ids+"</td><td>"+count+"</td></tr>"
        bar_data+="{ y:'"+ids+"', a:"+count+"},"
        donut_chart+="{ label:'"+ids+"', value:"+count+"},"
    response = """
<div id= "websites_graph">

<link rel="stylesheet" type="text/css" href="css/jquery.dataTables.css">
<script src="js/jquery-2.0.3.js"></script>
<script src="js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    $('#example5').dataTable( {
        "pagingType": "full_numbers"

		} );
                $('#example5_length').remove();
		$('#example5_info').remove();
		$('#example5_filter').css("margin-top","0px");
		$('#example5_filter').css("margin-bottom","-25px");
		$('#example5_paginate').css("margin-left","-25px");
		$('#example5_first').css("margin-lef","-20px");
		$('#websites_graph').css("margin-top","20px");
		$("input[type='search']").css('width',"255px");
                $("input[type='search']").css('height',"25px");		
	} );
</script>



<script type="text/javascript">
jQuery(document).ready(function($) 
{
	// Line Charts
	var line_chart_website = $("#line-chart-website");
	
	var line_charts_website = Morris.Bar({
		element: 'line-chart-website',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		redraw: true
	});
	
	line_chart_website.parent().attr('style', '');
	
	
	// Donut Chart
	var donut_chart_website = $("#donut-chart-website");
	
	donut_chart_website.parent().show();
	
	var donut_charts_website = Morris.Donut({
		element: 'donut-chart-website',
		data: [
			"""+donut_chart+"""
		],
		colors: ['#707f9b', '#455064', '#242d3c']
	});
	
	donut_chart_website.parent().attr('style', '');
	
	
	// Area Chart
	var area_chart_website = $("#area-chart-website");
	
	area_chart_website.parent().show();
	
	var area_charts_website = Morris.Area({
		element: 'area-chart-website',
		data: [
			"""+bar_data+"""
		],
		xkey: 'y',
		ykeys: ['a'],
		labels: ['Count'],
		lineColors: ['#303641', '#576277'],
		parseTime: false
	});
	
	area_chart_website.parent().attr('style', '');
	
	// Rickshaw
	var seriesData = [ [], [] ];
	
	var random = new Rickshaw.Fixtures.RandomData(50);
	
	for (var i = 0; i < 50; i++) 
	{
		random.addData(seriesData);
	}

	setInterval( function() {
		random.removeData(seriesData);
		random.addData(seriesData);
		//graph.update();
	
	}, 500 );
});


function getRandomInt(min, max) 
{
	return Math.floor(Math.random() * (max - min + 1)) + min;
}
</script>
<div class="row">
	<div class="col-sm-8">
	
		<div class="panel panel-primary" id="charts_env1">
		
			<div class="panel-heading">
				<div class="panel-title">Websites</div>
				
				<div class="panel-options">
					<ul class="nav nav-tabs">
						<li class=""><a href="#area-website" data-toggle="tab">Area Chart</a></li>
						<li class="active"><a href="#line-website" data-toggle="tab">Bar Charts</a></li>
						<li class=""><a href="#pie-website" data-toggle="tab">Pie Chart</a></li>
					</ul>
				</div>
			</div>
	
			<div class="panel-body">
			
				<div class="tab-content">
				
					<div class="tab-pane" id="area-website">							
						<div id="area-chart-website" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane active" id="line-website">
						<div id="line-chart-website" class="morrischart" style="height: 300px"></div>
					</div>
					
					<div class="tab-pane" id="pie-website">
						<div id="donut-chart-website" class="morrischart" style="height: 300px;"></div>
					</div>
					
				</div>
				
			</div>

			
		</div>	


	</div>

	<div class="col-sm-4">
<table id="example5" class="display" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Name</th>
                <th>Position</th>
            </tr>
        </thead>
 
 
        <tbody>
            """+table_data+"""
         
        </tbody>
    </table>

		

	</div>
</div>
</div>
"""
    print response

data = cgi.FieldStorage()

if(str(data["caller"].value)=="dropdown"):
    opt = int(data["option"].value)
    if(str(data["users"].value)=="1"):
        users_graph(opt)
    if(str(data["mime"].value)=="1"):
        mime_graph(opt)
    if(str(data["profiles"].value)=="1"):
        profiles_graph(opt)
    if(str(data["status"].value)=="1"):
        status_graph(opt)
    if(str(data["filters"].value)=="1"):
        filters_graph(opt)
    if(str(data["websites"].value)=="1"):
        websites_graph(opt)
    
if(str(data["caller"].value)=="checkbox"):
    opt=""
    if(str(data["topValue"].value)!="0"):
        opt = int(data["topValue"].value)

    if(str(data["option"].value)=="users"):
         print "Content-Type: text/html\n"
         users_graph(opt)
         #print "<p id='users_graph'>user</p>" #graph thing here !!!
    if(str(data["option"].value)=="mime"):
         print "Content-Type: text/html\n"
         mime_graph(opt)
         #print "<p id='mime_graph'>mime</p>" #graph thing here !!!
    if(str(data["option"].value)=="profiles"):
         print "Content-Type: text/html\n"
         profiles_graph(opt)
         #print "<p id='profiles_graph'>profiles</p>" #graph thing here !!!
    if(str(data["option"].value)=="status"):
         print "Content-Type: text/html\n"
         status_graph(opt)
         #print "<p id='status_graph'>status</p>" #graph thing here !!!
    if(str(data["option"].value)=="filters"):
         print "Content-Type: text/html\n"
         filters_graph(opt)
         #print "<p id='filters_graph'>filters</p>" #graph thing here !!!
    if(str(data["option"].value)=="websites"):
         print "Content-Type: text/html\n"
         websites_graph(opt)
        # print response #"<p id='websites_graph'>Websites</p>"
    if(str(data["option"].value)=="all"):
        users_graph(opt)
        mime_graph(opt)
        websites_graph(opt)


