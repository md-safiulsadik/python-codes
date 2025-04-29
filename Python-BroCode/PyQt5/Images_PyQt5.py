
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 200, 800, 720)
        self.setWindowTitle("Image.exe")
        self.setWindowIcon(QIcon("D:\\Study\\Python\\Python_BroCode\\PyQt5\\Icon.jpg"))

       
        heading = QLabel("This is a Image as you can see", self)

        heading.setFont(QFont("Space Mono", 20))
        heading.setGeometry(50, 0, 700, 80)
        heading.setStyleSheet("color: #e6a353;"
                         "background-color: #bdfeff;")
        heading.setAlignment(Qt.AlignCenter)


        image_heading = QLabel("This is a pic" , self)

        image_heading.setFont(QFont("Space Mono", 20))
        image_heading.setGeometry(50, 80, 700, 80)
        image_heading.setStyleSheet("color: #a5f720;"
                         "background-color: #99bfbf;")
        image_heading.setAlignment(Qt.AlignCenter)


        image = QLabel(self)
        image.setGeometry(0, 0, 512, 512)
        # image.setStyleSheet("background-color: #a5f720")
        
        pixmap = QPixmap("D:\\Study\\Python\\Python_BroCode\\PyQt5\\pixmap.png")

        image.setPixmap(pixmap)

        image.setScaledContents(True)

        image.setGeometry((self.width() - image.width())// 2,
                          ((self.height() - image.height()) // 2) + 80,
                          image.width(),
                          image.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# from PyQt5.QtGui import QIcon, QFont, QPixmap
# from PyQt5.QtCore import Qt

# # Constants
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 720
# LABEL_FONT_SIZE = 20

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(300, 200, WINDOW_WIDTH, WINDOW_HEIGHT)
#         self.setWindowTitle("Image.exe")
#         self.setWindowIcon(QIcon("Python_BroCode/PyQt5/Icon.jpg"))  # Use relative path

#         # Create central widget
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         # Create labels
#         labels_layout = QVBoxLayout()
#         for text in ["This is a Image as you can see", "This is a pic"]:
#             label = QLabel(text)
#             label.setFont(QFont("Space Mono", LABEL_FONT_SIZE))
#             label.setAlignment(Qt.AlignCenter)
#             labels_layout.addWidget(label)

#         # Create image
#         image = QLabel()
#         pixmap = QPixmap("Python_BroCode/PyQt5/pixmap.png")  # Use relative path
#         image.setPixmap(pixmap)
#         image.setScaledContents(True)

#         # Add widgets to layout
#         main_layout = QVBoxLayout()
#         main_layout.addLayout(labels_layout)
#         main_layout.addWidget(image)
#         central_widget.setLayout(main_layout)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()