from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QFrame, QTextEdit, QMessageBox, QCheckBox
)
from PySide6.QtCore import Qt, QDateTime

class DialogoCierreCaja(QDialog):
    def __init__(self, monto_esperado, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cierre de Caja / Arqueo")
        self.setFixedSize(400, 550)
        self.monto_esperado = monto_esperado
        self.setObjectName("DialogoCierre")
        self.configurar_interfaz()

    def configurar_interfaz(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        self.cabecera = QFrame()
        self.cabecera.setObjectName("CabeceraCierre")
        layout_cabecera = QVBoxLayout(self.cabecera)

        lbl_titulo = QLabel("RESUMEN DE CAJA (SISTEMA)")
        lbl_titulo.setObjectName("TituloCierre")
        lbl_titulo.setAlignment(Qt.AlignCenter)

        self.lbl_fecha = QLabel(f"Fecha Cierre: {QDateTime.currentDateTime().toString('dd/MM/yyyy HH:mm')}")
        self.lbl_fecha.setObjectName("InfoCierre")

        self.lbl_esperado = QLabel(f"Efectivo Esperado: ${self.monto_esperado:,.2f}")
        self.lbl_esperado.setObjectName("MontoEsperado")

        layout_cabecera.addWidget(lbl_titulo)
        layout_cabecera.addWidget(self.lbl_fecha)
        layout_cabecera.addWidget(self.lbl_esperado)
        layout.addWidget(self.cabecera)

        layout_entrada = QVBoxLayout()
        layout_entrada.addWidget(QLabel("Monto Contado en Físico:"))
        
        self.entrada_declarado = QLineEdit()
        self.entrada_declarado.setObjectName("EntradaDeclarado")
        self.entrada_declarado.setPlaceholderText("Ingrese el total contado")
        self.entrada_declarado.textChanged.connect(self.calcular_diferencia)
        layout_entrada.addWidget(self.entrada_declarado)
        layout.addLayout(layout_entrada)

        self.frame_dif = QFrame()
        self.frame_dif.setObjectName("FrameDiferencia")
        layout_dif = QHBoxLayout(self.frame_dif)
        
        layout_dif.addWidget(QLabel("Diferencia:"))
        self.lbl_diferencia = QLabel("$0.00")
        self.lbl_diferencia.setObjectName("LabelDiferencia")
        layout_dif.addWidget(self.lbl_diferencia, alignment=Qt.AlignRight)
        layout.addWidget(self.frame_dif)

        layout.addWidget(QLabel("Observaciones / Justificación:"))
        self.txt_observaciones = QTextEdit()
        self.txt_observaciones.setObjectName("TxtObservaciones")
        self.txt_observaciones.setPlaceholderText("Opcional: explique aquí cualquier descuadre...")
        layout.addWidget(self.txt_observaciones)
        
        self.check_exportar = QCheckBox("Exportar reporte del dia")
        self.check_exportar.setChecked(True)
        self.check_exportar.setObjectName("CheckExportar")
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
            diferencia = declarado - self.monto_esperado
            self.lbl_diferencia.setText(f"${diferencia:,.2f}")
            
            # Feedback visual de la diferencia
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
        return {
            "esperado": self.monto_esperado,
            "declarado": float(self.entrada_declarado.text() or 0),
            "observaciones": self.txt_observaciones.toPlainText()
        }