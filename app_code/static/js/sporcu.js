function preview_image(event){
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('camera_icon');
        output.style.backgroundImage = "url('" + reader.result + "')";
    }
    reader.readAsDataURL(event.target.files[0]);
    console.log(event.target.files[0].name);
    document.querySelector('.sporcuPhoto').value = event.target.files[0].name;
    document.querySelector('.defaultPhoto').style.display = 'none';

}