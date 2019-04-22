var piramid = [];
var contador = 7;
var numberDiviTrue = 0;
var numberDiviFalse = 0;
for (var ind = 1; ind <= contador; ind++) {
    if (piramid.length >= 1) {
        //verifica si el arreglo es mayor a uno 
        if (piramid.length == 1) {
            piramid[piramid.length] = [{ 'num': piramid.length }, { 'num': piramid.length }]
        } else if (piramid.length > 1) {
            //recorre la ultima posicion y empieza a sumar segun los numeros
            var totals = []
            totals[0] = { 'num': 1 };
            for (var act = 0; act <= piramid[piramid.length - 1].length - 1; act++) {
                if (piramid[piramid.length - 1][act + 1] != undefined) {
                    totals.push({ 'num': parseInt(piramid[piramid.length - 1][act].num) + parseInt(piramid[piramid.length - 1][act + 1].num) })
                }
            }
            totals[totals.length] = { 'num': 1 };
            piramid[piramid.length] = totals;
        }
    } else {
        piramid.push([{ 'num': ind }])
    }
}
//valida de todos los numeros cuales son divisibles 
piramid.forEach(el => {
    el.forEach(numb => {
        var modular = numb.num % 7;
        if (modular === 0) {
            numberDiviTrue = numberDiviTrue +1 
        } else {
            numberDiviFalse = numberDiviFalse +1 
        }
    });
});
console.log('numeros divisibles en 7 =' + numberDiviTrue);
console.log('numeros NO divisibles en 7 =' + numberDiviFalse);