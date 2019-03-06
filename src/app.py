# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys

from mainwindow import Ui_MainWindow
from singleInstance import singleInstance


if __name__ == '__main__':
    s = singleInstance()
    if s.aleradyrunning():
        exit(0)

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    exitCode = app.exec_()
    ui.saveConfig()
    sys.exit(exitCode)

