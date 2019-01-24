# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RSAUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import RSAEncryption
from Server import Server
from Client import Client

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    current_message = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(494, 430)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.main_text = QtGui.QTextEdit(self.centralwidget)
        self.main_text.setObjectName(_fromUtf8("main_text"))
        self.gridLayout_2.addWidget(self.main_text, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.encrypt_btn = QtGui.QPushButton(self.centralwidget)
        self.encrypt_btn.clicked.connect(self.encrypt_textbox)
        self.encrypt_btn.setObjectName(_fromUtf8("encrypt_btn"))
        self.horizontalLayout_3.addWidget(self.encrypt_btn)
        self.decrypt_btn = QtGui.QPushButton(self.centralwidget)
        self.decrypt_btn.setObjectName(_fromUtf8("decrypt_btn"))
        self.decrypt_btn.clicked.connect(self.decrypt_textbox)
        self.horizontalLayout_3.addWidget(self.decrypt_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        RSAEncryption.generate_RSA_key()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "My RSA Application", None))
        self.encrypt_btn.setText(_translate("MainWindow", "Encrypt", None))
        self.decrypt_btn.setText(_translate("MainWindow", "Decrypt", None))

    def encrypt_textbox(self):
        message = self.main_text.toPlainText()
        message = str(message)
        encrypted = RSAEncryption.encrypt_message(message)
        self.main_text.setText(str(encrypted))
        self.current_message = encrypted

    def decrypt_textbox(self):
        decrypted = RSAEncryption.decrypt_message(self.current_message)
        self.main_text.setText(str(decrypted))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

