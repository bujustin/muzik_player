var userIndex;

function addUser() {
	$.ajax({ 
        type: "get",
        url: "/playmusic/adusr",
        success: function(data){
            userIndex = data;
        }
    });
}

window.addEventListener("load", addUser);

function removeUser() {
	$.get("/playmusic/rmusr/" + userIndex);
}

window.addEventListener("beforeunload", removeUser);