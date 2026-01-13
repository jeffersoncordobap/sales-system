class ServicioInventario:
    def __init__(self,repositorio_producto):
        self.repositorio_producto = repositorio_producto

    def agregar_producto(self, producto):
        return self.repositorio_producto.agregar_producto(producto)
          
        
    def obtener_todos_productos(self):
        try:
            return self.repositorio_producto.listar_productos()
        except Exception as e:
            raise e
    
    def editar_producto(self, producto):
        try:
            self.repositorio_producto.actualizar_producto(producto)
            return True
        except Exception as e:
            raise e