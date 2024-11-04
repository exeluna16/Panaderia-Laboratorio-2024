const alertaSwal = (titleText,text,icon,confirmButtonText)=>{
    Swal.fire({
        titleText : titleText,
        text : text, 
        icon : icon, //valores => success,error,info,warning
        confirmButtonText : confirmButtonText,
    });
} 