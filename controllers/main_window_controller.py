from ui.main_window_view import VentanaPrincipal
class ControladorVentanaPrincipal:
    def __init__(self):
        self.vista = VentanaPrincipal()
        self._conectar_navegacion()

    def _conectar_navegacion(self):
        v = self.vista
        v.btn_ventas.clicked.connect(lambda: v.area_contenido.setCurrentIndex(0))
        v.btn_gastos.clicked.connect(lambda: v.area_contenido.setCurrentIndex(1))
        v.btn_devoluciones.clicked.connect(lambda: v.area_contenido.setCurrentIndex(2))
        v.btn_reportes.clicked.connect(lambda: v.area_contenido.setCurrentIndex(3))
        v.btn_inventario.clicked.connect(lambda: v.area_contenido.setCurrentIndex(4))
        v.btn_dashboard.clicked.connect(lambda: v.area_contenido.setCurrentIndex(5))
        v.btn_configuracion.clicked.connect(lambda: v.area_contenido.setCurrentIndex(6))

    def mostrar(self):
        self.vista.show()