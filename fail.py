# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_m1(object):
    def setupUi(self, m1):
        m1.setObjectName("m1")
        m1.resize(250, 250)
        m1.setStyleSheet("QDialog#m1\n"
"{\n"
"image: url(:/newPrefix/sad.jpg);\n"
"}\n"
"")
        self.label = QtWidgets.QLabel(m1)
        self.label.setGeometry(QtCore.QRect(80, 200, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.retranslateUi(m1)
        QtCore.QMetaObject.connectSlotsByName(m1)

    def retranslateUi(self, m1):
        _translate = QtCore.QCoreApplication.translate
        m1.setWindowTitle(_translate("m1", "Dialog"))
        self.label.setText(_translate("m1", "注册失败"))
import aaa_rc
