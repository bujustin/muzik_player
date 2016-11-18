/**
 * Created by Noah Feinberg on 10/21/2016.
 */

function deleteRow(currentRow) {
    var index = currentRow.parentNode.parentNode.rowIndex;
    document.getElementById("qTable").deleteRow(index);
    $.get("http://localhost:8000/playmusic/delete/",
        function(){
            alert('success');
            $(html(currentRow));
        });

}

function newRow(title) {
    var table = document.getElementById("qTable");
    var row = table.insertRow(1);
    var song = row.insertCell(0);
    song.innerHTML = '<div>' + title + '</div><button class="removeButton" onclick = "deleteRow(this)" >X</button></td>';

}