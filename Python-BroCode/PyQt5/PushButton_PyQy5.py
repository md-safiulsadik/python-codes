
import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 720, 720)
        self.setWindowTitle("Push Button")
        # self.setWindowIcon(QIcon("Python_BroCode/PyQt5/pushButton.png"))

        self.button = QPushButton("Click me !", self)
        self.label = QLabel(" ", self)

        self.label_img = QLabel(self)
        self.pixmap = QPixmap("Python_BroCode/PyQt5/pushButton.png")

        self.initUI()

        

    def initUI(self):
        self.button.setGeometry(230, 50, 250, 100)
        self.button.setStyleSheet("color: #f05151;"
                                  "background-color: #a6f7e8;")
        self.button.setFont(QFont("Space Mono", 20))
        self.label.setGeometry(220, 520 ,720, 100)
        self.label.setStyleSheet("font-size: 30px")
        self.label_img.setGeometry(200, 200, 312, 312)
        
        self.button.clicked.connect(self.no_click)


    def no_click(self):
        print("Button has been cliked")
        self.button.setText("Clicked !")
        self.button.setStyleSheet("color: #aef7a1;"
                                  "background-color: #fcfcfa;")

        self.label_img.setPixmap(self.pixmap)
        self.label_img.setScaledContents(True)

        self.button.setDisabled(True)
        self.label.setText("Thank You for cliking :)")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()