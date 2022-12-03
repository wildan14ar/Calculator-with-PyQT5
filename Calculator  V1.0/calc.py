from Calculator import *

def signals(self):
    self.pushButton_2.clicked.connect(self.calc)

def calc(self):
    a = int(self.lineEdit_1.text())
    b = int(self.lineEdit_2.text())
    operator = self.comboBox.currentText()
    try:
        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        else:
            result = "xx"
        self.lineEdit_3.setText(str(result))
            
    except:
        self.lineEdit_3.setText('Error!!!')
    

Ui_MainWindow.signals = signals
Ui_MainWindow.calc = calc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
