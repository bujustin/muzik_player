setInterval(function() {
                var bar_width = parseFloat(document.getElementById("progressbar").offsetWidth);
                var song_position = document.getElementById("current_position").getAttribute("data-position");
                var circle_position = 10 + (bar_width * song_position);
                document.getElementById("progress").style.left = circle_position.toString() + "px";
                var song_length = document.getElementById("current_length").getAttribute("data-length");
                var date_position = new Date(null);
                date_position.setSeconds(Math.trunc(song_position * song_length));
                var time_position = date_position.toISOString().substr(11, 8);
                var date_length = new Date(null);
                date_length.setSeconds(song_length);
                var time_length = date_length.toISOString().substr(11, 8);
                document.getElementById("duration").innerHTML = time_position;
                document.getElementById("length").innerHTML = time_length;
            }, 1000);
