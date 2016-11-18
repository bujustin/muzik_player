//no support for older browsers (IE)

/**
* Getting and displaying search results
**/

$("#searchButton").click(search($("#searchBox").val())

function search(query){
  var results = $.post("http://localhost:8000/playmusic/search/" + query,);
  displayResults(results);
}

function displayResults(results){
  var table = document.getElementbyId("searchResults");
  for (i = 0; i < results.length; i++) {
    var result = results[i];-
    var newSong = table.insertRow(0);
    var songTitle = newSong.insertCell(0);
    var songArtist = newSong.insertCell(1);
    var songTime = newSong.insertCell(2);
    var songSource = newSong.insertCell(3);
    var songID = newSong.insertCell(4);
    songTitle.innerHTML= result["title"];
    songArtist.innerHTML = result["author"];
    songTime.innerHTML = result["length"];
    songSource.innerHTML = "Youtube";
    songSource.innerHTML = i;
  }
}

/**
* Displaying songs added from search results to queue
**/

function addSong(e){
  var target, targetParent, targetGrandparent;
  target = e.target;
  targetParent = target.parentNode;
  targetGrandparent = targetParent.parentNode;
  $(targetGrandparent).appendTo("#queue");
  e.preventDefault();
}

//event listeners
var searchResults = document.getElementbyId("searchResults");
searchResults.addEventListener('click', function(e){
  addSong(e);
}, false);

searchResults.addEventListener('dblclick', function(e){
  addSong(e);
}, false)

/**
* Adding songs added to queue from search results to backend queue
**/
