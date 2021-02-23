function replaceAll(string, search, replace) {
    return string.split(search).join(replace);
}

var elementNum = 1;
$(document).on('click', '#addRow',
    function () {

        var ul = document.querySelector(".element_bar");
        var li = document.createElement("li");
        var base = document.getElementById("baseElement");

        li = base.cloneNode(true);

        base.querySelector("#mydiv").style.top = "500px";
        base.querySelector("#mydiv").style.left = "50px";

        //li.innerHTML = replaceAll(li.innerHTML,"mydiv","mydiv2");

        ul.appendChild(li);

    });

$(document).on('click', '#delRow',
    function () {
        var list = document.querySelector(".element_bar");
        list.removeChild(list.childNodes[list.childNodes.length - 1]);
    });


var imgArray = ["static/ball.png", "static/bosu.png", "static/up.png", "static/ladder.png", "static/hurdle.png", "static/rope.png", "static/duba.png", "static/weight.png", "static/right.png", "static/down.png", "static/left.png", "static/run.png", "static/refresh.png", "static/medal.png", "static/player.png", "static/net.png"]
var count = 0;
$(document).on('click', '#addImg',
    function () {
        var ul = document.querySelector(".element_bar");
        var li = ul.childNodes[1];
        ;
        count++;
        if (count == 16) {
            count = 0;
        }
        var elements = li.querySelectorAll(".myImg")[li.querySelectorAll(".myImg").length - 1];
        elements.src = imgArray[count];
    });


var doc = new jsPDF('p', 'mm', [240, 240]);
$(document).on('click', '#pdf',
    function () {

        console.log("entered")
        window.scrollTo(0, 0);


        html2canvas(document.getElementById("topdf2")).then(function (canvas) {

            console.log("entered html2canvas");
            var imgData = canvas.toDataURL("image/jpeg", 0.9);
            console.log(imgData)
            doc.addImage(imgData, 'JPEG', 0, 25, 240, 130);
            doc.save('sample-file.pdf');
        });
    });


dragElement(document.getElementById("mydiv"));

function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    if (document.getElementById(elmnt.id + "header")) {
        // if present, the header is where you move the DIV from:
        document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
        // otherwise, move the DIV from anywhere inside the DIV:
        elmnt.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        // stop moving when mouse button is released:
        document.onmouseup = null;
        document.onmousemove = null;
    }
}