from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QComboBox, QTextEdit, QPushButton, QFrame, QTableWidget, QHeaderView
)
from PySide6.QtCore import Qt, QDate

class ExpensesView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ExpensesView")
        self.main_layout = QHBoxLayout(self) 
        self.main_layout.setSpacing(20)

        self.create_form()
        self.create_daily_history()

    def create_form(self):
        """Sección izquierda: Formulario de Registro"""
        self.container_form = QFrame()
        self.container_form.setObjectName("container_form_expense")
        self.container_form.setFixedWidth(350)
        
        layout = QVBoxLayout(self.container_form)
        layout.setSpacing(15)

        expense_title = QLabel("REGISTRAR GASTO / EGRESO")
        expense_title.setObjectName("expense_title")
        layout.addWidget(expense_title)

        # Categoría
        layout.addWidget(QLabel("Categoría:"))
        self.combo_category = QComboBox()
        self.combo_category.addItems([
            "Insumos (Bolsas, Pegante, etc.)",
            "Servicios Públicos",
            "Pago de Turnos / Nómina",
            "Mantenimiento",
            "Compras a Proveedores",
            "Otros"
        ])
        layout.addWidget(self.combo_category)

        # Monto
        layout.addWidget(QLabel("Monto del Gasto ($):"))
        self.input_amount_of_expenditure = QLineEdit()
        self.input_amount_of_expenditure.setPlaceholderText("0.00")
        self.input_amount_of_expenditure.setObjectName("input_amount_of_expenditure")
        layout.addWidget(self.input_amount_of_expenditure)

        # Método de Pago (Fundamental para la contadora)
        layout.addWidget(QLabel("Pagado desde:"))
        self.combo_payment_method = QComboBox()
        self.combo_payment_method.addItems(["Caja Principal (Efectivo)", "Tarjeta","Transferencia", "Otro"])
        layout.addWidget(self.combo_payment_method)

        # Descripción
        layout.addWidget(QLabel("Descripción / Concepto:"))
        self.txt_description_of_the_expense = QTextEdit()
        self.txt_description_of_the_expense.setPlaceholderText("Ej: Compra de 100 bolsas medianas...")
        self.txt_description_of_the_expense.setMaximumHeight(100)
        layout.addWidget(self.txt_description_of_the_expense)

        layout.addStretch()

        # Botón
        self.btn_save_spent = QPushButton("GUARDAR GASTO")
        self.btn_save_spent.setObjectName("btn_save_spent")
        self.btn_save_spent.setMinimumHeight(45)
        layout.addWidget(self.btn_save_spent)

        self.main_layout.addWidget(self.container_form)

    def create_daily_history(self):
        """Sección derecha: Lista de gastos del día"""
        container_list = QFrame()
        layout = QVBoxLayout(container_list)

        lbl_spending_history = QLabel("Gastos Registrados Hoy")
        lbl_spending_history.setObjectName("lbl_spending_history")
        layout.addWidget(lbl_spending_history)

        self.table_today_expenses = QTableWidget()
        self.table_today_expenses.setColumnCount(4)
        self.table_today_expenses.setHorizontalHeaderLabels(["Hora", "Categoría", "Descripción", "Monto"])
        self.table_today_expenses.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        layout.addWidget(self.table_today_expenses)
        self.main_layout.addWidget(container_list)