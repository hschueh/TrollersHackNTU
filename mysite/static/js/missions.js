$(document).ready(function(){

	var days = $('#days').attr("value");
	var rdays = $('#rdays').attr("value");


    
	$('#daysbar').text(Math.round(days/rdays*100)+"%");

	var valeur = days/rdays*100;
	$('#daysbar').css('width', valeur+'%').attr('aria-valuenow', valeur);

});

$(document).ready(function(){

	var days = $('#con_bud_days').attr("value");
	var rdays = $('#con_bud_rdays').attr("value");
    var used = 1500;
    var budget = 10000;
    //var budget = $('#task_budget').attr("value");

    
	$('#budget_bar').text(Math.round(used/budget*100)+"%");

	var valeur = used/budget*100;
	$('#budget_bar').css('width', valeur+'%').attr('aria-valuenow', valeur);

});

$(document).ready(function(){

	var current = $('#con_con_c').attr("value");
	var required = $('#con_con_r').attr("value");
    console.log(current);
    console.log(required);
    
	$('#consume_bar').text(Math.round(current/required*100)+"%");

	var valeur = current/required*100;
	$('#consume_bar').css('width', valeur+'%').attr('aria-valuenow', valeur);

});