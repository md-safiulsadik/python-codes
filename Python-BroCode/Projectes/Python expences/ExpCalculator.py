import sys
import json
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/drive.file']

class ExpenseCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.current_month = datetime.now().strftime("%B %Y")
        self.expenses = {}
        self.service = None  # Google Drive service instance
        self.file_id = None  # Google Drive file ID for expenses.json
        self.init_google_drive()
        self.load_expenses()
        self.initUI()

    def init_google_drive(self):
        """Authenticate with Google and initialize Drive API service."""
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)

        # Check if expenses.json already exists on Drive
        query = "name='expenses.json' and trashed=false"
        results = self.service.files().list(q=query, fields="files(id)").execute()
        files = results.get('files', [])
        if files:
            self.file_id = files[0]['id']
        else:
            self.file_id = self.create_drive_file()

    def create_drive_file(self):
        """Create a new expenses.json file on Google Drive."""
        file_metadata = {'name': 'expenses.json'}
        media = MediaFileUpload('expenses.json', mimetype='application/json')
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def load_expenses(self):
        """Load expenses from Google Drive or initialize if not present."""
        if self.file_id:
            request = self.service.files().get_media(fileId=self.file_id)
            with open('expenses.json', 'wb') as local_file:
                downloader = MediaIoBaseDownload(local_file, request)
                done = False
                while not done:
                    _, done = downloader.next_chunk()
        if os.path.exists('expenses.json'):
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        if self.current_month not in self.expenses:
            self.expenses[self.current_month] = []

    def save_expenses(self):
        """Save expenses to both local file and Google Drive."""
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)
        media = MediaFileUpload('expenses.json', mimetype='application/json')
        self.service.files().update(fileId=self.file_id, media_body=media).execute()

    def initUI(self):
        self.setWindowTitle('Expense Calculator')

        # Global styles
        self.setStyleSheet("""
            QWidget {
                font-family: 'Arial', sans-serif;
                font-size: 22px;
                background-color: #eef3f8;
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
        add_button = QPushButton('Add Expense')
        add_button.clicked.connect(self.add_expense)
        layout.addWidget(add_button)

        # Table widget
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Item', 'Amount (BDT)'])
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table_widget)

        # Action buttons
        delete_button = QPushButton('Delete Selected')
        delete_button.clicked.connect(self.delete_expense)
        layout.addWidget(delete_button)

        total_button = QPushButton('Calculate Total')
        total_button.clicked.connect(self.calculate_total)
        layout.addWidget(total_button)

        self.setLayout(layout)
        self.update_table()

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

    def switch_month(self, month):
        self.current_month = month
        self.update_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ExpenseCalculator()
    calculator.show()
    sys.exit(app.exec_())
