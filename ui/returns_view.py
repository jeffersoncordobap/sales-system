from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFrame, QTableWidget, QHeaderView, QComboBox,
    QCheckBox, QSpinBox, QAbstractItemView, QTableWidgetItem
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class PaginaDevoluciones(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PaginaDevoluciones")
       
        self.layout_principal = QVBoxLayout(self)
        self.layout_principal.setContentsMargins(20, 20, 20, 20)
        self.layout_principal.setSpacing(15)

        self.crear_cabecera_busqueda()

        self.crear_barra_resumen_venta()

        self.cuerpo = QHBoxLayout()
        self.crear_tabla_detalle_venta()
        self.crear_panel_configuracion()
        
        self.layout_principal.addLayout(self.cuerpo)

    def crear_cabecera_busqueda(self):
        contenedor = QFrame()
        contenedor.setObjectName("ContenedorBusqueda")
        layout = QHBoxLayout(contenedor)
        
        layout.addWidget(QLabel("🔍 Número de Factura:"))
        self.entrada_busqueda = QLineEdit()
        self.entrada_busqueda.setObjectName("EntradaBusquedaDev")
        self.entrada_busqueda.setPlaceholderText("Escriba el numero de factura...")
        self.entrada_busqueda.setFixedWidth(250)
        
        self.btn_buscar = QPushButton("BUSCAR")
        self.btn_buscar.setObjectName("BtnBuscarVenta")
        self.btn_buscar.setFixedWidth(120)

        layout.addWidget(self.entrada_busqueda)
        layout.addWidget(self.btn_buscar)
        layout.addStretch() 

        self.layout_principal.addWidget(contenedor)

    def crear_barra_resumen_venta(self):
        """Nueva sección: Muestra datos clave de la factura encontrada"""
        self.barra_resumen = QFrame()
        self.barra_resumen.setObjectName("BarraResumen")
        self.barra_resumen.setMinimumHeight(50)
        
        layout = QHBoxLayout(self.barra_resumen)
        
        self.lbl_info_venta = QLabel("Esperando factura...")
        self.lbl_info_venta.setObjectName("InfoVentaEncontrada")
        
        self.lbl_fecha_venta = QLabel("Fecha: --/--/--")
        self.lbl_cliente_venta = QLabel("Cliente: General")

        layout.addWidget(self.lbl_info_venta)
        layout.addStretch()
        layout.addWidget(self.lbl_fecha_venta)
        layout.addSpacing(20)
        layout.addWidget(self.lbl_cliente_venta)

        self.layout_principal.addWidget(self.barra_resumen)

    def crear_tabla_detalle_venta(self):
        contenedor_tabla = QFrame()
        contenedor_tabla.setObjectName("CardBlanca")
        layout = QVBoxLayout(contenedor_tabla)

        titulo = QLabel("PRODUCTOS COMPRADOS")
        titulo.setObjectName("TituloSeccion")
        layout.addWidget(titulo)
        
        self.tabla_items = QTableWidget()
        self.tabla_items.setColumnCount(5)
        self.tabla_items.setHorizontalHeaderLabels(["Cód.", "Producto", "Cant. Comprada", "Precio Pagado", "Seleccionar"])
        self.tabla_items.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.tabla_items)
        self.cuerpo.addWidget(contenedor_tabla, 2)

    def crear_panel_configuracion(self):
        self.panel_opciones = QFrame()
        self.panel_opciones.setObjectName("PanelDerecho")
        self.panel_opciones.setFixedWidth(320)
        
        layout = QVBoxLayout(self.panel_opciones)
        layout.setSpacing(10)

        titulo = QLabel("DETALLES DE DEVOLUCIÓN")
        titulo.setObjectName("TituloSeccion")
        layout.addWidget(titulo)
    
        layout.addWidget(QLabel("Cantidad a devolver:"))
        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setMinimum(1)
        layout.addWidget(self.spin_cantidad)

        layout.addWidget(QLabel("Estado físico:"))
        self.combo_estado = QComboBox()
        self.combo_estado.addItems(["Buen Estado (Vuelve al Inventario)", "Dañado / Defectuoso (Baja)"])
        layout.addWidget(self.combo_estado)

        layout.addWidget(QLabel("Motivo:"))
        self.combo_motivo = QComboBox()
        self.combo_motivo.addItems(["Cambio de producto", "Garantía", "Error de compra", "Otro"])
        layout.addWidget(self.combo_motivo)

        layout.addStretch() 


        linea = QFrame()
        linea.setFrameShape(QFrame.HLine)
        linea.setFrameShadow(QFrame.Sunken)
        layout.addWidget(linea)

        self.lbl_total_reembolso = QLabel("REEMBOLSO: $0.00")
        self.lbl_total_reembolso.setObjectName("LabelTotalReembolso")
        self.lbl_total_reembolso.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lbl_total_reembolso)

        self.btn_procesar = QPushButton("CONFIRMAR DEVOLUCIÓN")
        self.btn_procesar.setObjectName("BtnProcesarDevolucion")
        self.btn_procesar.setMinimumHeight(60)
        layout.addWidget(self.btn_procesar)

        self.cuerpo.addWidget(self.panel_opciones)
        

    def cargar_producto_seleccionado(self, item):
        row_index = item.row()
        
        for r in range(self.tabla_items.rowCount()):
            self.tabla_items.setItem(r, 4, QTableWidgetItem("")) 
            for c in range(self.tabla_items.columnCount()):
                self.tabla_items.item(r, c).setBackground(QColor("white"))

        marca_seleccion = QTableWidgetItem(" ✅ ")
        marca_seleccion.setTextAlignment(Qt.AlignCenter)
        self.tabla_items.setItem(row_index, 4, marca_seleccion)
        
        for c in range(self.tabla_items.columnCount()):
            self.tabla_items.item(row_index, c).setBackground(QColor("#f4ecf7")) 

        self.producto_actual = self.tabla_items.item(row_index, 1).text()
        cantidad_comprada = int(self.tabla_items.item(row_index, 2).text())
        self.precio_unitario_venta = float(self.tabla_items.item(row_index, 3).text())

        self.spin_cantidad.setRange(1, cantidad_comprada) 
        self.spin_cantidad.setValue(1)
        
        self.lbl_info_venta.setText(f"Seleccionado: {self.producto_actual}")
        self.actualizar_calculo_reembolso()
    
    def actualizar_calculo_reembolso(self):
        cantidad = self.spin_cantidad.value()
        total = cantidad * self.precio_unitario_venta
        self.lbl_total_reembolso.setText(f"Total Reembolso: ${total:,.2f}")