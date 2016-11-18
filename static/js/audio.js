$('#pause').hide();

$('#play').click(function() {
  $.get("/playmusic/play");
  $('#play').hide();
  $('#pause').show();
});

$('#pause').click(function() {
  $.get("/playmusic/pause");
  $('#pause').hide();
  $('#play').show();
});

$('#next').click(function() {
  $.get("/playmusic/skip");
  $('#pause').show();
  $('#play').hide();
});

$('#prev').click(function() {
  $.get("/playmusic/prev");
  $('#pause').show();
  $('#play').hide();
});