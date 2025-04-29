
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtCore import Qt, QTime, QTimer

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.timer = QTimer()
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop Watch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
            QPushButton, QLabel {
                font-family: Arial;
                padding: 25px;
                
            }
            QPushButton {
                font-size: 25px;
                margin: 1px 5px;
            }
            QLabel {
                font-size: 70px;
                border-radius: 12px;
            }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.time_formate(self.time))


    def time_formate(self, time):
        hour = time.hour()
        minute = time.minute()
        seconds = time.second()
        millisecond = time.msec() // 10

        return f"{hour:02}:{minute:02}:{seconds:02}.{millisecond:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.time_formate(self.time))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    watch_window = StopWatch()
    watch_window.show()
    sys.exit(app.exec_())