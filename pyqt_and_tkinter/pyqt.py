from PyQt6 import QtWidgets, uic, QtCore, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("untitled.ui", self)
        self.ui.pushButton0.clicked.connect(self.calculator)
        self.ui.pushButton1.clicked.connect(self.calculator)
        self.ui.pushButton2.clicked.connect(self.calculator)
        self.ui.pushButton3.clicked.connect(self.calculator)
        self.ui.pushButton4.clicked.connect(self.calculator)
        self.ui.pushButton5.clicked.connect(self.calculator)
        self.ui.pushButton6.clicked.connect(self.calculator)
        self.ui.pushButton7.clicked.connect(self.calculator)
        self.ui.pushButton8.clicked.connect(self.calculator)
        self.ui.pushButton9.clicked.connect(self.calculator)
        self.ui.pushButton_divide.clicked.connect(self.calculator)
        self.ui.pushButton_eq.clicked.connect(self.calculator)
        self.ui.pushButton_plus.clicked.connect(self.calculator)
        self.ui.pushButton_multiply.clicked.connect(self.calculator)
        self.ui.pushButton_takeaway.clicked.connect(self.calculator)
        self.ui.pushButton_clear.clicked.connect(self.calculator)


    def calculator(self):
        button = self.sender()
        text = button.text()
        label_text = self.ui.label.text()


        if text.isdigit():
            self.ui.label.setText(label_text + text)
        elif text == "+":
            self.ui.label.setText(label_text + " " + "+ ")
        elif text == "-":
            self.ui.label.setText(label_text + " " + "- ")
        elif text == "*":
            self.ui.label.setText(label_text + " " + "* ")
        elif text == "/":
            self.ui.label.setText(label_text + " " + "/ ")
        elif text == "=":
            result = str(eval(label_text))
            self.ui.label.setText(result)
        elif text == "C":
            self.ui.label.setText('')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()
