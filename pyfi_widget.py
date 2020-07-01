import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

class PyFiUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyFi')
        self.setFixedSize(600,400)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

def main():
    pyfi_app = QApplication(sys.argv)
    view = PyFiUi()
    view.show()
    sys.exit(pyfi_app.exec())

if __name__ == '__main__':
    main()

