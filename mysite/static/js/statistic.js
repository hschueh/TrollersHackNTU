$(document).ready(function(){
	var charge_state = $("#chargestate-var").attr("value");

	
	$.get("/statistic_data/" + charge_state,function(data){
		var width = 370, height = 350, radius = Math.min(width,height)/2;

		console.log(data);

		var color = d3.scale.ordinal()
		    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

		var arc = d3.svg.arc()
		    .outerRadius(radius - 10)
		    .innerRadius(0);

		var labelArc = d3.svg.arc()
		    .outerRadius(radius - 40)
		    .innerRadius(radius - 40);

		var pie = d3.layout.pie()
		    .sort(null)
		    .value(function(d) { return d.money; });

		svg = d3.select("div.graph-block").append("svg").attr({
			"id": "main-graph",
			"width": width,
			"height": height
		})
		.append("g")
    	.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");


	});
});