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
            costo_compra=atributos_producto[5],
            precio_venta=atributos_producto[6],
            stock_actual=atributos_producto[7],
            stock_minimo=atributos_producto[8],
            estado_gestion=atributos_producto[9],
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
    
    def obtener_producto_por_nombre(self, nombre_producto):
        """Método que busca un producto por nombre y lo devuleve 
        si lo encuentra en caso contrario devulve None 

        Args:
            nombre_producto (str): El nombre del producto a buscar.

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            producto: Un objeto de la clase Producto o
            None si el nombre del producto no existe.  
        """        
        cursor = self.conexion_bd.cursor()
        consulta = "SELECT * FROM productos WHERE nombre = ?"
        try:
            cursor.execute(consulta, (nombre_producto,))
            atributos_producto = cursor.fetchone()
            if atributos_producto:
                return self.mapear_producto(atributos_producto)
            return None
        except Exception as e:
            raise e
        finally:
            cursor.close()
            
            
    def adicionar_producto(self, producto: Producto):
        cursor = self.conexion_bd.cursor()
        consulta = """INSERT INTO productos 
                      (codigo_barras,
                      nombre,
                      categoria,
                      talla,
                      costo_compra,
                      precio_venta,
                      stock_actual,
                      stock_minimo,
                      estado_gestion) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            cursor.execute(consulta, (producto.codigo_barras,
                                      producto.nombre,
                                      producto.categoria,
                                      producto.talla,
                                      producto.costo_compra,
                                      producto.precio_venta,
                                      producto.stock_actual,
                                      producto.stock_minimo,
                                      producto.estado_gestion))
            self.conexion_bd.commit()     
            return True     
        except Exception as e: 
            self.conexion_bd.rollback() 
            raise e
        finally:
            cursor.close()
            

    def actualizar_stock_producto(self, codigo_barras, nuevo_stock):
        cursor = self.conexion_bd.cursor()
        consulta = "UPDATE productos SET stock_actual = ? WHERE codigo_barras = ?"
        try:
            cursor.execute(consulta, (nuevo_stock, codigo_barras))
            self.conexion_bd.commit()
            return True
        except Exception as e:
            self.conexion_bd.rollback()
            raise e
        finally:
            cursor.close()
            















# class ProductRepository:
#     def __init__(self, db_connection):
#         self.db_connection = db_connection

#     def get_product_by_id(self, product_id):
#         cursor = self.db_connection.cursor()
#         query = "SELECT * FROM products WHERE id = %s"
#         cursor.execute(query, (product_id,))                                                                                
#         product = cursor.fetchone()
#         cursor.close()
#         return product

#     def add_product(self, name, price, stock):
#         cursor = self.db_connection.cursor()
#         query = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
#         cursor.execute(query, (name, price, stock))
#         self.db_connection.commit()
#         cursor.close()

#     def update_product_stock(self, product_id, new_stock):
#         cursor = self.db_connection.cursor()
#         query = "UPDATE products SET stock = %s WHERE id = %s"
#         cursor.execute(query, (new_stock, product_id))
#         self.db_connection.commit()
#         cursor.close()

#     def delete_product(self, product_id):
#         cursor = self.db_connection.cursor()
#         query = "DELETE FROM products WHERE id = %s"
#         cursor.execute(query, (product_id,))
#         self.db_connection.commit()
#         cursor.close()