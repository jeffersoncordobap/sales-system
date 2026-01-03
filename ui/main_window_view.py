from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QStackedWidget, QLabel, QFrame
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from ui.sales_view import PaginaVentas
from ui.inventory_view import PaginaInventario
from ui.reports_view import PaginaReportes
from ui.expenses_view import PaginaGastos
from ui.returns_view import PaginaDevoluciones

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SISTEMA POS - PALACIO DE LA CHANCLA")
        self.resize(1100, 600)
        
        self.widget_principal = QWidget()
        self.setCentralWidget(self.widget_principal)
        
        self.layout_principal = QHBoxLayout(self.widget_principal)
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.layout_principal.setSpacing(0)

        self.configurar_barra_lateral()
        self.configurar_area_contenido()

    def configurar_barra_lateral(self):
        """Crea la barra lateral izquierda"""
        self.barra_lateral = QFrame()
        self.barra_lateral.setObjectName("barraLateral")
        self.barra_lateral.setFixedWidth(200)
        
        layout_barra = QVBoxLayout(self.barra_lateral)
        layout_barra.setAlignment(Qt.AlignTop)

        self.lbl_logo = QLabel("Menú")
        self.lbl_logo.setObjectName("barraLateralLogo")
        self.lbl_logo.setAlignment(Qt.AlignCenter)
        layout_barra.addWidget(self.lbl_logo)
        layout_barra.addSpacing(20)

        self.btn_ventas = QPushButton(" Ventas")
        self.btn_ventas.setIcon(QIcon(":/icons/ventas.png"))
        
        self.btn_gastos = QPushButton(" Gastos")
        self.btn_gastos.setIcon(QIcon(":/icons/gastos.png"))
        
        self.btn_devoluciones = QPushButton(" Devoluciones")
        self.btn_devoluciones.setIcon(QIcon(":/icons/devoluciones.png"))
        
        self.btn_reportes = QPushButton(" Reportes")
        self.btn_reportes.setIcon(QIcon(":/icons/reportes.png"))
        
        self.btn_inventario = QPushButton(" Inventario")
        self.btn_inventario.setIcon(QIcon(":/icons/inventario.png"))
        
        self.btn_dashboard = QPushButton(" Dashboard")
        self.btn_dashboard.setIcon(QIcon(":/icons/dashboard.png"))
        
        self.btn_configuracion = QPushButton(" Configuración")
        self.btn_configuracion.setIcon(QIcon(":/icons/configuracion.png"))

        self.lista_botones = [
            self.btn_ventas, self.btn_gastos, self.btn_devoluciones, self.btn_reportes, 
            self.btn_inventario, self.btn_dashboard, self.btn_configuracion
        ]

        for boton in self.lista_botones:
            boton.setObjectName("botonMenu")
            boton.setCursor(Qt.PointingHandCursor)
            layout_barra.addWidget(boton)

        self.layout_principal.addWidget(self.barra_lateral)

    def configurar_area_contenido(self):
        """Crea el contenedor donde se intercambian los módulos"""
        self.area_contenido = QStackedWidget()
        
        self.pagina_ventas = PaginaVentas()
        self.pagina_gastos = PaginaGastos()
        self.pagina_devoluciones = PaginaDevoluciones()
        self.pagina_reportes = PaginaReportes()
        self.pagina_inventario = PaginaInventario()
        
        self.pagina_dashboard = QLabel("Panel de Control (Dashboard) - Próximamente")
        self.pagina_dashboard.setAlignment(Qt.AlignCenter)
        self.pagina_configuracion = QLabel("Panel de Control (Configuración) - Próximamente")
        self.pagina_configuracion.setAlignment(Qt.AlignCenter)
        
        self.area_contenido.addWidget(self.pagina_ventas)   
        self.area_contenido.addWidget(self.pagina_gastos)   
        self.area_contenido.addWidget(self.pagina_devoluciones)
        self.area_contenido.addWidget(self.pagina_reportes) 
        self.area_contenido.addWidget(self.pagina_inventario) 
        
        self.area_contenido.addWidget(self.pagina_dashboard)  
        self.area_contenido.addWidget(self.pagina_configuracion)  
        
        
        self.layout_principal.addWidget(self.area_contenido)