let productos = [];
let productoSeleccionado = null;
let item_numero = 0;
let total_venta = 0.00;
let cantidad_formularios = document.getElementById('id_venta-TOTAL_FORMS').value;
//cuando el HTML se cargue envia por el metodo GET una solicitud a la vista de 'listar_prpoductos'
//la vista devuelve un JSON que será usado a lo largo de esta implementación
document.addEventListener('DOMContentLoaded', function() {

    fetch('../inventario/listar_productos') //se envia la peticion a la url correcpondiente
    .then(response => response.json()) //la respuesta se trasnforma en un JSON por si acaso, es una validacion
    .then(data => {
        productos = data
    })
    .catch(error => console.error('Error:', error));
});
//


//Cargar datos venta
document.getElementById('formulario_de_venta').addEventListener('submit',function(event){

    //Pauso el envio del formulario
    event.preventDefault();

    //EN ESTA PARTE ELIMINO LOS ITEMS VACIOS
    console.log(document.getElementById('id_venta-TOTAL_FORMS').value)

    ///en esta parte del codigo se esta guardando el precio de la venta
    document.getElementById('id_total_venta').value = total_venta;
    //Ingreso el empleado
    document.getElementById('id_empleado').value=1;
    

     // Al final de se envia el formulario a la vista, rezemos para que se guarde
    this.submit();
});

function agregarItem(){
    console.log(productoSeleccionado.unidad_de_medida)
    guardarValores()
    //e.preventDefault();
    const nodo_base = document.getElementById('formset-container').children[0].cloneNode(true); //copia el primer nodo     
    ///del nodo clonado tengo que limpiar sus campos
    nodo_base.querySelectorAll('input').forEach(input =>input.value='');
    nodo_base.querySelectorAll('input[type="checkbox"]').forEach(checkbox =>checkbox.hidden=false);
    
    document.getElementById('formset-container').appendChild(nodo_base); //se agrega el nuevo nodo
    actualizarIndiceFormulario(); ///actaulizamos los indices dle formulario base
    
    agregarProducto() //al final se agrega el producto a la tabla
}
///guarda las cantidades en el formulario corresponidente, el cual siempre es uno menor a la cantidad total de formularios
function guardarValores() {
    cantidad_ingresada = document.getElementById('id_venta-'+(cantidad_formularios - 1)+'-cantidad').value;
    document.getElementById('id_venta-'+(cantidad_formularios - 1)+'-producto').value = productoSeleccionado.id;
    document.getElementById('id_venta-'+(cantidad_formularios - 1)+'-sub_total').value = productoSeleccionado.precio * cantidad_ingresada;
}

// Esta función para busca productos en el archivo JSON recibido
function buscarProducto() {
    const query = document.getElementById('search').value.toLowerCase();
    const resultados = document.getElementById('resultados');
    resultados.innerHTML = '';

    // Filtro los productos que coincidan con la búsqueda
    const productosFiltrados = productos.filter(p => p.nombre.toLowerCase().includes(query));

    // Muestro los productos
    productosFiltrados.forEach(producto => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'list-group-item-action');
        li.textContent = producto.nombre;
        li.onclick = () => seleccionarProducto(producto); //Se pasa el OBJETO producto
        resultados.appendChild(li);
    });
}

// Función para seleccionar un producto
function seleccionarProducto(producto) {
    productoSeleccionado = producto;
    document.getElementById('nombreProducto').textContent = producto.nombre; //muestra el nombre del producto en la pagina
    document.getElementById('productoSeleccionado');//
    document.getElementById('resultados').innerHTML = ''; // Limpia los campos
    document.getElementById('search').value = ''; // Limpiar la barra búsqueda

}

//Funcion para calcular el total de la venta
function totalVenta(){
    let list_sub_total = document.getElementsByClassName('fila_sub_total');
    let suma_sub_total = 0
    for (let i=0;i<list_sub_total.length;i++){
        let subTotalText = list_sub_total[i].textContent.replace('$', '').trim(); //quito el simbolo de $ y los espacios en blanco si hay
        suma_sub_total += parseFloat(subTotalText);
    }
    total_venta = suma_sub_total
    //total_venta = total_venta + (productoSeleccionado.precio * cantidad_ingresada);
    document.getElementById('p_total_venta').textContent = '$' + total_venta.toFixed(2)

}

// Función para agregar producto a la tabla de ventas
function agregarProducto() {
    if (!productoSeleccionado) return;
    
    const cantidad = document.getElementById('id_venta-'+item_numero+'-cantidad').value;

    item_numero++;
    // Agregar fila a la tabla
    const tabla = document.getElementById('cuerpo_tabla_ventas');
    const fila = document.createElement('tr');
    /* CAMPOS DE LA CABECERA DE LA TABLA
    <th>#</th>
    <th>Producto</th>
    <th>Cant</th>
    <th>Unidad de medida</th>
    <th>Precio</th>
    <th>Accion</th>
    */

    fila.innerHTML = `
        <td>${item_numero}</td>
        <td>${productoSeleccionado.nombre}</td>
        <td>${cantidad}</td>
        <td>${productoSeleccionado.unidad_de_medida}</td>
        <td>$${productoSeleccionado.precio}</td>
        <td class='fila_sub_total'>$${productoSeleccionado.precio*cantidad}</td>
        <td><button class="btn btn-danger btn-sm" onclick="eliminarFila(this)"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
        <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
        </svg></button></td>
    `;

    tabla.appendChild(fila);
    totalVenta()
    // limpio el resultado
    document.getElementById('nombreProducto').textContent = '';
    productoSeleccionado = null;

}

// Función para eliminar una fila de la tabla
function eliminarFila(boton) {

    const fila = boton.closest('tr');
    fila.remove();
    item_numero--;
    totalVenta(); ///como se elimino un producto se debe actualizar el total
}

function actualizarIndiceFormulario(){
    //Traigo como lista la todos los formularios dentro de 'formset-container'
    const items_formularios = document.getElementById('formset-container').getElementsByClassName('section-form');
    
    for(let i = 0; i < items_formularios.length; i++){
        //SE TRAEN LAS ETIQUETAS QUE SE DEBEN ACTUALIZAR MEDIANTE SUS CLASES
        //DICHAS ETIQUETAS TAMBIEN SON LISTAS DE ELEMENTOS HTML POR LO TANTO SE LAS DEBE ITERAR
        const form_input_producto = items_formularios[i].getElementsByClassName('producto-seleccionado')
        const form_input_sub_total = items_formularios[i].getElementsByClassName('sub-total')
        const form_input_cantidad = items_formularios[i].getElementsByClassName('cantidad-producto')
        
        for(input_producto of form_input_producto){
            ActualizarIndiceElemento(input_producto,'venta',i);
        }
        for(input_sub_total of form_input_sub_total){
            ActualizarIndiceElemento(input_sub_total,'venta',i);
        }
        for(input_cantidad of form_input_cantidad){
            ActualizarIndiceElemento(input_cantidad,'venta',i);
        }
    }
    //actualizo la cantidad directamente en el DOM porque sino se enviaria unicamente el primer item_venta
    document.getElementById('id_venta-TOTAL_FORMS').value = items_formularios.length;
    cantidad_formularios = items_formularios.length;
    
}

function ActualizarIndiceElemento(elemento,prefijo,indice_actual){

    const expresion_regular = new RegExp(`(${prefijo}-\\d+)`);
    const reemplazo = `${prefijo}-${indice_actual}`;
    if(elemento.id) elemento.id = elemento.id.replace(expresion_regular,reemplazo);
    if(elemento.name) elemento.name = elemento.name.replace(expresion_regular,reemplazo);
}


