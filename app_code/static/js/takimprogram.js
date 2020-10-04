var doc = new jsPDF('1','mm',[297, 210]);
$(document).on('click','#pdf',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);

    html2canvas(document.getElementById("topdf1")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 30, 15, 250, 5.8);
    
    });

    html2canvas(document.getElementById("topdf2")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 7.5, 25, 280, 180);
        doc.save('sample-file.pdf');
    });
});


var imgArray = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count = 0;
$(document).on('click','#addImg',
    function() {
  count ++;
  if (count == 15) {
    count = 0;
  }
  var elements = document.querySelector("#myImg1");
  elements.src = imgArray[count];
});

var imgArray2= ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count2 = 0;
$(document).on('click','#addImg2',
    function() {
  count2 ++;
  if (count2 == 15) {
    count2 = 0;
  }
  var elements2 = document.querySelector("#myImg2");
  elements2.src = imgArray2[count2];
});

var imgArray3= ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count3 = 0;
$(document).on('click','#addImg3',
    function() {
  count3 ++;
  if (count3 == 15) {
    count3 = 0;
  }
  var elements3 = document.querySelector("#myImg3");
  elements3.src = imgArray3[count3];
});

var imgArray4= ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count4 = 0;
$(document).on('click','#addImg4',
    function() {
  count4 ++;
  if (count4 == 15) {
    count4 = 0;
  }
  var elements4 = document.querySelector("#myImg4");
  elements4.src = imgArray4[count4];
});

var imgArray5 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count5 = 0;
$(document).on('click','#addImg5',
    function() {
  count5 ++;
  if (count5 == 15) {
    count5 = 0;
  }
  var elements5 = document.querySelector("#myImg5");
  elements5.src = imgArray5[count5];
});

var imgArray6 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count6 = 0;
$(document).on('click','#addImg6',
    function() {
  count6 ++;
  if (count6 == 15) {
    count6 = 0;
  }
  var elements6 = document.querySelector("#myImg6");
  elements6.src = imgArray6[count6];
});

var imgArray7 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count7 = 0;
$(document).on('click','#addImg7',
    function() {
  count7 ++;
  if (count7 == 15) {
    count7 = 0;
  }
  var elements7 = document.querySelector("#myImg7");
  elements7.src = imgArray7[count7];
});

//--------------------------------------------------


var imgArray8 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count8 = 0;
$(document).on('click','#addImg8',
    function() {
  count8 ++;
  if (count8 == 15) {
    count8 = 0;
  }
  var elements8 = document.querySelector("#myImg8");
  elements8.src = imgArray8[count8];
});

var imgArray9= ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count9 = 0;
$(document).on('click','#addImg9',
    function() {
  count9 ++;
  if (count9 == 15) {
    count9 = 0;
  }
  var elements9 = document.querySelector("#myImg9");
  elements9.src = imgArray9[count9];
});

var imgArray10= ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count10 = 0;
$(document).on('click','#addImg10',
    function() {
  count10 ++;
  if (count10 == 15) {
    count10 = 0;
  }
  var elements10 = document.querySelector("#myImg10");
  elements10.src = imgArray10[count10];
});

var imgArray11 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count11 = 0;
$(document).on('click','#addImg11',
    function() {
  count11 ++;
  if (count11 == 15) {
    count11 = 0;
  }
  var elements11 = document.querySelector("#myImg11");
  elements11.src = imgArray11[count11];
});

var imgArray12 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count12 = 0;
$(document).on('click','#addImg12',
    function() {
  count12 ++;
  if (count12 == 15) {
    count12 = 0;
  }
  var elements12 = document.querySelector("#myImg12");
  elements12.src = imgArray12[count12];
});

var imgArray13 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count13 = 0;
$(document).on('click','#addImg13',
    function() {
  count13 ++;
  if (count13 == 15) {
    count13 = 0;
  }
  var elements13 = document.querySelector("#myImg13");
  elements13.src = imgArray13[count13];
});

var imgArray14 = ["static/ball.png","static/up.png","static/ladder.png","static/hurdle.png","static/rope.png","static/duba.png","static/weight.png","static/right.png","static/down.png","static/left.png","static/run.png","static/refresh.png","static/medal.png","static/player.png","static/net.png"]
var count14 = 0;
$(document).on('click','#addImg14',
    function() {
  count14 ++;
  if (count14 == 15) {
    count14 = 0;
  }
  var elements14 = document.querySelector("#myImg14");
  elements14.src = imgArray14[count14];
});
