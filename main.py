import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QTextStream
from controllers.login_controller import ControladorLogin

def obtener_estilo():
    """Lee el archivo QSS desde el sistema de recursos de Qt."""
    archivo = QFile(":/styles/styles.qss")
    if archivo.open(QFile.ReadOnly | QFile.Text):
        flujo = QTextStream(archivo)
        return flujo.readAll()
    return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    estilo = obtener_estilo()
    app.setStyleSheet(estilo)

    controlador = ControladorLogin()
    controlador.mostrar_login()
    
    sys.exit(app.exec())
    