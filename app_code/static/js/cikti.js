var doc = new jsPDF('p', 'mm', "a4");
$(document).on('click','.add',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);
    html2canvas(document.getElementById("topdf")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData, 'JPEG', 15, 15, 180, 50);

        var ul = document.getElementById("antrenmanlar");
        var items = ul.getElementsByTagName("li");
        var rowNum = 1
        var columnNum = 0
        var totalElements = 0
        for (var i = 0; i < items.length; i++) {
            console.log(i)
            console.log(items.length)
            console.log(items[i]);
            listImagePaste(i+1,items.length,rowNum,columnNum,totalElements);
            columnNum++;
            totalElements++;
            if ( totalElements % 8 == 0){
                //doc.addPage();
                //console.log("NEW PAGE HERE");
                totalElements = 0;
            }
            if ( (i + 1) % 2 == 0){
                rowNum++;
                columnNum = 0;
            }
        }
    /*
    if ( totalElements % 8 == 0){
        doc.addPage();
        console.log("NEW PAGE HERE");
    }*/
        //doc.save('sample-file.pdf');
    });
});

function listImagePaste(index, maxindex, rowindex, columnindex, totalElements) {

    console.log("entered li ")
    html2canvas(document.getElementById("div" + index)).then(function (canvas2) {

        console.log("entered html2canvas li");
        var imgData2 = canvas2.toDataURL("image/jpeg",0.9);
        if (rowindex == 1) {
            doc.addImage(imgData2, 'JPEG', 10 + columnindex*70, 80*rowindex, 58, 40);
        }
        else {
            doc.addImage(imgData2, 'JPEG', 10 + columnindex*70, 75 + (50 * (rowindex-1)), 58, 40);
        }
        //doc.save("sample-pdf-2");
        if (index == maxindex) {
            doc.save("sample-pdf-2");
        }

    });
}





function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imagePreview').css('background-image', 'url('+e.target.result +')');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#imageUpload").change(function() {
    readURL(this);
});


function readURL2(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#blah')
                    .attr('src', e.target.result)
                    .width(150)
                    .height(200);
            };

            reader.readAsDataURL(input.files[0]);
        }
}

$(document).on('click','#c100',
    function() {

        document.querySelector("#c100").style.background = "darkred";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c90',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "darkred";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});


$(document).on('click','#c85',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "darkred";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c80',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "darkred";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c75',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "darkred";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c70',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "darkred";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c65',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "darkred";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c60',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "darkred";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c55',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "darkred";
        document.querySelector("#c50").style.background = "#D3B000";
});

$(document).on('click','#c50',
    function() {

        document.querySelector("#c100").style.background = "#D3B000";
        document.querySelector("#c90").style.background = "#D3B000";
        document.querySelector("#c85").style.background = "#D3B000";
        document.querySelector("#c80").style.background = "#D3B000";
        document.querySelector("#c75").style.background = "#D3B000";
        document.querySelector("#c70").style.background = "#D3B000";
        document.querySelector("#c65").style.background = "#D3B000";
        document.querySelector("#c60").style.background = "#D3B000";
        document.querySelector("#c55").style.background = "#D3B000";
        document.querySelector("#c50").style.background = "darkred";
});
var index = 0;
var array = ["static/athlete_images/mahiremrecan.png","static/athlete_images/halkbank.jpg"]
$(document).on('click','#changeImg',
    function() {
    console.log(array);
    index++;
    if (index == array.length) {
        index = 0;
    }
    document.querySelector("#img_div2").src = array[index];
});
    function readURL3(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#blah').attr('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function(){
        readURL3(this);
    });
