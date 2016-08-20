var pos_count = 0;
var pos_x = 100;
var pos_y = 260;
var width = 370;
var height = 500;
var padding_top = 0;
var static_img_url = '/static/img/';

$(document).ready(function(){
	console.log(bg_pic_dict);

	var svg = d3.select(".main-layout").append("svg").attr({
		"id": "main-svg",
		// "width": width,
		"height": height
	});

	var bg_sky = svg.append("svg:image").attr({
		'width': 370,
		'height': 300,
		'x': 0,
		'y': 0 + padding_top,
		'xlink:href': bg_pic_dict['bg_sky']
	});

	var bg_ground = svg.append("svg:image").attr({
		'width': 370,
		'height': 300,
		'x': 0,
		'y': 100 + padding_top,
		'xlink:href': bg_pic_dict['bg_ground']
	});

	var bg_ground = svg.append("svg:image").attr({
		'width': 370,
		'height': 300,
		'x': 0,
		'y': 100 + padding_top,
		'xlink:href': bg_pic_dict['bg_ground']
	});

	var boss = svg.append("svg:image").attr({
		'width': 176,
		'height': 140,
		'x': 90,
		'y': 160 + padding_top,
		'xlink:href': static_img_url + pic_dict['boss']
	});

	var wpn = svg.append("svg:image").attr({
		'width': 88,
		'height': 70,
		'x': 200,
		'y': 380 + padding_top,
		'xlink:href': pic_dict['wpn']
	});

	var hero = svg.append("svg:image").attr({
		'width': 176,
		'height': 140,
		'x': 90,
		'y': 360 + padding_top,
		'xlink:href': function(){
			if(gender)
				return static_img_url + "hero_boy.png";
			else
				return static_img_url + "hero_girl.png";
		}
	});

	window.setInterval(function(){
		hero.transition().duration(250).attr("y", 360 + padding_top - 20)
		.each("end", function(){
			hero.transition().duration(250).attr("y", 360 + padding_top);
		});

		wpn.transition().duration(250).attr("y", 380 + padding_top - 20)
		.each("end", function(){
			wpn.transition().duration(250).attr("y", 380 + padding_top);
		});
	}, 500);

	

	window.setInterval(function(){
		// var parentOffset = $("#rect-btn").parent().offset(); 
		if (pos_count%10 == 0){
			if (pos_count == 0) pos_x = 100;
			else pos_x += 60;
		}
		var txt = svg.append("text").attr({
			'x': pos_x,
			'y': pos_y
		})
		.style({
			"font-size": "20px",
			"fill": "red"
		})
		.text(dps)
		.transition().duration(1000)
		.attr({
			"y": pos_y - 100
		})
		.style("opacity", 0);

		txt.remove();

		if (pos_count == 29) pos_count = 0;
		else pos_count++;

	}, 100);


});

