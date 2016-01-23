$(document).ready(function() { 
	
	$("button").click(function(){
		var tutr = this.id;
		console.log(tutr);
		$.("button").detach()
		$.getJSON("/gettutr/" + tutr, function(data){
			console.log(data);
			$("#tutrName").text(data.tutrName);
			$("#tutrEmail").text(data.tutrEmail);
			$("#tutrLocation").text(data.tutrLocation);
			$("#tutrBio").text(data.tutrBio);
		    });
	    });
	    
    });
/*
reattach buttons by appending buttons 
to div's with id "d+buttonid" (buttonid = user)
*/