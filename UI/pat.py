# -*- encoding: utf-8 -*-
'''
@File    :   pat.py
@Time    :   2020/12/20 19:15:02
@Author  :   Xiaochuan LI 
@Version :   1.0
@Contact :   lixiaochuan@buua.edu.cn
@License :   (C)Copyright 2020-2021, Lixiaochuan-BUAA-vrlab
@Desc    :   None
'''

# here put the import lib

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pattern.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Pat_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(110, 150)
        Form.setFixedSize(110, 150)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(35, 60, 30, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 115, 82, 30))
        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("font-size:8px;")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
