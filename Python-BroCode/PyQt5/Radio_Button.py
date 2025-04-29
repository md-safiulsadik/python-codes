
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGridLayout,
                             QRadioButton, QButtonGroup, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(600, 250, 720, 720)
        self.setWindowTitle("Radio Button")
        self.setWindowIcon(QIcon("Python_BroCode/PyQt5/pushButton.png"))
        self.radio_button1 = QRadioButton("Visa", self) 
        self.radio_button2 = QRadioButton("MasterCard", self) 
        self.radio_button3 = QRadioButton("Gift Card", self) 
        self.radio_button4 = QRadioButton("In-Store", self) 
        self.radio_button5 = QRadioButton("Online", self) 
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.gbox = QGridLayout()

        self.initUI()

    def initUI(self):
       central_widget = QWidget()
       self.setCentralWidget(central_widget)
       
       self.button_group1.addButton(self.radio_button1)
       self.button_group1.addButton(self.radio_button2)
       self.button_group1.addButton(self.radio_button3)
       self.button_group2.addButton(self.radio_button4)
       self.button_group2.addButton(self.radio_button5)

       self.gbox.addWidget(self.radio_button1, 0, 0)
       self.gbox.addWidget(self.radio_button2, 1, 0) 
       self.gbox.addWidget(self.radio_button3, 2, 0)
       self.gbox.addWidget(self.radio_button5, 0, 1)
       self.gbox.addWidget(self.radio_button4, 1, 1)
       
       self.radio_button1.setObjectName("RB1")
       self.radio_button2.setObjectName("RB2")
       self.radio_button3.setObjectName("RB3")
       
       self.setStyleSheet("""
                          QRadioButton{
                          font-size: 25px;
                          font-family: Space Mono;
                          background-color: #e6edf5;
                          padding: 20px 80px;
                          border: 2px;
                          border-radius: 12px;
                          margin: 5px;
                          }
                          QRadioButton#RB1{
                            color: #216bbf;
                          }
                          QRadioButton#RB2{
                            color: #eb3e13;
                          }
                          QRadioButton#RB3{
                            color: #40dfed; 
                          }
                          
                          """)
       
       central_widget.setLayout(self.gbox)

       self.radio_button1.toggled.connect(self.radio_button_change)
       self.radio_button2.toggled.connect(self.radio_button_change)
       self.radio_button3.toggled.connect(self.radio_button_change)
       self.radio_button4.toggled.connect(self.radio_button_change)
       self.radio_button5.toggled.connect(self.radio_button_change)


    def radio_button_change(self):
      radio_button = self.sender()
      if radio_button.isChecked():
        print(f"You selected {radio_button.text()}")
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()