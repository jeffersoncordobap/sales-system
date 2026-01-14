from PySide6.QtWidgets import (
                                QDialog,
                                QVBoxLayout,
                                QFormLayout,
                                QLineEdit, 
                                QDoubleSpinBox,
                                QSpinBox, 
                                QComboBox, 
                                QPushButton, 
                                QHBoxLayout
                            )
from PySide6.QtCore import Qt
from models.product import Product

class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registrar Nuevo Producto")
        self.setFixedWidth(400)
        self.setObjectName("product_dialog")
        
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        
        self.form = QFormLayout()
        self.form.setSpacing(15)
        self.form.setLabelAlignment(Qt.AlignLeft)

        # self.input_code_bar = QLineEdit()
        # self.input_code_bar.setPlaceholderText("Escanee o deje vacío para autogenerar")
        # self.input_code_bar.setObjectName("input_code_bar")
        
        # self.input_code_bar.setToolTip("Si se deja vacío, el sistema asignará un código único basado en el ID.")
        
        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText("Ej: chancla eva")
        
        self.input_category = QComboBox()
        self.input_category.addItems(["Chancla", "Babucha","Botas", "Calzado", "Accesorios"])
        self.input_category.setEditable(True) 

        self.input_size = QLineEdit()
        self.input_size.setPlaceholderText("Ej: 36")
        
        self.input_color = QLineEdit()
        self.input_color.setPlaceholderText("Ej: Rojo, Azul, Verde")
        
        self.spn_precio = QDoubleSpinBox()
        self.spn_precio.setRange(0, 9999999)
        self.spn_precio.setPrefix("$ ")

        self.spn_stock = QSpinBox()
        self.spn_stock.setRange(0, 10000)

        #self.form.addRow("Código de Barras:", self.input_code_bar)
        self.form.addRow("Nombre Producto:", self.input_name)
        self.form.addRow("Categoría:", self.input_category)
        self.form.addRow("Talla:", self.input_size)
        self.form.addRow("Color:", self.input_color)
        self.form.addRow("Precio de Venta:", self.spn_precio)
        self.form.addRow("Stock Inicial:", self.spn_stock)

        main_layout.addLayout(self.form)

        buttons = QHBoxLayout()
        self.btn_save = QPushButton("GUARDAR PRODUCTO")
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setMinimumHeight(40)
        self.btn_save.clicked.connect(self.close_dialog)
        
        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.clicked.connect(self.reject)

        buttons.addWidget(self.btn_cancel)
        buttons.addWidget(self.btn_save)
        main_layout.addLayout(buttons)

    def validate_ui(self):
        """Valida solo lo visual (campos vacíos)."""
        self.input_name.setStyleSheet("")
        self.input_size.setStyleSheet("")
        self.input_color.setStyleSheet("")
        self.spn_precio.setStyleSheet("")   
        self.spn_stock.setStyleSheet("")
        
        if not self.input_name.text().strip():
            self.input_name.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.input_size.text().strip():
            self.input_size.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.input_color.text().strip():
            self.input_color.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.spn_precio.value():
            self.spn_precio.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.spn_stock.value():
            self.spn_stock.setStyleSheet("border: 1px solid red;")
            return False
        return True

    def get_product(self):
        """Retorna un objeto Producto listo para ser procesado."""
        return Product(
            #code_bar=self.input_code_bar.text().strip(),
            product_name = self.input_name.text().strip().upper(),
            category = self.input_category.currentText().upper(),
            product_size = self.input_size.text().strip(),
            color = self.input_color.text().strip().upper(),
            price = self.spn_precio.value(),
            stock = self.spn_stock.value(),
            management_status = "ACTIVO"
        )
        
    def close_dialog(self):
        if self.validate_ui():
            self.accept()