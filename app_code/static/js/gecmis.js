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
    localStorage.setItem("height", "800px");
    localStorage.setItem("width", "650px");
});

$(document).on('click','.fms',
function() {
    console.log("fms")
    localStorage.setItem("height", "1000px");
    localStorage.setItem("width", "750px");
});


$(document).on('click','.ybalance',
function() {
    localStorage.setItem("height", "800px");
    localStorage.setItem("width", "800px");
});

$(document).on('click','.jump',
function() {
    localStorage.setItem("height", "700px");
    localStorage.setItem("width", "550px");
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
