$('#pause').hide();

$('#play').click(function() {
  $.get("http://localhost:8000/playmusic/play");
  $('#play').hide();
  $('#pause').show();
});

$('#pause').click(function() {
  $.get("http://localhost:8000/playmusic/pause");
  $('#pause').hide();
  $('#play').show();
});

$('#next').click(function() {
  $.get("http://localhost:8000/playmusic/skip");
  $('#pause').show();
  $('#play').hide();
});

$('#prev').click(function() {
  $.get("http://localhost:8000/playmusic/prev");
  $('#pause').show();
  $('#play').hide();
});