import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

pyfi_app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyFi GUI')
window.setGeometry(100,100,280,80)
window.move(60,15)
helloMsg = QLabel('<h1>PyFi </h1>',parent=window)
helloMsg.move(60,15)
window.show()

sys.exit(pyfi_app.exec_())