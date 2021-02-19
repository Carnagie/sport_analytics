var defaultSelected;

$(document).on('click','.addInd',
function() {

	document.querySelector('.bg_modal').style.display = 'flex';

});

$(document).on('click','.delInd',
function() {

	document.querySelector('.bg_modal_delete').style.display = 'flex';

});

$(document).on('click','.updateInd',
function() {

	document.querySelector('.bg_modal_update').style.display = 'flex';

});

document.querySelector('.close').addEventListener('click',
function() {

	document.querySelector('.bg_modal').style.display = 'none';

});

document.querySelector('.close_delete').addEventListener('click',
function() {

	document.querySelector('.bg_modal_delete').style.display = 'none';

});

document.querySelector('.close_update').addEventListener('click',
function() {

	document.querySelector('.bg_modal_update').style.display = 'none';

});


function getDefaultSelected() {
	var e = document.querySelector('.tableToChose');
	defaultSelected = e.selectedIndex;
	localStorage.setItem("varkey", defaultSelected);
}

function setDefaultSelected() {
	var e = document.querySelector('.tableToChose');
	defaultSelected = localStorage.getItem("varkey");
	e.selectedIndex = defaultSelected;
}
$("#selectDel").change(function()
{
  //$("#id_search").val($(this).data("search"));
  //$("#id_search").keyup();

  console.log(document.querySelector('#selectDel').value);
  var string = document.querySelector('#selectDel').value;
  var elements = string.split("_");
  console.log(elements);

  document.querySelector('#popupdel1').value = elements[0];
  document.querySelector('#popupdel2').value = elements[1];
  document.querySelector('#popupdel3').value = elements[2];

})

$("#selectUpdate").change(function()
{
  //$("#id_search").val($(this).data("search"));
  //$("#id_search").keyup();

  console.log(document.querySelector('#selectUpdate').value);
  var string = document.querySelector('#selectUpdate').value;
  var elements = string.split("_");
  console.log(elements);

  document.querySelector('#popupUP1').value = elements[0];
  document.querySelector('#popupUP2').value = elements[1];
  document.querySelector('#popupUP3').value = elements[2];
  document.querySelector('#popupUP4').value = elements[3];
  document.querySelector('#popupUP5').value = elements[4];
  document.querySelector('#popupUP6').value = elements[5];
  document.querySelector('#popupUP7').value = elements[6];
  document.querySelector('#popupUP8').value = elements[7];
  document.querySelector('#popupUP9').value = elements[8];
  document.querySelector('#popupUP10').value = elements[9];
  document.querySelector('#popupUP11').value = elements[10];
  document.querySelector('#popupUP12').value = elements[11];
  document.querySelector('#popupUP13').value = elements[12];
  document.querySelector('#popupUP14').value = elements[13];

})




