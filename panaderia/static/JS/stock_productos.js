document.getElementById('dar_baja').addEventListener('submit',function (evento){
    evento.preventDefault();
    
    if (confirmarBaja()){
        this.submit();
    }
    return false;
});

async function confirmarBaja() {
    const confirmacion = await Swal.fire(
        {
            title: "¿Desea confirmar la Baja?",
            showCancelButton: true,
            confirmButtonText: "Dar BAJA",
            confirmButtonColor: "#dc3545", //rojo de bootstrap
            backdrop:true,
            preConfirm: () =>{
                return true;
            },
            showLoaderOnConfirm:true,
            allowOutsideClick: () => false,
            allowEscapeKey: ()  => false,
        }
    );
    return confirmacion; // Esto determina si se envía o no el formulario
}