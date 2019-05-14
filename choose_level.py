# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_level.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(493, 108)
        self.level_select_combobox = QtWidgets.QComboBox(Form)
        self.level_select_combobox.setGeometry(QtCore.QRect(10, 30, 471, 27))
        self.level_select_combobox.setObjectName("level_select_combobox")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.level_select_combobox.addItem("")
        self.dialog_button_box = QtWidgets.QDialogButtonBox(Form)
        self.dialog_button_box.setGeometry(QtCore.QRect(150, 70, 176, 27))
        self.dialog_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialog_button_box.setObjectName("dialog_button_box")
        self.choose_level_label = QtWidgets.QLabel(Form)
        self.choose_level_label.setGeometry(QtCore.QRect(10, 10, 461, 17))
        self.choose_level_label.setObjectName("choose_level_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.level_select_combobox.setItemText(0, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(1, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(2, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(3, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(4, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(5, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(6, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(7, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(8, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(9, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(10, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(11, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(12, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(13, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(14, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(15, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(16, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(17, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(18, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(19, _translate("Form", "New Item"))
        self.level_select_combobox.setItemText(20, _translate("Form", "New Item"))
        self.choose_level_label.setText(_translate("Form", "Choose monkeyball level to replace (Challenge Mode)"))

class ChooseLevelPopup(QMainWindow, Ui_Form):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChooseLevelPopup()
    window.show()
    sys.exit(app.exec_())
