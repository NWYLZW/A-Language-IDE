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
        MainWindow.setStyleSheet("#MainWindow{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"#Main{\n"
"    background-color: rgb(255,255,255);\n"
"    margin:10px;\n"
"    border-radius: 10px;\n"
"}\n"
"QTabBar::close-button{\n"
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
        self.Main.setStyleSheet("")
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
"    border:1px solid #afafaf; \n"
"    border-radius:10px;\n"
"}")
        self.ContentTabList.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.ContentTabList.setTabsClosable(True)
        self.ContentTabList.setObjectName("ContentTabList")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setObjectName("HomeTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.HomeTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1151, 631))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("padding:10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setStyleSheet("padding:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 2, 0, 1, 2)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_6.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_6.setStyleSheet("")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout_2.addWidget(self.graphicsView_6, 3, 1, 1, 1)
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_7.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_7.setStyleSheet("")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout_2.addWidget(self.graphicsView_7, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 2, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_4.setStyleSheet("")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 1, 0, 1, 1)
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
"    background-image: url(:/picture/Data/qrc/command.png);\n"
"}")
        self.CommandList_2.setObjectName("CommandList_2")
        self.gridLayout.addWidget(self.CommandList_2, 0, 2, 1, 1)
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
        self.HomeTab.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.HomeTab.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "运行指令到游戏"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">运行结果==&gt;</p></body></html>"))
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
        self.CommandList_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>指令列表</p></body></html>"))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">卡牌广场</span></p></body></html>"))
        self.ContentTabList.setTabText(self.ContentTabList.indexOf(self.HomeTab), _translate("MainWindow", "主页"))
from . import AL_IDE_MainInterFace_rc
