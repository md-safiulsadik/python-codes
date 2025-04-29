
import sys
import json
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator


class ExpenseCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.current_month = datetime.now().strftime("%B %Y")
        self.expenses = self.load_expenses()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Expense Calculator')

        # Global styles
        self.setStyleSheet("""
            QWidget {
                font-family: 'Arial', sans-serif;
                font-size: 22px;
                background-color: #eef3f8;
            }
            QLabel {
                font-weight: bold;
                color: #2c3e50;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                padding: 8px;
                border-radius: 6px;
                font-size: 22px;
            }
            QPushButton {
                background-color: #1abc9c;
                color: #ffffff;
                padding: 10px 15px;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #16a085;
            }
            QPushButton:disabled {
                background-color: #bdc3c7;
            }
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #ccc;
                gridline-color: #dfe6e9;
                border-radius: 6px;
                font-size: 22px;
            }
            QHeaderView::section {
                background-color: #2980b9;
                color: #ffffff;
                padding: 5px;
                border: none;
                font-size: 22px;
            }
        """)

        layout = QVBoxLayout()

        # Month-Year Selector
        self.month_selector = QComboBox()
        self.month_selector.addItems(sorted(self.expenses.keys()))
        self.month_selector.setCurrentText(self.current_month)
        self.month_selector.currentTextChanged.connect(self.switch_month)
        layout.addWidget(self.month_selector)

        # Form layout
        form_layout = QFormLayout()
        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("Enter item name")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount or expression (e.g., 23 + 40)")

        form_layout.addRow(QLabel('Item'), self.item_input)
        form_layout.addRow(QLabel('Amount (BDT)'), self.amount_input)
        layout.addLayout(form_layout)

        # Add expense button
        add_button = QPushButton('                                  Add Expense                                 ')
        add_button.clicked.connect(self.add_expense)
        layout.addWidget(add_button)

        # Table widget
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Item', 'Amount (BDT)'])
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        self.table_widget.horizontalHeaderItem(1).setTextAlignment(Qt.AlignCenter)
        layout.addWidget(self.table_widget)

        # Action buttons
        edit_button = QPushButton('Edit Selected')
        edit_button.clicked.connect(self.edit_expense)
        layout.addWidget(edit_button)

        delete_button = QPushButton('Delete Selected')
        delete_button.clicked.connect(self.delete_expense)
        layout.addWidget(delete_button)

        total_button = QPushButton('Calculate Total')
        total_button.clicked.connect(self.calculate_total)
        layout.addWidget(total_button)

        new_month_button = QPushButton('Add New Month')
        new_month_button.clicked.connect(lambda: self.add_month(1))
        layout.addWidget(new_month_button)

        previous_month_button = QPushButton('Add Previous Month')
        previous_month_button.clicked.connect(lambda: self.add_month(-1))
        layout.addWidget(previous_month_button)

        self.setLayout(layout)
        self.update_table()
        self.adjustSize()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ValueError("Invalid file format")
        except (FileNotFoundError, ValueError):
            data = {}

        if self.current_month not in data:
            data[self.current_month] = []
        return data

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        item = self.item_input.text().strip()
        amount_text = self.amount_input.text().strip()

        if not item or not amount_text:
            QMessageBox.warning(self, 'Input Error', 'Both fields are required.')
            return

        try:
            amount = eval(amount_text, {"__builtins__": None}, {})
            if not isinstance(amount, (int, float)):
                raise ValueError
            self.expenses[self.current_month].append({'item': item, 'amount': amount})
            self.save_expenses()
            self.update_table()
            self.item_input.clear()
            self.amount_input.clear()
        except (ValueError, SyntaxError):
            QMessageBox.critical(self, 'Error', 'Please enter a valid numerical amount or expression.')

    def update_table(self):
        self.table_widget.setRowCount(len(self.expenses[self.current_month]))
        for i, expense in enumerate(self.expenses[self.current_month]):
            item = QTableWidgetItem(expense['item'])
            item.setTextAlignment(Qt.AlignCenter)
            amount = QTableWidgetItem(f"{expense['amount']:.2f}")
            amount.setTextAlignment(Qt.AlignCenter)
            self.table_widget.setItem(i, 0, item)
            self.table_widget.setItem(i, 1, amount)

    def delete_expense(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()
        if selected_rows:
            rows_to_delete = sorted([index.row() for index in selected_rows], reverse=True)
            for row in rows_to_delete:
                self.expenses[self.current_month].pop(row)
            self.save_expenses()
            self.update_table()
        else:
            QMessageBox.warning(self, 'Selection Error', 'Please select at least one expense to delete.')

    def calculate_total(self):
        total = sum(expense['amount'] for expense in self.expenses[self.current_month])
        QMessageBox.information(self, 'Total Expenses', f'Total Expenses: BDT {total:.2f}')

    def add_month(self, offset):
        current_date = datetime.strptime(self.current_month, "%B %Y")
        year = current_date.year
        month = current_date.month + offset

        if month > 12:
            month -= 12
            year += 1
        elif month < 1:
            month += 12
            year -= 1

        new_month = datetime(year, month, 1).strftime("%B %Y")

        if new_month in self.expenses:
            QMessageBox.warning(self, 'Error', f'{new_month} already exists.')
        else:
            self.expenses[new_month] = []
            self.save_expenses()
            self.month_selector.addItem(new_month)
            self.month_selector.setCurrentText(new_month)

    def switch_month(self, month):
        self.current_month = month
        self.update_table()

    def edit_expense(self):
        selected_rows = self.table_widget.selectionModel().selectedRows()
        if len(selected_rows) != 1:
            QMessageBox.warning(self, 'Selection Error', 'Please select one expense to edit.')
            return

        row = selected_rows[0].row()
        expense = self.expenses[self.current_month][row]

        # Populate fields for editing
        self.item_input.setText(expense['item'])
        self.amount_input.setText(str(expense['amount']))

        # Remove the item being edited
        self.expenses[self.current_month].pop(row)
        self.save_expenses()
        self.update_table()

        QMessageBox.information(self, 'Edit Expense', 'Make your changes and press "Add Expense" to save edits.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ExpenseCalculator()
    calculator.show()
    sys.exit(app.exec_())