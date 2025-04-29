
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_name_label = QLabel("       Enter City Name:       ",self)
        self.input_line_edit = QLineEdit(self)
        self.weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Weather")
        self.input_line_edit.setPlaceholderText("New York")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_name_label)
        vbox.addWidget(self.input_line_edit)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_name_label.setAlignment(Qt.AlignCenter)
        self.input_line_edit.setAlignment(Qt.AlignLeft)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


        self.city_name_label.setObjectName("city_label")
        self.weather_button.setObjectName("weather_button")
        self.input_line_edit.setObjectName("input")
        self.temperature_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel,QPushButton,QLineEdit{
                font-family: Arial;
                padding: 15px;
            }QLabel#city_label{
                font-size: 45px;

            }QLabel#temp_label{
                font-size: 90px;

            }QLabel#emoji_label{
                font-size: 110px;
                font-family: Segoe UI emoji;
                
            }QLabel#description_label{
                font-size: 45px;

            }QPushButton#weather_button{
                font-size: 30px;
                font-weight: bold;

            }QLineEdit#input{
                font-size: 35px;
            }
        """)
        self.weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        API_key = "507f780ab35cd84f0d9831fd5ad59040"
        city_name = self.input_line_edit.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}" 

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")
                    
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
            
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
            
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, massage):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(massage)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 90px")
        temperature = data['main']['temp'] - 273.15
        description = data['weather'][0]['description']
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temperature:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)


    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())