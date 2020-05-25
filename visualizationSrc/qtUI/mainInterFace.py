# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/mainInterFace.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 740)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 740))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QTabBar::close-button{\n"
"    image: url(:/ico/Data/qrc/ico/close.png);\n"
"}\n"
"QTabBar::close-button:hover{\n"
"    image: url(:/ico/Data/qrc/ico/closed.png);\n"
"}\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(200,200,200);\n"
"}\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: rgb(100,100,100);\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;background: none;color: none;\n"
"}")
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Main.setStyleSheet("#MainWindow{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"#Main{\n"
"    background-color: rgb(255,255,255);\n"
"    margin:10px;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Main.setObjectName("Main")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Main)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1181, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Interface = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Interface.setContentsMargins(10, 10, 10, 10)
        self.Interface.setSpacing(5)
        self.Interface.setObjectName("Interface")
        self.HeadToolBar = QtWidgets.QHBoxLayout()
        self.HeadToolBar.setSpacing(0)
        self.HeadToolBar.setObjectName("HeadToolBar")
        self.top_right = QtWidgets.QHBoxLayout()
        self.top_right.setSpacing(0)
        self.top_right.setObjectName("top_right")
        self.EXETitle = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.EXETitle.setMaximumSize(QtCore.QSize(16777215, 24))
        self.EXETitle.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.EXETitle.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EXETitle.setStyleSheet("#EXETitle{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.EXETitle.setObjectName("EXETitle")
        self.top_right.addWidget(self.EXETitle)
        self.top_right.setStretch(0, 1)
        self.HeadToolBar.addLayout(self.top_right)
        self.top_left = QtWidgets.QHBoxLayout()
        self.top_left.setSpacing(10)
        self.top_left.setObjectName("top_left")
        self.min_window = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.min_window.setMaximumSize(QtCore.QSize(24, 24))
        self.min_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_window.setStyleSheet("#min_window{\n"
"    border-image: url(:/ico/Data/qrc/ico/min.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"#min_window:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/mined.png);\n"
"}")
        self.min_window.setObjectName("min_window")
        self.top_left.addWidget(self.min_window)
        self.max_window = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.max_window.setMaximumSize(QtCore.QSize(24, 24))
        self.max_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max_window.setStyleSheet("#max_window{\n"
"    border-image: url(:/ico/Data/qrc/ico/max.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"#max_window:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/maxed.png);\n"
"}")
        self.max_window.setObjectName("max_window")
        self.top_left.addWidget(self.max_window)
        self.close_window = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.close_window.setMaximumSize(QtCore.QSize(24, 24))
        self.close_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_window.setStyleSheet("#close_window{\n"
"    border-image: url(:/ico/Data/qrc/ico/close.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"#close_window:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/closed.png)\n"
"}")
        self.close_window.setObjectName("close_window")
        self.top_left.addWidget(self.close_window)
        self.HeadToolBar.addLayout(self.top_left)
        self.HeadToolBar.setStretch(0, 10)
        self.HeadToolBar.setStretch(1, 1)
        self.Interface.addLayout(self.HeadToolBar)
        self.ContentTabList = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.ContentTabList.setStyleSheet("QTextBrowser{\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border:none; \n"
"    border-radius:5px;\n"
"}")
        self.ContentTabList.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.ContentTabList.setTabsClosable(True)
        self.ContentTabList.setObjectName("ContentTabList")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setToolTip("")
        self.HomeTab.setObjectName("HomeTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.HomeTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1151, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.CardControler = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.CardControler.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CardControler.setStyleSheet("QTextBrowser{\n"
"    background-image: url(:/picture/Data/qrc/cardPkg.png);\n"
"}")
        self.CardControler.setObjectName("CardControler")
        self.gridLayout.addWidget(self.CardControler, 0, 0, 1, 1)
        self.CommandList = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.CommandList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.CommandList.setStyleSheet("QTextBrowser{\n"
"    background-image: url(:/picture/Data/qrc/command.png);\n"
"}")
        self.CommandList.setObjectName("CommandList")
        self.gridLayout.addWidget(self.CommandList, 0, 1, 1, 1)
        self.CommandList_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.CommandList_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.CommandList_2.setStyleSheet("QTextBrowser{\n"
"    background-image: url(:/picture/Data/qrc/store.png);\n"
"}")
        self.CommandList_2.setObjectName("CommandList_2")
        self.gridLayout.addWidget(self.CommandList_2, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setStyleSheet("#userSetting{\n"
"    border-image: url(:/ico/Data/qrc/ico/set.png);\n"
"}\n"
"#userSetting:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/seted.png);\n"
"}\n"
"#userData{\n"
"    border-image: url(:/ico/Data/qrc/ico/user.png);\n"
"}\n"
"#userData:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/usered.png);\n"
"}\n"
"#userLogin{\n"
"    border-image: url(:/ico/Data/qrc/ico/login.png);\n"
"}\n"
"#userLogin:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/logined.png);\n"
"}\n"
"#userLogout{\n"
"    border-image: url(:/ico/Data/qrc/ico/logout.png);\n"
"}\n"
"#userLogout:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/logouted.png);\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 371, 301))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.userLogin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.userLogin.setMinimumSize(QtCore.QSize(64, 64))
        self.userLogin.setMaximumSize(QtCore.QSize(64, 64))
        self.userLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.userLogin.setText("")
        self.userLogin.setObjectName("userLogin")
        self.gridLayout_3.addWidget(self.userLogin, 2, 0, 1, 1)
        self.userLogout = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.userLogout.setMinimumSize(QtCore.QSize(64, 64))
        self.userLogout.setMaximumSize(QtCore.QSize(64, 64))
        self.userLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.userLogout.setText("")
        self.userLogout.setObjectName("userLogout")
        self.gridLayout_3.addWidget(self.userLogout, 2, 1, 1, 1)
        self.userData = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.userData.setMinimumSize(QtCore.QSize(64, 64))
        self.userData.setMaximumSize(QtCore.QSize(64, 64))
        self.userData.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.userData.setText("")
        self.userData.setObjectName("userData")
        self.gridLayout_3.addWidget(self.userData, 1, 0, 1, 1)
        self.userSetting = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.userSetting.setMinimumSize(QtCore.QSize(64, 64))
        self.userSetting.setMaximumSize(QtCore.QSize(64, 64))
        self.userSetting.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.userSetting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userSetting.setText("")
        self.userSetting.setObjectName("userSetting")
        self.gridLayout_3.addWidget(self.userSetting, 0, 0, 1, 1)
        self.xxxxx = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.xxxxx.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx.setText("")
        self.xxxxx.setObjectName("xxxxx")
        self.gridLayout_3.addWidget(self.xxxxx, 2, 2, 1, 1)
        self.xxxxx_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.xxxxx_2.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx_2.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx_2.setText("")
        self.xxxxx_2.setObjectName("xxxxx_2")
        self.gridLayout_3.addWidget(self.xxxxx_2, 2, 3, 1, 1)
        self.simpleData = QtWidgets.QVBoxLayout()
        self.simpleData.setSpacing(0)
        self.simpleData.setObjectName("simpleData")
        self.ModName = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.ModName.setFont(font)
        self.ModName.setObjectName("ModName")
        self.simpleData.addWidget(self.ModName)
        self.UserName = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.UserName.setFont(font)
        self.UserName.setObjectName("UserName")
        self.simpleData.addWidget(self.UserName)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.GamePath = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.GamePath.setFont(font)
        self.GamePath.setObjectName("GamePath")
        self.horizontalLayout_2.addWidget(self.GamePath)
        self.sel_GamePath = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.sel_GamePath.setMinimumSize(QtCore.QSize(20, 20))
        self.sel_GamePath.setMaximumSize(QtCore.QSize(20, 20))
        self.sel_GamePath.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sel_GamePath.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 255);\n"
"}")
        self.sel_GamePath.setText("")
        self.sel_GamePath.setObjectName("sel_GamePath")
        self.horizontalLayout_2.addWidget(self.sel_GamePath)
        self.simpleData.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.gridLayoutWidget_2)
        self.graphicsView_3.setMaximumSize(QtCore.QSize(32, 32))
        self.graphicsView_3.setStyleSheet("border-image: url(:/picture/Data/qrc/tetra.png);")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout.addWidget(self.graphicsView_3)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.simpleData.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.simpleData, 0, 1, 2, 3)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget_2.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgba(240, 240, 240);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(205, 205, 205);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.widget_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 371, 301))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.xxxxx1_2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_2.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_2.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_2.setText("")
        self.xxxxx1_2.setObjectName("xxxxx1_2")
        self.gridLayout_2.addWidget(self.xxxxx1_2, 0, 0, 1, 1)
        self.xxxxx1_5 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_5.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_5.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_5.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_5.setText("")
        self.xxxxx1_5.setObjectName("xxxxx1_5")
        self.gridLayout_2.addWidget(self.xxxxx1_5, 2, 3, 1, 1)
        self.xxxxx1_3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_3.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_3.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_3.setText("")
        self.xxxxx1_3.setObjectName("xxxxx1_3")
        self.gridLayout_2.addWidget(self.xxxxx1_3, 0, 3, 1, 1)
        self.xxxxx1_4 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_4.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_4.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_4.setText("")
        self.xxxxx1_4.setObjectName("xxxxx1_4")
        self.gridLayout_2.addWidget(self.xxxxx1_4, 2, 0, 1, 1)
        self.xxxxx1_6 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_6.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_6.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_6.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_6.setText("")
        self.xxxxx1_6.setObjectName("xxxxx1_6")
        self.gridLayout_2.addWidget(self.xxxxx1_6, 0, 1, 1, 1)
        self.xxxxx1_7 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_7.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_7.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_7.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_7.setText("")
        self.xxxxx1_7.setObjectName("xxxxx1_7")
        self.gridLayout_2.addWidget(self.xxxxx1_7, 0, 2, 1, 1)
        self.xxxxx1_8 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_8.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_8.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_8.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_8.setText("")
        self.xxxxx1_8.setObjectName("xxxxx1_8")
        self.gridLayout_2.addWidget(self.xxxxx1_8, 1, 0, 1, 1)
        self.xxxxx1_9 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_9.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_9.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_9.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_9.setText("")
        self.xxxxx1_9.setObjectName("xxxxx1_9")
        self.gridLayout_2.addWidget(self.xxxxx1_9, 1, 1, 1, 1)
        self.xxxxx1_10 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_10.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_10.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_10.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_10.setText("")
        self.xxxxx1_10.setObjectName("xxxxx1_10")
        self.gridLayout_2.addWidget(self.xxxxx1_10, 1, 2, 1, 1)
        self.xxxxx1_11 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_11.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_11.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_11.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_11.setText("")
        self.xxxxx1_11.setObjectName("xxxxx1_11")
        self.gridLayout_2.addWidget(self.xxxxx1_11, 1, 3, 1, 1)
        self.xxxxx1_12 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_12.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_12.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_12.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_12.setText("")
        self.xxxxx1_12.setObjectName("xxxxx1_12")
        self.gridLayout_2.addWidget(self.xxxxx1_12, 2, 1, 1, 1)
        self.xxxxx1_13 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.xxxxx1_13.setMinimumSize(QtCore.QSize(64, 64))
        self.xxxxx1_13.setMaximumSize(QtCore.QSize(64, 64))
        self.xxxxx1_13.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.xxxxx1_13.setText("")
        self.xxxxx1_13.setObjectName("xxxxx1_13")
        self.gridLayout_2.addWidget(self.xxxxx1_13, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.OnlineServer = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.OnlineServer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.OnlineServer.setStyleSheet("QTextBrowser{\n"
"    background-image:url(:/picture/Data/qrc/server.png);\n"
"}")
        self.OnlineServer.setObjectName("OnlineServer")
        self.gridLayout.addWidget(self.OnlineServer, 1, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnMinimumWidth(2, 1)
        self.gridLayout.setRowMinimumHeight(0, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.ContentTabList.addTab(self.HomeTab, "")
        self.Interface.addWidget(self.ContentTabList)
        self.Interface.setStretch(0, 1)
        self.Interface.setStretch(1, 20)
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        self.ContentTabList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AL-IDE"))
        self.EXETitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">AL-IDE 1.0.0.1</span></p></body></html>"))
        self.min_window.setToolTip(_translate("MainWindow", "<html><head/><body><p>最小化</p></body></html>"))
        self.min_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.max_window.setToolTip(_translate("MainWindow", "<html><head/><body><p>最大化</p></body></html>"))
        self.max_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.close_window.setToolTip(_translate("MainWindow", "<html><head/><body><p>关闭</p></body></html>"))
        self.close_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.HomeTab.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.CardControler.setToolTip(_translate("MainWindow", "<html><head/><body><p>卡牌管理</p></body></html>"))
        self.CardControler.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">卡牌管理</span></p></body></html>"))
        self.CommandList.setToolTip(_translate("MainWindow", "<html><head/><body><p>指令列表</p></body></html>"))
        self.CommandList.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">指令列表</span></p></body></html>"))
        self.CommandList_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>卡牌酒馆</p></body></html>"))
        self.CommandList_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">卡牌酒馆</span></p></body></html>"))
        self.userData.setToolTip(_translate("MainWindow", "<html><head/><body><p>我的</p></body></html>"))
        self.userSetting.setToolTip(_translate("MainWindow", "<html><head/><body><p>设置</p></body></html>"))
        self.ModName.setToolTip(_translate("MainWindow", "<html><head/><body><p>模组名</p></body></html>"))
        self.ModName.setText(_translate("MainWindow", "*Mod"))
        self.UserName.setToolTip(_translate("MainWindow", "<html><head/><body><p>用户名</p></body></html>"))
        self.UserName.setText(_translate("MainWindow", "无名"))
        self.GamePath.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.GamePath.setText(_translate("MainWindow", "D:"))
        self.sel_GamePath.setToolTip(_translate("MainWindow", "<html><head/><body><p>设置游戏本体路径</p></body></html>"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>原石积分</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "∞"))
        self.OnlineServer.setToolTip(_translate("MainWindow", "<html><head/><body><p>卡牌酒馆</p></body></html>"))
        self.OnlineServer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">联机大厅(已死)</span></p></body></html>"))
        self.ContentTabList.setTabText(self.ContentTabList.indexOf(self.HomeTab), _translate("MainWindow", "主页"))
from . import AL_IDE_MainInterFace_rc
