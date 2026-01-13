class Producto:
    def __init__(self,
                 nombre,
                 categoria,
                 talla, 
                 color,
                 precio_venta,
                 stock_actual, 
                 estado_gestion="ACTIVO",
                 id_producto=None,
                 codigo_barras=None,
                 ):

        self.id_producto = id_producto
        self.codigo_barras = codigo_barras
        self.nombre = nombre
        self.categoria = categoria
        self.talla = talla
        self.color = color
        self.precio_venta = precio_venta
        self.stock_actual = stock_actual
        self.estado_gestion = estado_gestion

    def __str__(self):
        return f"Producto: {self.nombre} (Talla: {self.talla}) - Stock: {self.stock_actual}"