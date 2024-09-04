document.getElementById("form_proveedor").addEventListener("submit", function(event){
    const fecha_hoy=new Date();

    const fecha_ingresada=new Date(document.getElementById("fecha_pedido").value);

    if(fecha_ingresada<fecha_hoy){
        event.preventDefault();
        alert("la fecha ingresada no es valida");
    }

})
