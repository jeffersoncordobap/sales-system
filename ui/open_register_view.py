from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QMessageBox
)
from PySide6.QtCore import Qt, QDateTime

class OpenRegisterDialog(QDialog):
    def __init__(self, cashier_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Apertura de Turno")
        self.setFixedSize(350, 400)
        self.cashier_name = cashier_name
        self.setObjectName("OpenBoxDialog") 
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        self.header_open_register = QFrame()
        self.header_open_register.setObjectName("header_open_register")
        header_layout = QVBoxLayout(self.header_open_register)
        
        lbl_title_open_register = QLabel("APERTURA DE CAJA")
        lbl_title_open_register.setObjectName("lbl_title_open_register")
        lbl_title_open_register.setAlignment(Qt.AlignCenter)
        
        self.lbl_date = QLabel(f"Fecha: {QDateTime.currentDateTime().toString('dd/MM/yyyy HH:mm')}")
        self.lbl_date.setObjectName("lbl_opening_information")
        
        lbl_user = QLabel(f"Cajero: {self.cashier_name}")
        lbl_user.setObjectName("lbl_opening_information")

        header_layout.addWidget(lbl_title_open_register)
        header_layout.setSpacing(20)
        header_layout.addWidget(self.lbl_date)
        header_layout.setSpacing(10)
        header_layout.addWidget(lbl_user)
        layout.addWidget(self.header_open_register)


        amount_layout = QVBoxLayout()
        lbl_instruction = QLabel("Ingrese el monto inicial en caja (Base):")
        lbl_instruction.setObjectName("lbl_instruction_open_register")
        
        self.input_initial_amount = QLineEdit()
        self.input_initial_amount.setObjectName("input_initial_amount")
        self.input_initial_amount.setPlaceholderText("0.00")
        self.input_initial_amount.setAlignment(Qt.AlignCenter)
        
        amount_layout.addWidget(lbl_instruction,alignment=Qt.AlignCenter)
        amount_layout.addWidget(self.input_initial_amount)
        layout.addLayout(amount_layout)
        layout.addStretch()

        self.btn_confirm = QPushButton("INICIAR TURNO")
        self.btn_confirm.setObjectName("btn_confirm_open_register")
        self.btn_confirm.clicked.connect(self.validate_and_accept)
        layout.addWidget(self.btn_confirm)

    def validate_and_accept(self):
        try:
            monto = float(self.input_initial_amount.text())
            if monto < 0: raise ValueError
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingrese un monto válido.")

    def get_initial_amount(self):
        return float(self.input_initial_amount.text() or 0)

