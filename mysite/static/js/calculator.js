var now_category = "Breakfast";

$(document).ready(function(){
	//Dom is ready lets get the fun started.
	var money = '';
	var charge_state = $("#chargestate-var").attr("value");
	console.log(charge_state);
	var csrf_token = $("#csrf-var").attr("value");

	var Calculator = {
		runningTotal : '',	
		currentVal : '',
		setCurrentVal: false,
		executeAction: '',
		display: '',
		numAfterAct: false,
		calculated: false,
		adjustTotals: function(val){
			if (this.calculated && this.executeAction == ''){
				this.setCurrentVal = false;
				this.calculated = false;
				this.runningTotal = '';
			}
			if (!this.setCurrentVal) {
				//If this is the first number user has entered then it becomes runningTotal
				//Otherwise it becomes currentVal which will then be used to update runningTotal based on the action picked
				this.runningTotal += val;
			} else {
				//val is a string so we can append to currentVal for multiple digits
				this.currentVal += val;
			};
		},
		add: function(){
			this.runningTotal = parseInt(this.runningTotal) + parseInt(this.currentVal);
		},
		subtract: function() {
			this.runningTotal = parseInt(this.runningTotal) - parseInt(this.currentVal);
		},	
		multiply: function(){
			this.runningTotal = parseInt(this.runningTotal) * parseInt(this.currentVal);
		},
		divide: function(){
			this.runningTotal = parseInt(this.runningTotal) / parseInt(this.currentVal);
		},
		backspace: function(){
			console.log(this.numAfterAct);
			if(this.numAfterAct){
				this.currentVal = Math.floor(this.currentVal/10).toString();
			}
			else if (!this.numAfterAct && this.executeAction != ''){
				this.runningTotal = Math.floor(this.runningTotal/10).toString();
				this.executeAction = '';
				Calculator.setCurrentVal = false;
			}
			else{
				this.runningTotal = Math.floor(this.runningTotal/10).toString();
			}
    		
    		// console.log(this.currentVal);
    		// console.log(this.runningTotal);
		},
		clear: function(){
			this.runningTotal = '';
			this.currentVal = '';
			this.executeAction = '';
			this.setCurrentVal = false;
			this.display = '';
			numAfterAct = false;
		},
		resetCurrentVal: function (){
			this.currentVal = '';
		},
		calculate: function(){
			this.executeAction = '';
			this.currentVal = '';
			numAfterAct = false;
			
			// this.setCurrentVal = false;
			console.log(this.executeAction);
			if(this.calculated == true){
				return this.currentVal;
			}
			else{
				this.calculated = true;
				return this.runningTotal;
			}
		},
		getAction: function(val){
			 var method = '';
			switch (val) {
				case '+': 
					method = Calculator.add;
					break;
				case '-':
					method = Calculator.subtract;
					break;
				case 'x':
					method = Calculator.multiply;
					break;
				case '/':
					method = Calculator.divide;
					break;
			}

			return method;
		},
		setDisplay: function(){
			console.log(this.currentVal);
			console.log(this.runningTotal);
			return this.display = this.currentVal == '' ? this.runningTotal : this.currentVal;
		}
	};

	
	var onButtonPress = function (){
		var that = $(this),
			action = that.hasClass('action'),
			instant = that.hasClass('instant'),
			val = that.text();
		if (!action) {
			//No action means the button pressed is a number not an "action"
			Calculator.adjustTotals(val);
			if(Calculator.executeAction != '') Calculator.numAfterAct = true;
		} else if(!instant) { 
			//A action button was pressed. Store the action so it can be executed lator
			if (Calculator.executeAction != ''){
				Calculator.executeAction();
			};

			Calculator.executeAction = Calculator.getAction(val);
			Calculator.setCurrentVal = true;
			Calculator.resetCurrentVal();
		} else {
			//Either = or Clr is clicked. this needs immediate action.
			if (Calculator.executeAction != '' && val != '<-'){
				Calculator.executeAction();
			};

			switch (val){
				case 'AC': 
					method = Calculator.clear();
					break;
				case '=':
					method = Calculator.calculate();
					break;
				case '<-':
					method = Calculator.backspace();
					break;
			}
		}

		Calculator.setDisplay();
	}

	var refreshVal = function(){
		$('.calculator input[type=text]').val(Calculator.display);
	}

	$('div.key').click(function(){
		//We want this to stay as div.keyin the onButtonPress function
		onButtonPress.call(this);
		refreshVal();
	});

	$('div.big-key').click(function(){
		//We want this to stay as div.keyin the onButtonPress function
		onButtonPress.call(this);
		refreshVal();
	});

	$('div.ok-key').click(function(){
		money = Calculator.runningTotal;
		// console.log(money);
		if(parseFloat(money) > 0){
			$.ajax({
				url: "/create_record/",
				type: "POST",
				data: {
					"spend": money, 
					"category": now_category,
					"csrfmiddlewaretoken": csrf_token
				},
				success: function(){
					console.log("Create new record!");
				},
				error: function(xhr, errmsg, err){
					console.log(xhr.status + ": " + xhr.responseText);
				}
			})
			.done(function(){
				if (charge_state == "income") {
					window.location.href = "/income/";
				}
				else{
					window.location.href = "/charge/"
				}
			});

			
		}
		else{
			alert("請輸入金額！");
		}
	});

	$('.charge-category-btn').click(function(){
		selected_cate = $(this).attr("id").split("-")[0];
		if (selected_cate != now_category){
			$("#" + now_category + "-btn").css({
				'color': "black",
				'background-color': "white"
			});

			$("#" + selected_cate + "-btn").css({
				'color': "white",
				'background-color': "#808080"
			});

			now_category = selected_cate;
		}
	});
});