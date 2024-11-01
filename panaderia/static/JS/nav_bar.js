const selectElement = document.getElementById('slct_inventario');

selectElement.addEventListener('change', (event) => {
  const selectedOption = event.target.value;
  switch (selectedOption) {
    case 'productos':
      window.location.href = '/inventario/stock_productos';
      break;
    case 'insumos':
      window.location.href = '/inventario/almacen_insumos/';
      break;
    // Agrega más casos según las opciones que tengas
    default:
      // Si no hay ninguna opción seleccionada o no está definida, puedes hacer algo aquí
  }
});