from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
    QDoubleSpinBox, QSpinBox, QComboBox, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt

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

        self.ent_codigo = QLineEdit()
        self.ent_codigo.setPlaceholderText("Escanee o deje vacío para autogenerar")
        self.ent_codigo.setObjectName("EntradaCodigo")
        
        self.ent_codigo.setToolTip("Si se deja vacío, el sistema asignará un código único basado en el ID.")
        
        self.ent_nombre = QLineEdit()
        self.ent_nombre.setPlaceholderText("Ej: chancla capibara talla 32")
        
        self.ent_categoria = QComboBox()
        self.ent_categoria.addItems(["Chancla", "Babucha","Botas", "Calzado", "Accesorios"])
        self.ent_categoria.setEditable(True) 

        self.ent_talla = QLineEdit()
        self.ent_talla.setPlaceholderText("Ej: 32")

        self.spn_costo = QDoubleSpinBox()
        self.spn_costo.setRange(0, 9999999)
        self.spn_costo.setPrefix("$ ")

        self.spn_precio = QDoubleSpinBox()
        self.spn_precio.setRange(0, 9999999)
        self.spn_precio.setPrefix("$ ")

        self.spn_stock = QSpinBox()
        self.spn_stock.setRange(0, 10000)
        
        self.spn_minimo = QSpinBox()
        self.spn_minimo.setRange(0, 1000)
        self.spn_minimo.setValue(3) 

        # Agregar al formulario
        self.formulario.addRow("Código de Barras:", self.ent_codigo)
        self.formulario.addRow("Nombre Producto:", self.ent_nombre)
        self.formulario.addRow("Categoría:", self.ent_categoria)
        self.formulario.addRow("Talla:", self.ent_talla)
        self.formulario.addRow("Costo de Compra:", self.spn_costo)
        self.formulario.addRow("Precio de Venta:", self.spn_precio)
        self.formulario.addRow("Stock Inicial:", self.spn_stock)
        self.formulario.addRow("Stock Mínimo:", self.spn_minimo)

        layout_principal.addLayout(self.formulario)

        botones = QHBoxLayout()
        self.btn_guardar = QPushButton("GUARDAR PRODUCTO")
        self.btn_guardar.setObjectName("BtnGuardarProducto")
        self.btn_guardar.setMinimumHeight(40)
        self.btn_guardar.clicked.connect(self.validar_y_aceptar)
        
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.clicked.connect(self.reject)

        botones.addWidget(self.btn_cancelar)
        botones.addWidget(self.btn_guardar)
        layout_principal.addLayout(botones)

    def validar_y_aceptar(self):
        """Valida los datos antes de aceptar el diálogo."""
        if not self.ent_nombre.text() or not self.ent_codigo.text():
            self.ent_nombre.setStyleSheet("border: 1px solid red;")
            return
        
        if self.spn_precio.value() < self.spn_costo.value():
            print("Alerta: El precio es menor al costo")
            
        self.accept()

    def obtener_datos(self):
        """Retorna un diccionario con los datos listos para la BD"""
        return {
            "codigo": self.ent_codigo.text(),
            "nombre": self.ent_nombre.text(),
            "categoria": self.ent_categoria.currentText(),
            "talla": self.ent_talla.text(),
            "costo": self.spn_costo.value(),
            "precio": self.spn_precio.value(),
            "stock": self.spn_stock.value(),
            "minimo": self.spn_minimo.value(),
            "estado": "ACTIVO"
        }