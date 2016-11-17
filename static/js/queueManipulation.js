/**
 * Created by Noah Feinberg on 10/21/2016.
 */

function deleteRow(currentRow) {
    var index = currentRow.parentNode.parentNode.rowIndex;
    document.getElementById("qTable").deleteRow(index);
    $.get("http://localhost:8000/playmusic/delete/" + index);
}

function getSearch(){
    var input = $("#searchBox").val();
    var replaced = input.split(' ').join('+');
    $.ajax({ 
        type: "get",
        url: "http://localhost:8000/playmusic/search/" + replaced,
        success: function(data){
            $("#searchResults").html(data);
        }
    });
}
window.addEventListener("keypressed", function (e) {
    if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        getSearch();
    }
});

function addToQueue(currentRow) {
    var index = currentRow.parentNode.parentNode.parentNode.rowIndex;
    $.get("http://localhost:8000/playmusic/add/" + index);
}