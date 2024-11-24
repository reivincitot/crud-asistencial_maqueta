document.addEventListener("DOMContentLoaded", function () {
  const regionSelect = document.getElementById('region');
  const provinceSelect = document.getElementById('province');
  const communeSelect = document.getElementById('commune');

  const regiones = JSON.parse('{{ regiones| safe}}');  // Pasar las regiones como un objeto JSON en el contexto

regionSelect.addEventListener('change', function () {
  // Limpiar las opciones anteriores
  provinceSelect.innerHTML = '<option value="">Seleccione una provincia</option>';
  communeSelect.innerHTML = '<option value="">Seleccione una comuna</option>';

  const regionSeleccionada = regiones.find(region => region.nombre === regionSelect.value);

  if (regionSeleccionada) {
    regionSeleccionada.provincias.forEach(provincia => {
      const option = document.createElement('option');
      option.value = provincia.nombre;
      option.textContent = provincia.nombre;
      provinceSelect.appendChild(option);
    });
  }
});

provinceSelect.addEventListener('change', function () {
  // Limpiar las opciones anteriores
  communeSelect.innerHTML = '<option value="">Seleccione una comuna</option>';

  const regionSeleccionada = regiones.find(region => region.nombre === regionSelect.value);
  const provinciaSeleccionada = regionSeleccionada.provincias.find(provincia => provincia.nombre === provinceSelect.value);

  if (provinciaSeleccionada) {
    provinciaSeleccionada.comunas.forEach(comuna => {
      const option = document.createElement('option');
      option.value = comuna.nombre;
      option.textContent = comuna.nombre;
      communeSelect.appendChild(option);
    });
  }
});
  });

