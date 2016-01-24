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
	
	var setMatch = function setMatch(){
	    $.get("/setmatch", function(data){
		    console.log(data);
		});
	};
	/*
	document.getElementById("matcher").addEventListener('click',setMatch);
	document.getElementById("getter").addEventListener('click',getStatus);
	*/
	setInterval(getStatus,100);
	
	var getAllUsers = function getAllUsers(){
	    $.getJSON('/getallusers',function(data){
		    console.log(data);
		});
        };
	
        var getusers = setInterval(getAllUsers,1000);

	
    });