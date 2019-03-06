# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor


class Ui_DbForm(object):
    def setupUi(self, DbForm):
        DbForm.setObjectName("DbForm")
        DbForm.resize(900, 500)
        self.gridLayout = QtWidgets.QGridLayout(DbForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_data = QtWidgets.QHBoxLayout()
        self.horizontalLayout_data.setSpacing(0)
        self.horizontalLayout_data.setObjectName("horizontalLayout_data")
        self.listWidget = QtWidgets.QListWidget(DbForm)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_data.addWidget(self.listWidget)
        self.textEdit = QtWidgets.QTextEdit(DbForm)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_data.addWidget(self.textEdit)
        self.gridLayout.addLayout(self.horizontalLayout_data, 0, 0, 1, 1)
        self.horizontalLayout_button = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button.setSpacing(0)
        self.horizontalLayout_button.setObjectName("horizontalLayout_button")
        self.horizontalLayout_key = QtWidgets.QHBoxLayout()
        self.horizontalLayout_key.setObjectName("horizontalLayout_key")
        self.dbRefreshBt = QtWidgets.QPushButton(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.dbRefreshBt.setFont(font)
        self.dbRefreshBt.setObjectName("dbRefreshBt")
        self.horizontalLayout_key.addWidget(self.dbRefreshBt)
        spacerItem = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_key.addItem(spacerItem)
        self.addBt = QtWidgets.QPushButton(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.addBt.setFont(font)
        self.addBt.setObjectName("addBt")
        self.horizontalLayout_key.addWidget(self.addBt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_key.addItem(spacerItem1)
        self.horizontalLayout_button.addLayout(self.horizontalLayout_key)
        self.horizontalLayout_edit = QtWidgets.QHBoxLayout()
        self.horizontalLayout_edit.setObjectName("horizontalLayout_edit")
        self.commitBt = QtWidgets.QPushButton(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.commitBt.setFont(font)
        self.commitBt.setObjectName("commitBt")
        self.horizontalLayout_edit.addWidget(self.commitBt)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_edit.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_edit.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_edit.addItem(spacerItem4)
        self.valueStyleBox = QtWidgets.QComboBox(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.valueStyleBox.setFont(font)
        self.valueStyleBox.setObjectName("valueStyleBox")
        self.valueStyleBox.addItem("")
        self.valueStyleBox.addItem("")
        self.valueStyleBox.addItem("")
        self.horizontalLayout_edit.addWidget(self.valueStyleBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_edit.addItem(spacerItem5)
        self.comboBox = QtWidgets.QComboBox(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_edit.addWidget(self.comboBox)
        self.horizontalLayout_button.addLayout(self.horizontalLayout_edit)
        self.gridLayout.addLayout(self.horizontalLayout_button, 1, 0, 1, 1)
        self.verticalLayout_tip = QtWidgets.QVBoxLayout()
        self.verticalLayout_tip.setSpacing(0)
        self.verticalLayout_tip.setObjectName("verticalLayout_tip")
        self.tipLabel = QtWidgets.QLabel(DbForm)
        self.tipLabel.setObjectName("tipLabel")
        self.verticalLayout_tip.addWidget(self.tipLabel)
        self.gridLayout.addLayout(self.verticalLayout_tip, 2, 0, 1, 1)

        # 新增右键菜单 开始
        self.itemRightMenu = QtWidgets.QMenu(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.itemRightMenu.setFont(font)
        self.itemRightMenu.setObjectName("rightMenu")
        self.itemDelAct = QtWidgets.QAction(DbForm)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.itemDelAct.setFont(font)
        self.itemDelAct.setObjectName("itemDelAct")
        self.itemRightMenu.addAction(self.itemDelAct)
        # 新增右键菜单 结束

        self.retranslateUi(DbForm)
        QtCore.QMetaObject.connectSlotsByName(DbForm)

        self.window = DbForm

        self.textEdit.setAcceptRichText(True)
        self.textEdit.setFontPointSize(int(self.comboBox.currentText()))
        self.textEdit.setFontPointSize(int(self.comboBox.currentText()))
        self.curValue = None
        self.listWidget.itemDoubleClicked.connect(lambda: self.selectKey())
        self.listWidget.itemClicked.connect(lambda: self.selectKey())
        self.commitBt.clicked.connect(lambda: self.update())
        self.valueStyleBox.currentIndexChanged.connect(lambda: self.updateTextStyle())
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(lambda: self.showItemRightMenu())
        self.itemDelAct.triggered.connect(lambda: self.delItem())
        self.dbRefreshBt.clicked.connect(lambda: self.refresh())
        self.addBt.clicked.connect(lambda: self.addItem())
        self.comboBox.currentIndexChanged.connect(lambda: self.setFontSize())

        self.addBt.hide()
        self.diffKeyFunction = {"string": self.stringFunc, "hash": self.hashFunc, "list": self.listFunc,
                                "set": self.setFunc, "zset": self.setFunc, "none": self.noneFunc}

    def retranslateUi(self, DbForm):
        _translate = QtCore.QCoreApplication.translate
        DbForm.setWindowTitle(_translate("DbForm", "Form"))
        self.dbRefreshBt.setText(_translate("DbForm", "刷新"))
        self.addBt.setText(_translate("DbForm", "添加"))
        self.commitBt.setText(_translate("DbForm", "提交"))
        self.valueStyleBox.setItemText(0, _translate("DbForm", "Text"))
        self.valueStyleBox.setItemText(1, _translate("DbForm", "Json"))
        self.valueStyleBox.setItemText(2, _translate("DbForm", "Html"))
        self.comboBox.setCurrentText(_translate("DbForm", "9"))
        self.comboBox.setItemText(0, _translate("DbForm", "9"))
        self.comboBox.setItemText(1, _translate("DbForm", "10"))
        self.comboBox.setItemText(2, _translate("DbForm", "11"))
        self.comboBox.setItemText(3, _translate("DbForm", "12"))
        self.comboBox.setItemText(4, _translate("DbForm", "14"))
        self.comboBox.setItemText(5, _translate("DbForm", "16"))
        self.comboBox.setItemText(6, _translate("DbForm", "18"))
        self.comboBox.setItemText(7, _translate("DbForm", "20"))
        self.comboBox.setItemText(8, _translate("DbForm", "22"))
        self.comboBox.setItemText(9, _translate("DbForm", "24"))
        self.comboBox.setItemText(10, _translate("DbForm", "26"))
        self.comboBox.setItemText(11, _translate("DbForm", "28"))
        self.tipLabel.setText(_translate("DbForm", "<html><head/><body><p><br/></p></body></html>"))
        self.itemDelAct.setText(_translate("DbForm", "删除"))

    def setDb(self, redisDbHandler):
        self.dbHandler = redisDbHandler

    def getDb(self):
        return self.redis_handler

    def refresh(self):
        try:
            k = self.dbHandler.keys("*")
            self.listWidget.clear()
            self.listWidget.addItems(k)
        except Exception as e:
            self.tipLabel.setText(e.args[0])

    def selectKey(self):
        k = self.listWidget.currentItem().text()
        t = self.dbHandler.type(k)
        v = self.diffKeyFunction[t.lower()](k, op='view')
        self.curValue = v

    def update(self):
        v = self.textEdit.toPlainText()
        if len(v) == 0:
            return
        try:
            k = self.listWidget.currentItem().text()
            t = self.dbHandler.type(k)
            self.diffKeyFunction[t](k, op='commit', v=v)
            self.tipLabel.setText("更新成功")
        except Exception as e:
            self.tipLabel.setText(e.args[0])
            return
        self.selectKey()

    def updateTextStyle(self):
        v = self.curValue
        if v is None:
            return
        try:
            s = self.valueStyleBox.currentText()
            if s == 'Text':
                self.textEdit.setText(str(v))
            elif s == 'Json':
                v = json.dumps(v, indent=4, separators=(',', ':'))
                self.textEdit.setText(v)
            elif s == 'Html':
                self.textEdit.setHtml(str(v))
        except Exception as e:
            self.tipLabel.setText(e.args[0])

    def stringFunc(self, k, v=None, op=None):
        if op == 'view':
            v = self.dbHandler.get(k)
            self.textEdit.setText(str(v))
        elif op == 'commit':
            self.dbHandler.set(k, v)
        return v

    def hashFunc(self, k, v=None, op=None):
        if op == 'view':
            v = self.dbHandler.hgetall(k)
            self.textEdit.setText(json.dumps(v, indent=4, separators=(',', ':')))
        elif op == 'commit':
            v = json.loads(v, encoding='utf-8')
            self.del_key(k, 1000)
            for i, j in v.items():
                self.dbHandler.hset(k, i, j)
        return v

    def listFunc(self, k, v=None, op=None):
        if op == 'view':
            v = self.dbHandler.lrange(k, 0, -1)
            self.textEdit.setText(str(v))
        elif op == 'commit':
            v = ','.join(v)
            self.dbHandler.ltrim(k, 1, 0)
            self.dbHandler.lpush(k, v)
        return v

    def setFunc(self, k, v=None, op=None):
        v = self.dbHandler.smembers(k)
        if op == 'view':
            self.textEdit.setText(str(v))
        return v

    def noneFunc(self, k, v=None, op=None):
        self.tipLabel.setText(k + "不存在")
        return None

    def showItemRightMenu(self):
        self.itemRightMenu.exec(QCursor.pos())

    def delItem(self):
        items = self.listWidget.selectedItems()
        for i in items:
            try:
                self.dbHandler.delete(i.text())
                self.listWidget.takeItem(self.listWidget.row(i))
            except Exception as e:
                self.tipLabel.setText(e.args[0])

    def addItem(self):
        item = QtWidgets.QListWidgetItem()
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
        self.listWidget.insertItem(0, item)

    def del_key(self, hash_key, del_count):
        cursor = '0'
        while cursor != 0:
            pl = self.dbHandler.pipeline()
            cursor, data = self.dbHandler.hscan(hash_key, cursor=cursor, count=del_count)
            for item in data.items():
                pl.hdel(hash_key, item[0])
            pl.execute()

    def setFontSize(self):
        self.textEdit.setFontPointSize(int(self.comboBox.currentText()))
        self.textEdit.setText(self.textEdit.toPlainText())