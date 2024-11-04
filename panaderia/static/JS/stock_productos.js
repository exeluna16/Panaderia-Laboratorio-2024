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