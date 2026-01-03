from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QComboBox, QLineEdit,
    QHBoxLayout, QVBoxLayout, QHeaderView, QTableWidget,
    QAbstractItemView, QFrame
)
from PySide6.QtCore import Qt
from ui.confirm_payment_view import DialogoPago
from ui.open_box_view import DialogoAperturaCaja
from ui.close_box_view import DialogoCierreCaja


class PaginaVentas(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_principal = QVBoxLayout(self)
        self.layout_principal.setSpacing(15)
        self.layout_principal.setContentsMargins(25, 25, 25, 25)

        self.crear_encabezado()
        self.crear_formulario_entrada() 
        self.crear_tabla_productos()
        self.crear_pie_pagina()
        self.btn_pagar.clicked.connect(self.abrir_pago)
        self.btn_abrir_caja.clicked.connect(self.abrir_caja)
        self.btn_cerrar_caja.clicked.connect(self.cerrar_caja)
        self.combo_tipo_desc.currentTextChanged.connect(self.cambiar_place_holder_descuento)
        self.combo_tipo_desc.currentTextChanged.connect(self.habilitar_entrada_descuento)

    def crear_encabezado(self):
        layout_encabezado = QHBoxLayout()
        
        self.lbl_titulo = QLabel("Punto de Venta")
        self.lbl_titulo.setStyleSheet("font-size: 26px; font-weight: bold; color: #2c3e50;")
        
        self.btn_abrir_caja = QPushButton(" Abrir Caja")
        self.btn_abrir_caja.setObjectName("btnAbrirCaja")
        
        self.btn_cerrar_caja = QPushButton(" Cerrar Caja")
        self.btn_cerrar_caja.setObjectName("btnCerrarCaja")
        
        self.lbl_dinero_caja = QLabel("Caja: $0.00")
        self.lbl_dinero_caja.setStyleSheet("background: #ecf0f1; padding: 8px; border-radius: 5px; font-weight: bold;")

        layout_encabezado.addWidget(self.lbl_titulo)
        layout_encabezado.addStretch()
        layout_encabezado.addWidget(self.lbl_dinero_caja)
        layout_encabezado.addWidget(self.btn_abrir_caja)
        layout_encabezado.addWidget(self.btn_cerrar_caja)
        
        self.layout_principal.addLayout(layout_encabezado)

    def crear_formulario_entrada(self):
        contenedor = QFrame()
        contenedor.setObjectName("seccionEntrada")
        contenedor.setStyleSheet("QFrame#seccionEntrada { background-color: #f8f9fa; border-radius: 10px; border: 1px solid #dee2e6; }")
        
        layout_formulario = QVBoxLayout(contenedor)
     
        fila1 = QHBoxLayout()
        self.combo_producto = QComboBox()
        self.combo_producto.setObjectName("ComboBuscarProducto")
        self.combo_producto.setEditable(True)
        self.combo_producto.setPlaceholderText("Buscar producto...")

        fila1.addWidget(QLabel("Producto:"))
        fila1.addWidget(self.combo_producto, 1) 
        
        
        fila2 = QHBoxLayout()
        self.entrada_precio = QLineEdit()
        self.entrada_precio.setPlaceholderText("Precio")
        self.entrada_precio.setReadOnly(True)
        self.entrada_precio.setFixedWidth(120)
        self.entrada_cantidad = QLineEdit()
        self.entrada_cantidad.setPlaceholderText("Cant.")
        self.entrada_cantidad.setFixedWidth(80)
        
        self.combo_tipo_desc = QComboBox()
        self.combo_tipo_desc.setObjectName("ComboDescuento")
        self.combo_tipo_desc.addItems(["Sin Desc.", "% Desc.", "$ Desc."])
        self.combo_tipo_desc.setFixedWidth(100)

        self.entrada_descuento = QLineEdit()
        self.entrada_descuento.setReadOnly(True)
        self.entrada_descuento.setPlaceholderText("0.00")
        self.entrada_descuento.setFixedWidth(100)

        self.btn_agregar = QPushButton("Agregar al carrito")
        self.btn_agregar.setObjectName("btnAgregarCarrito") 
        self.btn_agregar.setMinimumHeight(35)

        
        fila2.addWidget(QLabel("Precio:"))
        fila2.addWidget(self.entrada_precio)
        fila2.addStretch()
        fila2.addWidget(QLabel("Cantidad:"))
        fila2.addWidget(self.entrada_cantidad)
        fila2.addStretch() 
        fila2.addWidget(QLabel("Descuento:"))
        fila2.addWidget(self.combo_tipo_desc)
        fila2.addWidget(self.entrada_descuento)
        fila2.addStretch()
        fila2.addWidget(self.btn_agregar)

        layout_formulario.addLayout(fila1)
        layout_formulario.addLayout(fila2)
        self.layout_principal.addWidget(contenedor)

    def crear_tabla_productos(self):
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["Código", "Descripción", "Precio Unit.", "Cant.","Descuento.", "Subtotal"])
        
        encabezado = self.tabla.horizontalHeader()
        encabezado.setSectionResizeMode(QHeaderView.ResizeToContents)
        encabezado.setSectionResizeMode(1, QHeaderView.Stretch) 
        
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layout_principal.addWidget(self.tabla)
        
    def crear_pie_pagina(self):
        pie = QHBoxLayout()
        
        self.btn_limpiar = QPushButton("Vaciar Carrito")
        self.btn_limpiar.setObjectName("btnVaciarCarrito") 
        
        self.lbl_total = QLabel("TOTAL A PAGAR: $0.00")
        self.lbl_total.setStyleSheet("font-size: 28px; font-weight: bold; color: #27ae60;")
        
        self.btn_pagar = QPushButton("CONFIRMAR PAGO")
        self.btn_pagar.setFixedSize(250, 60)
        self.btn_pagar.setObjectName("btnConfirmarPago") 

        pie.addWidget(self.btn_limpiar)
        pie.addStretch()
        pie.addWidget(self.lbl_total)
        pie.addSpacing(30)
        pie.addWidget(self.btn_pagar)

        self.layout_principal.addLayout(pie)
        
        
    def abrir_pago(self):
        """Método que abre el dialogo de confirmar pago.
        """        
        # Obtenemos el total de la tabla (ej. 50000)
        #total = self.obtener_total_carrito() 
        dialogo = DialogoPago(100000, self)
        if dialogo.exec():
            # Si el usuario confirmó, procesamos la venta
            print("Venta procesada con éxito")
            #self.limpiar_carrito()
            
            
    def abrir_caja(self):
        """Método que abre el dialogo de abrir caja.
        """   
        dialogo = DialogoAperturaCaja("Camila C",self)
        if dialogo.exec():
            print("caja abierta con exito...")     
            
    def cerrar_caja(self):
        """Método que abre el dialogo de cerrar caja.
        """   
        dialogo = DialogoCierreCaja(1245000,750000,50000,self)
        if dialogo.exec():
            print("caja cerrada con exito...") 
                

    def cambiar_place_holder_descuento(self,item):
        if item == "% Desc.":
            self.entrada_descuento.setPlaceholderText("0%")
        else:
            self.entrada_descuento.setPlaceholderText("0.00")
            
    def habilitar_entrada_descuento(self,descuento):
        if descuento =="% Desc." or descuento == "$ Desc.":
            self.entrada_descuento.setReadOnly(False)
        else:
            self.entrada_descuento.setReadOnly(True)