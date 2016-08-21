$(document).ready(function(){
	$(".row_custom").each(function(index){
		if(index + 1 == current_weapon_id)
			$(this).addClass('inuse');
	});


	$('.row_custom').click(function(){
		$(".row_custom.inuse").removeClass('inuse');
		$(this).addClass('inuse');
	});
});
