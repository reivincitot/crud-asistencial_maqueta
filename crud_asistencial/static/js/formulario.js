function actualizarRegion() {
  const paisId = document.getElementById("SeleccionPais").value;
  fetch(`/obtener-regiones/?pais_id=${paisId}`)
    .then(response => response.json())
    .then(data => {
      const regionSelect = document.getElementById("SeleccionRegion");
      regionSelect.innerHTML = '<option value="">Seleccione una Región</option>';
      data.forEach(region => {
        regionSelect.innerHTML += `<option value="${region.id}">${region.nombre}</option>`;
      });
      regionSelect.disabled = false;
    });
}

function actualizarProvincias() {
  const regionId = document.getElementById("SeleccionRegion").value;
  fetch(`/obtener-provincias/?region_id=${regionId}`)
    .then(response => response.json())
    .then(data => {
      const provinciaSelect = document.getElementById("SeleccionProvincia");
      provinciaSelect.innerHTML = '<option value="">Seleccione una Provincia</option>';
      data.forEach(provincia => {
        provinciaSelect.innerHTML += `<option value="${provincia.id}">${provincia.nombre}</option>`;
      });
      provinciaSelect.disabled = false;
    });
}

function verificarDuplicado(campo, valor) {
  fetch(`/verificar-duplicado/?nombre=${encodeURIComponent(valor)}`)
    .then(response => response.json())
    .then(data => {
      if (data.existe) {
        alert(`El valor "${valor}" ya existe en ${campo}.`);
      }
    });
}
