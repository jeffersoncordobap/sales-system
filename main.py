import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QFile, QTextStream

from database.connection import DatabaseConnection
from controllers.login_controller import LoginController
from services.inventory_service import InventoryService
from repositories.product_repository import ProductRepository


def get_style():
    """Lee el archivo QSS desde el sistema de recursos de Qt."""
    file = QFile(":/styles/styles.qss")
    if file.open(QFile.ReadOnly | QFile.Text):
        flow = QTextStream(file)
        return flow.readAll()
    return ""

def main():
    db = DatabaseConnection()
    try:
        db.initialize_db()
        conn = db.connect_database()
    except Exception as e:
        print(f"Error crítico al iniciar la base de datos: {e}")
        return 


    product_repository = ProductRepository(conn)
    services = {"inventario": InventoryService(product_repository)}


    app = QApplication(sys.argv)
    style = get_style()
    if style:
        app.setStyleSheet(style)

    controlador = LoginController(services)
    controlador.show_login()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    