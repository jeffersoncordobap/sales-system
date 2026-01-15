from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QComboBox, QLineEdit,
    QHBoxLayout, QVBoxLayout, QHeaderView, QTableWidget,
    QAbstractItemView, QFrame
)
from PySide6.QtCore import Qt
from ui.confirm_payment_view import ConfirmPaymentDialog
from ui.open_register_view import OpenRegisterDialog
from ui.close_register_view import CloseRegisterDialog

class SalesView(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(25, 25, 25, 25)

        self.create_header()
        self.create_entry_form() 
        self.create_products_table()
        self.create_footer()
        self.btn_pay.clicked.connect(self.open_confirm_payment_dialog)
        self.btn_open_register.clicked.connect(self.open_box)
        self.btn_close_register.clicked.connect(self.close_box)
        self.combo_discount_type.currentTextChanged.connect(self.change_place_holder_discount)
        self.combo_discount_type.currentTextChanged.connect(self.enable_discount_entry)

    def create_header(self):
        header_layout = QHBoxLayout()
        
        self.lbl_title = QLabel("Punto de Venta")
        self.lbl_title.setStyleSheet("font-size: 26px; font-weight: bold; color: #2c3e50;")
        
        self.btn_open_register = QPushButton(" Abrir Caja")
        self.btn_open_register.setObjectName("btn_open_register")
        
        self.btn_close_register = QPushButton(" Cerrar Caja")
        self.btn_close_register.setObjectName("btn_close_register")

        self.lbl_cash_in_register = QLabel("Caja: $0.00")
        self.lbl_cash_in_register.setStyleSheet("background: #ecf0f1; padding: 8px; border-radius: 5px; font-weight: bold;")

        header_layout.addWidget(self.lbl_title)
        header_layout.addStretch()
        header_layout.addWidget(self.lbl_cash_in_register)
        header_layout.addWidget(self.btn_open_register)
        header_layout.addWidget(self.btn_close_register)
        
        self.main_layout.addLayout(header_layout)

    def create_entry_form(self):
        entry_section_container = QFrame()
        entry_section_container.setObjectName("entry_section_container")
        entry_section_container.setStyleSheet("QFrame#entry_section_container { background-color: #f8f9fa; border-radius: 10px; border: 1px solid #dee2e6; }")
        
        form_layout = QVBoxLayout(entry_section_container)
     
        row1 = QHBoxLayout()
        self.combo_search_product = QComboBox()
        self.combo_search_product.setObjectName("combo_search_product")
        self.combo_search_product.setEditable(True)
        self.combo_search_product.setPlaceholderText("Buscar producto...")

        row1.addWidget(QLabel("Producto:"))
        row1.addWidget(self.combo_search_product, 1) 
        
        
        row2 = QHBoxLayout()
        self.input_price = QLineEdit()
        self.input_price.setPlaceholderText("Precio")
        self.input_price.setReadOnly(True)
        self.input_price.setFixedWidth(120)
        self.input_amount = QLineEdit()
        self.input_amount.setPlaceholderText("Cant.")
        self.input_amount.setFixedWidth(80)
        
        self.combo_discount_type = QComboBox()
        self.combo_discount_type.setObjectName("combo_discount_type")
        self.combo_discount_type.addItems(["Sin Desc.", "% Desc.", "$ Desc."])
        self.combo_discount_type.setFixedWidth(100)

        self.input_discount = QLineEdit()
        self.input_discount.setReadOnly(True)
        self.input_discount.setPlaceholderText("0.00")
        self.input_discount.setFixedWidth(100)

        self.btn_add_to_cart = QPushButton("Agregar al carrito")
        self.btn_add_to_cart.setObjectName("btn_add_to_cart") 
        self.btn_add_to_cart.setMinimumHeight(35)

        
        row2.addWidget(QLabel("Precio:"))
        row2.addWidget(self.input_price)
        row2.addStretch()
        row2.addWidget(QLabel("Cantidad:"))
        row2.addWidget(self.input_amount)
        row2.addStretch() 
        row2.addWidget(QLabel("Descuento:"))
        row2.addWidget(self.combo_discount_type)
        row2.addWidget(self.input_discount)
        row2.addStretch()
        row2.addWidget(self.btn_add_to_cart)

        form_layout.addLayout(row1)
        form_layout.addLayout(row2)
        self.main_layout.addWidget(entry_section_container)

    def create_products_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Código", "Descripción", "Precio Unit.", "Cant.","Descuento.", "Subtotal"])
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch) 
        
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.main_layout.addWidget(self.table)
        
    def create_footer(self):
        footer_layout = QHBoxLayout()
        
        self.btn_clean = QPushButton("Vaciar Carrito")
        self.btn_clean.setObjectName("btn_clean") 
        
        self.lbl_total = QLabel("TOTAL A PAGAR: $0.00")
        self.lbl_total.setStyleSheet("font-size: 28px; font-weight: bold; color: #27ae60;")
        
        self.btn_pay = QPushButton("CONFIRMAR PAGO")
        self.btn_pay.setFixedSize(250, 60)
        self.btn_pay.setObjectName("btn_pay") 

        footer_layout.addWidget(self.btn_clean)
        footer_layout.addStretch()
        footer_layout.addWidget(self.lbl_total)
        footer_layout.addSpacing(30)
        footer_layout.addWidget(self.btn_pay)

        self.main_layout.addLayout(footer_layout)
        
        
    def open_confirm_payment_dialog(self):
        """Método que abre el dialogo de confirmar pago.
        """        
        # Obtenemos el total de la tabla (ej. 50000)
        #total = self.obtener_total_carrito() 
        dialog = ConfirmPaymentDialog(100000, self)
        if dialog.exec():
            # Si el usuario confirmó, procesamos la venta
            print("Venta procesada con éxito")
            #self.limpiar_carrito()
            
            
    def open_box(self):
        """Método que abre el dialogo de abrir caja.
        """   
        dialog = OpenRegisterDialog("Camila C",self)
        if dialog.exec():
            print("caja abierta con exito...")     
            
    def close_box(self):
        """Método que abre el dialogo de cerrar caja.
        """   
        dialog = CloseRegisterDialog(1245000,750000,50000,self)
        if dialog.exec():
            print("caja cerrada con exito...") 
                

    def change_place_holder_discount(self,item):
        if item == "% Desc.":
            self.input_discount.setPlaceholderText("0%")
        else:
            self.input_discount.setPlaceholderText("0.00")
            
    def enable_discount_entry(self,discount):
        if discount =="% Desc." or discount == "$ Desc.":
            self.input_discount.setReadOnly(False)
        else:
            self.input_discount.setReadOnly(True)