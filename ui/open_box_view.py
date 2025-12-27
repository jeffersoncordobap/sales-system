from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QMessageBox
)
from PySide6.QtCore import Qt, QDateTime

class DialogoAperturaCaja(QDialog):
    def __init__(self, nombre_cajero, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Apertura de Turno")
        self.setFixedSize(350, 400)
        self.nombre_cajero = nombre_cajero
        self.setObjectName("DialogoApertura") # ID para el QSS
        self.configurar_interfaz()

    def configurar_interfaz(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        self.cabecera = QFrame()
        self.cabecera.setObjectName("CabeceraApertura")
        layout_cabecera = QVBoxLayout(self.cabecera)
        
        lbl_titulo = QLabel("APERTURA DE CAJA")
        lbl_titulo.setObjectName("TituloApertura")
        lbl_titulo.setAlignment(Qt.AlignCenter)
        
        self.lbl_fecha = QLabel(f"Fecha: {QDateTime.currentDateTime().toString('dd/MM/yyyy HH:mm')}")
        self.lbl_fecha.setObjectName("InfoApertura")
        
        lbl_usuario = QLabel(f"Cajero: {self.nombre_cajero}")
        lbl_usuario.setObjectName("InfoApertura")

        layout_cabecera.addWidget(lbl_titulo)
        layout_cabecera.setSpacing(20)
        layout_cabecera.addWidget(self.lbl_fecha)
        layout_cabecera.setSpacing(10)
        layout_cabecera.addWidget(lbl_usuario)
        layout.addWidget(self.cabecera)


        layout_monto = QVBoxLayout()
        lbl_instruccion = QLabel("Ingrese el monto inicial en caja (Base):")
        lbl_instruccion.setObjectName("EtiquetaInstruccion")
        
        self.entrada_monto = QLineEdit()
        self.entrada_monto.setObjectName("EntradaMontoApertura")
        self.entrada_monto.setPlaceholderText("0.00")
        self.entrada_monto.setAlignment(Qt.AlignCenter)
        
        layout_monto.addWidget(lbl_instruccion,alignment=Qt.AlignCenter)
        layout_monto.addWidget(self.entrada_monto)
        layout.addLayout(layout_monto)

        layout.addStretch()


        self.btn_confirmar = QPushButton("INICIAR TURNO")
        self.btn_confirmar.setObjectName("BtnConfirmarApertura")
        self.btn_confirmar.clicked.connect(self.validar_y_aceptar)
        layout.addWidget(self.btn_confirmar)

    def validar_y_aceptar(self):
        try:
            monto = float(self.entrada_monto.text())
            if monto < 0: raise ValueError
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un monto válido.")

    def obtener_monto_inicial(self):
        return float(self.entrada_monto.text() or 0)