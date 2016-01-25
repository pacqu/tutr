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
						  "tut.r location: " + tutr[6] + "<br>" +
						  '<button id="'+ tutr[0] + '" style="background-color:#Ffc687;width:500px;height:50px;		      color:white;font-size:20px;border-radius:15px">' +
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
		$("#matchedtutr").append(  
					 '<h2 id="tutrstatus"></h2>' + 
					 '<div>' +
					 '<p id="tutrName"></p>'+
					 '<p id="tutrEmail"></p>' +
					 '<p id="tutrLocation"></p>' +
					 '<p id="tutrBio"></p>' +
					 '</div>'
					   );
		$.getJSON("/gettutr/" + tutr, function(data){
			console.log(data);
			$("#tutrstatus").text("here's your perfect tut.r's info!" +
				 "return to the dashboard when you're done")
			$("#tutrName").text(data.tutrName);
			$("#tutrEmail").text(data.tutrEmail);
			$("#tutrLocation").text(data.tutrLocation);
			$("#tutrBio").text(data.tutrBio);
			console.log(data.tutrAvail);
		    });
	    });
	
	var getAllUsers = function getAllUsers(){
	$.getJSON('/getallusers',function(data){
		console.log(data);
	    });
	};
	
	var getusers = setInterval(getAllUsers,1000);
	
    });


/*
reattach buttons by appending buttons 
to div's with id "d+buttonid" (buttonid = user)
*/
