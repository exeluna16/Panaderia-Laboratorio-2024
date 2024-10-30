document.getElementById('formulario_agregar_empleado').addEventListener('submit',function(e){
    e.preventDefault();
    document.getElementById('id_tipo_persona').value = 'FISICA'; //Por defecto los empleados son personas fisicas
    this.submit();
});