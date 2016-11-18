$('#pause').hide();



var audio;

initAudio($('#playlist li:first-child'));

function initAudio(element){

  var song = element.attr('song');
  song = "Arctic Monkeys - Arabella (Official Audio).mp3";
  var title = element.text();
  var cover = element.attr("cover");
  var artist = element.attr("artist");
  var length = element.attr("length");

  audio = new Audio("assets/music/"+song);

  if(!audio.currentTime){
    $("#duration").html('0.00');
  }


}

$(document).ready(function(){
  function title(){
    $.getJSON("/Users/apple/Desktop/testing_stuff1/cs196Project/musicapp/playmusic/song.py", function(results) {
      title = results.title;
      artist = results.author;
      cover = results.thumbnail;
      length = results.length;
    });

    $('#audio-player.title').text(title);
    $('#audio-player.artist').text(artist);
    $('#audio-player.length').text(length);
    $('img.cover').attr(cover);
}

});

$('#play').click(function() {
  audio.play();
  $.get("http://localhost:8000/playmusic/play/",
        function(){
            audio.play();
        });
  $('#play').hide();
  $('#pause').show();
  $('#duration').fadeIn(400);

});



$('#pause').click(function() {
  audio.pause();

  $.get("http://localhost:8000/playmusic/pause/",
        function(){
          audio.pause();

        });

  $('#pause').hide();
  $('#play').show();

});

$('#next').click(function() {
  audio.pause();
  var next = $('#playlist li.active').next();
  if(next.length==0){
    next = $('playlist li:first-child');
  }
  initAudio(next);
  audio.play();
  showDuration();
});

//prev
$('#prev').click(function() {
  audio.pause();
  var prev = $('#playlist li.active').prev();
  if(prev.length==0){
    prev = $('playlist li:last-child');
  }
  initAudio(prev);
  audio.play();
  showDuration();
});





function showDuration() {
  $(audio).bind('timeupdate',function() {
    //Get hrs and mins
    var s = parseInt(audio.currentTime % 60);
    var m = parseInt((audio.currentTime)/60)%60;
    //Add 0 if less than 10
    if(s<10){

      s= '0' + s;

    }
    $('#duration').html(m+'.'+s);
    var value = 0;
    if(audio.currentTime > 0){
      value = Math.floor((100/audio.duration)*audio.currentTime);
    }
    $('#progress').css('width',value+'%');

  })
}
