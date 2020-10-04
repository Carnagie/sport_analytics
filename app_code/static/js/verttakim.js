(function ($) {
  "use strict";

  // Porfolio isotope and filter
  var portfolioIsotope = $('.portfolio-container').isotope({
    itemSelector: '.portfolio-item',
    layoutMode: 'fitRows'
  });

  $('#portfolio-flters li').on( 'click', function() {
    $("#portfolio-flters li").removeClass('filter-active');
    $(this).addClass('filter-active');

    portfolioIsotope.isotope({ filter: $(this).data('filter') });
  });

  ///////////////////// Porfolio2 isotope and filter
  var portfolioIsotope2 = $('.portfolio-container2').isotope({
    itemSelector: '.portfolio-item2',
    layoutMode: 'fitRows'
  });

  $('#portfolio-flters2 li').on( 'click', function() {
    $("#portfolio-flters2 li").removeClass('filter-active');
    $(this).addClass('filter-active');

    portfolioIsotope2.isotope({ filter: $(this).data('filter') });
  });


})(jQuery);



var doc = new jsPDF('p', 'mm', "a4");
$(document).on('click','#pdf',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);
    html2canvas(document.getElementById("topdf")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        console.log(imgData)

        var items = document.getElementsByClassName("graphs");
        var rowNum = 1;


        for (var i = 0; i < items.length; i++) {
            console.log(i)
            console.log(items.length)
            console.log(items[i]);
            listImagePaste(i+1,items.length,rowNum);
            if ( rowNum == 4 ){
                rowNum = 1;
            }
            else {
                rowNum++;
            }
        }
    });
});

function listImagePaste(index, maxindex, rowindex) {

    console.log("entered li ")
    html2canvas(document.getElementById("div" + index)).then(function (canvas2) {

        console.log("entered html2canvas li");
        var imgData2 = canvas2.toDataURL("image/jpeg",0.9);
        doc.addImage(imgData2, 'JPEG', 0, 17 + (rowindex-1)*74, 200, 55);
        if ( rowindex == 4 ){
            doc.addPage();
        }
        if (index == maxindex) {
            doc.save("sample-pdf-2");
        }

    });
}



/*
var doc = new jsPDF('p', 'mm', "a4");
$(document).on('click','#pdf',
    function() {

    console.log("entered")
    window.scrollTo(0, 0);

    html2canvas(document.getElementById("topdf2")).then(function (canvas) {

        console.log("entered html2canvas");
        var imgData = canvas.toDataURL("image/jpeg",0.9);
        console.log(imgData)
        doc.addImage(imgData, 'JPEG', 0, 15, 180, 120);
        doc.save('sample-file.pdf');
    });
});
*/