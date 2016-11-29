function poll() {
	$.ajax({ 
        type: "get",
        url: "/playmusic/poll",
        success: function(json){
        	var data = JSON.parse(json);
            $("#musicInfo").html(data.info);
            $("#qTable").html(data.queue);
            updateProgress(data.position, data.length);
        }
    });
}
function pollLoop() {
    setInterval(poll,1000);
}
window.addEventListener("load", pollLoop);

