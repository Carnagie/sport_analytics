$(document).on('click','#add',
function() {
    var itm = document.querySelector('#base').cloneNode( true );
    document.getElementById("dynamicInputs").appendChild(itm);
});


$(document).on('click','.button',
function() {
    document.querySelector('.bg-modal').style.display = 'flex';
});



$(document).on('click','.maximalTestForm',
function() {
    document.querySelector('.maximalTest').style.display = 'flex';
    document.querySelector('.fmsTest').style.display = 'none';
    document.querySelector('.ybalanceTest').style.display = 'none';
    document.querySelector('.jumpTest').style.display = 'none';
    document.querySelector('.vertTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '780px';
    document.querySelector('.modal-content').style.width = '1000px';
    document.querySelector('.polarTest').style.display = 'none';
    document.querySelector('.servisTest').style.display = 'none';
});

$(document).on('click','.fmsTestForm',
function() {
    document.querySelector('.maximalTest').style.display = 'none';
    document.querySelector('.fmsTest').style.display = 'flex';
    document.querySelector('.ybalanceTest').style.display = 'none';
    document.querySelector('.jumpTest').style.display = 'none';
    document.querySelector('.vertTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '1140px';
    document.querySelector('.modal-content').style.width = '1000px';
    document.querySelector('.polarTest').style.display = 'none';
    document.querySelector('.servisTest').style.display = 'none';

});

$(document).on('click','.ybalanceTestForm',
function() {
    document.querySelector('.maximalTest').style.display = 'none';
    document.querySelector('.fmsTest').style.display = 'none';
    document.querySelector('.ybalanceTest').style.display = 'flex';
    document.querySelector('.jumpTest').style.display = 'none';
    document.querySelector('.vertTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '840px';
    document.querySelector('.modal-content').style.width = '1000px';
    document.querySelector('.polarTest').style.display = 'none';
    document.querySelector('.servisTest').style.display = 'none';
});

$(document).on('click','.jumpTestForm',
function() {
    document.querySelector('.maximalTest').style.display = 'none';
    document.querySelector('.fmsTest').style.display = 'none';
    document.querySelector('.ybalanceTest').style.display = 'none';
    document.querySelector('.jumpTest').style.display = 'flex';
    document.querySelector('.vertTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '645px';
    document.querySelector('.modal-content').style.width = '1000px';
    document.querySelector('.polarTest').style.display = 'none';
    document.querySelector('.servisTest').style.display = 'none';

});

$(document).on('click','.vertTestForm',
function() {
    document.querySelector('.vertTest').style.display = 'flex';
    document.querySelector('.maximalTest').style.display = 'none';
    document.querySelector('.fmsTest').style.display = 'none';
    document.querySelector('.ybalanceTest').style.display = 'none';
    document.querySelector('.jumpTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '545px';
    document.querySelector('.modal-content').style.width = '1000px';
    document.querySelector('.polarTest').style.display = 'none';
    document.querySelector('.servisTest').style.display = 'none';

});

$(document).on('click','.polarTestForm',
function() {
    document.querySelector('.polarTest').style.display = 'flex';
    document.querySelector('.vertTest').style.display = 'none';
    document.querySelector('.maximalTest').style.display = 'none';
    document.querySelector('.fmsTest').style.display = 'none';
    document.querySelector('.ybalanceTest').style.display = 'none';
    document.querySelector('.jumpTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '545px';
    document.querySelector('.modal-content').style.width = '1000px';
    document.querySelector('.servisTest').style.display = 'none';

});
$(document).on('click','.servisTestForm',
function() {
    document.querySelector('.servisTest').style.display = 'flex';
    document.querySelector('.polarTest').style.display = 'none';
    document.querySelector('.vertTest').style.display = 'none';
    document.querySelector('.maximalTest').style.display = 'none';
    document.querySelector('.fmsTest').style.display = 'none';
    document.querySelector('.ybalanceTest').style.display = 'none';
    document.querySelector('.jumpTest').style.display = 'none';
    document.querySelector('.modal-content').style.height = '545px';
    document.querySelector('.modal-content').style.width = '1000px';

});


document.querySelector('.close').addEventListener('click',
function() {
    document.querySelector('.bg-modal').style.display = 'none';
});


function getID(params){
    document.querySelector('.bg-modal').style.display = 'flex';
    console.log(params);
    var a = document.getElementsByName("rowDatas")[params-1].value;
    document.querySelector('.rowDataInput').value = a;
    console.log(a);
}


function totalCalculator(){ // run anytime the value changes
    var deepSquatValue      = Number($('#deepSquat').val());   // get value of field
    var hurdleStepValue     = Number($('#hurdleStep').val()); // convert it to a float
    var inlineLungeValue    = Number($('#inlineLunge').val());
    var shoulderMobValue    = Number($('#shoulderMob').val());
    var impClearValue       = Number($('#impClear').val());
    var actStrLegRaiseValue = Number($('#actStrLegRaise').val());
    var trunkStabPushValue  = Number($('#trunkStabPush').val());
    var pressUpClearValue   = Number($('#pressUpClear').val());
    var rotStabValue        = Number($('#rotStab').val());
    var postRockClearValue  = Number($('#postRockClear').val());

    //$('#total').html(deepSquatValue + hurdleStepValue + inlineLungeValue + shoulderMobValue); // add them and output it
    document.getElementById('total').value = deepSquatValue + hurdleStepValue + inlineLungeValue  + shoulderMobValue + impClearValue + actStrLegRaiseValue + trunkStabPushValue + pressUpClearValue + rotStabValue + postRockClearValue;
    //console.log(deepSquatValue + hurdleStepValue + inlineLungeValue  + shoulderMobValue)
// add them and output it
}

function totalCalculatorY(){ // run anytime the value changes

    var limbValue      = Number($('#limb').val());   // get value of field

    var ant_leftSL1Value  = Number($('#ant_leftSL1').val()); // convert it to a float
    var ant_leftSL2Value  = Number($('#ant_leftSL2').val());
    var ant_leftSL3Value  = Number($('#ant_leftSL3').val());

    var ant_rightX1Value  = Number($('#ant_rightX1').val());
    var ant_rightX2Value  = Number($('#ant_rightX2').val());
    var ant_rightX3Value  = Number($('#ant_rightX3').val());

    var pos1_leftSL1Value  = Number($('#pos1_leftSL1').val()); // convert it to a float
    var pos1_leftSL2Value  = Number($('#pos1_leftSL2').val());
    var pos1_leftSL3Value  = Number($('#pos1_leftSL3').val());

    var pos1_rightX1Value  = Number($('#pos1_rightX1').val()); // convert it to a float
    var pos1_rightX2Value  = Number($('#pos1_rightX2').val());
    var pos1_rightX3Value  = Number($('#pos1_rightX3').val());

    var pos2_leftSL1Value  = Number($('#pos2_leftSL1').val()); // convert it to a float
    var pos2_leftSL2Value  = Number($('#pos2_leftSL2').val());
    var pos2_leftSL3Value  = Number($('#pos2_leftSL3').val());

    var pos2_rightX1Value  = Number($('#pos2_rightX1').val()); // convert it to a float
    var pos2_rightX2Value  = Number($('#pos2_rightX2').val());
    var pos2_rightX3Value  = Number($('#pos2_rightX3').val());


    var ant_Left = Number(( (((ant_leftSL1Value + ant_leftSL2Value + ant_leftSL3Value) / 3) / limbValue) * 100 ));
    var ant_Right = Number(( (((ant_rightX1Value + ant_rightX2Value + ant_rightX3Value) / 3) / limbValue) * 100 ));

    document.getElementById('ant_def').value = Number( Math.abs(ant_Left - ant_Right)).toPrecision(3);

    var pos1_Left = Number(( (((pos1_leftSL1Value + pos1_leftSL2Value + pos1_leftSL3Value) / 3) / limbValue) * 100 ));
    var pos1_Right = Number(( (((pos1_rightX1Value + pos1_rightX2Value + pos1_rightX3Value) / 3) / limbValue) * 100 ));

    document.getElementById('pos1_def').value = Number(Math.abs(pos1_Left - pos1_Right)).toPrecision(3);

    var pos2_Left = Number(( (((pos2_leftSL1Value + pos2_leftSL2Value + pos2_leftSL3Value) / 3) / limbValue) * 100 ));
    var pos2_Right = Number(( (((pos2_rightX1Value + pos2_rightX2Value + pos2_rightX3Value) / 3) / limbValue) * 100 ));

    document.getElementById('pos2_def').value = Number(Math.abs(pos2_Left - pos2_Right)).toPrecision(3);

    document.getElementById('totalLeft').value = Number( (ant_Left + pos1_Left + pos2_Left) / 3 ).toPrecision(3);
    document.getElementById('totalRight').value = Number( (ant_Right + pos1_Right + pos2_Right) / 3 ).toPrecision(3);

}


function addNewAce(){

var table = document.getElementById("aceHitTable");
var row = table.insertRow(-1);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);

cell1.innerHTML = "<td> Ace <input type='text' value='Ace' name='aceHitTableLabels' style='display: none;' > </td>";
cell2.innerHTML = "<td>" + document.getElementById("aceHitVal").value  + "<input type='number' value='"+ document.getElementById("aceHitVal").value  +"' name='aceHitTableValues' style='display: none;' step='0.01'> </td>";

}

function addNewHit(){

var table = document.getElementById("aceHitTable");
var row = table.insertRow(-1);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);

cell1.innerHTML = "<td> Hit <input type='text' value='Hit' name='aceHitTableLabels' style='display: none;' > </td>";
cell2.innerHTML = "<td>" + document.getElementById("aceHitVal").value  + "<input type='number' value='"+ document.getElementById("aceHitVal").value  +"' name='aceHitTableValues' style='display: none;' step='0.01'> </td>";

}

function addNewServis(){

var table = document.getElementById("aceHitTable");
var row = table.insertRow(-1);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);

cell1.innerHTML = "<td> Servis <input type='text' value='Servis' name='aceHitTableLabels' style='display: none;' > </td>";
cell2.innerHTML = "<td>" + document.getElementById("aceHitVal").value  + "<input type='number' value='"+ document.getElementById("aceHitVal").value  +"' name='aceHitTableValues' style='display: none;' step='0.01'> </td>";

}

function addNewHata(){

var table = document.getElementById("aceHitTable");
var row = table.insertRow(-1);
var cell1 = row.insertCell(0);
var cell2 = row.insertCell(1);

cell1.innerHTML = "<td> Hata <input type='text' value='Hata' name='aceHitTableLabels' style='display: none;' > </td>";
cell2.innerHTML = "<td>" + document.getElementById("aceHitVal").value  + "<input type='number' value='"+ document.getElementById("aceHitVal").value  +"' name='aceHitTableValues' style='display: none;' step='0.01'> </td>";

}

function deleteNewFromTable(){

var table = document.getElementById("aceHitTable");

if (table.rows.length > 1){
    table.deleteRow(-1);
}
}






