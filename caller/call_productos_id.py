import requests

# URL base de la API
base_url = "http://127.0.0.1:5000"

# Obtener un producto por ID
producto_id = 6  # Cambiar al ID del producto que deseas obtener
response = requests.get(f"{base_url}/productos/{producto_id}")
producto = response.json()
print("Producto:", producto)

