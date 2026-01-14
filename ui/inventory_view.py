from PySide6.QtWidgets import (
                                QWidget, 
                                QVBoxLayout, 
                                QHBoxLayout, 
                                QPushButton, 
                                QTableWidget, 
                                QLabel, 
                                QHeaderView, 
                                QAbstractItemView
)
from PySide6.QtCore import Qt


class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Configura la estructura visual de la página de inventario."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        header_layout = QHBoxLayout()
        self.lbl_title = QLabel("Control de Inventario")
        self.lbl_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        
        self.btn_update = QPushButton("Actualizar Stock")
        self.btn_add_product = QPushButton("Nuevo Producto")
        self.btn_export = QPushButton("Exportar CSV")

        self.btn_update.setObjectName("btn_update")
        self.btn_add_product.setObjectName("btn_add_product")
        self.btn_export.setObjectName("btn_export")

        header_layout.addWidget(self.lbl_title)
        header_layout.addStretch()
        header_layout.addWidget(self.btn_update)
        header_layout.addWidget(self.btn_add_product)
        header_layout.addWidget(self.btn_export)
        main_layout.addLayout(header_layout)

        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Referencia", "Categoría", "Talla","Color", "Precio", "Stock Actual", "Acciones"
        ])
        
        header_table = self.table.horizontalHeader()
        header_table.setSectionResizeMode(QHeaderView.Stretch)
        header_table.setMinimumSectionSize(150)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setColumnWidth(6, 80)
        
        self.table.setAlternatingRowColors(False) 
        
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)
       
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        