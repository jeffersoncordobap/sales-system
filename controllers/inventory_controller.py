from PySide6.QtWidgets import QMessageBox
from ui.add_product_view import AddProductDialog

from PySide6.QtWidgets import QPushButton, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class InventoryController:
    def __init__(self,inventory_view,inventory_service):
        self.inventory_view = inventory_view
        self.inventory_service = inventory_service
        self.dialogo_agregar_producto = AddProductDialog(self.inventory_view)
        
        self.inventory_view.btn_add_product.clicked.connect(self.open_dialog_add_product)
        self.dialogo_agregar_producto.btn_save.clicked.connect(self.add_product)
        self.inventory_view.btn_update.clicked.connect(self.update_inventory)


    def open_dialog_add_product (self):
        dialogo = self.dialogo_agregar_producto
        if dialogo.exec():
            print("Producto agregado con exito...")

    def add_product(self):
        product = self.dialogo_agregar_producto.get_product()
        if not product.product_name:
            QMessageBox.warning(self.inventory_view, "Error de Validación", "El nombre del product es obligatorio.")
            return None
        
        if not product.product_size:
            QMessageBox.warning(self.inventory_view, "Error de Validación", "La size del product es obligatoria.")
            return None
        
        if not product.color:
            QMessageBox.warning(self.inventory_view, "Error de Validación", "El color del product es obligatorio.")
            return None

        if product.price <= 0:
            QMessageBox.warning(self.inventory_view, "Error de Validación", "El precio de venta debe ser mayor que cero.")
            return None
        
        if product.stock < 0:
            QMessageBox.warning(self.inventory_view, "Error de Validación", "El stock inicial no puede ser negativo.")
            return None
        
        try:
            if self.inventory_service.add_product(product):
                QMessageBox.information(self.inventory_view, "Éxito", "Producto agregado exitosamente.")
                return product
        except Exception as e:
            QMessageBox.critical(self.inventory_view, "Error", f"No se pudo agregar el product: {str(e)}")
            return None
    
    def update_inventory(self):
        products_in_inventory = self.inventory_service.get_all_products()
        """Llena la tabla con los productos activos en el inventario
        y aplica colores según stock."""

        self.inventory_view.table.setRowCount(len(products_in_inventory))

        for i,product in enumerate(products_in_inventory):
            self.inventory_view.table.setItem(i, 0, QTableWidgetItem(product.product_name))
            self.inventory_view.table.setItem(i, 1, QTableWidgetItem(product.category))
            self.inventory_view.table.setItem(i, 2, QTableWidgetItem(product.product_size))
            self.inventory_view.table.setItem(i, 3, QTableWidgetItem(product.color))
            self.inventory_view.table.setItem(i, 4, QTableWidgetItem(str(product.price)))
            self.inventory_view.table.setItem(i, 5, QTableWidgetItem(str(product.stock)))

            self.btn_edit = QPushButton("Editar")
            self.btn_edit.setObjectName("btn_edit")
            self.btn_edit.setCursor(Qt.PointingHandCursor)
            self.inventory_view.table.setCellWidget(i, 6, self.btn_edit)
            background_color = QColor("#ffffff")
            if int(product.stock) == 0:
                background_color = QColor("#f8d7da") 
            else:
                background_color = QColor("#d4edda")

            for col in range(7):
                item = self.inventory_view.table.item(i, col)
                if item:
                    item.setBackground(background_color)
                    item.setForeground(QColor("#444444"))       
                    
                    
    def edit_product(self, product):
        pass
            