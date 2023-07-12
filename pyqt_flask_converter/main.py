from flask import Flask, request, jsonify, render_template
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# Инициализация Flask приложения
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


# Маршрут Flask приложения для конвертации валюты
@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    base_currency = request.form['base_currency'].upper()
    target_currency = request.form['target_currency'].upper()

    # Запрос к API для получения курса валют
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)

    try:
        data = response.json()
        exchange_rate = data['rates'][target_currency]

        converted_amount = round(amount * exchange_rate, 2)
        result = f"{amount} {base_currency} = {converted_amount} {target_currency}"
    except ValueError:
        result = "Error: Invalid response from API"

    # Возвращение результата конвертации в формате JSON
    return jsonify(result=result)


# Создание PyQt5 виджетов
class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Currency Converter')

        self.amount_label = QLabel('Amount:', self)
        self.amount_label.move(20, 20)
        self.amount_input = QLineEdit(self)
        self.amount_input.move(100, 20)

        self.base_currency_label = QLabel('Base Currency:', self)
        self.base_currency_label.move(20, 60)
        self.base_currency_input = QLineEdit(self)
        self.base_currency_input.move(140, 60)

        self.target_currency_label = QLabel('Target Currency:', self)
        self.target_currency_label.move(20, 100)
        self.target_currency_input = QLineEdit(self)
        self.target_currency_input.move(140, 100)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.move(20, 140)
        self.convert_button.clicked.connect(self.convert)

        self.result_label = QLabel(self)
        self.result_label.move(20, 180)

    def convert(self):
        amount = float(self.amount_input.text())
        base_currency = self.base_currency_input.text()
        target_currency = self.target_currency_input.text()

        # Запрос к Flask API для конвертации валюты
        url = 'http://localhost:5000/convert'
        data = {
            'amount': amount,
            'base_currency': base_currency,
            'target_currency': target_currency
        }
        response = requests.post(url, data=data)

        try:
            result = response.json()['result']
            self.result_label.setText(result)
            print("1", result)
        except ValueError:
            result = "Error: Invalid response from Flask API"
            self.result_label.setText(result)
            print("0", result)


# Создание экземпляра QApplication
qapp = QApplication([])

# Создание экземпляра CurrencyConverter
app_widget = CurrencyConverter()
app_widget.show()


# Функция запуска Flask приложения
def run_flask_app():
    app.run()


# Запуск Flask приложения в отдельном потоке
flask_thread = QThread()
flask_thread.run = run_flask_app
flask_thread.start()

# Запуск PyQt event loop
qapp.exec_()
