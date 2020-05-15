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
        MainWindow.resize(1200, 720)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 720))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Main.setStyleSheet("")
        self.Main.setObjectName("Main")
        self.ContentTabList = QtWidgets.QTabWidget(self.Main)
        self.ContentTabList.setGeometry(QtCore.QRect(20, 40, 1161, 671))
        self.ContentTabList.setObjectName("ContentTabList")
        self.HomeTab = QtWidgets.QWidget()
        self.HomeTab.setObjectName("HomeTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.HomeTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1161, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_7.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_7.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout_2.addWidget(self.graphicsView_7, 2, 0, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_8.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_8.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout_2.addWidget(self.graphicsView_8, 0, 0, 1, 2)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_6.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_6.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout_2.addWidget(self.graphicsView_6, 2, 1, 1, 1)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_9.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_9.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout_2.addWidget(self.graphicsView_9, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 2, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_2.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 2, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView_4.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.graphicsView_4.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 1, 0, 1, 1)
        self.CardMakeCard = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.CardMakeCard.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CardMakeCard.setStyleSheet("background-image: url(:/picture/Data/qrc/Card.png);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom;\n"
"\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.CardMakeCard.setObjectName("CardMakeCard")
        self.gridLayout.addWidget(self.CardMakeCard, 0, 0, 1, 1)
        self.PeopleMake = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.PeopleMake.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PeopleMake.setStyleSheet("background-image: url(:/picture/Data/qrc/Card.png);\n"
"background-repeat: no-repeat;\n"
"background-position: bottom;\n"
"\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.PeopleMake.setObjectName("PeopleMake")
        self.gridLayout.addWidget(self.PeopleMake, 0, 1, 1, 1)
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
        self.CardMakeTab = QtWidgets.QWidget()
        self.CardMakeTab.setObjectName("CardMakeTab")
        self.CMT_Tab = QtWidgets.QTabWidget(self.CardMakeTab)
        self.CMT_Tab.setGeometry(QtCore.QRect(0, 0, 1151, 651))
        self.CMT_Tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CMT_Tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.CMT_Tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.CMT_Tab.setElideMode(QtCore.Qt.ElideNone)
        self.CMT_Tab.setUsesScrollButtons(True)
        self.CMT_Tab.setDocumentMode(True)
        self.CMT_Tab.setTabsClosable(True)
        self.CMT_Tab.setMovable(True)
        self.CMT_Tab.setTabBarAutoHide(False)
        self.CMT_Tab.setObjectName("CMT_Tab")
        self.CMT_CardList = QtWidgets.QWidget()
        self.CMT_CardList.setObjectName("CMT_CardList")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.CMT_CardList)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 301, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.CMT_C_Search = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.CMT_C_Search.setContentsMargins(0, 0, 0, 0)
        self.CMT_C_Search.setObjectName("CMT_C_Search")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.CMT_C_Search.addWidget(self.label)
        self.CMT_C_Search_Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.CMT_C_Search_Input.setStyleSheet("margin:10px;")
        self.CMT_C_Search_Input.setObjectName("CMT_C_Search_Input")
        self.CMT_C_Search.addWidget(self.CMT_C_Search_Input)
        self.CMT_C_cardScroll = QtWidgets.QScrollArea(self.CMT_CardList)
        self.CMT_C_cardScroll.setGeometry(QtCore.QRect(10, 70, 1111, 571))
        self.CMT_C_cardScroll.setWidgetResizable(True)
        self.CMT_C_cardScroll.setObjectName("CMT_C_cardScroll")
        self.CMT_C_cardScrollWidget = QtWidgets.QWidget()
        self.CMT_C_cardScrollWidget.setGeometry(QtCore.QRect(0, 0, 1109, 569))
        self.CMT_C_cardScrollWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.CMT_C_cardScrollWidget.setObjectName("CMT_C_cardScrollWidget")
        self.CMT_C_cardScroll.setWidget(self.CMT_C_cardScrollWidget)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.CMT_CardList)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(310, 10, 136, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.CMT_C_btnList = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.CMT_C_btnList.setContentsMargins(5, 5, 5, 5)
        self.CMT_C_btnList.setObjectName("CMT_C_btnList")
        self.makeNewCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.makeNewCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.makeNewCard.setStyleSheet("background: #2866bd;\n"
"color: #fff;\n"
"padding: 6px;\n"
"border: none;\n"
"border-radius: 8px;")
        self.makeNewCard.setObjectName("makeNewCard")
        self.CMT_C_btnList.addWidget(self.makeNewCard)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_2.setStyleSheet("background: #2866bd;\n"
"color: #fff;\n"
"padding: 6px;\n"
"border: none;\n"
"border-radius: 8px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.CMT_C_btnList.addWidget(self.pushButton_2)
        self.CMT_Tab.addTab(self.CMT_CardList, "")
        self.CMT_CardDetails_Model = QtWidgets.QWidget()
        self.CMT_CardDetails_Model.setMaximumSize(QtCore.QSize(1127, 651))
        self.CMT_CardDetails_Model.setObjectName("CMT_CardDetails_Model")
        self.CMT_Tab.addTab(self.CMT_CardDetails_Model, "")
        self.ContentTabList.addTab(self.CardMakeTab, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.HeadToolBar = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.HeadToolBar.setContentsMargins(0, 0, 0, 0)
        self.HeadToolBar.setSpacing(0)
        self.HeadToolBar.setObjectName("HeadToolBar")
        self.top_right = QtWidgets.QHBoxLayout()
        self.top_right.setSpacing(0)
        self.top_right.setObjectName("top_right")
        self.EXETitle = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.EXETitle.setMaximumSize(QtCore.QSize(16777215, 24))
        self.EXETitle.setStyleSheet("border: none;")
        self.EXETitle.setObjectName("EXETitle")
        self.top_right.addWidget(self.EXETitle)
        self.HeadToolBar.addLayout(self.top_right)
        self.top_left = QtWidgets.QHBoxLayout()
        self.top_left.setSpacing(10)
        self.top_left.setObjectName("top_left")
        self.max_window = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.max_window.setMaximumSize(QtCore.QSize(24, 24))
        self.max_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.max_window.setStyleSheet("border-image: url(:/ico/Data/qrc/ico/max.png);\n"
"background-size:100%;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.max_window.setObjectName("max_window")
        self.top_left.addWidget(self.max_window)
        self.min_window = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.min_window.setMaximumSize(QtCore.QSize(24, 24))
        self.min_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.min_window.setStyleSheet("border-image: url(:/ico/Data/qrc/ico/min.png);\n"
"background-size:100%;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.min_window.setObjectName("min_window")
        self.top_left.addWidget(self.min_window)
        self.close_window = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.close_window.setMaximumSize(QtCore.QSize(24, 24))
        self.close_window.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_window.setStyleSheet("border-image: url(:/ico/Data/qrc/ico/close.png);\n"
"background-size:100%;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.close_window.setObjectName("close_window")
        self.top_left.addWidget(self.close_window)
        self.HeadToolBar.addLayout(self.top_left)
        self.HeadToolBar.setStretch(0, 10)
        self.HeadToolBar.setStretch(1, 1)
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        self.ContentTabList.setCurrentIndex(0)
        self.CMT_Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AL-IDE"))
        self.HomeTab.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.HomeTab.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.CardMakeCard.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">卡牌管理</span></p></body></html>"))
        self.PeopleMake.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">人物管理</span></p></body></html>"))
        self.ContentTabList.setTabText(self.ContentTabList.indexOf(self.HomeTab), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "搜索"))
        self.makeNewCard.setText(_translate("MainWindow", "制作新卡"))
        self.pushButton_2.setText(_translate("MainWindow", "删除已选"))
        self.CMT_Tab.setTabText(self.CMT_Tab.indexOf(self.CMT_CardList), _translate("MainWindow", "Tab 1"))
        self.CMT_Tab.setTabText(self.CMT_Tab.indexOf(self.CMT_CardDetails_Model), _translate("MainWindow", "Tab 2"))
        self.ContentTabList.setTabText(self.ContentTabList.indexOf(self.CardMakeTab), _translate("MainWindow", "Tab 2"))
        self.EXETitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">AL-IDE 1.0.0.1</span></p></body></html>"))
        self.max_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.min_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.close_window.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
from . import AL_IDE_MainInterFace_rc
