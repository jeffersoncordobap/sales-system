class InventoryService:
    def __init__(self,product_repository):
        self.product_repository = product_repository

    def add_product(self, producto):
        return self.product_repository.add_product(producto)
          

    def get_all_products(self):
        try:
            return self.product_repository.get_all_products()
        except Exception as e:
            raise e

    def edit_product(self, producto):
        try:
            self.product_repository.edit_product(producto)
            return True
        except Exception as e:
            raise e