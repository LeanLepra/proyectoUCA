// Realizar una solicitud GET al servidor
        fetch('http://localhost:4500/productos')
            .then(response => response.json()) // Convertir la respuesta a JSON
            .then(data => {
                // Procesar los datos y mostrarlos en la página
                const productosContainer = document.getElementById('productos');

                // Iterar sobre cada producto en la respuesta
                data.forEach(producto => {
                    
                    // Construir el contenido HTML para cada producto
                    const contenidoProducto = `                         
                            <div class="card" style="width: 18rem;">
                                <div class="card-header bg-primary">
                                    <strong>Detalle del producto</strong>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item"><strong>ID:</strong> ${producto.ID_Producto}</li>
                                    <li class="list-group-item"><strong>Descripcion:</strong> ${producto.Descripcion}</li>
                                    <li class="list-group-item"><strong>Comentario:</strong> ${producto.Comentario}</li>
                                    <li class="list-group-item"><strong>Precio:</strong> $${producto.Precio}</li>
                                    <li class="list-group-item"><strong>Fecha:</strong> ${producto.Fecha}</li>
                                    <button type="button" class="btn btn-outline-warning" data-id="${producto.ID_Producto}" onclick="">Modificar Producto</button>
                                    <button type="button" class="btn btn-outline-danger" data-id="${producto.ID_Producto}" onclick="eliminarProducto(this)">Eliminar Producto</button>
                                </ul>
                            </div>
                             
                        `;

                    // Agregar el contenido HTML del producto al contenedor
                    productosContainer.innerHTML += contenidoProducto;
                });
            })
            .catch(error => console.error('Error al cargar los datos:', error));

// Crear productos
function crearProducto() {
            const Descripcion = document.getElementById('Descripcion').value;
            const Fecha = document.getElementById('Fecha').value;
            const Precio = document.getElementById('Precio').value;
            const Comentario = document.getElementById('Comentario').value;

            const newProduct = {
                Descripcion: Descripcion,
                Fecha: Fecha,
                Precio: parseFloat(Precio),
                Comentario: Comentario
            };

            fetch('http://localhost:4500/productos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newProduct)
            })
            .then(response => response.json())
            .then(data => {
                if (data.mensaje) {
                    alert(data.mensaje);
                    location.reload();
                } else if (data.error) {
                    alert('Error: ' + data.error);
                }
            })
            .catch(error => {
                alert('Error: ' + error.message);
            });
        }

// Eliminar productos

function eliminarProducto(button) {
    const idProducto = button.getAttribute('data-id');
    
    if (idProducto) {
        fetch(`http://localhost:4500/productos/${idProducto}`, {
            method: 'DELETE',
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensaje) {
                // El producto se eliminó con éxito, puedes mostrar un mensaje de éxito o recargar la página
                alert(data.mensaje);
                location.reload();
            } else if (data.error) {
                // Ocurrió un error durante la eliminación, puedes mostrar un mensaje de error
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            // Maneja errores de red u otros errores
            alert('Error al eliminar el producto: ' + error.message);
        });
    } else {
        alert('No se pudo obtener el ID del producto.');
    }
}

// Editar productos
