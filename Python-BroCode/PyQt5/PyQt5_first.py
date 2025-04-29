# Python GUI

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practic GUI")
        self.setGeometry(300, 200, 700, 700)        
        self.setWindowIcon(QIcon("D:\\Study\\Python\\Python_BroCode\\pyQt5\\Icon.jpg"))

def main():
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()