function capitalizeWords(text) {
  return text
    .toLowerCase() // Asegúrate de que todo esté en minúsculas primero
    .split(' ')    // Divide el texto en palabras
    .map(word => word.charAt(0).toUpperCase() + word.slice(1)) // Capitaliza cada palabra
    .join(' ');    // Une las palabras nuevamente
}

// Ejemplo de uso
const originalText = "juan perez y asociacion";
const formattedText = capitalizeWords(originalText);

console.log(formattedText); // Output: "Juan Perez Y Asociacion"
