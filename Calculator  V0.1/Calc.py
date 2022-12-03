from Calculator import *

def signals(self):
    self.ENTER.clicked.connect(self.calc)
    self.ENTER_2.clicked.connect(self.rest)

def rest(self):
    self.label_4.setText('')
    self.perhitungan.setText('')

def calc(self):
    data = self.perhitungan.text()
    try:
        if "x" in data:
            data = data.replace("x", "*")
        if ":" in data:
            data = data.replace(":", "/")
        if "^" in data:
            data = data.replace("^", "**")
        hasil = eval(data)
        self.label_4.setText(str(hasil))
    except:
        self.label_4.setText('Terdapat kesalahan di penulisanmu!!!')

Ui_masukkan.signals = signals
Ui_masukkan.rest = rest
Ui_masukkan.calc = calc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_masukkan()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())



