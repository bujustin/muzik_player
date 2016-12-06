/*
Scrolling*********************************
*/

/**
* Scrolling text (right to left)
**/

function scrollText(container, element){

  alert('ok');

  var elementWidth = element.width();
  var startPos = container.width(); //rightmost position of the container

  //if the text is bigger than the container
  if(elementWidth > startPos){
    var endPos = -1 * elementWidth; //farthest to the left text can go
    if(element.position().left <= endPos){
      element.css("left", startPos);
    }
    else {
      time = (parseInt(element.position().left, 10) - endPos) * (10000 / (startPos - endPos));
      element.animate({
        'left': -elementWidth,
        time,
        'linear',
        scrollText()});
    }
    element.css({
      'width': elementWidth,
      'left': startPos
    });
  }
}


//event listeners for scrolling text
$(".songTitle").mouseenter(function(e){
  var container = e.target;
  var element = container.closest('.songInfo');
  if(container.scrollWidth > container.innerWidth()) //overflow
  {
    scrollText(container, element);
  }
});
