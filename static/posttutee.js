$(document).ready(function() { 
	
	var tutrlist = function tutrlist(){
	    $.getJSON("/gettutrlist",function(data){
		    $("#tutrlist").empty();
		    console.log(data);
		    $.each(data, function(i, tutr){
			    console.log(tutr);
			    $("#tutrlist").append("<div>" +
					      "tut.r name: " + tutr[1] + "<br>" +
					      "tut.r bio: " + tutr[3] + "<br>" +
					      '<button id="'+ tutr[0] + '">' +
					      "this is the perf tutr </button>" +
					      "</div><br>"
						  )
				});
		});
	};
			/*
		    console.log(data.length);
		    for ( var i = 0, l = data.length; i < l; i++ ) {
			$("#tutrlist").append("<div>" +
					      "tut.r name: " + data[i][1] + "<br>" +                                                                                    
					      "tut.r bio: " + data[i][3] + "<br>" +
					      '<button id="'+ data[i][0] + '">' +
					      "this is the perf tutr </button>" +
					      "</div><br>"
					      );
		    }
		    */
	       
	     
	
	var updatelist = setInterval(tutrlist,5000);
	//tutrlist();
	
	$('body').on('click','button', function(){
		clearInterval(updatelist)
		var tutr = this.id;
		console.log(tutr);
		$("#tutrlist").empty();
		$("button").detach();
		$.getJSON("/gettutr/" + tutr, function(data){
			console.log(data);
			$("#tutrName").text(data.tutrName);
			$("#tutrEmail").text(data.tutrEmail);
			$("#tutrLocation").text(data.tutrLocation);
			$("#tutrBio").text(data.tutrBio);
			console.log(data.tutrAvail);
		    });
	    });
	
    });
/*
reattach buttons by appending buttons 
to div's with id "d+buttonid" (buttonid = user)
*/