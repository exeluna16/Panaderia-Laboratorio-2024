let productos = [];
let clientes = [];
let productoSeleccionado = null;
const numero_comprobante = generarNumeroComprobante();
let item_numero = 0;
let total_venta = 0.00;
let cantidad_formularios = document.getElementById('id_venta-TOTAL_FORMS').value;
let productosEnTabla = [];  // Array para almacenar los IDs de productos en la tabla
//cuando el HTML se cargue envia por el metodo GET una solicitud a la vista de 'listar_prpoductos'
//la vista devuelve un JSON que será usado a lo largo de esta implementación
document.addEventListener('DOMContentLoaded', function() {

    fetch('../inventario/listar_productos') //se envia la peticion a la url correcpondiente
    .then(response => response.json()) //la respuesta se trasnforma en un JSON por si acaso, es una validacion
    .then(data => {
        productos = data
    })
    .catch(error => console.error('Error: al recueperar a los productos', error));

    fetch('../cliente_mayorista/ver_clientes_mayoristas')
    .then(respuesta => respuesta.json())
    .then(datos =>{
        clientes = datos
    })
    .catch(error => console.error('Error al recuperar a los clientes',error));

    fechaActual();
    
    document.getElementById('num_comprobante').value = numero_comprobante;// se agrega el numero en la vista
});

function fechaActual(){
    const fecha_actual = new Date();
    //agrego la fecha actual
    //.padStart(2, '0') se asegura de que los dias o meses tengan el 0 delante si son menores a 10.
    const fecha_formateada = `${fecha_actual.getFullYear()}-${String(fecha_actual.getMonth() + 1).padStart(2, '0')}-${String(fecha_actual.getDate()).padStart(2, '0')}`;
    document.getElementById('fecha_venta').value = fecha_formateada;
    //desabilito el campo para que no se pueda cambiar
    document.getElementById('fecha_venta').disabled = true;

}
//
//Cargar datos venta
document.getElementById('formulario_de_venta').addEventListener('submit',function(event){
    //Pauso el envio del formulario
    event.preventDefault();
    //EN ESTA PARTE ELIMINO LOS ITEMS VACIOS
    guardarValores();
    ///en esta parte del codigo se esta guardando el precio de la venta
    document.getElementById('id_total_venta').value = total_venta;

    document.getElementById('id_numero_comprobante').value = numero_comprobante;
    //Ingreso el empleado
    //document.getElementById('id_empleado').value=1;
     // Al final de se envia el formulario a la vista, rezemos para que se guarde
    this.submit();
});

function generarNumeroComprobante() {
    return Math.floor(Math.random() * 241183880);
}

// Función para seleccionar un producto
function seleccionarProducto(producto) {
    productoSeleccionado = producto;
    document.getElementById('nombreProducto').textContent = producto.nombre; //muestra el nombre del producto en la pagina
    document.getElementById('productoSeleccionado');//
    document.getElementById('resultados').innerHTML = ''; // Limpia los campos
    document.getElementById('search').value = ''; // Limpiar la barra búsqueda

}

// Esta función para busca productos en el archivo JSON recibido
function buscarProducto() {
    const query = document.getElementById('search').value.toLowerCase();
    const resultados = document.getElementById('resultados');//me trae la lista de resultados
    resultados.innerHTML = '';

    // Filtro los productos que coincidan con la búsqueda
    const productosFiltrados = productos.filter(p => p.nombre.toLowerCase().includes(query) && !productosEnTabla.includes(p.id));

    // Muestro los productos
    productosFiltrados.forEach(producto => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'list-group-item-action');
        li.textContent = producto.nombre;
        li.onclick = () => seleccionarProducto(producto); //Se pasa el OBJETO producto
        resultados.appendChild(li);
    });

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
//Funcion para comprobar desde el Front-End si hay suficiente cantidad de un producto ingresado
function existeSuficienteCantidad(cantidad){
    if (productoSeleccionado.cantidad < cantidad){
        //alert('NO hay suficiente cantidadad');
        alertaSwal('Aviso','no hay suficiente cantidad, la cantidad actual es: '+productoSeleccionado.cantidad,'warning','Ok')
        return false;
    }
    return true;
}

function agregarItem(){
    //le resto uno a la cantidad de formularios totales porque al agregar estamos sumando 1 pero nos interesa la cantidad del anterior
    let cantidad_ingresada = document.getElementById('cantidad_seleccionada').value;
    if(existeSuficienteCantidad(cantidad_ingresada) && !es_numero_negativo(cantidad_ingresada)){ 
        agregarProducto(); //al final se agrega el producto a la tabla
    }
}

// Función para agregar producto a la tabla de ventas
function agregarProducto() {
    if (!productoSeleccionado) return;
    
    const cantidad = document.getElementById('cantidad_seleccionada').value;
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
        <td class='fila_cantidad'>${cantidad}</td>
        <td>${productoSeleccionado.unidad_de_medida}</td>
        <td>$${productoSeleccionado.precio}</td>
        <td class='fila_sub_total'>$${productoSeleccionado.precio*cantidad}</td>
        <td><button class="btn btn-danger btn-sm" onclick="eliminarFila(this, ${productoSeleccionado.id})"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
        <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
        </svg></button></td>
    `;

    tabla.appendChild(fila);
    totalVenta()
    //agrego el producto elegido en la lista de ya elegidos
    productosEnTabla.push(productoSeleccionado.id);
    // limpio el resultado
    document.getElementById('nombreProducto').textContent = '';
    productoSeleccionado = null;

}


// Función para eliminar una fila de la tabla
function eliminarFila(boton,productoId) {

    const fila = boton.closest('tr');
    fila.remove();
    item_numero--;
    totalVenta(); ///como se elimino un producto se debe actualizar el total

    // Eliminamos el ID del producto de productosEnTabla para que se pueda volver a seleccionar
    productosEnTabla = productosEnTabla.filter(id => id !== productoId);
}

function actualizarIndiceFormulario(){
    //Traigo como lista la todos los formularios dentro de 'formset-container'
    const items_formularios = document.getElementById('formset-container').getElementsByClassName('section-form');
    
    for(let i = 0; i < items_formularios.length; i++){
        //SE TRAEN LAS ETIQUETAS QUE SE DEBEN ACTUALIZAR MEDIANTE SUS CLASES
        //DICHAS ETIQUETAS TAMBIEN SON LISTAS DE ELEMENTOS HTML POR LO TANTO SE LAS DEBE ITERAR
        const form_input_producto = items_formularios[i].getElementsByClassName('producto-seleccionado');//me rerotrna una lista
        const form_input_sub_total = items_formularios[i].getElementsByClassName('sub-total');
        const form_input_cantidad = items_formularios[i].getElementsByClassName('cantidad-producto');
        const form_delete_checkbox = items_formularios[i].querySelectorAll('input[type="checkbox"]');
        
        for(input_producto of form_input_producto){
            ActualizarIndiceElemento(input_producto,'venta',i);
        }
        for(input_sub_total of form_input_sub_total){
            ActualizarIndiceElemento(input_sub_total,'venta',i);
        }
        for(input_cantidad of form_input_cantidad){
            ActualizarIndiceElemento(input_cantidad,'venta',i);
        }
        for(checkbox_delete of form_delete_checkbox){
            ActualizarIndiceElemento(checkbox_delete,'venta',i);
        }
    }
    //actualizo la cantidad directamente en el DOM porque sino se enviaria unicamente el primer item_venta
    //document.getElementById('id_venta-TOTAL_FORMS').value = items_formularios.length;
    //cantidad_formularios = items_formularios.length; //obtenemos la cantidad de formularios
    
}

function ActualizarIndiceElemento(elemento,prefijo,indice_actual){

    const expresion_regular = new RegExp(`(${prefijo}-\\d+)`);//crea una expresion regular con del tipo 'prefijo'-(digito)
    const reemplazo = `${prefijo}-${indice_actual}`; 
    if(elemento.id) elemento.id = elemento.id.replace(expresion_regular,reemplazo); //se reemplaza el id 
    if(elemento.name) elemento.name = elemento.name.replace(expresion_regular,reemplazo); //se reemplaza el name de la etiqueta
}


function guardarValores(){
    //la cantidad de formsets debe ser iguala la cantidad de productos en la tabla
    document.getElementById('id_venta-TOTAL_FORMS').value = productosEnTabla.length;//funciona
    ///traigo una lista de las filas cargadas dinamicamente
    const filas = document.querySelectorAll('#cuerpo_tabla_ventas tr');
    //copiamos el primer nodo
    const nodo_base = document.getElementById('formset-container').children[0].cloneNode(true); 
    //Lenamos el primer formset
    nodo_base.querySelector('.producto-seleccionado').value = productosEnTabla[0];
    
    //TRAIGO LA CANTIDAD DE PRODUCTO INGRESADA EN DICHA FILA
    nodo_base.querySelector('.cantidad-producto').value = filas[0].querySelector('td.fila_cantidad').textContent.trim();
    
    //TRAIGO EL SUBTOTAL DE LA TABLA, PERO COMO TIENE EL SIGNO '$' SE UTILIZA .replace para porner un espacio en blanco que despues se elimina con .trim()
    nodo_base.querySelector('.sub-total').value = filas[0].querySelector('td.fila_sub_total').textContent.replace('$', '').trim();

     // Limpio el contenedor de formularios y agrego el nodo base como primer elemento
    const formsetContainer = document.getElementById('formset-container');
    formsetContainer.innerHTML = '';  // Borra el contenido previo
    formsetContainer.appendChild(nodo_base);

    for(let i = 1 ; i < productosEnTabla.length;i++){    
        // Clonamos el nodo base con los valores que le dimos antes
        const nuevo_nodo = nodo_base.cloneNode(true);

        //llenamos el nuevo nodo con cada valor que viene de la fila actual en la que estamos iterando
        nuevo_nodo.querySelector('.producto-seleccionado').value = productosEnTabla[i];

        nuevo_nodo.querySelector('.cantidad-producto').value = filas[i].querySelector('td.fila_cantidad').textContent.trim();

        nuevo_nodo.querySelector('.sub-total').value = filas[i].querySelector('td.fila_sub_total').textContent.replace('$', '').trim();


        // Agrego el nuevo nodo al contenedor
        formsetContainer.appendChild(nuevo_nodo);

        //actualizo los indices de los formularios
        actualizarIndiceFormulario()
    }

}

function buscarMayorista(){
    const consulta = document.getElementById('buscador-mayorista').value.toLowerCase();

    const lista_clientes = document.getElementById('lista-clientes');
    lista_clientes.innerHTML='';

    const resultados = clientes.filter(cli => cli.nombre.toLowerCase().includes(consulta));
    resultados.forEach(cliente =>{
        const li = document.createElement('li');
        li.classList.add('list-group-item','list-group-item-action');
        li.textContent = cliente.nombre;
        li.onclick = () => seleccionarMayorista(cliente);
        lista_clientes.appendChild(li);
    });

}

function seleccionarMayorista(cliente){
    //pongo el valor del cliente mayorista en su formulario
    document.getElementById('id_cliente_mayorista').value = cliente.id;
    //cierro el modal
    const modal = bootstrap.Modal.getInstance(document.getElementById('staticBackdrop'));
    modal.hide();

    //Se carga el valor del cliente seleccionado para que el usuario lo vea
    document.getElementById('cliente-elegido').value = cliente.nombre;
}

