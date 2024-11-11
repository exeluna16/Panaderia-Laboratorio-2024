const alertaSwal = (titleText,text,icon,confirmButtonText)=>{
    Swal.fire({
        titleText : titleText,
        text : text, 
        icon : icon, //valores => success,error,info,warning
        confirmButtonText : confirmButtonText,
    });
} 
//funcion para dar baja desde el template de cada listado
document.getElementById('dar_baja').addEventListener('submit', async function (evento) {
    evento.preventDefault();
    await confirmarBaja(evento.target.action);
});

async function confirmarBaja(link) {
    const respuesta = await Swal.fire({
        title: "¿Desea confirmar la Baja?",
        showCancelButton: true,
        confirmButtonText: "Dar BAJA",
        confirmButtonColor: "#dc3545", // rojo de bootstrap
        backdrop: true,
        showLoaderOnConfirm: true,
        allowOutsideClick: () => false,
        allowEscapeKey: () => false,
    });

    if (respuesta.isConfirmed) {
        const form = document.getElementById('dar_baja');
        form.action = link;
        form.submit();
    } else {
        console.log('El usuario canceló la acción');
    }
}


function es_numero_negativo(numero){
    if(numero<1){
        alertaSwal('Error','Estas ingresando un número negativo','error','OK!');
        return true;
    }
    return false;
}

function es_numero(numero){
    if(isNaN(numero)){
        alertaSwal('Error', numero + ' No es un número. Por favor controlar','error','OK!');
        return false;
    }
    return true;
}