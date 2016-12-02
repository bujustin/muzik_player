var progressbarWidth = parseFloat(document.getElementById("progressbar").offsetWidth);
var progress = document.getElementById("progress");
var progressHead = document.getElementById("progressHead");
var song_length = 0;

function updateProgress(position, length) {
	progress.style.width = (position * 100).toString() + "%";

	var positionDate = new Date(null);
	positionDate.setSeconds(Math.trunc(position * length));
	var positionTime = positionDate.toISOString().substr(11, 8);

	song_length = length;
	var lengthDate = new Date(null);
	lengthDate.setSeconds(length);
	var lengthTime = lengthDate.toISOString().substr(11, 8);

	document.getElementById("duration").innerHTML = positionTime;
	document.getElementById("length").innerHTML = lengthTime;
}

function setProgress(event) {
    clickX = event.offsetX;
    newPercent = Math.max(0, Math.min(1, clickX / progressbarWidth));
    progress.style.width = (newPercent * 100).toString() + "%";

    $.get("/playmusic/setpos/" + (Math.floor(newPercent * 100)));

    var positionDate = new Date(null);
    positionDate.setSeconds(Math.trunc(newPercent * song_length));
    var positionTime = positionDate.toISOString().substr(11, 8);
    document.getElementById("duration").innerHTML = positionTime;
}

/*function visualProgress(event) {
    clickX = event.offsetX;
    newPercent = Math.max(0, Math.min(1, clickX / progressbarWidth));
    progress.style.width = (newPercent * 100).toString() + "%";
}*/
