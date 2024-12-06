from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
Form, Windows = uic.loadUiType('pochty pervaya proga.ui')
win = QApplication([])
windows = Windows()
app = Form()
app.setupUi(windows)

def on():
    kon = int(app.kon.text())
    nach = int(app.nach.text())
    vremya = int(app.vremya.text())

    o = (kon - nach)/vremya
    app.otvet.setText(f'{o}')
app.result.clicked.connect(on)




windows.show()
win.exec()