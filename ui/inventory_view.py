from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QTableWidget, QTableWidgetItem, QLabel, QHeaderView
)
from PySide6.QtGui import QColor
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
        self.btn_nuevo = QPushButton("Nuevo Producto")
        self.btn_exportar = QPushButton("Exportar CSV")

        self.btn_actualizar.setObjectName("btnActualizar")
        self.btn_nuevo.setObjectName("btnNuevo")
        self.btn_exportar.setObjectName("btnExportar")

        layout_encabezado.addWidget(self.lbl_titulo)
        layout_encabezado.addStretch()
        layout_encabezado.addWidget(self.btn_actualizar)
        layout_encabezado.addWidget(self.btn_nuevo)
        layout_encabezado.addWidget(self.btn_exportar)
        layout_principal.addLayout(layout_encabezado)

        self.tabla = QTableWidget()
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.setSelectionMode(QTableWidget.SingleSelection)
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels([
            "Código", "Nombre", "Categoría", "Talla", "Precio", "Stock Actual", "Acciones"
        ])
        
        encabezado_tabla = self.tabla.horizontalHeader()
        encabezado_tabla.setSectionResizeMode(QHeaderView.ResizeToContents)
        encabezado_tabla.setSectionResizeMode(1, QHeaderView.Stretch) 
        encabezado_tabla.setSectionResizeMode(2, QHeaderView.Stretch) 
        encabezado_tabla.setSectionResizeMode(4, QHeaderView.Stretch) 
        encabezado_tabla.setSectionResizeMode(6, QHeaderView.Fixed)  
        self.tabla.setColumnWidth(6, 80)
        
        self.tabla.setAlternatingRowColors(False) 
        
        layout_principal.addWidget(self.tabla)

        self.agregar_datos_prueba()

    def agregar_datos_prueba(self):
        """Llena la tabla con datos de ejemplo y aplica colores según stock."""
        datos = [
            ("MP0002", "M500", "Chancla", "38", "30000", "0"),
            ("PT0001", "Nike", "Chancla", "37", "30000", "10"),
            ("MP0003", "Capibara", "Babucha", "38", "30000", "30"),
            ("MP0004", "Conejo", "Babucha", "38", "30000", "20"),
            ("MP0005", "Gato", "Babucha", "36", "30000", "12"),
            ("MP0006", "Perro", "Babucha", "30", "30000", "5"),
            ("MP0007", "León", "Babucha", "28", "30000", "3"),
            ("MP0008", "Cerdito", "Babucha", "38", "30000", "0")
        ]

        self.tabla.setRowCount(len(datos))

        for fila, (cod, nom, cat, talla, precio, stock) in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(cod))
            self.tabla.setItem(fila, 1, QTableWidgetItem(nom))
            self.tabla.setItem(fila, 2, QTableWidgetItem(cat))
            self.tabla.setItem(fila, 3, QTableWidgetItem(talla))
            self.tabla.setItem(fila, 4, QTableWidgetItem(precio))
            self.tabla.setItem(fila, 5, QTableWidgetItem(stock))
            
            btn_ver = QPushButton("Ver")
            btn_ver.setObjectName("btnVerTabla")
            btn_ver.setCursor(Qt.PointingHandCursor)
            self.tabla.setCellWidget(fila, 6, btn_ver)

            color_fondo = QColor("#ffffff")
            if int(stock) == 0:
                color_fondo = QColor("#f8d7da") 
            elif int(stock) <= 3:
                color_fondo = QColor("#fff3cd") 
            elif int(stock) > 3:
                color_fondo = QColor("#d4edda") 

            for col in range(6):
                item = self.tabla.item(fila, col)
                if item:
                    item.setBackground(color_fondo)
                    item.setForeground(QColor("#444444"))