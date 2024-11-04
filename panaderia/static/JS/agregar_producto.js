function validarCampos(){
    const codigo = document.getElementById('id_codigo').value;
    const cant = document.getElementById('id_cantidad').value;
    const cant_minima = document.getElementById('id_cantidad_minima').value;
    const precio = document.getElementById('id_precio').value;
    const precio_mayorista = document.getElementById('id_precio_mayorista').value;

    if(!numero_valido(codigo) || !numero_valido(cant) || !numero_valido(cant_minima) || !numero_valido(precio) || !numero_valido(precio_mayorista)){
        return false;
    }
    return true;
}

function numero_valido(numero){
    return es_numero(numero) && !es_numero_negativo(numero);
    /*true && true*/
}

