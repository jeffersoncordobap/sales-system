class Producto:
    def __init__(self, codigo_barras, nombre, categoria, talla, 
                 costo_compra, precio_venta, stock_actual, 
                 stock_minimo, estado_gestion="ACTIVO", id_producto=None):
      
        self.id_producto = id_producto
        self.codigo_barras = codigo_barras
        self.nombre = nombre
        self.categoria = categoria
        self.talla = talla
        self.costo_compra = costo_compra
        self.precio_venta = precio_venta
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.estado_gestion = estado_gestion

    def __str__(self):
        return f"Producto: {self.nombre} (Talla: {self.talla}) - Stock: {self.stock_actual}"