from PySide6.QtWidgets import QMessageBox
from ui.login_view import PaginaLogin
from services.auth_service import ServicioAutenticacion
from controllers.main_window_controller import ControladorVentanaPrincipal

class ControladorLogin:
    def __init__(self):
        self.vista_login = PaginaLogin()
        self.servcioAutenticacion = ServicioAutenticacion()
        self.vista_login.btn_ingresar.clicked.connect(self.manejar_inicio_sesion)
        self.vista_login.inicio_sesion_exitoso.connect(self.mostrar_ventana_principal)

    def manejar_inicio_sesion(self):
        """
        Maneja el evento de clic en el botón de ingresar.
        Valida las credenciales y emite la señal de éxito si son correctas.
        """
        
        usuario, contrasena = self.vista_login.obtener_credenciales()
        if self.servcioAutenticacion.autenticar_usuario(usuario, contrasena):
            self.vista_login.entrada_contrasena.clear()
            self.vista_login.inicio_sesion_exitoso.emit()
            
        else:
            QMessageBox.warning(
                    self.vista_login,
                    "Error de Acceso",
                    "Credenciales inválidas. Intente con 'admin' / '123'."
                )
            self.vista_login.entrada_contrasena.clear()
    def mostrar_ventana_principal(self):
        """
        Cierra la vista de login y abre la ventana principal del sistema.
        """
        self.controlador_principal = ControladorVentanaPrincipal()
        self.controlador_principal.mostrar()
        self.vista_login.close()
        
    def conectar_navegacion(self):
        """
        Conecta los botones de la barra lateral con las páginas del contenedor.
        """
        vp = self.ventana_principal
        vp.btn_ventas.clicked.connect(lambda: vp.area_contenido.setCurrentIndex(0))
        vp.btn_inventario.clicked.connect(lambda: vp.area_contenido.setCurrentIndex(1))
        vp.btn_dashboard.clicked.connect(lambda: vp.area_contenido.setCurrentIndex(2))

    def mostrar_login(self):
        """Método inicial para arrancar la aplicación."""
        self.vista_login.show()