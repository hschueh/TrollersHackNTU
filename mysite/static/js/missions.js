var count = 0;

$(document).ready(function(){

	$.get("/mission_data/", function(data){
		data = JSON.parse(data);
		console.log(data);

		for(var i in data){
			if (data[i]['missionType'] == "meal"){
				count++;
				if(data[i]['status'] == "success"){
					$("#checkbox-" + count).attr("checked", true);
					$("#checkbox-" + count).prop("disabled", false);
				}
			}
		}

		/*$(".form-group").click(function(){
			if($(this).find("input").attr("checked") == true){
				$(this).remove();
			}
		});*/
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