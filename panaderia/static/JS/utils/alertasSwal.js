const alertaSwal = (titleText,text,icon,confirmButtonText)=>{
    Swal.fire({
        titleText : titleText,
        text : text, 
        icon : icon, //valores => success,error,info,warning
        confirmButtonText : confirmButtonText,
    });
} 




function es_numero_negativo(numero){
    if(numero<0){
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