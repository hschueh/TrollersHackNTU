var origin_btn_id = "charge";

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();

function modNum(n){
	if(n<10) {
	    return '0' + n;
	}
	else return n;
}

mm = modNum(mm);
dd = modNum(dd);

today = mm+'/'+dd+'/'+yyyy;

var day = parseInt(dd);
var mon = parseInt(mm);
var yr = parseInt(yyyy);

function daysInMonth(month,year) {
    return new Date(year, month, 0).getDate();
}

function CreateTable(data){
	
}

$(document).ready(function(){
	$(".main-btn").css("background-color", "#f8f8f8");
	$("#charge-btn").css("background-color", "#808080");

	$(".main-btn").click(function(){
		var id = $(this).attr("id").split("-")[0];

		if (id != origin_btn_id){
			if (id == "statistic")
				window.location.href = '/' + id + '/expense/';
			else window.location.href = '/' + id + '/';

			$("#" + origin_btn_id + "-btn").css("background-color", "#f8f8f8");
			$("#" + id + "-btn").css("background-color", "#808080");
		}		
	});

	$(".plus-btn").click(function(){
		window.location.href = '/calculator/expense/';
	});

	// $('#datetimepicker').data("DateTimePicker").FUNCTION()

	$("#datetimepicker").datetimepicker({
		defaultDate: today,
		format: "MM/DD"
	});

	$(".date-nav").click(function(){
		if($(this).attr("id").split("-")[0] == "left"){
			// console.log("press");
			if (day == 1){
				if (mon == 1){
					yr -= 1;
					mon = 12;
					day = 31;
				}
				else{
					mon -= 1;
					day = daysInMonth(mon,yr)
				}
			}
			else{
				day -= 1;
			}
			// console.log(yr+"-" + mon + "-" +day);
		}
		else{
			if (day == daysInMonth(mon, yr)){
				if (mon == 12){
					yr += 1;
					mon = 1;
					day = 1;
				}
				else{
					mon += 1;
					day = 1;
				}
			}
			else{
				day += 1;
			}
		}
		$("#datetimepicker").data("DateTimePicker").date(modNum(mon) + "-" + modNum(day) + "-" + yr);
	});

	$("#datetimepicker").on("dp.change",function(e){
		// console.log(e);
		// console.log(e.date._d);
		mon = parseInt(e.date._d.getMonth()+1);
		day = parseInt(e.date._d.getDate());
		yr = parseInt(e.date._d.getFullYear());

		$.post("/date_changed/expense/",{'yr':yr, 'mon':mon, 'day':day},
		  function(data,status){
		    console.log("Data: " + data + "\nStatus: " + status);
		  });
		// console.log(mon + "-" + day + "-" + yr);
	});
});