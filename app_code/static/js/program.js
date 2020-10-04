var elementNum = 1;
$(document).on('click','#addRow',
    function() {

  var ul   = document.querySelector(".element_bar");
  var li   = document.createElement("li");
  var base = document.getElementById("baseElement")
  li.innerHTML = base.innerHTML

  ul.appendChild(li);

  elementNum++;

});

$(document).on('click','#delRow',
    function() {
  var list = document.querySelector(".element_bar");
  list.removeChild(list.childNodes[list.childNodes.length-1]);
});

$(document).on('click','#addRow2',
    function() {
  var ul   = document.querySelector(".element_bar");
  var li = "";
  console.log(ul.childNodes.length)
  if ( 3 == ul.childNodes.length) {
    li   = ul.childNodes[1];
  }
  else {
    li   = ul.childNodes[ul.childNodes.length-1];
  }
  var newDiv = document.createElement("div");
  newDiv.innerHTML = document.getElementById("baseDiv").innerHTML;
  newDiv.className = "elementsIn";
  li.appendChild(newDiv);

  elementNum--;

});

$(document).on('click','#delRow2',
    function() {
  var ul   = document.querySelector(".element_bar");
  var li = "";
  if ( 3 == ul.childNodes.length) {
    li   = ul.childNodes[1];
  }
  else {
    li   = ul.childNodes[ul.childNodes.length-1];
  }
  li.removeChild(li.childNodes[li.childNodes.length-1]);
});

var imgArray = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count = 0;
$(document).on('click','#addImg',
    function() {
  var ul   = document.querySelector(".element_bar");
  var li = "";
  if ( 3 == ul.childNodes.length) {
    li   = ul.childNodes[1];
  }
  else {
    li   = ul.childNodes[ul.childNodes.length-1];
  }
  count ++;
  if (count == 15) {
    count = 0;
  }
  var elements = li.querySelectorAll(".myImg")[li.querySelectorAll(".myImg").length-1];
  elements.src = imgArray[count];
});




var doc = new jsPDF('p', 'mm', "a4");
$(document).on('click','#pdf',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);

    html2canvas(document.getElementById("topdf1")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 15, 15, 180, 6);

    });

    html2canvas(document.getElementById("topdf2")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 15, 25, 180, 40*elementNum);
        doc.save('sample-file.pdf');
    });
});