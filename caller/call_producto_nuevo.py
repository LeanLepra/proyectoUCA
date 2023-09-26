import requests

# URL base de la API
base_url = "http://127.0.0.1:5000"

# Agregar un nuevo producto
nuevo_producto = {
    "ID": 11,
    "Descripcion": "Nuevo producto",
    "Precio": 99.99,
    "Cantidad": 5
}
response = requests.post(f"{base_url}/productos", json=nuevo_producto)
print("Respuesta:", response.json())

