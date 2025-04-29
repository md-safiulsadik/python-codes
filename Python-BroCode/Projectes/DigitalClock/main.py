import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QIcon, QColor, QFont

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.is_fullscreen = False  # Track fullscreen state
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("ClcokIcon.ico"))  # Ensure "ClockIcon.ico" is in the same directory
        self.setGeometry(600, 400, 500, 200)

        # Enable window resizing and show standard title bar buttons
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        
        # Set layout
        vbox = QVBoxLayout()
        
        # Add title bar with buttons
        title_bar = self.create_title_bar()
        vbox.addLayout(title_bar)
        
        # Digital clock display
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 85px; font-family: Arial; color: #333333;")
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)
        
        # Set window background color
        self.setStyleSheet("background-color: white; border-radius: 10px;")

        # Connect timer for updating time
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def create_title_bar(self):
        # Custom title bar layout
        title_layout = QHBoxLayout()
        
        # Fullscreen button
        self.fullscreen_button = QPushButton("□")
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)
        
        # Close button
        close_button = QPushButton("X")
        close_button.clicked.connect(self.close)
        
        # Style buttons
        for btn in [self.fullscreen_button, close_button]:
            btn.setFixedSize(30, 30)
            btn.setStyleSheet("background-color: #e0e0e0; font-size: 12px; font-weight: bold;")
        
        # Add buttons to layout
        title_layout.addStretch(1)
        title_layout.addWidget(self.fullscreen_button)
        title_layout.addWidget(close_button)
        
        return title_layout

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

    def toggle_fullscreen(self):
        # Toggle between fullscreen and normal window state
        if self.is_fullscreen:
            self.showNormal()
            self.is_fullscreen = False
            self.fullscreen_button.setText("□")
        else:
            self.showFullScreen()
            self.is_fullscreen = True
            self.fullscreen_button.setText("❐")  # Update button to indicate exit fullscreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)  # Enable high DPI scaling
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
