from models.product import Producto 

class RepositorioProducto:
    def  __init__(self, conexion_bd):
        self.conexion_bd = conexion_bd
        
    
    def mapear_producto(self, atributos_producto):
        """Método que convierte una tupla en un obejto
        de la clase Producto

        Args:
            atributos_producto (tuple): Una tupla con los atributos del producto.

        Returns:
            producto: Un objeto de la clase Producto.
        """        
        producto = Producto(
            id_producto=atributos_producto[0],
            codigo_barras=atributos_producto[1],
            nombre=atributos_producto[2],
            categoria=atributos_producto[3],
            talla=atributos_producto[4],
            color=atributos_producto[5],
            precio_venta=atributos_producto[6],
            stock_actual=atributos_producto[7],
            estado_gestion=atributos_producto[8],
        )
        return producto
    
    def obtener_producto_por_codigo_de_barras(self, codigo_barras):
        """Método que busca y retorna un producto por codigo de barras

        Args:
            codigo_barras (str): El código de barras del producto a buscar.

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            producto: Un objeto de la clase Producto o
            None si el código de barras no existe.
        """        
        cursor = self.conexion_bd.cursor()
        consulta = "SELECT * FROM productos WHERE codigo_barras = ?"
        try:
            cursor.execute(consulta, (codigo_barras,))
            atributos_producto = cursor.fetchone()
            if atributos_producto:
                return self.mapear_producto(atributos_producto)
            return None
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def producto_existe(self, producto: Producto):
        cursor = self.conexion_bd.cursor()
        consulta = "SELECT * FROM productos WHERE nombre = ? AND talla = ? AND color = ?"
        try:
            cursor.execute(consulta, (producto.nombre, producto.talla, producto.color))
            atributos_producto = cursor.fetchone()
            if atributos_producto:
                return True
            return False
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def buscar_productos_por_filtro(self, palabras):
        """Método que devuleve una lista de productos los cuales algunos
        de sus atributos coinciden con la lista de palabras enviadas.

        Args:
            palabras (list): Una lista de palabras para buscar productos.

        Returns:
            list: Una lista de objetos Producto que coinciden con los criterios de búsqueda.
        """        
        cursor = self.conexion_bd.cursor()

        consulta = """
            SELECT *
            FROM productos
            WHERE estado_gestion = 1
        """

        parametros = []

        for palabra in palabras:
            consulta += """
                AND (
                    nombre LIKE ?
                    OR categoria LIKE ?
                    OR color LIKE ?
                    OR CAST(talla AS TEXT) LIKE ?
                )
            """
            like = f"%{palabra}%"
            parametros.extend([like, like, like, like])

        try:
            cursor.execute(consulta, parametros)
            filas = cursor.fetchall()
            return [self.mapear_producto(fila) for fila in filas]
        finally:
            cursor.close()

            
    def agregar_producto(self, producto: Producto):
        """Métdo que adiciona un nuevo producto a la base de datos

        Args:
            producto (Producto): obejeto de la clase producto

        Raises:
            ValueError: Error por codigo de barras duplicado
            e: Error al adicionar producto

        Returns:
            Bool: True si el producto fue agregado exitosamente
        """        
        if self.producto_existe(producto):
            mensaje = (f"No se puede registrar: El producto: '{producto.nombre},"
                       f"'{producto.talla}','{producto.color}'\n "
                       f"ya existe en el inventario.")
            raise ValueError(mensaje)
        cursor = self.conexion_bd.cursor()
        consulta = """INSERT INTO productos 
                      (codigo_barras,
                      nombre,
                      categoria,
                      talla,
                      color,
                      precio_venta,
                      stock_actual,
                      estado_gestion) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            cursor.execute(consulta, (producto.codigo_barras,
                                      producto.nombre,
                                      producto.categoria,
                                      producto.talla,
                                      producto.color,
                                      producto.precio_venta,
                                      producto.stock_actual,
                                      producto.estado_gestion))
            self.conexion_bd.commit()     
            return True     
        except Exception as e: 
            self.conexion_bd.rollback() 
            raise e
        finally:
            cursor.close()
            

    def actualizar_stock_producto(self, codigo_barras, nuevo_stock):
        """Método que actualiza el stock actual de un producto
        Args:
            codigo_barras (str): El código de barras del producto a actualizar.
            nuevo_stock (int): El nuevo valor de stock actual.
        Raises:
            Exception: Si no se encuentra el producto o hay un error en la actualización.
        Returns:
            bool: True si la actualización fue exitosa.
        """
        cursor = self.conexion_bd.cursor()
        consulta = "UPDATE productos SET stock_actual = ? WHERE codigo_barras = ?"
        try:
            cursor.execute(consulta, (nuevo_stock, codigo_barras))
            if cursor.rowcount == 0:
                mensaje = (f"Error: No se encontró ningún producto \n"
                           f"con el código '{codigo_barras}'.")
                raise Exception(mensaje)
            self.conexion_bd.commit()
            return True
        except Exception as e:
            self.conexion_bd.rollback()
            raise e
        finally:
            cursor.close()
            
    def actualizar_producto(self, producto: Producto):
        """Método que actualiza los datos de un producto existente

        Args:
            producto (Producto): Objeto de la clase Producto con los datos actualizados.

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            bool: True si la actualización fue exitosa.
        """        
        cursor = self.conexion_bd.cursor()
        consulta = """UPDATE productos 
                      SET codigo_barras = ?,
                          nombre = ?, 
                          categoria = ?, 
                          talla = ?, 
                          color = ?, 
                          precio_venta = ?, 
                          stock_actual = ?, 
                          estado_gestion = ? 
                      WHERE id_producto = ?"""
        try:
            cursor.execute(consulta, (producto.codigo_barras,
                                      producto.nombre,
                                      producto.categoria,
                                      producto.talla,
                                      producto.color,
                                      producto.precio_venta,
                                      producto.stock_actual,
                                      producto.estado_gestion,
                                      producto.id_producto))
            
            if cursor.rowcount == 0:
                mensaje = (f"Error: No se encontró ningún producto \n"
                           f"con el ID '{producto.id_producto}'.")
                raise Exception(mensaje)
            
            self.conexion_bd.commit()
            return True
        except Exception as e:
            self.conexion_bd.rollback()
            raise e
        finally:
            cursor.close()


    def listar_productos(self):
        """Método que lista todos los productos en la base de datos

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            lista_productos: Una lista de objetos de la clase Producto.
        """        
        cursor = self.conexion_bd.cursor()
        consulta = "SELECT * FROM productos"
        lista_productos = []
        try:
            cursor.execute(consulta)
            filas_productos = cursor.fetchall()
            for atributos_producto in filas_productos:
                producto = self.mapear_producto(atributos_producto)
                lista_productos.append(producto)
            return lista_productos
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def cambiar_estado_gestion_producto(self, codigo_barras, nuevo_estado):
        """Método que cambia el estado de gestión de un producto

        Args:
            codigo_barras (str): El código de barras del producto.
            nuevo_estado (str): El nuevo estado de gestión ("ACTIVO" o "INACTIVO").

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            bool: True si la actualización fue exitosa.
        """        
        cursor = self.conexion_bd.cursor()
        consulta = "UPDATE productos SET estado_gestion = ? WHERE codigo_barras = ?"
        try:
            cursor.execute(consulta, (nuevo_estado, codigo_barras))
            if cursor.rowcount == 0:
                mensaje = (f"Error: No se encontró ningún producto \n"
                           f"con el código '{codigo_barras}'.")
                raise Exception(mensaje)
            self.conexion_bd.commit()
            return True
        except Exception as e:
            self.conexion_bd.rollback()
            raise e
        finally:
            cursor.close()
            
