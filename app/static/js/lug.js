
let mostrador = document.getElementById("mostrador");
let seleccion = document.getElementById("seleccion");
let imgSeleccionada = seleccion.querySelector("img"); // Cambiado para obtener la imagen del contenedor de selección
let modeloSeleccionado = document.getElementById("modelo");
let descripSeleccionada = document.getElementById("descripcion");
let precioSeleccionado = document.getElementById("precio");

function cargar(item) {
    quitarBordes(); // Llama a la función para quitar bordes de otros items
    mostrador.style.width = "60%"; // Ajusta el ancho del mostrador
    seleccion.style.width = "40%"; // Ajusta el ancho del contenedor de selección
    seleccion.style.opacity = "1"; // Asegúrate de que el contenedor sea visible
    item.style.border = "2px solid red"; // Agrega un borde al item seleccionado

    // Carga la información del item seleccionado
    imgSeleccionada.src = item.getElementsByTagName("img")[0].src;
    modeloSeleccionado.innerHTML = item.getElementsByTagName("p")[0].innerHTML;
    descripSeleccionada.innerHTML = "Descripción del modelo"; // Puedes personalizar esto si tienes descripciones específicas
    precioSeleccionado.innerHTML = item.getElementsByTagName("span")[0] ? item.getElementsByTagName("span")[0].innerHTML : ""; // En caso de que haya un precio
}

function cerrar() {
    mostrador.style.width = "100%"; // Restaura el ancho del mostrador
    seleccion.style.width = "0%"; // Oculta el contenedor de selección
    seleccion.style.opacity = "0"; // Asegúrate de que el contenedor no sea visible
    quitarBordes(); // Quita los bordes de todos los items
}

function quitarBordes() {
    var items = document.getElementsByClassName("item");
    for (let i = 0; i < items.length; i++) {
        items[i].style.border = "none"; // Quita el borde de cada item
    }
}

// Opcional: Cerrar el contenedor de selección al hacer clic fuera de él
window.onclick = function(event) {
    if (event.target === seleccion) {
        cerrar();
    }
};
