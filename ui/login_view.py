from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout,
    QLineEdit, QLabel, QPushButton
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon,QPixmap,Qt,QFont
import resources.resources_rc

class PaginaLogin(QWidget):
    inicio_sesion_exitoso = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acceso al Sistema")
        self.setObjectName("VentanaLogin") 
        self.setWindowIcon(QIcon(":/icons/login.png"))
        self.setGeometry(550, 200, 250, 300)
        self.setFixedSize(250, 300) 

        self.configurar_interfaz()

    def configurar_interfaz(self):
        """Configura la interfaz del inicio de sesión."""        
        layout_principal = QVBoxLayout(self)
        layout_formulario = QVBoxLayout()

    
        self.lbl_logo = QLabel()
        pixmap_logo = QPixmap(":/icons/login1.png") 
        logo_escalado = pixmap_logo.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lbl_logo.setPixmap(logo_escalado)


        self.entrada_usuario = QLineEdit()
        self.entrada_usuario.setPlaceholderText("Nombre de usuario")

        self.entrada_contrasena = QLineEdit()
        self.entrada_contrasena.setEchoMode(QLineEdit.Password)
        self.entrada_contrasena.setPlaceholderText("Contraseña")
        
        self.btn_ingresar = QPushButton("Iniciar sesión")
        
        self.btn_olvide_contraseña = QPushButton("¿Olvidó su contraseña?")
        self.btn_olvide_contraseña.setFlat(True)
        self.btn_olvide_contraseña.setCursor(Qt.PointingHandCursor)
        self.btn_olvide_contraseña.setObjectName("btnOlvido")
        
        layout_formulario.addWidget(self.entrada_usuario)
        layout_formulario.addWidget(self.entrada_contrasena)
        layout_formulario.addWidget(self.btn_ingresar, alignment=Qt.AlignCenter)
        layout_formulario.addWidget(self.btn_olvide_contraseña, alignment=Qt.AlignCenter)
        
        layout_principal.addStretch() 
        layout_principal.addWidget(self.lbl_logo, alignment=Qt.AlignCenter)
        layout_principal.addLayout(layout_formulario)
        layout_principal.addStretch()

        self.setLayout(layout_principal)

    def obtener_credenciales(self):
        """Retorna el usuario y contraseña ingresados."""
        return self.entrada_usuario.text(), self.entrada_contrasena.text()
