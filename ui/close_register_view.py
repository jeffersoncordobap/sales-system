from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QTextEdit, QMessageBox, QCheckBox
)
from PySide6.QtCore import Qt, QDateTime

class CloseRegisterDialog(QDialog):
    def __init__(self, expected_cash_amount, amount_per_transfer, amount_per_card, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cierre de Caja / Arqueo")
        self.setFixedSize(430, 630) 
        self.expected_cash_amount = expected_cash_amount
        self.amount_per_transfer = amount_per_transfer
        self.amount_per_card = amount_per_card
        self.total_sales = expected_cash_amount + amount_per_transfer + amount_per_card

        self.setObjectName("CloseRegisterDialog")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        self.header = QFrame()
        self.header.setObjectName("frame_header_close_register")
        header_layout = QVBoxLayout(self.header)

        lbl_title = QLabel("RESUMEN DE VENTAS (SISTEMA)")
        lbl_title.setObjectName("lbl_title_summary_close_register")
        lbl_title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(lbl_title)

        self.frame_card_and_transfer = QFrame()
        self.frame_card_and_transfer.setObjectName("frame_card_and_transfer")
        card_and_transfer_layout = QHBoxLayout(self.frame_card_and_transfer)
        
        info_card_and_transfer = (f"💳 Tarjeta: **${self.amount_per_card:,.2f}** |  "
                        f"📲 Transf: **${self.amount_per_transfer:,.2f}**")
        lbl_info_card_and_transfer = QLabel(info_card_and_transfer)
        lbl_info_card_and_transfer.setObjectName("lbl_info_card_and_transfer")
        lbl_info_card_and_transfer.setAlignment(Qt.AlignCenter)
        card_and_transfer_layout.addWidget(lbl_info_card_and_transfer)
        header_layout.addWidget(self.frame_card_and_transfer)

        self.lbl_expected_cash = QLabel(f"💵 Efectivo Esperado: ${self.expected_cash_amount:,.2f}")
        self.lbl_expected_cash.setObjectName("lbl_expected_cash")
        
        self.lbl_general_total = QLabel(f"💰 VENTA TOTAL DÍA: ${self.total_sales:,.2f}")
        self.lbl_general_total.setObjectName("lbl_general_total")
        self.lbl_general_total.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(self.lbl_expected_cash)
        header_layout.addWidget(self.lbl_general_total)
        layout.addWidget(self.header)

        cash_count_layout = QVBoxLayout()
        lbl_instruction = QLabel("CONTEO FÍSICO DE EFECTIVO:")
        lbl_instruction.setStyleSheet("font-weight: bold; color: #7f8c8d;")
        cash_count_layout.addWidget(lbl_instruction)

        self.input_cash_counted = QLineEdit()
        self.input_cash_counted.setObjectName("input_cash_counted")
        self.input_cash_counted.setPlaceholderText("0.00")
        self.input_cash_counted.setAlignment(Qt.AlignCenter)
        self.input_cash_counted.textChanged.connect(self.calculate_difference)
        cash_count_layout.addWidget(self.input_cash_counted)
        layout.addLayout(cash_count_layout)

        self.frame_difference = QFrame()
        self.frame_difference.setObjectName("frame_difference_close_register")
        layout_dif = QHBoxLayout(self.frame_difference)
        layout_dif.addWidget(QLabel("Diferencia en Caja:"))
        self.lbl_difference_close_register = QLabel("$0.00")
        self.lbl_difference_close_register.setObjectName("lbl_difference_close_register")
        layout_dif.addWidget(self.lbl_difference_close_register, alignment=Qt.AlignRight)
        layout.addWidget(self.frame_difference)

    
        layout.addWidget(QLabel("Notas del cierre:"))
        self.text_observations = QTextEdit()
        self.text_observations.setObjectName("text_observations_close_register")    
        self.text_observations.setPlaceholderText("Opcional: explique aquí cualquier descuadre...")
        self.text_observations.setMaximumHeight(80)
        layout.addWidget(self.text_observations)

        self.check_export = QCheckBox("Generar reporte PDF al finalizar")
        self.check_export.setObjectName("check_export_report_close_register")
        self.check_export.setChecked(True)
        layout.addWidget(self.check_export)


        buttons = QHBoxLayout()
        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.clicked.connect(self.reject)
        self.btn_finish = QPushButton("FINALIZAR CIERRE")
        self.btn_finish.setObjectName("btn_finish_close_register")
        self.btn_finish.clicked.connect(self.confirm_cash_register_closing)
        
        buttons.addWidget(self.btn_cancel)
        buttons.addWidget(self.btn_finish)
        layout.addLayout(buttons)

    def calculate_difference(self):
        try:
            cash_couented = float(self.input_cash_counted.text() or 0)
            difference = cash_couented - self.expected_cash_amount
            self.lbl_difference_close_register.setText(f"${difference:,.2f}")
            
            if difference < 0:
                self.lbl_difference_close_register.setStyleSheet("color: #e74c3c; font-weight: bold;") # Rojo
            elif difference > 0:
                self.lbl_difference_close_register.setStyleSheet("color: #f39c12; font-weight: bold;") # Naranja (sobrante)
            else:
                self.lbl_difference_close_register.setStyleSheet("color: #27ae60; font-weight: bold;") # Verde (exacto)
        except ValueError:
            pass

    def confirm_cash_register_closing(self):
        if not self.input_cash_counted.text():
            QMessageBox.warning(self, "Atención", "Debe ingresar el monto contado.")
            return
        self.accept()


    def get_closing_data(self):
        """Devuelve todos los montos para guardarlos en la BD"""
        return {
            "efectivo_esperado": self.expected_cash_amount,
            "efectivo_declarado": float(self.input_cash_counted.text() or 0),
            "transferencias": self.amount_per_transfer,
            "tarjetas": self.amount_per_card,
            "total_sistema": self.total_sales,
            "observaciones": self.text_observations.toPlainText(),
            "exportar": self.check_export.isChecked()
        }