import requests

# URL base de la API
base_url = "http://127.0.0.1:4000"

# Obtener todos los productos
response = requests.get(f"{base_url}/productos")
productos = response.json()
print("Productos:", productos)
