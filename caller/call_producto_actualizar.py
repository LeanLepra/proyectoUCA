import requests

# URL base de la API
base_url = "http://127.0.0.1:5000"


# Obtener un producto por ID
producto_id = 11  # Cambiar al ID del producto que deseas obtener

# Actualizar un producto por ID
producto_actualizado = {
    "Descripcion": "Producto actualizado",
    "Precio": 79.99,
    "Cantidad": 10
}

response = requests.put(f"{base_url}/productos/{producto_id}", json=producto_actualizado)
print("Respuesta:", response.json())
