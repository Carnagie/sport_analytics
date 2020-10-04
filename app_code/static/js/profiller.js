document.querySelector('.closeVert').addEventListener('click',
function() {
    document.querySelector('.bg-modalVert').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.buttonVert',
function() {
    document.querySelector('.bg-modalVert').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.closeVert2').addEventListener('click',
function() {
    document.querySelector('.bg-modalVert2').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.buttonVert2',
function() {
    document.querySelector('.bg-modalVert2').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close1').addEventListener('click',
function() {
    document.querySelector('.bg-modal1').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button1',
function() {
    document.querySelector('.bg-modal1').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close2').addEventListener('click',
function() {
    document.querySelector('.bg-modal2').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button2',
function() {
    document.querySelector('.bg-modal2').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close3').addEventListener('click',
function() {
    document.querySelector('.bg-modal3').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button3',
function() {
    document.querySelector('.bg-modal3').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close4').addEventListener('click',
function() {
    document.querySelector('.bg-modal4').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button4',
function() {
    document.querySelector('.bg-modal4').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close5').addEventListener('click',
function() {
    document.querySelector('.bg-modal5').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button5',
function() {
    document.querySelector('.bg-modal5').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close6').addEventListener('click',
function() {
    document.querySelector('.bg-modal6').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});

$(document).on('click','.button6',
function() {
    document.querySelector('.bg-modal6').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});




document.querySelector('.close7').addEventListener('click',
function() {
    document.querySelector('.bg-modal7').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button7',
function() {
    document.querySelector('.bg-modal7').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});



document.querySelector('.close8').addEventListener('click',
function() {
    document.querySelector('.bg-modal8').style.display = 'none';
    document.querySelector('.all_content_wrapped').style.display = 'inline';
});
$(document).on('click','.button8',
function() {
    document.querySelector('.bg-modal8').style.display = 'flex';
    document.querySelector('.all_content_wrapped').style.display = 'none';
});
var doc = new jsPDF('p', 'mm', "a4");
$(document).on('click','#pdf',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);

    html2canvas(document.getElementById("topdf1")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        console.log(imgData)
        doc.addImage(imgData, 'JPEG', 5, 5, 200, 55);

    });

    html2canvas(document.getElementById("topdf2")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        console.log(imgData)
        doc.addImage(imgData, 'JPEG', 5, 58, 200, 240);
        doc.save('sample-file.pdf');
    });
});