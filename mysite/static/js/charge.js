origin_btn_id = "charge";

$(document).ready(function(){
	$(".main-btn").css("background-color", "#f8f8f8");
	$("#charge-btn").css("background-color", "#808080");

	$(".main-btn").click(function(){
		var id = $(this).attr("id").split("-")[0];

		if (id != origin_btn_id){
			window.location.href = '/' + id + '/';
			$("#" + origin_btn_id + "-btn").css("background-color", "#f8f8f8");
			$("#" + id + "-btn").css("background-color", "#808080");
		}		
	});

	// $('#datetimepicker').data("DateTimePicker").FUNCTION()

	$("#datetimepicker").datetimepicker({
		defaultDate: "8/21/2016",
		format: "MM/DD"
	});
});