import requests

# URL base de la API
base_url = "http://127.0.0.1:5000"

# Obtener un producto por ID
producto_id = 11  # Cambiar al ID del producto que deseas obtener

# Eliminar un producto por ID
response = requests.delete(f"{base_url}/productos/{producto_id}")
print("Respuesta:", response.json())
