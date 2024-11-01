let proveedores = [];
let insumos = [];
let insumosEnTabla = [];
document.addEventListener('DOMContentLoaded', function() {
    
    fetch('../proveedores/ver_proveedores')//se envia la petición
    .then(respuesta => respuesta.json())//transformo la respuesta en un JSON
    .then(datos =>{
        proveedores = datos
    })
    .catch(error=>console.error('No se pudo traer a los proveedores de la BD',error));
    
    fetch('../inventario/listar_insumos')
    .then(respuesta => respuesta.json())
    .then(datos => {
        insumos = datos
    })
    .catch(error=>console.error('No se pudo traer los insumos de la BD',error));

    fechaActual();
    
});

function fechaActual(){
    const fecha_actual = new Date();
    //agrego la fecha actual
    //.padStart(2, '0') se asegura de que los dias o meses tengan el 0 delante si son menores a 10.
    const fecha_formateada = `${fecha_actual.getFullYear()}-${String(fecha_actual.getMonth() + 1).padStart(2, '0')}-${String(fecha_actual.getDate()).padStart(2, '0')}`;
    document.getElementById('fecha_pedido').value = fecha_formateada;
    //desabilito el campo para que no se pueda cambiar
    document.getElementById('fecha_pedido').disabled = true;

}

function buscarProveedor(){
    const consulta = document.getElementById('buscador-proveedor').value.toLowerCase();
    const lista_proveedores = document.getElementById('lista-proveedores');
    lista_proveedores.innerHTML = '';

    const resultados = proveedores.filter(p =>p.nombre.toLowerCase().includes(consulta));

    resultados.forEach(proveedor=>{
        const li = document.createElement('li');
        li.classList.add('list-group-item','list-group-item-action');
        li.textContent = proveedor.nombre;
        li.onclick = () => seleccionarProveedor(proveedor);
        lista_proveedores.appendChild(li);
    });
}
function buscarInsumo(){
    const consulta = document.getElementById('buscar-insumo').value.toLowerCase();
    const lista_insumos = document.getElementById('lista-insumos');
    lista_insumos.innerHTML = '';

    const resultados = insumos.filter(i => i.nombre.toLowerCase().includes(consulta));

    resultados.forEach(insumo=> {
        const li = document.createElement('li');
        li.classList.add('list-group-item','list-group-item-action');
        li.textContent = insumo.nombre;
        li.onclick = () => seleccionarInsumo(insumo);
        lista_insumos.appendChild(li);
    });
}

function seleccionarProveedor(proveedor){
    document.getElementById('proveedor-elegido').value = proveedor.nombre;
    //a continuacion se cierra el modal de Bootstrap
    //para eso se necesita instanciar la clase Modal y llamar el metodo .hide()    
    const modal = bootstrap.Modal.getInstance(document.getElementById('staticBackdrop'));
    modal.hide();
}

function seleccionarInsumo(insumo){
    document.getElementById('insumo-elegido').value = insumo.nombre;
    document.getElementById('lista-insumos').innerHTML='';
    document.getElementById('buscar-insumo').value='';
}