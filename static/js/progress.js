var bar_width = parseFloat(document.getElementById("progressbar").offsetWidth);
var progress = document.getElementById("progress");
var song_length = 0;

var progressHead = document.getElementById("progressHead");
var newPercent = 0;
var paused = false;
//var bar= setInterval(function () {updateBar();}, 1000);

setInterval(function updateBar() {
    if (!paused) {

        song_length = document.getElementById("current_song").getAttribute("data-length");
        var song_position = document.getElementById("position").getAttribute("data-position");
        progress.style.width = (song_position * 100).toString() + "%";


        var date_position = new Date(null);
        date_position.setSeconds(Math.trunc(song_position * song_length));
        var time_position = date_position.toISOString().substr(11, 8);

        var date_length = new Date(null);
        date_length.setSeconds(song_length);
        var time_length = date_length.toISOString().substr(11, 8);

        document.getElementById("duration").innerHTML = time_position;
        document.getElementById("length").innerHTML = time_length;


    }
}, 1000);


$('#play').click(function () {
    paused = false;
});
$('#pause').click(function () {
    paused = true;
});

function setProgress(event) {
    clickX = event.offsetX;
    newPercent = Math.max(0, Math.min(1, clickX / bar_width));
    progress.style.width = (newPercent * 100).toString() + "%";
    var date_position = new Date(null);
    date_position.setSeconds(Math.trunc(newPercent * song_length));
    var time_position = date_position.toISOString().substr(11, 8);

    document.getElementById("duration").innerHTML = time_position;

    $.get("http://localhost:8000/playmusic/setpos/" + (Math.floor(newPercent * 100000)));


}

function visualProgress(event) {
    paused = true;
    clickX = event.offsetX;
    newPercent = Math.max(0, Math.min(1, clickX / bar_width));
    progress.style.width = (newPercent * 100).toString() + "%";
    var date_position = new Date(null);
    date_position.setSeconds(Math.trunc(newPercent * song_length));
    var time_position = date_position.toISOString().substr(11, 8);

    document.getElementById("duration").innerHTML = time_position;

}



