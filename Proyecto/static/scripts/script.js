function load() {
    for (let i = 0; i < document.getElementsByName("div-agregado").length; i++) {
        const element = document.getElementsByName("div-agregado")[i];
        element.classList.remove("claseParaProbar");
    }
    //document.getElementsByName("div-agregado").classList.remove("claseParaProbar");

    document.getElementById("estilo2").classList.add("estilo");
    document.getElementById("estilo1").classList.remove("estilo");
    document.getElementById("estilo3").classList.remove("estilo");

}

function agregarDiv(element) {
    console.log(element);
    element.children[1].classList.toggle("claseParaProbar");
}


function publicacion(){
    document.getElementById("estilo2").classList.add("estilo");
    document.getElementById("estilo1").classList.remove("estilo");
    document.getElementById("estilo3").classList.remove("estilo");
    document.getElementById("icono-subir-foto").classList.remove("estilo");

}

function mensaje(){
    document.getElementById("estilo2").classList.remove("estilo");
    document.getElementById("estilo1").classList.remove("estilo");
    document.getElementById("estilo3").classList.add("estilo");
    document.getElementById("icono-subir-foto").classList.remove("estilo");

}

function buscar(){
    document.getElementById("estilo2").classList.remove("estilo");
    document.getElementById("estilo1").classList.add("estilo");
    document.getElementById("estilo3").classList.remove("estilo");
    document.getElementById("icono-subir-foto").classList.remove("estilo");
}

function lineaFoto(){
    document.getElementById("icono-subir-foto").classList.add("estilo");
    document.getElementById("estilo2").classList.remove("estilo");
    document.getElementById("estilo1").classList.remove("estilo");
    document.getElementById("estilo3").classList.remove("estilo");
}
function favorito(element){
    //document.getElementById("favorito").classList.add("borde");
    element.children[0].classList.toggle("borde");
}

