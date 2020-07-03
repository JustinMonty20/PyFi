# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finance_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from finance_funcs import simple_return,log_return,sec_volatility
from finance_funcs import portfolio_return,portfolio_volatility
from finance_funcs import beta,expected_return,sharpe_ratio


class Ui_PyFiUi(object):
    def setupUi(self, PyFiUi):
        PyFiUi.setObjectName("PyFiUi")
        PyFiUi.resize(800, 600)
        self.singleSecFunctions = QtWidgets.QFrame(PyFiUi)
        self.singleSecFunctions.setEnabled(True)
        self.singleSecFunctions.setGeometry(QtCore.QRect(30, 20, 291, 221))
        self.singleSecFunctions.setObjectName("singleSecFunctions")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.singleSecFunctions)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 40, 141, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SimpleReturn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.SimpleReturn.setObjectName("SimpleReturn")
        self.verticalLayout.addWidget(self.SimpleReturn)
        self.LogReturn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.LogReturn.setObjectName("LogReturn")
        self.verticalLayout.addWidget(self.LogReturn)
        self.SecVol = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.SecVol.setChecked(False)
        self.SecVol.setAutoExclusive(True)
        self.SecVol.setObjectName("SecVol")
        self.verticalLayout.addWidget(self.SecVol)
        self.label = QtWidgets.QLabel(self.singleSecFunctions)
        self.label.setGeometry(QtCore.QRect(40, 10, 201, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.singleSecFunctions)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 40, 141, 161))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Securityinput = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.Securityinput.setObjectName("Securityinput")
        self.verticalLayout_4.addWidget(self.Securityinput)
        self.Submitsingle = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Submitsingle.setObjectName("Submitsingle")
        self.verticalLayout_4.addWidget(self.Submitsingle)
        self.portfolioFuncs = QtWidgets.QFrame(PyFiUi)
        self.portfolioFuncs.setGeometry(QtCore.QRect(390, 20, 321, 231))
        self.portfolioFuncs.setObjectName("portfolioFuncs")
        self.PortfolioiLabel = QtWidgets.QLabel(self.portfolioFuncs)
        self.PortfolioiLabel.setGeometry(QtCore.QRect(80, 10, 171, 21))
        self.PortfolioiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PortfolioiLabel.setObjectName("PortfolioiLabel")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.portfolioFuncs)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 50, 121, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.folioReturns = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.folioReturns.setObjectName("folioReturns")
        self.verticalLayout_2.addWidget(self.folioReturns)
        self.folioVolatility = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.folioVolatility.setObjectName("folioVolatility")
        self.verticalLayout_2.addWidget(self.folioVolatility)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.portfolioFuncs)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 50, 161, 131))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.weights = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.weights.setObjectName("weights")
        self.verticalLayout_5.addWidget(self.weights)
        self.securities = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.securities.setObjectName("securities")
        self.verticalLayout_5.addWidget(self.securities)
        self.submit_folio = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.submit_folio.setObjectName("submit_folio")
        self.verticalLayout_5.addWidget(self.submit_folio)
        self.capmFuncs = QtWidgets.QFrame(PyFiUi)
        self.capmFuncs.setGeometry(QtCore.QRect(30, 270, 411, 261))
        self.capmFuncs.setObjectName("capmFuncs")
        self.label_3 = QtWidgets.QLabel(self.capmFuncs)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 171, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.capmFuncs)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(200, 50, 171, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Beta = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.Beta.setObjectName("Beta")
        self.verticalLayout_3.addWidget(self.Beta)
        self.execReturn = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.execReturn.setObjectName("execReturn")
        self.verticalLayout_3.addWidget(self.execReturn)
        self.sharpeRatio = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.sharpeRatio.setObjectName("sharpeRatio")
        self.verticalLayout_3.addWidget(self.sharpeRatio)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.capmFuncs)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(20, 50, 160, 191))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sec_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.sec_2.setObjectName("sec_2")
        self.verticalLayout_6.addWidget(self.sec_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_6.addWidget(self.lineEdit)
        self.submit_CAPM = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.submit_CAPM.setObjectName("submit_CAPM")
        self.verticalLayout_6.addWidget(self.submit_CAPM)
        self.output_area = QtWidgets.QFrame(PyFiUi)
        self.output_area.setGeometry(QtCore.QRect(470, 300, 211, 221))
        self.output_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_area.setObjectName("output_area")
        self.output = QtWidgets.QLabel(self.output_area)
        self.output.setGeometry(QtCore.QRect(10, 30, 191, 161))
        self.output.setObjectName("output")

        self.retranslateUi(PyFiUi)
        QtCore.QMetaObject.connectSlotsByName(PyFiUi)

        #functionality of the GUI 
        self.Submitsingle.clicked.connect(self.single_sec)
        self.output.setText('')
    
    def retranslateUi(self, PyFiUi):
        _translate = QtCore.QCoreApplication.translate
        PyFiUi.setWindowTitle(_translate("PyFiUi", "PyFi"))
        self.SimpleReturn.setText(_translate("PyFiUi", "Simple Return"))
        self.LogReturn.setText(_translate("PyFiUi", "Log Return"))
        self.SecVol.setText(_translate("PyFiUi", "Sec Volatility"))
        self.label.setText(_translate("PyFiUi", "Single Security Functions"))
        self.Submitsingle.setText(_translate("PyFiUi", "Calculate"))
        self.PortfolioiLabel.setText(_translate("PyFiUi", "Portfolio Functions"))
        self.folioReturns.setText(_translate("PyFiUi", "Returns"))
        self.folioVolatility.setText(_translate("PyFiUi", "Volatility"))
        self.submit_folio.setText(_translate("PyFiUi", "Calculate"))
        self.label_3.setText(_translate("PyFiUi", "Capital Asset Pricing Model"))
        self.Beta.setText(_translate("PyFiUi", "Beta"))
        self.execReturn.setText(_translate("PyFiUi", "Expected Return"))
        self.sharpeRatio.setText(_translate("PyFiUi", "Sharpe Ratio"))
        self.submit_CAPM.setText(_translate("PyFiUi", "Calculate"))
        self.output.setText(_translate("PyFiUi", "TextLabel"))

    # function that handles submission of the single securities button. 
    def single_sec(self):
        if self.SimpleReturn.isChecked():
            self.output.setText(simple_return(self.Securityinput.text()))
        elif self.LogReturn.isChecked():
            self.output.setText(log_return(self.Securityinput.text()))
        else:
            self.output.setText(sec_volatility(self.Securityinput.text()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyFiUi = QtWidgets.QWidget()
    ui = Ui_PyFiUi()
    ui.setupUi(PyFiUi)
    PyFiUi.show()
    sys.exit(app.exec_())
