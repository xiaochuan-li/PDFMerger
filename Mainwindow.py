# -*- encoding: utf-8 -*-
'''
@File    :   Mainwindow.py
@Time    :   2020/12/20 19:14:45
@Author  :   Xiaochuan LI 
@Version :   1.0
@Contact :   lixiaochuan@buua.edu.cn
@License :   (C)Copyright 2020-2021, Lixiaochuan-BUAA-vrlab
@Desc    :   None
'''

# here put the import lib

from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
from src.merger import MergePDF
from QCandyUi import CandyWindow
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.UI import Ui_MainWindow
import sys
sys.path.append("resources")

DATAPATH = "./data/" if os.path.isdir("./data/") else "./resources/data/"


class UI_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.line.setText('D://result.pdf')

        self.browser.browse = lambda x: self.line.setText(x)
        self.browser.filemode = "save"
        self.browser.clicked.connect(self.browserFunc)
        self.gridLayout.filemode = "load"
        self.gridLayout.clicked.connect(self.browserFunc)
        self.pushButton.clicked.connect(self.submit)

    def submit(self):
        files = [x.fileinfo.filePath()
                 for x in self.gridLayout.files if x.checked]
        target = self.line.text()
        res = MergePDF(files, target)
        QMessageBox.information(self, "Information", res, QMessageBox.Ok)

    def browserFunc(self):
        sender = self.sender()
        if sender.filemode == "load":
            file_, _ = QFileDialog.getOpenFileName(
                self, 'Open file', './', 'PDF files (*.pdf)')
        else:
            file_, _ = QFileDialog.getSaveFileName(
                self, 'Save file', 'D://result.pdf', 'PDF files (*.pdf)')
        if file_ != "":
            sender.browse(file_)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = CandyWindow.createWindow(
        UI_window(), theme="blueDeep", title='PDFMerger', ico_path=DATAPATH+"head.ico")
    window.show()
    sys.exit(app.exec_())
