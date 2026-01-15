from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QFrame, QTableWidget, QHeaderView, QComboBox,
    QCheckBox, QSpinBox, QAbstractItemView, QTableWidgetItem
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class ReturnsView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ReturnsView")
       
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        self.create_search_header()

        self.create_sales_summary_bar()

        self.body = QHBoxLayout()
        self.create_sales_detail_table()
        self.create_configuration_panel()
        
        self.main_layout.addLayout(self.body)

    def create_search_header(self):
        search_container = QFrame()
        search_container.setObjectName("search_container")
        layout = QHBoxLayout(search_container)
        
        layout.addWidget(QLabel("🔍 Número de Factura:"))
        self.input_search_return = QLineEdit()
        self.input_search_return.setObjectName("input_search_return")
        self.input_search_return.setPlaceholderText("Escriba el numero de factura...")
        self.input_search_return.setFixedWidth(250)
        
        self.btn_search = QPushButton("BUSCAR")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.setFixedWidth(120)

        layout.addWidget(self.input_search_return)
        layout.addWidget(self.btn_search)
        layout.addStretch() 

        self.main_layout.addWidget(search_container)

    def create_sales_summary_bar(self):
        """Nueva sección: Muestra datos clave de la factura encontrada"""
        self.summary_bar = QFrame()
        self.summary_bar.setObjectName("summary_bar")
        self.summary_bar.setMinimumHeight(50)
        
        layout = QHBoxLayout(self.summary_bar)
        
        self.lbl_sales_information = QLabel("Esperando factura...")
        self.lbl_sales_information.setObjectName("lbl_sales_information")
        
        self.lbl_sale_date = QLabel("Fecha: --/--/--")
        self.lbl_sale_client = QLabel("Cliente: General")

        layout.addWidget(self.lbl_sales_information)
        layout.addStretch()
        layout.addWidget(self.lbl_sale_date)
        layout.addSpacing(20)
        layout.addWidget(self.lbl_sale_client)

        self.main_layout.addWidget(self.summary_bar)

    def create_sales_detail_table(self):
        container_table_details = QFrame()
        container_table_details.setObjectName("container_table_details")
        layout = QVBoxLayout(container_table_details)

        seccion_title = QLabel("PRODUCTOS COMPRADOS")
        seccion_title.setObjectName("seccion_title")
        layout.addWidget(seccion_title)
        
        self.items_table = QTableWidget()
        self.items_table.setColumnCount(5)
        self.items_table.setHorizontalHeaderLabels(["Cód.", "Producto", "Cant. Comprada", "Precio Pagado", "Seleccionar"])
        self.items_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.items_table)
        self.body.addWidget(container_table_details, 2)

    def create_configuration_panel(self):
        self.options_panel = QFrame()
        self.options_panel.setObjectName("options_panel")
        self.options_panel.setFixedWidth(320)
        
        layout = QVBoxLayout(self.options_panel)
        layout.setSpacing(10)

        titulo_return_details = QLabel("DETALLES DE DEVOLUCIÓN")
        titulo_return_details.setObjectName("titulo_return_details")
        layout.addWidget(titulo_return_details)
    
        layout.addWidget(QLabel("Cantidad a devolver:"))
        self.spin_amount = QSpinBox()
        self.spin_amount.setMinimum(1)
        layout.addWidget(self.spin_amount)

        layout.addWidget(QLabel("Estado físico:"))
        self.combo_state = QComboBox()
        self.combo_state.addItems(["Buen Estado (Vuelve al Inventario)", "Dañado / Defectuoso (Baja)"])
        layout.addWidget(self.combo_state)

        layout.addWidget(QLabel("Motivo:"))
        self.combo_reason = QComboBox()
        self.combo_reason.addItems(["Cambio de producto", "Garantía", "Error de compra", "Otro"])
        layout.addWidget(self.combo_reason)

        layout.addStretch() 


        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        self.lbl_full_refund = QLabel("REEMBOLSO: $0.00")
        self.lbl_full_refund.setObjectName("lbl_full_refund")
        self.lbl_full_refund.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lbl_full_refund)

        self.btn_process = QPushButton("CONFIRMAR DEVOLUCIÓN")
        self.btn_process.setObjectName("btn_process")
        self.btn_process.setMinimumHeight(60)
        layout.addWidget(self.btn_process)

        self.body.addWidget(self.options_panel)
        

    def cargar_selected_product(self, item):
        row_index = item.row()
        
        for r in range(self.items_table.rowCount()):
            self.items_table.setItem(r, 4, QTableWidgetItem("")) 
            for c in range(self.items_table.columnCount()):
                self.items_table.item(r, c).setBackground(QColor("white"))

        selection_mark = QTableWidgetItem(" ✅ ")
        selection_mark.setTextAlignment(Qt.AlignCenter)
        self.items_table.setItem(row_index, 4, selection_mark)
        
        for c in range(self.items_table.columnCount()):
            self.items_table.item(row_index, c).setBackground(QColor("#f4ecf7")) 

        self.current_product = self.items_table.item(row_index, 1).text()
        quantity_purchased = int(self.items_table.item(row_index, 2).text())
        self.unit_sales_price = float(self.items_table.item(row_index, 3).text())

        self.spin_amount.setRange(1, quantity_purchased) 
        self.spin_amount.setValue(1)
        
        self.lbl_sales_information.setText(f"Seleccionado: {self.current_product}")
        self.update_refund_calculation()
    
    def update_refund_calculation(self):
        amount = self.spin_amount.value()
        total = amount * self.unit_sales_price
        self.lbl_full_refund.setText(f"Total Reembolso: ${total:,.2f}")