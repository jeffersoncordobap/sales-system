from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QTextEdit, QMessageBox, QCheckBox
)
from PySide6.QtCore import Qt, QDateTime

class CloseBoxDialog(QDialog):
    def __init__(self, monto_efectivo_esperado, monto_tranferencia, monto_tarjeta, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cierre de Caja / Arqueo")
        self.setFixedSize(430, 630) 
        self.monto_efectivo_esperado = monto_efectivo_esperado
        self.monto_tranferencia = monto_tranferencia
        self.monto_tarjeta = monto_tarjeta
        self.venta_total_sistema = monto_efectivo_esperado + monto_tranferencia + monto_tarjeta
        
        self.setObjectName("DialogoCierre")
        self.configurar_interfaz()

    def configurar_interfaz(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        self.cabecera = QFrame()
        self.cabecera.setObjectName("CabeceraCierre")
        layout_cabecera = QVBoxLayout(self.cabecera)

        lbl_titulo = QLabel("RESUMEN DE VENTAS (SISTEMA)")
        lbl_titulo.setObjectName("TituloCierre")
        lbl_titulo.setAlignment(Qt.AlignCenter)
        layout_cabecera.addWidget(lbl_titulo)

        self.frame_digital = QFrame()
        self.frame_digital.setObjectName("FrameDigital")
        layout_digital = QHBoxLayout(self.frame_digital)
        
        info_digital = (f"💳 Tarjeta: **${self.monto_tarjeta:,.2f}** |   "
                        f"📲 Transf: **${self.monto_tranferencia:,.2f}**")
        lbl_digital = QLabel(info_digital)
        lbl_digital.setAlignment(Qt.AlignCenter)
        layout_digital.addWidget(lbl_digital)
        layout_cabecera.addWidget(self.frame_digital)

        self.lbl_efectivo_esperado = QLabel(f"💵 Efectivo Esperado: ${self.monto_efectivo_esperado:,.2f}")
        self.lbl_efectivo_esperado.setObjectName("MontoEsperadoPrincipal")
        
        self.lbl_total_general = QLabel(f"💰 VENTA TOTAL DÍA: ${self.venta_total_sistema:,.2f}")
        self.lbl_total_general.setObjectName("MontoTotalGeneral")
        self.lbl_total_general.setAlignment(Qt.AlignCenter)

        layout_cabecera.addWidget(self.lbl_efectivo_esperado)
        layout_cabecera.addWidget(self.lbl_total_general)
        layout.addWidget(self.cabecera)

        layout_arqueo = QVBoxLayout()
        lbl_instruccion = QLabel("CONTEO FÍSICO DE EFECTIVO:")
        lbl_instruccion.setStyleSheet("font-weight: bold; color: #7f8c8d;")
        layout_arqueo.addWidget(lbl_instruccion)

        self.entrada_declarado = QLineEdit()
        self.entrada_declarado.setObjectName("EntradaDeclarado")
        self.entrada_declarado.setPlaceholderText("0.00")
        self.entrada_declarado.setAlignment(Qt.AlignCenter)
        self.entrada_declarado.textChanged.connect(self.calcular_diferencia)
        layout_arqueo.addWidget(self.entrada_declarado)
        layout.addLayout(layout_arqueo)

        self.frame_dif = QFrame()
        self.frame_dif.setObjectName("FrameDiferencia")
        layout_dif = QHBoxLayout(self.frame_dif)
        layout_dif.addWidget(QLabel("Diferencia en Caja:"))
        self.lbl_diferencia = QLabel("$0.00")
        self.lbl_diferencia.setObjectName("LabelDiferencia")
        layout_dif.addWidget(self.lbl_diferencia, alignment=Qt.AlignRight)
        layout.addWidget(self.frame_dif)

    
        layout.addWidget(QLabel("Notas del cierre:"))
        self.txt_observaciones = QTextEdit()
        self.txt_observaciones.setPlaceholderText("Opcional: explique aquí cualquier descuadre...")
        self.txt_observaciones.setMaximumHeight(80)
        layout.addWidget(self.txt_observaciones)

        self.check_exportar = QCheckBox("Generar reporte PDF al finalizar")
        self.check_exportar.setChecked(True)
        layout.addWidget(self.check_exportar)


        botones = QHBoxLayout()
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_finalizar = QPushButton("FINALIZAR CIERRE")
        self.btn_finalizar.setObjectName("BtnFinalizarCierre")
        self.btn_finalizar.clicked.connect(self.confirmar_cierre)
        
        botones.addWidget(self.btn_cancelar)
        botones.addWidget(self.btn_finalizar)
        layout.addLayout(botones)

    def calcular_diferencia(self):
        try:
            declarado = float(self.entrada_declarado.text() or 0)
            diferencia = declarado - self.monto_efectivo_esperado
            self.lbl_diferencia.setText(f"${diferencia:,.2f}")
            
            if diferencia < 0:
                self.lbl_diferencia.setStyleSheet("color: #e74c3c; font-weight: bold;") # Rojo
            elif diferencia > 0:
                self.lbl_diferencia.setStyleSheet("color: #f39c12; font-weight: bold;") # Naranja (sobrante)
            else:
                self.lbl_diferencia.setStyleSheet("color: #27ae60; font-weight: bold;") # Verde (exacto)
        except ValueError:
            pass

    def confirmar_cierre(self):
        if not self.entrada_declarado.text():
            QMessageBox.warning(self, "Atención", "Debe ingresar el monto contado.")
            return
        self.accept()

    def obtener_datos_cierre(self):
        """Devuelve todos los montos para guardarlos en la BD"""
        return {
            "efectivo_esperado": self.monto_efectivo_esperado,
            "efectivo_declarado": float(self.entrada_declarado.text() or 0),
            "transferencias": self.monto_tranferencia,
            "tarjetas": self.monto_tarjeta,
            "total_sistema": self.venta_total_sistema,
            "observaciones": self.txt_observaciones.toPlainText(),
            "exportar": self.check_exportar.isChecked()
        }