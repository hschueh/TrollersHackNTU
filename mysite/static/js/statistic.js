$(document).ready(function(){
	var charge_state = $("#chargestate-var").attr("value");

	
	$.getJSON("/statistic_data/" + charge_state,function(data){
		var width = 370, height = 350, radius = Math.min(width,height)/2;

		var color = d3.scale.ordinal()
		    .range(["#3399FF", "#5DAEF8", "#86C3FA", "#ADD6FB", "#D6EBFD"]);

		var arc = d3.svg.arc()
		    .outerRadius(radius - 10)
		    .innerRadius(0);

		/*var labelArc = d3.svg.arc()
		    .outerRadius(radius +15)
		    .innerRadius(radius +10);*/

		var pie = d3.layout.pie()
		    .sort(null)
		    .value(function(d) { return parseFloat(d.money); });

		// console.log(data);

		svg = d3.select("div.graph-block").append("svg").attr({
			"id": "main-graph",
			"width": width,
			"height": height
		})
		.append("g")
    	.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    	// console.log(data);

    	var g = svg.selectAll(".arc")
		      .data(pie(data))
		   	  .enter().append("g")
		      .attr("class", "arc");

		  	g.append("path")
		      .attr("d", arc)
		      .attr("data-legend", function(d){console.log(d.data.name);return d.data.name + "  " + d.data.money + "元"})
		      .style("fill", function(d, i) { return color(i); });

		legend = svg.append("g")
            .attr("class", "legend")
            .attr("transform", "translate(50,100)")
            .style("font-size", "12px")
            .call(d3.legend);


	});
});