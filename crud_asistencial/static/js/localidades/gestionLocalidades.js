// Espera a que el DOM esté completamente cargado antes de ejecutar el script
document.addEventListener("DOMContentLoaded", function () {
  // Carga la lista de países en el <select> al cargar la página
  obtenerPaises();

  // Referencia al elemento <select> de país y al elemento <span> donde se mostrará el código telefónico
  const paisSelect = document.getElementById("pais_select");
  const codigoTelefonicoSpan = document.getElementById("codigo-telefonico");

  // Evento de cambio en el <select> de país para mostrar el código telefónico
  if (paisSelect) {
    paisSelect.addEventListener("change", function () {
      // Obtiene el valor del código telefónico desde el atributo "data-codigo" de la opción seleccionada
      const selectedOption = paisSelect.options[paisSelect.selectedIndex];
      const codigoTelefonico = selectedOption.getAttribute("data-codigo");

      // Muestra el código telefónico o limpia el <span> si no hay código
      codigoTelefonicoSpan.textContent = codigoTelefonico || "No disponible";
    });
  } else {
    console.error("Elemento pais_select no encontrado en el DOM.");
  }
});

/* Obtiene la lista de países de la API y llena el <select> de países con los datos. */
function obtenerPaises() {
  fetch(paisListUrl) // URL de la API que devuelve la lista de países
    .then(response => response.json()) // Convierte la respuesta en JSON
    .then(paises => {
      const select = document.getElementById("pais_select");

      // Limpia el <select> y agrega una opción inicial
      select.innerHTML = '<option value="">Selecciona un país</option>';

      // Itera sobre los países obtenidos y agrega cada uno como opción en el <select>
      paises.forEach(pais => {
        const option = document.createElement("option");
        option.value = pais.id; // ID del país para enviar en futuras solicitudes
        option.textContent = pais.nombre_pais; // Nombre del país a mostrar
        option.setAttribute("data-codigo", pais.codigo_telefonico_pais); // Guarda el código telefónico en un atributo personalizado
        select.appendChild(option); // Añade la opción al <select>
      });
    })
    .catch(error => {
      console.error("Error al cargar los países:", error);
    });
}

function limpiarFormulario(formularioId) {
  const formulario = document.getElementById(formularioId);
  if (formulario) {
    formulario.reset();

  } else {
    console.error(`Formulario con ID "${formularioId}" no encontrado.`);
  }
}

/* Envía el nuevo país a la API mediante una solicitud POST y recarga el <select> de países. */
document.addEventListener('DOMContentLoaded', () => {

  function guardarPais(event) {
    event.preventDefault();

    // Obtener los valores de los campos del formulario
    const nombrePais = document.getElementById('nombre_pais').value;
    const codigoPais = document.getElementById('codigo_telefonico_pais').value;
    const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    // Crear un objeto con los datos a enviar
    const data = {
      nombre_pais: nombrePais,
      codigo_telefonico_pais: codigoPais
    };

    // Enviar una solicitud POST a la API
    fetch(paisListUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(data)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Error al guardar el país');
        }
        return response.json();
      })
      .then(data => {
        alert('País guardado exitosamente');
        obtenerPaises(); // Actualizar la lista de países
        limpiarFormulario(); // Limpiar el formulario
      })
      .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al guardar el país. Por favor, inténtalo de nuevo.');
      });
  }
  document.getElementById('formulario-localidad').addEventListener('submit', guardarPais);
});