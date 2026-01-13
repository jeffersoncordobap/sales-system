from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
    QDoubleSpinBox, QSpinBox, QComboBox, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt
from models.product import Producto

class DialogoProducto(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registrar Nuevo Producto")
        self.setFixedWidth(400)
        self.setObjectName("DialogoProducto")
        
        self.configurar_interfaz()

    def configurar_interfaz(self):
        layout_principal = QVBoxLayout(self)
        
        self.formulario = QFormLayout()
        self.formulario.setSpacing(15)
        self.formulario.setLabelAlignment(Qt.AlignLeft)

        # self.ent_codigo_de_barras = QLineEdit()
        # self.ent_codigo_de_barras.setPlaceholderText("Escanee o deje vacío para autogenerar")
        # self.ent_codigo_de_barras.setObjectName("EntradaCodigo")
        
        # self.ent_codigo_de_barras.setToolTip("Si se deja vacío, el sistema asignará un código único basado en el ID.")
        
        self.ent_nombre = QLineEdit()
        self.ent_nombre.setPlaceholderText("Ej: chancla eva")
        
        self.ent_categoria = QComboBox()
        self.ent_categoria.addItems(["Chancla", "Babucha","Botas", "Calzado", "Accesorios"])
        self.ent_categoria.setEditable(True) 

        self.ent_talla = QLineEdit()
        self.ent_talla.setPlaceholderText("Ej: 32")
        
        self.ent_color = QLineEdit()
        self.ent_color.setPlaceholderText("Ej: Rojo, Azul, Verde")

        self.spn_precio = QDoubleSpinBox()
        self.spn_precio.setRange(0, 9999999)
        self.spn_precio.setPrefix("$ ")

        self.spn_stock = QSpinBox()
        self.spn_stock.setRange(0, 10000)

        #self.formulario.addRow("Código de Barras:", self.ent_codigo_de_barras)
        self.formulario.addRow("Nombre Producto:", self.ent_nombre)
        self.formulario.addRow("Categoría:", self.ent_categoria)
        self.formulario.addRow("Talla:", self.ent_talla)
        self.formulario.addRow("Color:", self.ent_color)
        self.formulario.addRow("Precio de Venta:", self.spn_precio)
        self.formulario.addRow("Stock Inicial:", self.spn_stock)

        layout_principal.addLayout(self.formulario)

        botones = QHBoxLayout()
        self.btn_guardar = QPushButton("GUARDAR PRODUCTO")
        self.btn_guardar.setObjectName("BtnGuardarProducto")
        self.btn_guardar.setMinimumHeight(40)
        self.btn_guardar.clicked.connect(self.cerrar_dialogo)
        
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.clicked.connect(self.reject)

        botones.addWidget(self.btn_cancelar)
        botones.addWidget(self.btn_guardar)
        layout_principal.addLayout(botones)

    def validar_interfaz(self):
        """Valida solo lo visual (campos vacíos)."""
        self.ent_nombre.setStyleSheet("")
        self.ent_talla.setStyleSheet("")
        self.ent_color.setStyleSheet("")
        self.spn_precio.setStyleSheet("")   
        self.spn_stock.setStyleSheet("")
        
        if not self.ent_nombre.text().strip():
            self.ent_nombre.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.ent_talla.text().strip():
            self.ent_talla.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.ent_color.text().strip():
            self.ent_color.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.spn_precio.value():
            self.spn_precio.setStyleSheet("border: 1px solid red;")
            return False
        elif not self.spn_stock.value():
            self.spn_stock.setStyleSheet("border: 1px solid red;")
            return False
        return True

    def obtener_producto(self):
        """Retorna un objeto Producto listo para ser procesado."""
        return Producto(
            #codigo_barras=self.ent_codigo_de_barras.text().strip(),
            nombre=self.ent_nombre.text().strip().upper(),
            categoria=self.ent_categoria.currentText().upper(),
            talla=self.ent_talla.text().strip(),
            color=self.ent_color.text().strip().upper(),
            precio_venta=self.spn_precio.value(),
            stock_actual=self.spn_stock.value(),
            estado_gestion="ACTIVO"
        )
        
    def cerrar_dialogo(self):
        if self.validar_interfaz():
            self.accept()