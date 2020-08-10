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
