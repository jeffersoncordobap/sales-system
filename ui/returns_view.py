from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFrame, QTableWidget, QHeaderView, QComboBox,
    QCheckBox, QSpinBox, QAbstractItemView
)
from PySide6.QtCore import Qt

class PaginaDevoluciones(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PaginaDevoluciones")
        self.layout_principal = QVBoxLayout(self)

        self.crear_cabecera_busqueda()
        self.cuerpo = QHBoxLayout()
        self.crear_tabla_detalle_venta()
        self.crear_panel_configuracion()
        
        self.layout_principal.addLayout(self.cuerpo)

    def crear_cabecera_busqueda(self):
        """Buscador de la venta original"""
        contenedor = QFrame()
        contenedor.setObjectName("CabeceraDevolucion")
        layout = QHBoxLayout(contenedor)

        layout.addWidget(QLabel("Ingrese N° de Factura:"))
        self.entrada_busqueda = QLineEdit()
        self.entrada_busqueda.setPlaceholderText("Ej: 150")
        self.entrada_busqueda.setObjectName("EntradaBusquedaDev")
        
        self.btn_buscar = QPushButton("BUSCAR VENTA")
        self.btn_buscar.setObjectName("BtnBuscarVenta")

        layout.addWidget(self.entrada_busqueda)
        layout.addWidget(self.btn_buscar)
        layout.addStretch()
        
        self.lbl_info_venta = QLabel("Esperando búsqueda...")
        self.lbl_info_venta.setObjectName("InfoVentaEncontrada")
        layout.addWidget(self.lbl_info_venta)

        self.layout_principal.addWidget(contenedor)

    def crear_tabla_detalle_venta(self):
        """Muestra los productos que el cliente compró"""
        contenedor = QVBoxLayout()
        contenedor.addWidget(QLabel("Productos de la Venta Original:"))
        
        self.tabla_items = QTableWidget()
        self.tabla_items.setColumnCount(5)
        self.tabla_items.setHorizontalHeaderLabels(["Cód.", "Producto", "Cant. Comprada", "Precio Pagado", "Seleccionar"])
        self.tabla_items.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_items.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        contenedor.addWidget(self.tabla_items)
        self.cuerpo.addLayout(contenedor, 2) 

    def crear_panel_configuracion(self):
        """Opciones de la devolución actual"""
        self.panel_opciones = QFrame()
        self.panel_opciones.setObjectName("PanelOpcionesDev")
        self.panel_opciones.setFixedWidth(300)
        layout = QVBoxLayout(self.panel_opciones)

        layout.addWidget(QLabel("CANTIDAD A DEVOLVER:"))
        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setMinimum(1)
        self.spin_cantidad.setObjectName("SpinDevolucion")
        layout.addWidget(self.spin_cantidad)

        layout.addWidget(QLabel("ESTADO DEL PRODUCTO:"))
        self.combo_estado = QComboBox()
        self.combo_estado.addItems(["Buen Estado (Vuelve al Inventario)", "Dañado / Defectuoso (Baja)"])
        layout.addWidget(self.combo_estado)

        layout.addWidget(QLabel("MOTIVO:"))
        self.combo_motivo = QComboBox()
        self.combo_motivo.addItems(["Garantía", "Cambio de producto", "Error de compra", "Otro"])
        layout.addWidget(self.combo_motivo)

        layout.addStretch()

        self.lbl_total_reembolso = QLabel("Total Reembolso: $0.00")
        self.lbl_total_reembolso.setObjectName("LabelTotalReembolso")
        layout.addWidget(self.lbl_total_reembolso)

        self.btn_procesar = QPushButton("PROCESAR DEVOLUCIÓN")
        self.btn_procesar.setObjectName("BtnProcesarDevolucion")
        self.btn_procesar.setMinimumHeight(50)
        layout.addWidget(self.btn_procesar)

        self.cuerpo.addWidget(self.panel_opciones)
        

    def conectar_eventos(self):
        self.tabla_items.itemClicked.connect(self.cargar_producto_seleccionado)
        self.spin_cantidad.valueChanged.connect(self.actualizar_calculo_reembolso)

    def cargar_producto_seleccionado(self, item):
        row = item.row()
        self.producto_actual = self.tabla_items.item(row, 1).text()
        cantidad_comprada = int(self.tabla_items.item(row, 2).text())
        self.precio_unitario_venta = float(self.tabla_items.item(row, 3).text())

        self.spin_cantidad.setRange(1, cantidad_comprada) 
        self.spin_cantidad.setValue(1)
        
        self.lbl_info_venta.setText(f"Seleccionado: {self.producto_actual}")
        self.actualizar_calculo_reembolso()

    def actualizar_calculo_reembolso(self):
        cantidad = self.spin_cantidad.value()
        total = cantidad * self.precio_unitario_venta
        self.lbl_total_reembolso.setText(f"Total Reembolso: ${total:,.2f}")