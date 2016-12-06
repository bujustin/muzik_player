var prevInfoUrl = "";
var prevQueueLength = 0;

function poll() {
	$.ajax({ 
        type: "get",
        url: "/playmusic/poll",
        success: function(json){
        	var data = JSON.parse(json);
        	
        	if (prevInfoUrl != data.infourl) {
        		$("#musicInfo").html(data.info);
        	}
        	if (prevQueueLength != data.queuelength) {
        		$("#qTable").html(data.queue);
        	}

        	if (data.isplaying == true) {
        		$('#play').hide();
        		$('#pause').show();
        	}
        	else {
        		$('#pause').hide();
        		$('#play').show();
        	}
        	$("#friendStatus").html(data.friendlist);
        	updateProgress(data.position, data.length);

        	prevInfoUrl = data.infourl;
        	prevQueueLength = data.queuelength;
        }
    });
	setTimeout(poll,1000);
}

window.addEventListener("load", poll);