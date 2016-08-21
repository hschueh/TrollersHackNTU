$(document).ready(function(){
	var csrf_token = $("#csrf-var").attr("value");

	$(".row_custom").each(function(index){
		if(index + 1 == current_weapon_id)
			$(this).addClass('inuse');
	});


	$('.row_custom').click(function(){
		$(".row_custom.inuse").removeClass('inuse');
		$(this).addClass('inuse');
		console.log($(this).attr("id"));

		$.post("/change_item/",{"id": $(this).attr("id").split("-")[1],"csrfmiddlewaretoken": csrf_token },
		  function(status){
		    console.log("Status: " + status);
		});
	});
});
