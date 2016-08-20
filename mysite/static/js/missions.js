$(document).ready(function(){

	var days = $('#days').attr("value");
	var rdays = $('#rdays').attr("value");


    
	$('#daysbar').text(Math.round(days/rdays*100)+"%");

	var valeur = days/rdays*100;
	$('#daysbar').css('width', valeur+'%').attr('aria-valuenow', valeur);


	
    var used = 1500;
    var budget = 10000;
    //var budget = $('#task_budget').attr("value");

    
	$('#budget_bar').text(Math.round(used/budget*100)+"%");

	valeur = used/budget*100;
	$('#budget_bar').css('width', valeur+'%').attr('aria-valuenow', valeur);





	var current = $('#con_con_c').attr("value");
	var required = $('#con_con_r').attr("value");
   
    
	$('#consume_bar').text(Math.round(current/required*100)+"%");

	valeur = current/required*100;
	$('#consume_bar').css('width', valeur+'%').attr('aria-valuenow', valeur);

	


});