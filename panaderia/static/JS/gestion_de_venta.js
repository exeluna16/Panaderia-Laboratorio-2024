let productos = [];
let productoSeleccionado = null;

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
    document.getElementById('nombreProducto').textContent = producto.nombre;
    document.getElementById('productoSeleccionado').style.display = 'block';
    document.getElementById('resultados').innerHTML = ''; // Limpia los campos
    document.getElementById('search').value = ''; // Limpiar la barra búsqueda
}

// Función para agregar producto a la tabla de ventas
function agregarProducto() {
    if (!productoSeleccionado) return;

    const cantidad = document.getElementById('cantidad').value;

    // Agregar fila a la tabla
    const tabla = document.getElementById('tablaVentas');
    const fila = document.createElement('tr');

    fila.innerHTML = `
        <td>${productoSeleccionado.nombre}</td>
        <td>${cantidad}</td>
        <td><button class="btn btn-danger btn-sm" onclick="eliminarFila(this)">Eliminar</button></td>
    `;

    tabla.appendChild(fila);

    // Limpiar la selección
    productoSeleccionado = null;
    document.getElementById('productoSeleccionado').style.display = 'none';
    document.getElementById('cantidad').value = 1;
}

// Función para eliminar una fila de la tabla
function eliminarFila(boton) {
    const fila = boton.closest('tr');
    fila.remove();
}