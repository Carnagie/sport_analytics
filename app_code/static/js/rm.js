function totalCalculator(){ // run anytime the value changes
    var rowValue      = Number($('#rowNum').val());   // get value of field
    var massValue     = Number($('#kgNum').val()); // convert it to a float


    //$('#total').html(deepSquatValue + hurdleStepValue + inlineLungeValue + shoulderMobValue); // add them and output it
    document.getElementById('row3_100').value =  (massValue * (1 + rowValue / 30)).toPrecision(4);
    document.getElementById('row3_95').value =  (massValue * (1 + rowValue / 30) * 95 / 100).toPrecision(4);
    document.getElementById('row3_90').value =  (massValue * (1 + rowValue / 30) * 90 / 100).toPrecision(4);
    document.getElementById('row3_85').value =  (massValue * (1 + rowValue / 30) * 85 / 100).toPrecision(4);
    document.getElementById('row3_80').value =  (massValue * (1 + rowValue / 30) * 80 / 100).toPrecision(4);
    document.getElementById('row3_75').value =  (massValue * (1 + rowValue / 30) * 75 / 100).toPrecision(4);
    document.getElementById('row3_70').value =  (massValue * (1 + rowValue / 30) * 70 / 100).toPrecision(4);
    document.getElementById('row3_65').value =  (massValue * (1 + rowValue / 30) * 65 / 100).toPrecision(4);
    document.getElementById('row3_60').value =  (massValue * (1 + rowValue / 30) * 60 / 100).toPrecision(4);
    document.getElementById('row3_55').value =  (massValue * (1 + rowValue / 30) * 55 / 100).toPrecision(4);
    document.getElementById('row3_50').value =  (massValue * (1 + rowValue / 30) * 50 / 100).toPrecision(4);
    document.getElementById('row3_45').value =  (massValue * (1 + rowValue / 30) * 45 / 100).toPrecision(4);


    document.getElementById('row4_100').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  )).toPrecision(4);
    document.getElementById('row4_95').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 95 / 100).toPrecision(4);
    document.getElementById('row4_90').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 90 / 100).toPrecision(4);
    document.getElementById('row4_85').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 85 / 100).toPrecision(4);
    document.getElementById('row4_80').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 80 / 100).toPrecision(4);
    document.getElementById('row4_75').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 75 / 100).toPrecision(4);
    document.getElementById('row4_70').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 70 / 100).toPrecision(4);
    document.getElementById('row4_65').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 65 / 100).toPrecision(4);
    document.getElementById('row4_60').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 60 / 100).toPrecision(4);
    document.getElementById('row4_55').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 55 / 100).toPrecision(4);
    document.getElementById('row4_50').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 50 / 100).toPrecision(4);
    document.getElementById('row4_45').value =  (massValue / (1.0278 - ( 0.0278 * rowValue)  ) * 45 / 100).toPrecision(4);

    //console.log(deepSquatValue + hurdleStepValue + inlineLungeValue  + shoulderMobValue)
// add them and output it
}