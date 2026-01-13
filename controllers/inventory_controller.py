from PySide6.QtWidgets import QMessageBox
from ui.add_product_view import DialogoProducto

from PySide6.QtWidgets import QPushButton, QTableWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class ControladorInventario:
    def __init__(self,pagina_inventario,servicio_inventario):
        self.pagina_inventario = pagina_inventario
        self.servicio_inventario = servicio_inventario
        self.dialogo_agregar_producto = DialogoProducto(self.pagina_inventario)
        
        self.pagina_inventario.btn_adicionar_producto.clicked.connect(self.abrir_dialogo_adicionar_producto)
        self.dialogo_agregar_producto.btn_guardar.clicked.connect(self.agregar_producto)
        self.pagina_inventario.btn_actualizar.clicked.connect(self.actualizar_inventario)


    def abrir_dialogo_adicionar_producto (self):
        dialogo = self.dialogo_agregar_producto
        if dialogo.exec():
            print("Producto agregado con exito...")

    def agregar_producto(self):
        producto = self.dialogo_agregar_producto.obtener_producto()
        if not producto.nombre:
            QMessageBox.warning(self.pagina_inventario, "Error de Validación", "El nombre del producto es obligatorio.")
            return None
        
        if not producto.talla:
            QMessageBox.warning(self.pagina_inventario, "Error de Validación", "La talla del producto es obligatoria.")
            return None
        
        if not producto.color:
            QMessageBox.warning(self.pagina_inventario, "Error de Validación", "El color del producto es obligatorio.")
            return None
        
        if producto.precio_venta <= 0:
            QMessageBox.warning(self.pagina_inventario, "Error de Validación", "El precio de venta debe ser mayor que cero.")
            return None
        
        if producto.stock_actual < 0:
            QMessageBox.warning(self.pagina_inventario, "Error de Validación", "El stock inicial no puede ser negativo.")
            return None
        
        try:
            if self.servicio_inventario.agregar_producto(producto):
                QMessageBox.information(self.pagina_inventario, "Éxito", "Producto agregado exitosamente.")
                return producto
        except Exception as e:
            QMessageBox.critical(self.pagina_inventario, "Error", f"No se pudo agregar el producto: {str(e)}")
            return None
    
    def actualizar_inventario(self):
        productos_en_inventario = self.servicio_inventario.obtener_todos_productos()
        """Llena la tabla con los productos activos en el inventario
        y aplica colores según stock."""

        self.pagina_inventario.tabla.setRowCount(len(productos_en_inventario))

        for i,producto in enumerate(productos_en_inventario):
            self.pagina_inventario.tabla.setItem(i, 0, QTableWidgetItem(producto.nombre))
            self.pagina_inventario.tabla.setItem(i, 1, QTableWidgetItem(producto.categoria))
            self.pagina_inventario.tabla.setItem(i, 2, QTableWidgetItem(producto.talla))
            self.pagina_inventario.tabla.setItem(i, 3, QTableWidgetItem(producto.color))
            self.pagina_inventario.tabla.setItem(i, 4, QTableWidgetItem(str(producto.precio_venta)))
            self.pagina_inventario.tabla.setItem(i, 5, QTableWidgetItem(str(producto.stock_actual)))

            self.btn_ver = QPushButton("Editar")
            self.btn_ver.setObjectName("btnVerTabla")
            self.btn_ver.setCursor(Qt.PointingHandCursor)
            self.pagina_inventario.tabla.setCellWidget(i, 6, self.btn_ver)
            color_fondo = QColor("#ffffff")
            if int(producto.stock_actual) == 0:
                color_fondo = QColor("#f8d7da") 
            else:
                color_fondo = QColor("#d4edda")

            for col in range(7):
                item = self.pagina_inventario.tabla.item(i, col)
                if item:
                    item.setBackground(color_fondo)
                    item.setForeground(QColor("#444444"))       
                    
                    
    def editar_producto(self, producto):
        pass
            