let productos = [];
let productoSeleccionado = null;
let item_numero = 0;
let total_venta = 0.00;
let cantidad_formularios = 0;

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

//Cargar datos venta
document.getElementById('formulario_de_venta').addEventListener('submit',function(event){

    //Pauso el envio del formulario
    event.preventDefault();

    //EN ESTA PARTE CARGO LOS DATOS DE LOS ITEMS seria conveniente hacerlo en un JSON y enviarlos a django


    ///en esta parte del codigo se esta guardando el precio de la venta
    document.getElementById('id_total_venta').value = total_venta;

     // Al final de se envia el formulario a la vista, rezemos para que se guarde
    this.submit();
});


//
const nodo_base_cantidad = document.querySelector('#id_form-0-cantidad').cloneNode(true);
const nodo_base_producto = document.querySelector('#id_form-0-producto').cloneNode(true);
const nodo_base_sub_total = document.querySelector('#id_form-0-sub_total').cloneNode(true);
function agregarItem(){

    //EL PRODUCTO SE DEBE AGREGARA A LA TABLA AL HACER CLICK
    //le asigno valores a los campos
    if(item_numero===0){ //en la primera iteracion
        nodo_base_producto.value = productoSeleccionado.nombre;
        document.querySelector('#id_form-0-sub_total').value = document.querySelector('#id_form-0-cantidad').value * productoSeleccionado.precio
    }


    //CAMPOS QUE SE AGREGAN
    cantidad_formularios = document.querySelector('#id_form-TOTAL_FORMS');

    let nueva_cantidad = nodo_base_cantidad.cloneNode(true)//document.querySelector('#id_form-0-cantidad').cloneNode(true); /// copio el campo completo
    let campo_prod = nodo_base_producto.cloneNode(true);
    let campo_sub_total = nodo_base_sub_total.cloneNode(true);

    //CAMPO PRODUCTO
    campo_prod.name='form-'+cantidad_formularios.value+'-producto';
    campo_prod.id = 'id_form'+cantidad_formularios.value+'-producto';
    //CAMPO CANTIDAD
    nueva_cantidad.name='form-'+cantidad_formularios.value+'-cantidad';
    nueva_cantidad.id = 'id_form-'+cantidad_formularios.value+'-cantidad';
    //Campo Subtotal
    campo_sub_total.name='form-'+cantidad_formularios.value+'-sub_total';
    campo_sub_total.id = 'id_form-'+cantidad_formularios.value+'sub_total';
    //
    campo_prod.value = productoSeleccionado.nombre

    //campo_sub_total.value = productoSeleccionado.precio * nueva_cantidad.value


    document.querySelector('#item_contenedor').appendChild(campo_prod);
    document.querySelector('#item_contenedor').appendChild(nueva_cantidad);
    document.querySelector('#item_contenedor').appendChild(campo_sub_total);

    //aumento la cantidad de formularios en 1
    cantidad_formularios.value = parseInt(cantidad_formularios.value) + 1;

    agregarProducto() //al final se agrega el producto a la lista
}


// Función para buscar productos en el archivo JSON recibido
function buscarProducto() {
    const query = document.getElementById('search').value.toLowerCase();
    const resultados = document.getElementById('resultados');
    resultados.innerHTML = '';

    // Filtrar productos que coincidan con la búsqueda
    const productosFiltrados = productos.filter(p => p.nombre.toLowerCase().includes(query));

    // Mostrar los productos
    productosFiltrados.forEach(producto => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'list-group-item-action');
        li.textContent = producto.nombre;
        li.onclick = () => seleccionarProducto(producto);
        resultados.appendChild(li);
    });
}

// Función para seleccionar un producto
function seleccionarProducto(producto) {
    productoSeleccionado = producto;
    document.getElementById('nombreProducto').textContent = producto.nombre; //muestra el nombre del producto en la pagina
    document.getElementById('productoSeleccionado')//
    document.getElementById('resultados').innerHTML = ''; // Limpia los campos
    document.getElementById('search').value = ''; // Limpiar la barra búsqueda

}

//Funcion para calcular el total de la venta
function totalVenta(cantidad_ingresada){

    total_venta = total_venta + (productoSeleccionado.precio * cantidad_ingresada);
    document.getElementById('p_total_venta').textContent = '$' + total_venta.toFixed(2)

}

// Función para agregar producto a la tabla de ventas
function agregarProducto() {
    if (!productoSeleccionado) return;

    const cantidad = document.getElementById('id_form-'+item_numero+'-cantidad').value;

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
        <td><button class="btn btn-danger btn-sm" onclick="eliminarFila(this)">Eliminar</button></td>
    `;

    tabla.appendChild(fila);
    totalVenta(cantidad)
    // Limpiar la cantidad
    productoSeleccionado = null;

    //document.getElementById('cantidad').value = 0;
}



// Función para eliminar una fila de la tabla
function eliminarFila(boton) { //{{ form.DELETE.id }}
    const fila = boton.closest('tr');
    fila.remove();
    item_numero--;
}