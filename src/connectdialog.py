# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox


class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        ConnectDialog.setObjectName("ConnectDialog")
        ConnectDialog.resize(480, 340)
        self.gridLayout = QtWidgets.QGridLayout(ConnectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(ConnectDialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.conName = QtWidgets.QLineEdit(ConnectDialog)
        self.conName.setObjectName("conName")
        self.horizontalLayout.addWidget(self.conName)
        self.label_5 = QtWidgets.QLabel(ConnectDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(ConnectDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hostLi = QtWidgets.QLineEdit(ConnectDialog)
        self.hostLi.setObjectName("hostLi")
        self.horizontalLayout_3.addWidget(self.hostLi)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(ConnectDialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(ConnectDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.portLi = QtWidgets.QLineEdit(ConnectDialog)
        self.portLi.setObjectName("portLi")
        self.horizontalLayout_7.addWidget(self.portLi)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(ConnectDialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(ConnectDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.passwordLi = QtWidgets.QLineEdit(ConnectDialog)
        self.passwordLi.setObjectName("passwordLi")
        self.horizontalLayout_11.addWidget(self.passwordLi)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(ConnectDialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConnectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(ConnectDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectDialog)

        # 设置内部变量以及槽函数等
        self.parentUI = None
        self.window = ConnectDialog
        self.curConnectName = None
        self.buttonBox.button(QDialogButtonBox.Ok).setText("确定")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("取消")
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.newConnect)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(lambda: self.window.hide())

    def retranslateUi(self, ConnectDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectDialog.setWindowTitle(_translate("ConnectDialog", "新建连接"))
        self.label_4.setText(_translate("ConnectDialog", "连接名称："))
        self.label_5.setText(_translate("ConnectDialog", "<html><head/><body><pre><span style=\" "
                                                         "font-family:\'Courier New\'; color:#ff0000;\">*            "
                                                         "         </span></pre></body></html>"))
        self.label.setText(_translate("ConnectDialog", "主机："))
        self.label_6.setText(_translate("ConnectDialog", "<html><head/><body><pre style=\" margin-top:12px; "
                                                         "margin-bottom:12px; margin-left:0px; margin-right:0px; "
                                                         "-qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                                         "font-family:\'Courier New\'; color:#ff0000;\">*             "
                                                         "        </span></pre></body></html>"))
        self.label_2.setText(_translate("ConnectDialog", "端口："))
        self.label_7.setText(_translate("ConnectDialog", "<html><head/><body><pre><span style=\" "
                                                         "font-family:\'Courier New\'; color:#ff0000;\">*            "
                                                         "         </span></pre></body></html>"))
        self.label_3.setText(_translate("ConnectDialog", "密码："))
        self.label_9.setText(_translate("ConnectDialog", "<html><head/><body><pre><span style=\" "
                                                         "font-family:\'Courier New\'; color:#ff0000;\"/>            "
                                                         "          </pre></body></html>"))

    def setParent(self, parent):
        self.parentUI = parent

    def newConnect(self):
        if self.parentUI.isConnectNameExist(self.conName.text()):
            _translate = QtCore.QCoreApplication.translate
            self.label_5.setText(_translate("ConnectDialog",
                                            "<html><head/><body><p><span style=\" color:#ff0000;\"> "
                                            "*连接名称已存在</span></p></body></html>"))
            return
        try:
            result = self.parentUI.newConnect(self.conName.text(), self.hostLi.text(), int(self.portLi.text()),
                                              self.passwordLi.text(), self.curConnectName)
            if result is None:
                self.window.hide()
        except Exception as e:
            pass
        self.clearInfo()

    def cancel(self):
        self.window.hide()
        self.clearInfo()

    def clearInfo(self):
        self.portLi.clear()
        self.hostLi.clear()
        self.passwordLi.clear()
        self.conName.clear()
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("ConnectDialog", "<html><head/><body><pre><span style=\" "
                                                         "font-family:\'Courier New\'; color:#ff0000;\">*            "
                                                         "         </span></pre></body></html>"))
