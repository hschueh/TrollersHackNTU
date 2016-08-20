$(document).ready(function(){

	var days = $('#days').attr("value");
	var rdays = $('#rdays').attr("value");


    console.log(days);
    console.log(rdays);
    console.log(days/rdays);
	$('#daysbar').text(Math.round(days/rdays*100)+"%");

	var valeur = days/rdays*100;
	$('#daysbar').css('width', valeur+'%').attr('aria-valuenow', valeur);

});