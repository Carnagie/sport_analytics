$(document).on('click','#pdf',
    function() {
    var doc = new jsPDF('p', 'mm', "a4");
    console.log("entered");
    window.scrollTo(0, 0);

    html2canvas(document.getElementById("topdf")).then(function (canvas) {

        console.log("canvas start page");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 15, 15, 180, 280);
        doc.save("sample-pdf-2");
    });

});