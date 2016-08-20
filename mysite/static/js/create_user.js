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
});

