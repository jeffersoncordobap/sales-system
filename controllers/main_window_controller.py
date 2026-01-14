from ui.main_window_view import MainWindowView
from controllers.inventory_controller import InventoryController


class MainWindowController:
    def __init__(self,services):
        self.services = services
        self.main_window_view = MainWindowView()
        self._main_window_navigation()
        self.main_window_view.btn_inventory.clicked.connect(self.inicializar_inventario)
        
        self.inventory_controller = InventoryController(
                self.main_window_view.inventory_view, 
                self.services['inventario']
            )

    def _main_window_navigation(self):
        view = self.main_window_view
        view.btn_sales.clicked.connect(lambda: view.content_area.setCurrentIndex(0))
        view.btn_expenses.clicked.connect(lambda: view.content_area.setCurrentIndex(1))
        view.btn_returns.clicked.connect(lambda: view.content_area.setCurrentIndex(2))
        view.btn_reports.clicked.connect(lambda: view.content_area.setCurrentIndex(3))
        view.btn_inventory.clicked.connect(lambda: view.content_area.setCurrentIndex(4))
        view.btn_dashboard.clicked.connect(lambda: view.content_area.setCurrentIndex(5))
        view.btn_configuration.clicked.connect(lambda: view.content_area.setCurrentIndex(6))

    def show_main_window(self):
        self.main_window_view.show()
        
    def inicializar_inventario(self):
        self.inventory_controller.update_inventory()