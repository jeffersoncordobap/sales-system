from PySide6.QtWidgets import QMessageBox
from ui.login_view import LoginView
from services.auth_service import AuthService
from controllers.main_window_controller import MainWindowController

class LoginController:
    def __init__(self,services):
        self.login_view = LoginView()
        self.auth_service = AuthService()
        self.services = services
        self.login_view.btn_login.clicked.connect(self.manage_login)
        self.login_view.successful_login.connect(self.show_main_window)

    def manage_login(self):
        """
        Maneja el evento de clic en el botón de ingresar.
        Valida las credenciales y emite la señal de éxito si son correctas.
        """

        user, password = self.login_view.get_credentials()
        if self.auth_service.authenticate_user(user, password):
            self.login_view.input_password.clear()
            self.login_view.successful_login.emit()
            
        else:
            QMessageBox.warning(
                    self.login_view,
                    "Error de Acceso",
                    "Credenciales inválidas. Intente con 'admin' / '123'."
                )
            self.login_view.input_password.clear()

    def show_main_window(self):
        """
        Cierra la vista de login y abre la ventana principal del sistema.
        """
        self.main_window_controller = MainWindowController(self.services)
        self.main_window_controller.show_main_window()
        self.login_view.close()

    def show_login(self):
        """Método inicial para arrancar la aplicación."""
        self.login_view.show()