
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 720, 720)
        self.setWindowTitle("Check Box")
        self.setWindowIcon(QIcon("Python_BroCode/PyQt5/checkBox.png"))

        self.checkbox1 = QCheckBox("Do you like burgar?", self)
        self.checkbox2 = QCheckBox("Do you like chocolate?", self)
        self.checkbox3 = QCheckBox("Do you like pizza?", self)

        self.initUI()

    def initUI(self):

        self.checkbox1.setGeometry(85, 10, 500, 50)
        self.checkbox2.setGeometry(85, 65, 500, 50)
        self.checkbox3.setGeometry(85, 120, 500, 50)

        self.setStyleSheet("QCheckBox{"
                            "font-size: 25px;"
                            "font-family: Space Mono;"
                            "color: green;"
                            "background-color: yellow;"
                            "padding: 60px;"
                            "margin: 2px;"
                            "border: 2px solid;"
                            "border-radius: 15px;"
                         "}")

        self.checkbox1.setChecked(False)
        self.checkbox2.setChecked(False)
        self.checkbox3.setChecked(False)

        self.checkbox1.stateChanged.connect(self.checkbox_checked)
        self.checkbox2.stateChanged.connect(self.checkbox_checked)
        self.checkbox3.stateChanged.connect(self.checkbox_checked)

    def checkbox_checked(self):
        if self.checkbox1.isChecked():
            print("You like burger\n")
        else:
            print("You DO NOT like burger\n")

        if self.checkbox2.isChecked():
            print("You like chocolate\n")
        else:
            print("You DO NOT like chocolate\n")

        if self.checkbox3.isChecked():
            print("You like pizza\n")
        else:
            print("You DO NOT like pizza\n")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()