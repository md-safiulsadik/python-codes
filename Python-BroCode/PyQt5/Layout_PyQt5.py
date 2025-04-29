
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QLabel, QVBoxLayout, 
                             QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLayout.exe")
        self.setGeometry(300, 200, 800, 720)
        self.initUI()
                

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Label no. 1", self)
        label2 = QLabel("Label no. 2", self)
        label3 = QLabel("Label no. 3", self)
        label4 = QLabel("Label no. 4", self)
        label5 = QLabel("Label no. 5", self)

        label1.setFont(QFont("Mono Space", 15))
        label2.setFont(QFont("Mono Space", 15))
        label3.setFont(QFont("Mono Space", 15))
        label4.setFont(QFont("Mono Space", 15))
        label5.setFont(QFont("Mono Space", 15))

        label1.setAlignment(Qt.AlignCenter)
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)
        label4.setAlignment(Qt.AlignCenter)
        label5.setAlignment(Qt.AlignCenter)


        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: green")
        label3.setStyleSheet("background-color: blue")
        label4.setStyleSheet("background-color: yellow")
        label5.setStyleSheet("background-color: purple")

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)

        # hbox = QHBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        

        gbox = QGridLayout()

        gbox.addWidget(label1, 0, 0)
        gbox.addWidget(label2, 0, 4)
        gbox.addWidget(label3, 2, 2)
        gbox.addWidget(label4, 4, 0)
        gbox.addWidget(label5, 4, 4)

        central_widget.setLayout(gbox)


def main():
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()