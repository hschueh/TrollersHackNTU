var pos_count = 0;
var pos_x = 100;
var pos_y = 260;
var width = 370;
var height = 500;
var padding_top = 0;
var static_img_url = '/static/img/';

$(document).ready(function(){
	var token = localStorage.getItem("gcmToken");
	var facebookID = "";
	var csrf_token = $("#csrf-var").attr("value");
	var gender = "M";
    
	$('#ok-key').click(function(){
		console.log("create_user_submit");
		$.ajax({
			url: "/create_user_submit/",
			type: "POST",
			data: {
				"gender": gender, 
				"facebookID": facebookID,
				"token": token,
				"csrfmiddlewaretoken": csrf_token
			},
			success: function(){
				console.log("Create new User!");
			},
			error: function(xhr, errmsg, err){
				console.log(xhr.status + ": " + xhr.responseText);
			}
		})
		.done(function(){
			window.location.href = "/income/";
		});
	});
	$('#switchBtn').click(function(){
		if(gender == "M") {
			console.log("gender = M");
			gender = "F";
			$('#heroImg').attr('src', $("#girl_pic").attr("value"));
		}
		else {
			gender = "M";
			$('#heroImg').attr('src', $("#boy_pic").attr("value"));
		}
	});
	
	
	var svg = d3.select(".main-layout").append("svg").attr({
		"id": "main-svg",
		"width": "100%",
		"height": height
	});
    var el   = document.getElementById("main-svg"); // or other selector like querySelector()
    var rect = el.getBoundingClientRect(); 

	
	
	var bg_sky = svg.append("svg:image").attr({
		'width': rect.width,
		'height': rect.width*3.0/3.7,
		'x': 0,
		'y': 0 + padding_top,
		'xlink:href': bg_pic_dict['bg_sky'],
		'image-rendering':'optimizeQuality'
	});


	var bg_ground = svg.append("svg:image").attr({
		'width': rect.width,
		'height': rect.width*3.0/3.7,
		'x': 0,
		'y': 100 + padding_top,
		'xlink:href': bg_pic_dict['bg_ground'],
		'image-rendering':'optimizeQuality'
	});

});

