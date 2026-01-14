from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QStackedWidget, QLabel, QFrame
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from ui.sales_view import SalesView
from ui.inventory_view import InventoryView
from ui.reports_view import ReportsView
from ui.expenses_view import ExpensesView
from ui.returns_view import ReturnsView

class MainWindowView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SISTEMA POS - PALACIO DE LA CHANCLA")
        self.resize(1100, 600)
        
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QHBoxLayout(self.main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.setup_sidebar()
        self.setup_content_area()

    def setup_sidebar(self):
        """Crea la barra lateral izquierda"""
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(200)
        
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setAlignment(Qt.AlignTop)

        self.lbl_logo = QLabel("Menú")
        self.lbl_logo.setObjectName("lbl_logo")
        self.lbl_logo.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(self.lbl_logo)
        sidebar_layout.addSpacing(20)

        self.btn_sales = QPushButton(" Ventas")
        self.btn_sales.setIcon(QIcon(":/icons/ventas.png"))
        
        self.btn_expenses = QPushButton(" Gastos")
        self.btn_expenses.setIcon(QIcon(":/icons/gastos.png"))
        
        self.btn_returns = QPushButton(" Devoluciones")
        self.btn_returns.setIcon(QIcon(":/icons/devoluciones.png"))
        
        self.btn_reports = QPushButton(" Reportes")
        self.btn_reports.setIcon(QIcon(":/icons/reportes.png"))

        self.btn_inventory = QPushButton(" Inventario")
        self.btn_inventory.setIcon(QIcon(":/icons/inventario.png"))

        self.btn_dashboard = QPushButton(" Dashboard")
        self.btn_dashboard.setIcon(QIcon(":/icons/dashboard.png"))
        
        self.btn_configuration = QPushButton(" Configuración")
        self.btn_configuration.setIcon(QIcon(":/icons/configuracion.png"))

        self.list_buttons = [
            self.btn_sales, self.btn_expenses, self.btn_returns, self.btn_reports, 
            self.btn_inventory, self.btn_dashboard, self.btn_configuration
        ]

        for btn in self.list_buttons:
            btn.setObjectName("btn_sidebar")
            btn.setCursor(Qt.PointingHandCursor)
            sidebar_layout.addWidget(btn)

        self.main_layout.addWidget(self.sidebar)

    def setup_content_area(self):
        """Crea el contenedor donde se intercambian los módulos"""
        self.content_area = QStackedWidget()
        
        self.sales_view = SalesView()
        self.expenses_view = ExpensesView()
        self.returns_view = ReturnsView()
        self.reports_view = ReportsView()
        self.inventory_view = InventoryView()
        
        self.dashboard_view = QLabel("Panel de Control (Dashboard) - Próximamente")
        self.dashboard_view.setAlignment(Qt.AlignCenter)
        self.configuration_view = QLabel("Panel de Control (Configuración) - Próximamente")
        self.configuration_view.setAlignment(Qt.AlignCenter)
        
        self.content_area.addWidget(self.sales_view)   
        self.content_area.addWidget(self.expenses_view)   
        self.content_area.addWidget(self.returns_view)
        self.content_area.addWidget(self.reports_view) 
        self.content_area.addWidget(self.inventory_view) 
        
        self.content_area.addWidget(self.dashboard_view)  
        self.content_area.addWidget(self.configuration_view)  
        
        
        self.main_layout.addWidget(self.content_area)