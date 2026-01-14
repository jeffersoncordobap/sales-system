class Product:
    def __init__(self,
                 product_name,
                 category,
                 product_size, 
                 color,
                 price,
                 stock, 
                 management_status="ACTIVO",
                 product_id=None,
                 bar_code=None,
                 ):

        self.product_id = product_id
        self.bar_code = bar_code
        self.product_name = product_name
        self.category = category
        self.product_size = product_size
        self.color = color
        self.price = price
        self.stock = stock
        self.management_status = management_status
    def __str__(self):
        return f"Producto: {self.product_name} (Talla: {self.product_size}) - Stock: {self.stock}"