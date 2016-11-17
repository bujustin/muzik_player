function poll() {
    $.ajax({ 
        type: "get",
        url: "http://localhost:8000/playmusic/poll",
        success: function(data){
            $("#sidebar").html(data);
            setTimeout(poll,1000);
        }
    });
}
window.addEventListener("load", poll);