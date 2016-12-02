function poll() {
	$.ajax({ 
        type: "get",
        url: "/playmusic/poll",
        success: function(json){
        	var data = JSON.parse(json);
        	if (data.refresh == true) {
        		$("#musicInfo").html(data.info);
        		$("#qTable").html(data.queue);
        		updateProgress(data.position, data.length);
        	}
        	else if (data.refresh == false) {
        		updateProgress(data.position, data.length);
        	}
        }
    });
	setTimeout(poll,1000);
}

window.addEventListener("load", poll);
