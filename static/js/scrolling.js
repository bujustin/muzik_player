/**
* Scrolling text (right to left)
**/

function scrollText(container, element){

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
  }
}


//event listeners for scrolling text
$("#searchResults").bind("mouseover", function(e){
  var row = e.target.closest(".song");
  var container = row.first(); //song title cell
  var element = container.find(".songInfo:first"); //the span
  if(container[0].scrollWidth > container.innerWidth()) //overflow
  {
    scrollText(container, element);
  }
}
));
