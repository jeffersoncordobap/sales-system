from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, 
    QDateEdit, QPushButton, QTableWidget, QFrame, QHeaderView,
    QAbstractItemView, QTabWidget
)
from PySide6.QtCore import Qt, QDate

class PaginaReportes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("PaginaReportes")
        self.layout_principal = QVBoxLayout(self)
        self.layout_principal.setSpacing(15)
        
        self.crear_cabecera_filtros()
        self.crear_resumen_contable() 
        self.crear_area_datos()
        self.crear_barra_acciones()
        self.combo_filtro.currentTextChanged.connect(self.configurar_columnas_tabla)

    def crear_cabecera_filtros(self):
        contenedor = QFrame()
        contenedor.setObjectName("ContenedorFiltrosBusqueda")
        layout = QHBoxLayout(contenedor)

        self.f_inicio = QDateEdit(QDate.currentDate())
        self.f_inicio.setCalendarPopup(True)
        
        self.f_fin = QDateEdit(QDate.currentDate())
        self.f_fin.setCalendarPopup(True)

        # Filtro de categoría (Lo que antes se escribía mezclado en el cuaderno)
        layout.addWidget(QLabel("Filtrar por:"))
        self.combo_filtro = QComboBox()
        self.combo_filtro.addItems([
            "Todos los Movimientos", 
            "Resumen de Ventas", 
            "Detalle de Ventas", 
            "Gastos Operativos",
            "Registros de de Cajas"
        ])
        
        self.btn_consultar = QPushButton("Actualizar Libro")
        self.btn_consultar.setObjectName("BtnActualizarLibro")
        
        layout.addWidget(QLabel("Periodo del:"))
        layout.addWidget(self.f_inicio)
        layout.addWidget(QLabel("al:"))
        layout.addWidget(self.f_fin)
        layout.addWidget(self.combo_filtro, 1)
        layout.addWidget(self.btn_consultar)
        
        self.layout_principal.addWidget(contenedor)

    def crear_resumen_contable(self):
        """Tarjetas que dan el balance neto automático para la contadora"""
        self.cont_resumen = QFrame()
        layout = QHBoxLayout(self.cont_resumen)
        
        # Estas etiquetas se actualizarán dinámicamente según el filtro
        self.card_ingresos = self._crear_mini_kpi("TOTAL INGRESOS", "$0.00", "textoVerde")
        self.card_gastos = self._crear_mini_kpi("TOTAL EGRESOS", "$0.00", "textoRojo")
        self.card_balance = self._crear_mini_kpi("BALANCE NETO", "$0.00", "textoAzul")

        layout.addWidget(self.card_ingresos)
        layout.addWidget(self.card_gastos)
        layout.addWidget(self.card_balance)
        self.layout_principal.addWidget(self.cont_resumen)

    def _crear_mini_kpi(self, titulo, valor, color_class):
        frame = QFrame()
        frame.setObjectName("CardContable")
        ly = QVBoxLayout(frame)
        
        lbl_t = QLabel(titulo)
        lbl_t.setObjectName("KpiTituloMini")
        
        lbl_v = QLabel(valor)
        lbl_v.setObjectName(color_class) 
        
        ly.addWidget(lbl_t, alignment=Qt.AlignCenter)
        ly.addWidget(lbl_v, alignment=Qt.AlignCenter)
        return frame

    def crear_area_datos(self):
        """El cuerpo del reporte: similar a las filas del cuaderno"""
        self.tabla = QTableWidget()
        columnas = ["Fecha/Hora", "Tipo", "Descripción", "Usuario", "Ingreso (+)", "Egreso (-)", "Estado"]
        self.tabla.setColumnCount(len(columnas))
        self.tabla.setHorizontalHeaderLabels(columnas)
        
        encabezado = self.tabla.horizontalHeader()
        encabezado.setSectionResizeMode(QHeaderView.Stretch)
        encabezado.setMinimumSectionSize(150)
        self.tabla.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.layout_principal.addWidget(self.tabla)

    def crear_barra_acciones(self):
        layout = QHBoxLayout()
        layout.addStretch()
        
        self.btn_pdf = QPushButton("Generar Reporte PDF")
        self.btn_pdf.setObjectName("BtnExportarPDF")
        self.btn_excel = QPushButton("Exportar Excel")
        self.btn_excel.setObjectName("BtnExportarExcel")
        
        
        layout.addWidget(self.btn_pdf)
        layout.addWidget(self.btn_excel)
        self.layout_principal.addLayout(layout)
        
    def configurar_columnas_tabla(self,tipo):
        """Reconfigura las cabeceras según el tipo de reporte"""
        self.tabla.setRowCount(0)

        if tipo == "Resumen de Ventas":
            columnas = ["Fecha/Hora", "N° Venta", "Vendedor", "Subtotal", "Desc.", "Total", "Estado"]
        elif tipo == "Detalle de Ventas":
            columnas = ["Fecha/Hora", "N° Venta","Vendedor", "Producto","Precio unit.", "Cant.","Subtotal", "Desc.", "Total"]
        elif tipo == "Gastos Operativos":
            columnas = ["Fecha/Hora", "Responsable", "Monto", "Categoria","Metodo de pago"]
        elif tipo == "Registros de de Cajas":
            columnas = ["Fecha/Hora apertura", "Fecha/Hora cierre", "Monto inicial", "Monto esperado","Monto declarado","Diferencia","Obervaciones"]
        else:
            columnas = ["Fecha/Hora", "Tipo", "Descripción", "Usuario", "Ingreso (+)", "Egreso (-)", "Estado"]
        self.tabla.setColumnCount(len(columnas))
        self.tabla.setHorizontalHeaderLabels(columnas)
        encabezado = self.tabla.horizontalHeader()

        if len(columnas) > 6:
            encabezado.setMinimumSectionSize(170) 
        else:
            encabezado.setMinimumSectionSize(150) 
