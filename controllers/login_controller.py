from PySide6.QtWidgets import QMessageBox
from ui.login_view import PaginaLogin
from services.auth_service import ServicioAutenticacion
from controllers.main_window_controller import ControladorVentanaPrincipal

class ControladorLogin:
    def __init__(self,servicios):
        self.vista_login = PaginaLogin()
        self.servcioAutenticacion = ServicioAutenticacion()
        self.servicios = servicios
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
        self.controlador_principal = ControladorVentanaPrincipal(self.servicios)
        self.controlador_principal.mostrar()
        self.vista_login.close()

    def mostrar_login(self):
        """Método inicial para arrancar la aplicación."""
        self.vista_login.show()