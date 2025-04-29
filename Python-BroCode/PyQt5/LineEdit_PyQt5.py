
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import(QApplication, QMainWindow, QGridLayout, QLabel,
                            QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                            QLineEdit, QWidget)


class MainWindow(QMainWindow):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Line Edit")
        self.setWindowIcon(QIcon("Python_BroCode/PyQt5/LineEdit.png"))

        self.label = QLabel(self)
        self.get_user_name = QLineEdit(self)
        self.get_mail = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)

        self.vbox = QVBoxLayout()

        self.initUI()
        self.style_sheet()
        self.line_edit()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # self.label.setGeometry(0, 0, 500, 100)

        self.vbox.addWidget(self.get_user_name)
        self.vbox.addWidget(self.get_mail)
        self.vbox.addWidget(self.submit_button)
        self.vbox.addWidget(self.label)
        central_widget.setLayout(self.vbox)

        self.submit_button.clicked.connect(self.on_click)

    def line_edit(self):
        self.get_user_name.setPlaceholderText("UserName")
        self.get_mail.setPlaceholderText("example@gmail.com")
        # self.get_user_name.setAlignment(Qt.AlignLeft)
        # self.get_mail.setAlignment(Qt.AlignLeft)

    def style_sheet(self):
        # self.submit_button.setMaximumSize(200, 100)
        self.setStyleSheet("""
                    QLineEdit{
                        font-size: 25px;
                        font-family: Arial;
                        margin: 5px;
                        padding: 10px;
                        text-align: Left;
                    }
                    QPushButton{
                        font-size: 25px;
                        font-family: Space Mono;                       
                        margin: 10px;
                    }
                    QLabel{
                    background-color: red;
                    }
                """)
    
    def on_click(self):
        self.submit_button.setDisabled(True)
        user_name = self.get_user_name.text()
        mail = self.get_mail.text()

        print(user_name)
        print(mail)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()