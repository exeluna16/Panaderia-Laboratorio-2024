let insumos = [];
let insumosEnTabla = [];
let insumoSeleccionado = null;

document.addEventListener('DOMContentLoaded',function(){

    fetch('../inventario/listar_insumos')
    .then(respuesta => respuesta.json())
    .then(datos => {
        insumos = datos
    })
    .catch(error=>console.error('No se pudo traer los insumos de la BD',error));
});

document.getElementById('form_descuento_insumos').addEventListener('submit',function(e){
    e.preventDefault();
    guardarValores();
    this.submit();
});

function buscarInsumo(){
    const consulta = document.getElementById('buscar-insumo').value.toLowerCase();
    const lista_insumos = document.getElementById('lista-insumos');
    lista_insumos.innerHTML = '';

    const resultados = insumos.filter(i => i.nombre.toLowerCase().includes(consulta) && !insumosEnTabla.includes(i.id));

    resultados.forEach(insumo => {
        const li = document.createElement('li');
        li.classList.add('list-group-item','list-group-item-action');
        li.textContent = insumo.nombre;
        li.onclick = () => seleccionarInsumo(insumo);
        lista_insumos.appendChild(li);
    });
}

function seleccionarInsumo(insumo){
    insumoSeleccionado = insumo; //se guarda el insumo seleccionado
    document.getElementById('insumo-elegido').value = insumo.nombre;
    document.getElementById('lista-insumos').innerHTML='';
    document.getElementById('buscar-insumo').value='';
}

function existeCantidadSuficiente(cantidad){
    if (insumoSeleccionado.cantidad < cantidad){
        alertaSwal('CUIDADO','No hay suficiente cantidadad, la cantidad actual es '+ insumoSeleccionado.cantidad,'info','Entendido');
        return false;
    }
    return true;
}

function agregarItemInsumo(){
    //traigo la cantidad ingresada
    let cantidad = document.getElementById('boton-cantidad').value;
    if(existeCantidadSuficiente(cantidad)){
        const tabla = document.getElementById('cuerpo-tabla');//traigo la tabla
        const fila = document.createElement('tr'); //creo una fila
        /* campos de las cabecera
        <th>#</th>
        <th>Insumo</th>
        <th>Cantidad</th>
        <th>Acción</th>
         */
        //creo la fila
        fila.innerHTML = `
        <td>${insumoSeleccionado.id}</td>
        <td>${insumoSeleccionado.nombre}</td>
        <td>${insumoSeleccionado.unidad_de_medida}</td>
        <td class="fila_cantidad">${cantidad}</td>
        <td>
            <button class="btn btn-danger btn-sm" onclick="eliminarFila(this, ${insumoSeleccionado.id})"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
            <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/></svg>
            </button>
        </td>
        `
        //agrego la fila nueva a la tabla
        tabla.appendChild(fila);
        //agrego el insumo a la tabla para que no se repitan en el pedido
        insumosEnTabla.push(insumoSeleccionado.id);
        //limpio el valor del insumo seleccionado
        insumoSeleccionado = null;
        //limpio el campo "cantidad"
        document.getElementById('boton-cantidad').value='';
        document.getElementById('insumo-elegido').value='';
    }

}

function eliminarFila(boton,insumoId){
    //.closest trae el nodo anteior más cercano de un elemento, que debe coincidir con un selector como parametro.
    const fila = boton.closest('tr');
    //elimino la fila del DOM.
    fila.remove();
    
    //filtra los insumos en la lista
    insumosEnTabla = insumosEnTabla.filter(id => id !== insumoId);
}


function reiniciarTabla(){
    const tabla = document.getElementById('cuerpo-tabla');
    tabla.innerHTML = ''; // Elimina todas las filas de la tabla

    // Reinicia la lista de insumos en la tabla para que puedan volver a seleccionarse
    insumosEnTabla = [];
}


function actualizarIndiceElemento(elemento,prefijo,indice_actual){

    const expresion_regular = new RegExp(`(${prefijo}-\\d+)`);//crea una expresion regular con del tipo 'prefijo'-(digito)
    const reemplazo = `${prefijo}-${indice_actual}`; 
    if(elemento.id) elemento.id = elemento.id.replace(expresion_regular,reemplazo); //se reemplaza el id 
    if(elemento.name) elemento.name = elemento.name.replace(expresion_regular,reemplazo); //se reemplaza el name de la etiqueta
}


function actualizarIndiceFormulario(){
    //Traigo como lista la todos los formularios dentro de 'formset-container'
    const items_formularios = document.getElementById('formset-container').getElementsByClassName('section-form');
    
    for(let i = 0; i < items_formularios.length; i++){
        //SE TRAEN LAS ETIQUETAS QUE SE DEBEN ACTUALIZAR MEDIANTE SUS CLASES
        //DICHAS ETIQUETAS TAMBIEN SON LISTAS DE ELEMENTOS HTML POR LO TANTO SE LAS DEBE ITERAR
        const form_input_insumo = items_formularios[i].getElementsByClassName('insumo-seleccionado');//me rerotrna una lista
        const form_input_cantidad = items_formularios[i].getElementsByClassName('cantidad-insumo');
        
        for(input_insumo of form_input_insumo){
            actualizarIndiceElemento(input_insumo,'form',i);
        }
        for(input_cantidad of form_input_cantidad){
            actualizarIndiceElemento(input_cantidad,'form',i);
        }
        
    }
    
}

function guardarValores(){
    //la cantidad de formset debe ser igual a la cantidad de insumos en la tabla
    document.getElementById('id_form-TOTAL_FORMS').value = insumosEnTabla.length;
    
    //traigo las filas que se crearon dinamicamente
    const filas = document.querySelectorAll('#cuerpo-tabla tr');

    //defino mi nodo base que contiene la info necesaria de los formset
    const nodo_base = document.getElementById('formset-container').children[0].cloneNode(true);
    
    //ingreso valores al primer form set
    nodo_base.querySelector('.insumo-seleccionado').value = insumosEnTabla[0]; //guardo el id del primer insumo elegido
    //ingreso la cantidad de la fila
    nodo_base.querySelector('.cantidad-insumo').value = filas[0].querySelector('td.fila_cantidad').textContent.trim();

    //Limpio el contenedor de formularios y agrego el nodo base como primer elemento
    const formsetContenedor = document.getElementById('formset-container');
    formsetContenedor.innerHTML = '';
    formsetContenedor.appendChild(nodo_base);

    for (let i = 1; i < insumosEnTabla.length;i++){
        //clono el nodo base
        const nuevo_nodo = nodo_base.cloneNode(true);

        //ahora relleno el nuevo nodo con los datos
        nuevo_nodo.querySelector('.insumo-seleccionado').value = insumosEnTabla[i];

        nuevo_nodo.querySelector('.cantidad-insumo').value = filas[i].querySelector('td.fila_cantidad').textContent.trim();

        //agrego el nuevo nodo al contenedor
        formsetContenedor.appendChild(nuevo_nodo);
        //mando a actualizar el indice de los formularios
        actualizarIndiceFormulario();
    }
}