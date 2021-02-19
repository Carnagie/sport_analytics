var defaultSelected;
$(document).on('click','.button',
function() {
    document.querySelector('.bg-modal').style.display = 'flex';
});

document.querySelector('.close').addEventListener('click',
function() {
    document.querySelector('.bg-modal').style.display = 'none';
});

document.querySelector('.close2').addEventListener('click',
function() {
    document.querySelector('.bg-modal2').style.display = 'none';
    getDefaultSelected();
});

$(document).on('click','.maximal',
function() {
    localStorage.setItem("height", "80vh");
    localStorage.setItem("width", "70%");
});

$(document).on('click','.fms',
function() {
    console.log("fms")
    localStorage.setItem("height", "80vh");
    localStorage.setItem("width", "50%");
});


$(document).on('click','.ybalance',
function() {
    localStorage.setItem("height", "80vh");
    localStorage.setItem("width", "70%");
});

$(document).on('click','.jump',
function() {
    localStorage.setItem("height", "75vh");
    localStorage.setItem("width", "60%");
});

$(document).on('click','.vert',
function() {
    localStorage.setItem("height", "65vh");
    localStorage.setItem("width", "60%");
});
$(document).on('click','.polar',
function() {
    localStorage.setItem("height", "65vh");
    localStorage.setItem("width", "60%");
});
$(document).on('click','.servis',
function() {
    localStorage.setItem("height", "65vh");
    localStorage.setItem("width", "60%");
});




function getID(params){
    console.log(params);
    var a = document.getElementsByName("rowDatas")[params-1].value
    document.querySelector('.rowDataInput').value = a;
    console.log(a)
}

function getDefaultSelected() {
    var e = "none";
    defaultSelected = e;
    localStorage.setItem("varkey", defaultSelected);
    console.log(e)
}

function getDefaultSelected2() {
    var e = "flex";
    defaultSelected = e;
    localStorage.setItem("varkey", defaultSelected);
    console.log(e);
}

function setDefaultSelectedBody() {
    console.log(localStorage.getItem("varkey"));
    var e = document.querySelector('.bg-modal2');
    defaultSelected = localStorage.getItem("varkey");
    e.style.display = defaultSelected;
    var e = document.querySelector('.modal-content2');
    e.style.height = localStorage.getItem("height");
    e.style.width = localStorage.getItem("width");
}


var doc = new jsPDF('p', 'mm', "a4");
$(document).on('click','.buttonGecmisCikti',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);



    html2canvas(document.getElementById("toPDF")).then(function (canvas) {

        console.log("canvas start page");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 15, 15, 180, 280);
        doc.save("sample-pdf");
    });

});









