import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QFile, QTextStream

from database.connection import ConexionDB
from controllers.login_controller import ControladorLogin
from services.inventory_service import ServicioInventario
from repositories.product_repository import RepositorioProducto


def obtener_estilo():
    """Lee el archivo QSS desde el sistema de recursos de Qt."""
    archivo = QFile(":/styles/styles.qss")
    if archivo.open(QFile.ReadOnly | QFile.Text):
        flujo = QTextStream(archivo)
        return flujo.readAll()
    return ""

def main():
    db = ConexionDB()
    try:
        db.inicializar_db()
        conexion = db.conectar()
    except Exception as e:
        print(f"Error crítico al iniciar la base de datos: {e}")
        return 


    repo_producto = RepositorioProducto(conexion)
    servicios = {"inventario": ServicioInventario(repo_producto)}


    app = QApplication(sys.argv)
    estilo = obtener_estilo()
    if estilo:
        app.setStyleSheet(estilo)

    controlador = ControladorLogin(servicios)
    controlador.mostrar_login()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    