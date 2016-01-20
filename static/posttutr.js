$(document).ready(function() {
	
	function getStatus(){
	    $.get("/getstatus/", function(data){
		    console.log(data);
		    
		});
	};

    });