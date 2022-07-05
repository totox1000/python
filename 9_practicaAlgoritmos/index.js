//Leccion 1 predice el resultado

var a = 25;
a = a - 13;
console.log(a/2);
    
a = "hola";
console.log(a + " hola");

/*el resultado es 6 "hola,hola*/

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

// Leccion 2 predice los bucles

for(var i=0; i<10; i++) {
    console.log(i);
    i = i + 3; 
}
    
console.log("fuera del bucle " + i);

/*0,4,8 fuera del bucle 12*/

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

//leccion 3 Predice lo que hace el codigo

function getTotal(arrayOfNumbers) {
    
    var sum = arrayOfNumbers[0];
    
    for(var i=0; i<arrayOfNumbers.length; i++) {
    sum += arrayOfNumbers[i];
    console.log("la suma actual es: " + sum); 
    }
    
    console.log("el total es: " + sum);
    
}
    
getTotal([1, 3, 5]);

/*La respuesta es */

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

//Ejercicio siempre esta soleado

var estáSoleado = true;
var temperatura = 45; // supongamos que son grados Fahrenheit
var estáLloviendo = false;
var quéLlevar = "Debería llevar: ";
    
if(estáSoleado) {
    quéLlevar += "gafas, ";
}
if(temperatura < 50) {
    quéLlevar += "un abrigo, ";
}
if(estáLloviendo) {
    quéLlevar += "un paraguas, ";
}
quéLlevar += "y una sonrisa!";
    
console.log(quéLlevar);

/*La respuesta es: "Debería llevar: gafas, un abrigo, y una sonrisa!" */

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

//Preparate para la cuenta regresiva

for(var i=10; i>0; i--) {
    if(i != 2) {
    console.log(i);
    } else {
    console.log("ignición!");
    }
    }
    
    console.log("despegue!");

/*La respuesta es: 10,9,8,7,6,5,4,3,"ignicion!" 1 "despegue!" */