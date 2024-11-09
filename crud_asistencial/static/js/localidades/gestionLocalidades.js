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

  // Vincula la función al evento de clic en el botón para guardar el país
  const botonGuardar = document.getElementById("guardar-pais-btn");
  if (botonGuardar) {
    botonGuardar.addEventListener("click", guardarPais);
  }
});

// Función para guardar el país
function guardarPais(event) {
  event.preventDefault();  // Previene el envío normal del formulario

  // Obtener los valores de los campos del formulario
  const nombrePais = document.getElementById('nombre_pais').value;
  const codigoPais = document.getElementById('codigo_telefonico_pais').value;
  const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

  const data = {
    nombre_pais: nombrePais,
    codigo_telefonico_pais: codigoPais
  };

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
        return response.text().then(erroData =>{
          throw new Error(erroData.detail || 'Error al guardar el país');
        })
      }
      return response.json();
    })
    .then(data => {
      alert('País guardado exitosamente');
      obtenerPaises(); // Actualizar la lista de países
      limpiarFormulario('formulario-localidad'); // Limpiar el formulario
    })
    .catch(error => {
      console.error('Error:', error);
      alert(`Hubo un error al guardar el país:${error.message}`);
    });
}

// Función para obtener los países
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

// Función para limpiar el formulario
function limpiarFormulario(formularioId) {
  const formulario = document.getElementById(formularioId);
  if (formulario) {
    formulario.reset();
  } else {
    console.error(`Formulario con ID "${formularioId}" no encontrado.`);
  }
}
