from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QComboBox, QListWidget, 
    QFrame, QMessageBox, QCheckBox,QApplication
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


class DialogoPago(QDialog):
    def __init__(self, total_a_pagar, parent=None):
        super().__init__(parent)
        self.total_total = total_a_pagar
        self.saldo_restante = total_a_pagar
        self.pagos_realizados = []

        self.setWindowTitle("Finalizar Venta")
        self.setFixedSize(450, 550)
        self.setObjectName("VentanaPago") 
        self.configurar_interfaz()

    def configurar_interfaz(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setSpacing(15)

        resumen = QFrame()
        resumen.setObjectName("ContenedorResumen")
        layout_resumen = QVBoxLayout(resumen)

        self.lbl_total = QLabel(f"TOTAL: ${self.total_total:,.2f}")
        self.lbl_total.setObjectName("LabelTotal")
        
        self.lbl_restante = QLabel(f"Pendiente: ${self.saldo_restante:,.2f}")
        self.lbl_restante.setObjectName("LabelRestante")

        layout_resumen.addWidget(self.lbl_total, alignment=Qt.AlignCenter)
        layout_resumen.addWidget(self.lbl_restante, alignment=Qt.AlignCenter)
        layout_principal.addWidget(resumen)

        seccion_entrada = QHBoxLayout()
        
        self.combo_medio_pago = QComboBox()
        self.combo_medio_pago.setObjectName("ComboMedioPago")
        self.combo_medio_pago.addItems(["Efectivo", "Tarjeta", "Transferencia"])
        
        self.entrada_monto = QLineEdit()
        self.entrada_monto.setPlaceholderText("0.00")
        self.entrada_monto.setObjectName("EntradaMonto")
        
        self.btn_agregar = QPushButton("Añadir")
        self.btn_agregar.setObjectName("BtnAnadir")
        self.btn_agregar.clicked.connect(self.agregar_abono)

        seccion_entrada.addWidget(self.combo_medio_pago, 2)
        seccion_entrada.addWidget(self.entrada_monto, 2)
        seccion_entrada.addWidget(self.btn_agregar, 1)
        layout_principal.addLayout(seccion_entrada)


        layout_lista = QVBoxLayout()
        cabecera_lista = QHBoxLayout()
        cabecera_lista.addWidget(QLabel("Desglose de pagos:"))
        
        self.btn_limpiar = QPushButton("Limpiar Todo")
        self.btn_limpiar.setObjectName("BtnLimpiar")
        self.btn_limpiar.clicked.connect(self.reiniciar_pagos)
        cabecera_lista.addWidget(self.btn_limpiar, alignment=Qt.AlignRight)
        
        layout_lista.addLayout(cabecera_lista)
        
        self.lista_pagos_ui = QListWidget()
        self.lista_pagos_ui.setObjectName("ListaPagos")
        layout_lista.addWidget(self.lista_pagos_ui)
        layout_principal.addLayout(layout_lista)

        layout_inferior = QHBoxLayout()
        
        self.check_imprimir = QCheckBox("Imprimir Comprobante")
        self.check_imprimir.setChecked(True)
        self.check_imprimir.setObjectName("CheckFactura")
        
        self.lbl_vuelto = QLabel("Vuelto: $0.00")
        self.lbl_vuelto.setObjectName("LabelVuelto")
        
        layout_inferior.addWidget(self.check_imprimir)
        layout_inferior.addStretch()
        layout_inferior.addWidget(self.lbl_vuelto)
        layout_principal.addLayout(layout_inferior)

        botones_finales = QHBoxLayout()
        self.btn_cancelar = QPushButton("Volver")
        self.btn_cancelar.setObjectName("BtnCancelar")
        self.btn_cancelar.clicked.connect(self.reject)
        
        self.btn_confirmar = QPushButton("CONFIRMAR Y CERRAR")
        self.btn_confirmar.setObjectName("BtnConfirmar")
        self.btn_confirmar.setEnabled(False)
        self.btn_confirmar.clicked.connect(self.accept)

        botones_finales.addWidget(self.btn_cancelar)
        botones_finales.addWidget(self.btn_confirmar)
        layout_principal.addLayout(botones_finales)


    def agregar_abono(self):
        try:
            monto = float(self.entrada_monto.text())
            metodo = self.combo_medio_pago.currentText()
            
            if monto <= 0: return

            if metodo != "Efectivo" and monto > self.saldo_restante:
                QMessageBox.warning(self, "Monto Excedido", "Este medio de pago no permite exceder el saldo.")
                return

            self.pagos_realizados.append({"metodo": metodo, "monto": monto})
            self.lista_pagos_ui.addItem(f"{metodo}: ${monto:,.2f}")
            
            if metodo == "Efectivo" and monto > self.saldo_restante:
                vuelto = monto - self.saldo_restante
                self.lbl_vuelto.setText(f"Vuelto: ${vuelto:,.2f}")
                self.saldo_restante = 0
            else:
                self.saldo_restante -= monto
            
            if self.saldo_restante < 0: self.saldo_restante = 0
            
            self.lbl_restante.setText(f"Pendiente: ${self.saldo_restante:,.2f}")
            self.entrada_monto.clear()

            if self.saldo_restante <= 0:
                self.btn_confirmar.setEnabled(True)
                self.btn_agregar.setEnabled(False)

        except ValueError:
            QMessageBox.critical(self, "Error", "Ingrese un monto numérico.")

    def reiniciar_pagos(self):
        """Limpia todos los pagos y resetea el diálogo."""
        self.pagos_realizados = []
        self.lista_pagos_ui.clear()
        self.saldo_restante = self.total_total
        self.lbl_restante.setText(f"Pendiente: ${self.saldo_restante:,.2f}")
        self.lbl_vuelto.setText("Vuelto: $0.00")
        self.btn_confirmar.setEnabled(False)
        self.btn_agregar.setEnabled(True)
        self.entrada_monto.clear()


