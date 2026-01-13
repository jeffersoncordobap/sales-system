from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QTableWidget, QLabel, QHeaderView, QAbstractItemView
)
from PySide6.QtCore import Qt


class PaginaInventario(QWidget):
    def __init__(self):
        super().__init__()
        self.configurar_interfaz()

    def configurar_interfaz(self):
        """Configura la estructura visual de la página de inventario."""
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        
        layout_encabezado = QHBoxLayout()
        self.lbl_titulo = QLabel("Control de Inventario")
        self.lbl_titulo.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        
        self.btn_actualizar = QPushButton("Actualizar Stock")
        self.btn_adicionar_producto = QPushButton("Nuevo Producto")
        self.btn_exportar = QPushButton("Exportar CSV")

        self.btn_actualizar.setObjectName("btnActualizar")
        self.btn_adicionar_producto.setObjectName("btnNuevo")
        self.btn_exportar.setObjectName("btnExportar")

        layout_encabezado.addWidget(self.lbl_titulo)
        layout_encabezado.addStretch()
        layout_encabezado.addWidget(self.btn_actualizar)
        layout_encabezado.addWidget(self.btn_adicionar_producto)
        layout_encabezado.addWidget(self.btn_exportar)
        layout_principal.addLayout(layout_encabezado)

        self.tabla = QTableWidget()
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.setSelectionMode(QTableWidget.SingleSelection)
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels([
            "Referencia", "Categoría", "Talla","Color", "Precio", "Stock Actual", "Acciones"
        ])
        
        encabezado_tabla = self.tabla.horizontalHeader()
        encabezado_tabla.setSectionResizeMode(QHeaderView.Stretch)
        encabezado_tabla.setMinimumSectionSize(150)
        self.tabla.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.setColumnWidth(6, 80)
        
        self.tabla.setAlternatingRowColors(False) 
        
        layout_principal.addWidget(self.tabla)

       
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        