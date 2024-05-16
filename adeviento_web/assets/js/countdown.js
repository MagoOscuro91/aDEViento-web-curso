//Este script de js es de mouredev vamos a intentar entenderlo.

//Esta linea es una variable que coge un dato temporal con Date y getTime().
var countDownDate = new Date("Dec 1, 2024 15:00:00 UTC").getTime();// Sería mejor trabajar con la hora local, pero lo haremos así con hora UTC.

// Crea una función que se ejecuta cada segundo.
var x = setInterval(function () {

    var now = new Date().getTime();// Obtiene la hora actual en milisegundos desde el 1 de enero de 1970.
    var distance = countDownDate - now; // Calcula la diferencia entre la hora objetivo y la hora actual.

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));// Calcula el número de días restantes.
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));//Cuantas horas faltan.
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));//Cuantos minutos faltan.
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);//Cuantos segundos faltan.

    // Actualiza el contenido HTML del elemento con id "countdown" para mostrar el tiempo restante
    document.getElementById("countdown").innerHTML = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

    // Si la cuenta regresiva ha terminado, muestra un mensaje y detiene la actualización
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("countdown").innerHTML = "¡Comienza el calendario de MAGIA OSCURA!";
    }
}, 1000);// La función se ejecuta cada 1000 milisegundos (1 segundo)
/*
Este script crea un temporizador de cuenta regresiva
que se actualiza cada segundo y muestra el tiempo restante en días, horas, minutos y segundos en un elemento HTML con el id `countdown`.
Una vez que el tiempo se acaba (cuando `distance` es menor que 0), cambia el contenido del mismo elemento para mostrar un mensaje 
de finalización y detiene el intervalo que actualiza la cuenta regresiva.
*/