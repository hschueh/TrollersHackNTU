$(document).ready(function(){
	$(".pics").each(function(index){
		if(index + 1 > current_monster_id)
			$(this).attr("src",$(this).attr("src").replace("boss","shadow"));
	});
});