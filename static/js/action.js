function deleteRow(currentRow) {
    var index = currentRow.parentNode.parentNode.rowIndex;
    document.getElementById("qTable").deleteRow(index);
    $.get("/playmusic/delete/" + index);
}


function getSearch(){
    var input = $("#searchBox").val();
    var replaced = input.split(' ').join('+');
    $.ajax({ 
        type: "get",
        url: "/playmusic/search/" + replaced,
        success: function(data){
            $("#searchResults").html(data);
        }
    });
}

function addToQueue(currentRow) {
    var index = currentRow.parentNode.parentNode.parentNode.rowIndex;
    $.get("/playmusic/add/" + index);
}
$("#searchBox").keyup(function(event){
    if(event.keyCode == 13){
        $("#searchButton").click();
    }
});

$('#searchButton').click(function() {
  var input = $("#searchBox").val();
    var replaced = input.split(' ').join('+');
    $.ajax({ 
        type: "get",
        url: "/playmusic/search/" + replaced,
        success: function(data){
            $("#searchResults").html(data);
        }
    });
});
