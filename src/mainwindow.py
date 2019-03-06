# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import json

import redis
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QCursor

from config import ConfigUtil
from connectdialog import Ui_ConnectDialog
from dbform import Ui_DbForm


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout.addWidget(self.treeWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setIconSize(QtCore.QSize(36, 36))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        self.versionLabel = QtWidgets.QLabel(self.centralWidget)
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout.addWidget(self.versionLabel, 1, 0, 1, 1)
        self.errorLabel = QtWidgets.QLabel(self.centralWidget)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.connectAct = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.connectAct.setFont(font)
        self.connectAct.setObjectName("connectAct")
        self.exitAct = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.exitAct.setFont(font)
        self.exitAct.setObjectName("exitAct")
        self.cmdAct = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.cmdAct.setFont(font)
        self.cmdAct.setObjectName("cmdAct")
        self.menu.addAction(self.connectAct)
        self.menu.addAction(self.exitAct)
        self.menu_2.addAction(self.cmdAct)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        # 新增右键菜单 开始
        self.itemRightMenu = QtWidgets.QMenu(MainWindow)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.itemRightMenu.setFont(font)
        self.itemRightMenu.setObjectName("rightMenu")

        # self.itemEditAct = QtWidgets.QAction(MainWindow)
        # font = QtGui.QFont()
        # font.setFamily("新宋体")
        # font.setPointSize(9)
        # self.itemEditAct.setFont(font)
        # self.itemEditAct.setObjectName("itemEditAct")
        # self.itemRightMenu.addAction(self.itemEditAct)

        self.itemDelAct = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(9)
        self.itemDelAct.setFont(font)
        self.itemDelAct.setObjectName("itemDelAct")
        self.itemRightMenu.addAction(self.itemDelAct)
        # 新增右键菜单 结束

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 设置内部变量以及槽函数等
        self.configUtil = ConfigUtil('C:\\Users\\Administrator\\.redisViewConfig')
        self.window = MainWindow
        self.connectDialog = Ui_ConnectDialog()
        self.connectDialogWindow = QtWidgets.QDialog()
        self.connectDialog.setupUi(self.connectDialogWindow)
        self.connectDialogWindow.hide()
        self.connectDialog.setParent(self)

        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.treeWidgetShowRightMenu)
        # self.itemEditAct.triggered.connect(self.editConnect)
        self.itemDelAct.triggered.connect(self.delConnect)
        self.connectList = {}
        self.connectAct.triggered.connect(self.showConnect)
        self.treeWidget.doubleClicked.connect(self.openDB)
        self.exitAct.triggered.connect(lambda: self.window.close())
        self.tabWidget.tabCloseRequested.connect(self.closeDB)

        self.treeWidgetInit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redis可视化客户端"))
        self.versionLabel.setText(_translate("MainWindow", "Version: 0.1.1"))
        self.errorLabel.setText(_translate("MainWindow", "      "))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "工具"))
        self.connectAct.setText(_translate("MainWindow", "新建连接"))
        self.exitAct.setText(_translate("MainWindow", "退出(X)"))
        self.cmdAct.setText(_translate("MainWindow", "命令行"))
        self.itemDelAct.setText(_translate("MainWindow", "删除连接"))
        # self.itemEditAct.setText(_translate("MainWindow", "编辑连接"))

    def showConnect(self):
        self.connectDialogWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.connectDialogWindow.show()

    def isConnectNameExist(self, conName):
        return conName in self.connectList.keys()

    def treeWidgetInit(self):
        data = self.configUtil.getAllConfig()
        if data is None:
            return
        dataList = json.loads(data)
        for i in dataList:
            self.newConnect(i['connectName'], i['host'], i['port'], i['password'])

    def newConnect(self, conName, host, port, password, curConnectName=None):
        if curConnectName is not None:
            pass
        info = self.connectList[conName] = {}
        item = QtWidgets.QTreeWidgetItem()
        item.setText(0, conName)
        self.treeWidget.addTopLevelItem(item)
        info['host'] = host
        info['port'] = port
        info['password'] = password
        info['conName'] = conName
        info['item'] = item
        info['db'] = []
        for i in range(16):
            info['db'].append({'index': i, 'ui': None, 'window': None, 'close': False})
            t = QtWidgets.QTreeWidgetItem()
            t.setIcon(0, QIcon("../resource/redis.png"))
            t.setText(0, "DB(%d)" % i)
            item.addChild(t)
        return None

    def findConnectByChildItem(self, item):
        for i in self.connectList.keys():
            if self.connectList[i]['item'] == item:
                return self.connectList[i]
        return None

    def openDB(self):
        # print(self.treeWidget.currentIndex().row())
        if self.treeWidget.currentItem().parent() is None:
            return
        connectInfo = self.findConnectByChildItem(self.treeWidget.currentItem().parent())
        dbIndex = self.treeWidget.currentIndex().row()
        # print(dbIndex)
        dbInfo = connectInfo['db'][dbIndex]
        if dbInfo['ui'] is None:
            dbInfo = connectInfo['db'][dbIndex] = {'index': dbIndex}
            try:
                h = redis.StrictRedis(host=connectInfo['host'], port=connectInfo['port'],
                                      password=connectInfo['password'], db=dbIndex,
                                      decode_responses=True)
                h.ping()
            except Exception as res:
                # print(res)
                self.errorLabel.setText(res.args[0])
                return
            ui = Ui_DbForm()
            window = QtWidgets.QWidget()
            ui.setupUi(window)
            ui.setDb(h)
            self.tabWidget.addTab(window, "DB(" + str(dbIndex) + ")")
            dbInfo['ui'] = ui
            dbInfo['window'] = window
        elif dbInfo['close'] is True:
            self.tabWidget.addTab(dbInfo['window'], "DB(" + str(dbIndex) + ")")
        self.tabWidget.setCurrentWidget(dbInfo['window'])
        dbInfo['close'] = False
        dbInfo['ui'].refresh()

    def closeDB(self):
        widget = self.tabWidget.currentWidget()
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        for i in self.connectList.keys():
            dbList = self.connectList[i]['db']
            for j in dbList:
                if j['window'] == widget:
                    j['close'] = True

    def treeWidgetShowRightMenu(self):
        if self.treeWidget.currentItem() is None:
            return
        if self.treeWidget.currentItem().parent() is not None:
            return
        self.itemRightMenu.exec(QCursor.pos())

    def editConnect(self):
        item = self.treeWidget.currentItem()
        for i in self.connectList.keys():
            info = self.connectList[i]
            if info['item'] == item:
                self.connectDialog.curConnectName = info['conName']
                self.connectDialog.conName.setText(info['conName'])
                self.connectDialog.hostLi.setText(info['host'])
                self.connectDialog.portLi.setText(str(info['port']))
                self.connectDialog.passwordLi.setText(info['password'])
                self.connectDialogWindow.show()
                break

    def delConnect(self):
        item = self.treeWidget.currentItem()
        for i in self.connectList.keys():
            if self.connectList[i]['item'] == item:
                info = self.connectList.pop(i)
                for j in info['db']:
                    if 'window' in j and j['window'] is not None:
                        index = self.tabWidget.indexOf(j['window'])
                        self.tabWidget.removeTab(index)
                break
        self.treeWidget.takeTopLevelItem(self.treeWidget.currentIndex().row())

    def saveConfig(self):
        data = []
        for i in self.connectList.keys():
            info = self.connectList[i]
            data.append({'connectName': info['conName'], 'host': info['host'],
                         'port': info['port'], 'password': info['password']})
        self.configUtil.saveConfig(json.dumps(data))
