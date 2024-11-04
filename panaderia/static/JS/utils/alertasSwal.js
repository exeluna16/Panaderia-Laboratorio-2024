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
        alertaSwal('Error','Ingrese un numero valido','error','OK!');
        return true;
    }
    return false;
}