from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QComboBox, QTextEdit, QPushButton, QFrame, QTableWidget, QHeaderView
)
from PySide6.QtCore import Qt, QDate

class PaginaGastos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PaginaGastos")
        self.layout_principal = QHBoxLayout(self) 
        self.layout_principal.setSpacing(20)

        self.crear_formulario()
        self.crear_historial_diario()

    def crear_formulario(self):
        """Sección izquierda: Formulario de Registro"""
        self.contenedor_form = QFrame()
        self.contenedor_form.setObjectName("ContenedorFormGastos")
        self.contenedor_form.setFixedWidth(350)
        
        layout = QVBoxLayout(self.contenedor_form)
        layout.setSpacing(15)

        titulo = QLabel("REGISTRAR GASTO / EGRESO")
        titulo.setObjectName("TituloGastos")
        layout.addWidget(titulo)

        # Categoría
        layout.addWidget(QLabel("Categoría:"))
        self.combo_categoria = QComboBox()
        self.combo_categoria.addItems([
            "Insumos (Bolsas, Pegante, etc.)",
            "Servicios Públicos",
            "Pago de Turnos / Nómina",
            "Mantenimiento",
            "Compras a Proveedores",
            "Otros"
        ])
        layout.addWidget(self.combo_categoria)

        # Monto
        layout.addWidget(QLabel("Monto del Gasto ($):"))
        self.entrada_monto = QLineEdit()
        self.entrada_monto.setPlaceholderText("0.00")
        self.entrada_monto.setObjectName("EntradaMontoGasto")
        layout.addWidget(self.entrada_monto)

        # Método de Pago (Fundamental para la contadora)
        layout.addWidget(QLabel("Pagado desde:"))
        self.combo_pago = QComboBox()
        self.combo_pago.addItems(["Caja Principal (Efectivo)", "Tarjeta","Transferencia", "Otro"])
        layout.addWidget(self.combo_pago)

        # Descripción
        layout.addWidget(QLabel("Descripción / Concepto:"))
        self.txt_descripcion = QTextEdit()
        self.txt_descripcion.setPlaceholderText("Ej: Compra de 100 bolsas medianas...")
        self.txt_descripcion.setMaximumHeight(100)
        layout.addWidget(self.txt_descripcion)

        layout.addStretch()

        # Botón
        self.btn_guardar = QPushButton("GUARDAR GASTO")
        self.btn_guardar.setObjectName("BtnGuardarGasto")
        self.btn_guardar.setMinimumHeight(45)
        layout.addWidget(self.btn_guardar)

        self.layout_principal.addWidget(self.contenedor_form)

    def crear_historial_diario(self):
        """Sección derecha: Lista de gastos del día"""
        contenedor_lista = QFrame()
        layout = QVBoxLayout(contenedor_lista)

        lbl_historial = QLabel("Gastos Registrados Hoy")
        lbl_historial.setObjectName("SubtituloGastos")
        layout.addWidget(lbl_historial)

        self.tabla_hoy = QTableWidget()
        self.tabla_hoy.setColumnCount(4)
        self.tabla_hoy.setHorizontalHeaderLabels(["Hora", "Categoría", "Descripción", "Monto"])
        self.tabla_hoy.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.tabla_hoy)
        self.layout_principal.addWidget(contenedor_lista)