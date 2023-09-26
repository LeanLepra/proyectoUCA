import requests

# URL del endpoint
url = 'http://localhost:5000/productos/alta-masiva'

# Datos de los productos para la alta masiva
productos_nuevos = [
    {
        "Cantidad": 50,
        "Descripcion": "Camiseta de futbol Seleccion Adidas",
        "ID": 21,
        "Precio": "29999.99"
    },
    {
        "Cantidad": 40,
        "Descripcion": "Shorts deportivos Adidas",
        "ID": 22,
        "Precio": "4999.99"
    },
    {
        "Cantidad": 30,
        "Descripcion": "Zapatillas de running Adidas",
        "ID": 23,
        "Precio": "45000.00"
    },
    {
        "Cantidad": 20,
        "Descripcion": "Pelota de futbol Adidas",
        "ID": 24,
        "Precio": "60500.00"
    },
    {
        "Cantidad": 100,
        "Descripcion": "Medias deportivas Adidas",
        "ID": 25,
        "Precio": "5999.99"
    },
    {
        "Cantidad": 8000,
        "Descripcion": "Camiseta LEPROSA Adidas",
        "ID": 26,
        "Precio": "300000.00"
    },
    {
        "Cantidad": 1,
        "Descripcion": "Gorra deportiva SINA Adidas",
        "ID": 27,
        "Precio": "1.99"
    },
    {
        "Cantidad": 30,
        "Descripcion": "Guantes de gimnasio Adidas",
        "ID": 28,
        "Precio": "11999.99"
    },
    {
        "Cantidad": 15,
        "Descripcion": "Rodillera deportiva Adidas",
        "ID": 29,
        "Precio": "9008.99"
    },
    {
        "Cantidad": 10,
        "Descripcion": "Mochila deportiva Adidas",
        "ID": 30,
        "Precio": "24000.00"
    }
]

# Realizar la solicitud POST
response = requests.post(url, json=productos_nuevos)

# Verificar la respuesta
if response.status_code == 201:
    print("Alta masiva de productos exitosa")
else:
    print("Error en la alta masiva de productos:", response.json())
