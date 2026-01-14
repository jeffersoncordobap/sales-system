from models.product import Product

class ProductRepository:
    def  __init__(self, db_connection):
        self.db_connection = db_connection
        
    
    def convert_to_product(self, product_atributes):
        """Método que convierte una tupla en un obejto
        de la clase Product

        Args:
            product_atributes (tuple): Una tupla con los atributos del product.

        Returns:
            product: Un objeto de la clase Product.
        """        
        product = Product(
            product_id = product_atributes[0],
            bar_code = product_atributes[1],
            product_name = product_atributes[2],
            category = product_atributes[3],
            product_size = product_atributes[4],
            color = product_atributes[5],
            price = product_atributes[6],
            stock = product_atributes[7],
            management_status = product_atributes[8],
        )
        return product

    def get_product_by_bar_code(self, bar_code):
        """Método que busca y retorna un product por codigo de barras

        Args:
            bar_code (str): El código de barras del product a buscar.

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            product: Un objeto de la clase Product o
            None si el código de barras no existe.
        """        
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM products WHERE bar_code = ?"
        try:
            cursor.execute(query, (bar_code,))
            product_atributes = cursor.fetchone()
            if product_atributes:
                return self.convert_to_product(product_atributes)
            return None
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def product_exists(self, product: Product):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM products WHERE product_name = ? AND product_size = ? AND color = ?"
        try:
            cursor.execute(query, (product.product_name, product.product_size, product.color))
            product_atributes = cursor.fetchone()
            if product_atributes:
                return True
            return False
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def get_products_by_filter(self, words):
        """Método que devuleve una lista de products los cuales algunos
        de sus atributos coinciden con la lista de words enviadas.

        Args:
            words (list): Una lista de words para buscar products.

        Returns:
            list: Una lista de objetos Product que coinciden con los criterios de búsqueda.
        """        
        cursor = self.db_connection.cursor()

        query = """
            SELECT *
            FROM products
            WHERE management_status = 1
        """

        parameters = []

        for word in words:
            query += """
                AND (
                    product_name LIKE ?
                    OR category LIKE ?
                    OR color LIKE ?
                    OR CAST(product_size AS TEXT) LIKE ?
                )
            """
            like = f"%{word}%"
            parameters.extend([like, like, like, like])

        try:
            cursor.execute(query, parameters)
            filas = cursor.fetchall()
            return [self.convert_to_product(fila) for fila in filas]
        finally:
            cursor.close()

            
    def add_product(self, product: Product):
        """Métdo que adiciona un nuevo product a la base de datos

        Args:
            product (Product): obejeto de la clase product

        Raises:
            ValueError: Error por codigo de barras duplicado
            e: Error al adicionar product

        Returns:
            Bool: True si el product fue agregado exitosamente
        """        
        if self.product_exists(product):
            message = (f"No se puede registrar: El product: '{product.product_name},"
                       f"'{product.product_size}','{product.color}'\n "
                       f"ya existe en el inventario.")
            raise ValueError(message)
        cursor = self.db_connection.cursor()
        query = """INSERT INTO products 
                      (bar_code,
                      product_name,
                      category,
                      product_size,
                      color,
                      price,
                      stock,
                      management_status) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            cursor.execute(query, (product.bar_code,
                                      product.product_name,
                                      product.category,
                                      product.product_size,
                                      product.color,
                                      product.price,
                                      product.stock,
                                      product.management_status))
            self.db_connection.commit()     
            return True     
        except Exception as e: 
            self.db_connection.rollback() 
            raise e
        finally:
            cursor.close()
            

    def update_product_stock(self, bar_code, new_stock):
        """Método que actualiza el stock actual de un product
        Args:
            bar_code (str): El código de barras del product a actualizar.
            new_stock (int): El nuevo valor de stock actual.
        Raises:
            Exception: Si no se encuentra el product o hay un error en la actualización.
        Returns:
            bool: True si la actualización fue exitosa.
        """
        cursor = self.db_connection.cursor()
        query = "UPDATE products SET stock = ? WHERE bar_code = ?"
        try:
            cursor.execute(query, (new_stock, bar_code))
            if cursor.rowcount == 0:
                message = (f"Error: No se encontró ningún product \n"
                           f"con el código '{bar_code}'.")
                raise Exception(message)
            self.db_connection.commit()
            return True
        except Exception as e:
            self.db_connection.rollback()
            raise e
        finally:
            cursor.close()

    def edit_product(self, product: Product):
        """Método que actualiza los datos de un product existente

        Args:
            product (Product): Objeto de la clase Product con los datos actualizados.

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            bool: True si la actualización fue exitosa.
        """        
        cursor = self.db_connection.cursor()
        query = """UPDATE products 
                      SET bar_code = ?,
                          product_name = ?, 
                          category = ?, 
                          product_size = ?, 
                          color = ?, 
                          price = ?, 
                          stock = ?, 
                          management_status = ? 
                      WHERE id_producto = ?"""
        try:
            cursor.execute(query, (product.bar_code,
                                      product.product_name,
                                      product.category,
                                      product.product_size,
                                      product.color,
                                      product.price,
                                      product.stock,
                                      product.management_status,
                                      product.id_producto))
            
            if cursor.rowcount == 0:
                message = (f"Error: No se encontró ningún product \n"
                           f"con el ID '{product.id_producto}'.")
                raise Exception(message)
            
            self.db_connection.commit()
            return True
        except Exception as e:
            self.db_connection.rollback()
            raise e
        finally:
            cursor.close()


    def get_all_products(self):
        """Método que lista todos los products en la base de datos

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            lista_productos: Una lista de objetos de la clase Product.
        """        
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM products"
        lista_productos = []
        try:
            cursor.execute(query)
            filas_productos = cursor.fetchall()
            for product_atributes in filas_productos:
                product = self.convert_to_product(product_atributes)
                lista_productos.append(product)
            return lista_productos
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def change_product_management_status(self, bar_code, new_status):
        """Método que cambia el estado de gestión de un product

        Args:
            bar_code (str): El código de barras del product.
            new_status (str): El nuevo estado de gestión ("ACTIVO" o "INACTIVO").

        Raises:
            e: Descripción del error que puede ocurrir.

        Returns:
            bool: True si la actualización fue exitosa.
        """        
        cursor = self.db_connection.cursor()
        query = "UPDATE products SET management_status = ? WHERE bar_code = ?"
        try:
            cursor.execute(query, (new_status, bar_code))
            if cursor.rowcount == 0:
                message = (f"Error: No se encontró ningún product \n"
                           f"con el código '{bar_code}'.")
                raise Exception(message)
            self.db_connection.commit()
            return True
        except Exception as e:
            self.db_connection.rollback()
            raise e
        finally:
            cursor.close()
            
