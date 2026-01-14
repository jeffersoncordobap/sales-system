from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout,
    QLineEdit, QLabel, QPushButton
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon,QPixmap,Qt,QFont
import resources.resources_rc

class LoginView(QWidget):
    successful_login = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acceso al Sistema")
        self.setObjectName("login_view") 
        self.setWindowIcon(QIcon(":/icons/login.png"))
        self.setGeometry(550, 200, 250, 300)
        self.setFixedSize(250, 300) 

        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz del inicio de sesión."""        
        main_layout = QVBoxLayout(self)
        form_layout = QVBoxLayout()

    
        self.lbl_logo = QLabel()
        pixmap_logo = QPixmap(":/icons/login1.png") 
        scaled_logo = pixmap_logo.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lbl_logo.setPixmap(scaled_logo)


        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("Nombre de usuario")

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setPlaceholderText("Contraseña")
        
        self.btn_login = QPushButton("Iniciar sesión")
        
        self.btn_forgot_password = QPushButton("¿Olvidó su contraseña?")
        self.btn_forgot_password.setFlat(True)
        self.btn_forgot_password.setCursor(Qt.PointingHandCursor)
        self.btn_forgot_password.setObjectName("btn_forgot_password")
        
        form_layout.addWidget(self.input_user)
        form_layout.addWidget(self.input_password)
        form_layout.addWidget(self.btn_login, alignment=Qt.AlignCenter)
        form_layout.addWidget(self.btn_forgot_password, alignment=Qt.AlignCenter)
        
        main_layout.addStretch() 
        main_layout.addWidget(self.lbl_logo, alignment=Qt.AlignCenter)
        main_layout.addLayout(form_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def get_credentials(self):
        """Retorna el usuario y contraseña ingresados."""
        return self.input_user.text().strip(), self.input_password.text().strip()
