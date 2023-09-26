from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

# Cadena de conexión
cadena_conexion = "DRIVER={ODBC Driver 17 for SQL Server};Server=.\SQLEXPRESS;Database=Carrito;UID=Mazazo;PWD=Clave52;"
conexion = pyodbc.connect(cadena_conexion)
cursor = conexion.cursor()


# Función para obtener un producto por ID
def obtener_producto_por_id(id_producto):
    cursor.execute('SELECT * FROM Producto WHERE ID_Producto = ?', id_producto)
    fila = cursor.fetchone()
    if fila:
        producto = {
            'ID_Producto': fila.ID_Producto,
            'Descripcion': fila.Descripcion,
            'Fecha': fila.Fecha,
            'Precio': fila.Precio,
            'Comentario': fila.Comentario
        }
        return producto
    return None

# Ruta para obtener la página defaul (en general se la llama Index.HTML)
@app.route('/')
def index():
    return render_template('Index.html')

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        cursor.execute('SELECT * FROM Producto')
        productos = []
        for fila in cursor.fetchall():
            producto = {
                'ID_Producto': fila.ID_Producto,
                'Descripcion': fila.Descripcion,
                'Fecha': fila.Fecha,
                'Precio': fila.Precio,
                'Comentario': fila.Comentario
            }
            productos.append(producto)
        return jsonify(productos)
    except Exception as e:
        return jsonify({'error': 'Error al obtener los productos: ' + str(e)}), 500

# Ruta para obtener un producto por ID
@app.route('/productos/<int:id_producto>', methods=['GET'])
def obtener_producto(id_producto):
    try:
        producto = obtener_producto_por_id(id_producto)
        if producto:
            return jsonify(producto)
        return jsonify({'error': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al obtener el producto: ' + str(e)}), 500

# Ruta para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    try:
        nuevo_producto = request.json
        cursor.execute('INSERT INTO Producto (Descripcion, Fecha, Precio, Comentario) VALUES (?, ?, ?, ?)',
                       nuevo_producto['Descripcion'], nuevo_producto['Fecha'], nuevo_producto['Precio'], nuevo_producto['Comentario'])
        conexion.commit()
        return jsonify({'mensaje': 'Producto agregado correctamente'}), 201
    except Exception as e:
        return jsonify({'error': 'Error al agregar el producto: ' + str(e)}), 500

# Ruta para actualizar un producto por ID
@app.route('/productos/<int:id_producto>', methods=['PUT'])
def actualizar_producto(id_producto):
    try:
        producto_actualizado = request.json
        cursor.execute('UPDATE Producto SET Descripcion=?, Fecha=?, Precio=?, Comentario=? WHERE ID_Producto=?',
                       producto_actualizado['Descripcion'], producto_actualizado['Fecha'], producto_actualizado['Precio'], producto_actualizado['Comentario'], id_producto)
        conexion.commit()
        return jsonify({'mensaje': 'Producto actualizado correctamente'})
    except Exception as e:
        return jsonify({'error': 'Error al actualizar el producto: ' + str(e)}), 500

# Ruta para eliminar un producto por ID
@app.route('/productos/<int:id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    try:
        producto = obtener_producto_por_id(id_producto)
        if producto:
            cursor.execute('DELETE FROM Producto WHERE ID_Producto = ?', id_producto)
            conexion.commit()
            return jsonify({'mensaje': 'Producto eliminado correctamente'})
        return jsonify({'error': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Error al eliminar el producto: ' + str(e)}), 500

# Ruta para alta masiva de productos
@app.route('/productos/alta-masiva', methods=['POST'])
def alta_masiva_productos():
    try:
        productos_nuevos = request.json
        for nuevo_producto in productos_nuevos:
            cursor.execute('INSERT INTO Productos (ID, Descripcion, Precio, Cantidad) VALUES (?, ?, ?, ?)',
                           nuevo_producto['ID'], nuevo_producto['Descripcion'], nuevo_producto['Precio'], nuevo_producto['Cantidad'])
        conexion.commit()
        return jsonify({'mensaje': 'Alta masiva de productos exitosa'}), 201
    except Exception as e:
        return jsonify({'error': 'Error en la alta masiva de productos: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=4500)