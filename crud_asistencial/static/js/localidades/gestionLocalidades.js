document.addEventListener("DOMContentLoaded", function () {
  obtenerPaises();
});

function obtenerPaises() {
  fetch(paisListUrl)
    .then(response => response.json())
    .then(paises => {
      const select = document.getElementById("pais_select");
      select.innerHTML = '<option value="">Selecciona un país</option>';

      paises.forEach(pais => {
        const option = document.createElement("option");
        option.value = pais.id;
        option.textContent = pais.nombre_pais;
        select.appendChild(option);
      });
    })
    .catch(error => {
      console.error("Error al cargar los países:", error);
    });
}

function guardarPais(event) {
  event.preventDefault(); // Previene el envío automático del formulario
  const nombrePais = document.getElementById('nombre_pais').value;
  const codigoPais = document.getElementById('codigo_telefonico_pais').value;

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch(paisListUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken
    },
    body: JSON.stringify({
      "nombre_pais": nombrePais,
      "codigo_telefonico_pais": codigoPais
    })
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Error en la solicitud');
      }
      return response.json();
    })
    .then(data => {
      alert('País guardado exitosamente');
      obtenerPaises();  // Recarga la lista de países al guardar uno nuevo
    })
    .catch(error => {
      alert('Hubo un error al guardar el país');
      console.error(error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  const paisSelect = document.getElementById("pais_select");
  const codigoTelefonicoSpan = document.getElementById("codigo-telefonico");

  if (paisSelect) {
    // Funcionalidad cuando el select existe en el DOM
    paisSelect.addEventListener("change", async function () {
      const paisId = paisSelect.value;

      if (paisId) {
        try {
          const response = await fetch(`/api/obtener-codigo-telefonico?pais_id=${paisId}`);

          if (response.ok) {
            const data = await response.json();
            codigoTelefonicoSpan.textContent = data.codigo_telefonico;
          } else {
            console.error("Error al obtener el código telefónico del país.");
            codigoTelefonicoSpan.textContent = "";
          }
        } catch (error) {
          console.error("Error de conexión:", error);
          codigoTelefonicoSpan.textContent = "";
        }
      } else {
        codigoTelefonicoSpan.textContent = "";
      }
    });
  } else {
    console.error("Elemento pais_select no encontrado en el DOM.");
  }
});
