$(document).ready(function(){
	var charge_state = $("#chargestate-var").attr("value");
	
	$.get("/statistic_data/",function(data){
		var width = 370, height = 350, radius = Math.min(width,height)/2;

		console.log(data);
		svg = d3.select("div.graph-block").append("svg").attr({
			"id": "main-graph",
			"width": width,
			"height": height
		});


	});
});