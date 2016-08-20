$(document).ready(function(){

	$.get("/missions/", function(data){
		console.log(data);
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