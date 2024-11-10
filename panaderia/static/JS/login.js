window.onload = function() {
    // Mostrar el mensaje durante 5 segundos
    setTimeout(function() {
        const mensaje = document.getElementById('mansaje_deslogueo');
        if (mensaje) {
            mensaje.style.display = 'none';
        }
    }, 5000); // 5000 ms = 5 segundos
};