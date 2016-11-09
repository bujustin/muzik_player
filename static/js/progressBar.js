function progress() {
    $.ajax({
        type: "get",
        url: "http://localhost:8000/playmusic/progress",
        success: function(data){
            // $("#audio_player").html(data);
            // setTimeout(progress,1000);
            // var progressBarHead = document.getElementById("#progressBarHead");
            // var progressBar = document.getElementById("#progressBar");
            // progressBarHead.style.right = 10+((data.currentSong.length-data.position)/data.currentSong.length)*progressBar.width;
            
        }
    });
}
window.addEventListener("load", progress)