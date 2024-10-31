document.addEventListener('DOMContentLoaded',function(){
    const fecha_actual = new Date();
    //agrego la fecha actual
    const fecha_formateada = `${fecha_actual.getFullYear()}-${fecha_actual.getMonth()+1}-${fecha_actual.getDate()}`;
    document.getElementById('fecha_pedido').value = fecha_formateada;
    //desabilito el campo para que no se pueda cambiar
    document.getElementById('fecha_pedido').disabled = true;

});

