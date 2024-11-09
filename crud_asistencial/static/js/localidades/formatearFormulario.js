// Validación de campos obligatorios
function validarCamposObligatorios() {
  const camposRequeridos = document.querySelectorAll("input[required], select[required]");
  return Array.from(camposRequeridos).every(campo => campo.value.trim() !== "");
}

// Validación de código telefónico con formato internacional
function validarCodigoTelefonico(codigo) {
  const regex = /^\+\d{1,3}\s?\d{10}$/; 
  return regex.test(codigo);
}

// Función para mostrar un mensaje de error personalizado
function mostrarErrorPersonalizado(input, mensaje) {
  // Agregar clase de error para aplicar estilos CSS
  errorElement.classList.add('error');
}

// Formato para mostrar al usuario (primera letra en mayúscula excepto "y")
function formatearTextoParaUsuario(texto) {
  return texto
      .toLowerCase()
      .replace(/\b\w/g, letra => letra.toUpperCase())
      .replace(/\by\b/g, "y");
}

// Normalización del texto para enviar al servidor (todo en minúsculas y sin acentos)
function normalizarTexto(texto) {
  return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

// Verificar si el dato ya existe en el servidor
async function verificarDuplicado(input, tipo) {
  const dato = normalizarTexto(input.value);
  try {
      const response = await fetch(`/api/paises/verificar-duplicado/?tipo=${tipo}&dato=${dato}`);
      const result = await response.json();

      if (result.existe) {
          mostrarError(input, `El ${tipo} ya existe en la base de datos.`);
      } else {
          limpiarError(input);
      }
  } catch (error) {
      console.error("Error al verificar duplicado:", error);
      mostrarError(input, "Hubo un problema al verificar el dato. Intenta de nuevo.");
  }
}

// Mostrar mensaje de error en el input
function mostrarError(input, mensaje) {
  const errorElement = input.parentElement.querySelector(".error");
  if (errorElement) {
      errorElement.textContent = mensaje;
      errorElement.style.display = "block";
  }
}

// Limpiar el mensaje de error en el input
function limpiarError(input) {
  const errorElement = input.parentElement.querySelector(".error");
  if (errorElement) {
      errorElement.style.display = "none";
  }
}

// Validación completa del formulario antes del envío
function validarFormulario() {
  // Campos telefónicos (Ejemplo: código de país y región)
  const codigoTelefonicoPais = document.getElementById("codigoTelefonicoPais");
  const codigoTelefonicoRegion = document.getElementById("codigoTelefonicoRegion");

  // Verificar si los elementos existen antes de intentar acceder a sus valores
  if (!codigoTelefonicoPais || !codigoTelefonicoRegion) {
    console.error("Faltan los campos de código telefónico.");
    return false; // Evita la validación si los elementos no existen
  }

  // Validación de códigos numéricos
  if (!validarCodigoTelefonico(codigoTelefonicoPais.value)) {
      mostrarError(codigoTelefonicoPais, "El código telefónico del país debe ser numérico.");
      return false;
  }
  if (!validarCodigoTelefonico(codigoTelefonicoRegion.value)) {
      mostrarError(codigoTelefonicoRegion, "El código telefónico de la región debe ser numérico.");
      return false;
  }

  // Validación de campos obligatorios
  if (!validarCamposObligatorios()) {
      alert("Por favor, completa todos los campos obligatorios.");
      return false;
  }

  return true; // Si todas las validaciones pasan, se puede enviar
}


// Formatear el texto al mostrar al usuario
function actualizarVista(input) {
  input.value = formatearTextoParaUsuario(input.value);
}

// Event listeners para el formulario
document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.getElementById("formulario-localidad");
  
  if (formulario) {  // Verifica que el formulario exista
      formulario.addEventListener("submit", (e) => {
          if (!validarFormulario()) {
              e.preventDefault(); // Evitar el envío si hay campos incompletos o con errores
          }
      });

      // Agregar validación de duplicados en tiempo real
      formulario.querySelectorAll("input[data-duplicado]").forEach(input => {
          input.addEventListener("blur", () => verificarDuplicado(input, input.dataset.duplicado));
          input.addEventListener("input", () => actualizarVista(input)); // Formato de visualización
      });
  }
});
