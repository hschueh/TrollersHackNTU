var count = 0;


$(document).ready(function(){
	var csrf_token = $("#csrf-var").attr("value");

	$.get("/mission_data/", function(data){
		data = JSON.parse(data);
		// console.log(data);

		for(var i in data){
			if (data[i]['missionType'] == "meal"){
				count++;
				if(data[i]['status'] == "success"){
					$("#checkbox-" + count).attr("checked", true);
					$("#checkbox-" + count).prop("disabled", false);
				}
			}
		}

		$("div.form-group").click(function(e){
			if($(this).parent().find("input").attr("checked") == "checked"){
				// console.log(e.pageX);
				// console.log(e.pageY);
				var id = $(this).find("input").attr("id");
				var div_exp = d3.select(".container").append("div").style({
					"position": "absolute",
					"top": e.pageY + "px",
					"left": e.pageX + "px",
					"z-index": 20,
					"color": "blue",
					"font-size": "20px"
				});
				$('<p>+50 EXP!</p>').appendTo(div_exp);
				
				div_exp.transition().duration(800).style({
					"top": (e.pageY-150) + "px",
					"left": (e.pageX+150) + "px",
					"opacity": 0
				})
				.each("end",function(){
					var div_gold = d3.select(".container").append("div").style({
						"position": "absolute",
						"top": (e.pageY) + "px",
						"left": (e.pageX+30) + "px",
						"z-index": 20,
						"color": "orange",
						"font-size": "20px"
					});
					$('<p>+50 GOLD!</p>').appendTo(div_gold);
					div_gold.transition().duration(800).style({
						"top": (e.pageY-150) + "px",
						"left": (e.pageX+150) + "px",
						"opacity": 0
					})
					.each("end", function(){
						$("#" + id).parent().remove();
					});
					
				});

				var id_num = id.split("-")[1];

				$.post("/mission_complete/", {"id": id_num, "csrfmiddlewaretoken": csrf_token},function(status){
					console.log("Status: " + status);
				});
			}
		});
	});

	var days = $('#days').attr("value");
	var rdays = $('#rdays').attr("value");


    
	$('#daysbar').text(Math.round(days/rdays*100)+"%");

	var valuer = days/rdays*100;
	$('#daysbar').css('width', valuer+'%').attr('aria-valuenow', valuer);


	
    var used = 100;
    // var budget = 10000;
    var budget = $('#task_budget').attr("value");

    
	$('#budget_bar').text(Math.round(used/budget*100)+"%");

	valuer = used/budget*100;
	$('#budget_bar').css('width', valuer+'%').attr('aria-valuenow', valuer);





	var current = $('#con_con_c').attr("value");
	var required = $('#con_con_r').attr("value");
   
    
	$('#consume_bar').text(Math.round(current/required*100)+"%");

	valuer = current/required*100;
	$('#consume_bar').css('width', valuer+'%').attr('aria-valuenow', valuer);

	


});