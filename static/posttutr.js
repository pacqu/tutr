$(document).ready(function() {
	
	var getStatus = function getStatus(){
	    $.getJSON("/getstatus", function(data){
		    console.log(data);
		    $("#tuteeName").text(data.tuteeName);
		    $("#tuteeEmail").text(data.tuteeEmail);
		    $("#tuteeLocation").text(data.tuteeLocation);
		    $("#tuteeBio").text(data.tuteeBio);
		    $("#status").text(data.status);
		});
	};
	
	document.getElementById("getter").addEventListener('click',getStatus);
	
    });