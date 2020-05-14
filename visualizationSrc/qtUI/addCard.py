# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/addCard.ui'
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.CardMakeTab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1151, 642))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.CM_addNewCard = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.CM_addNewCard.setContentsMargins(0, 0, 0, 0)
        self.CM_addNewCard.setObjectName("CM_addNewCard")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CMT_settingTab = QtWidgets.QTabWidget(self.horizontalLayoutWidget_2)
        self.CMT_settingTab.setMaximumSize(QtCore.QSize(384, 16777215))
        self.CMT_settingTab.setObjectName("CMT_settingTab")
        self.CMT_baseSetting = QtWidgets.QWidget()
        self.CMT_baseSetting.setObjectName("CMT_baseSetting")
        self.scrollArea = QtWidgets.QScrollArea(self.CMT_baseSetting)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 361, 601))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 599))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(359, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 361, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.data03 = QtWidgets.QHBoxLayout()
        self.data03.setSpacing(0)
        self.data03.setObjectName("data03")
        self.L_displayName = QtWidgets.QHBoxLayout()
        self.L_displayName.setSpacing(0)
        self.L_displayName.setObjectName("L_displayName")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.L_displayName.addWidget(self.label_6)
        self.CM_displayName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CM_displayName.setObjectName("CM_displayName")
        self.L_displayName.addWidget(self.CM_displayName)
        self.data03.addLayout(self.L_displayName)
        self.L_price_2 = QtWidgets.QHBoxLayout()
        self.L_price_2.setSpacing(0)
        self.L_price_2.setObjectName("L_price_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.L_price_2.addWidget(self.label_7)
        self.CM_price = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.CM_price.setObjectName("CM_price")
        self.L_price_2.addWidget(self.CM_price)
        self.data03.addLayout(self.L_price_2)
        self.L_energyReq_2 = QtWidgets.QHBoxLayout()
        self.L_energyReq_2.setSpacing(0)
        self.L_energyReq_2.setObjectName("L_energyReq_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.L_energyReq_2.addWidget(self.label_9)
        self.CM_energyReq = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.CM_energyReq.setObjectName("CM_energyReq")
        self.L_energyReq_2.addWidget(self.CM_energyReq)
        self.data03.addLayout(self.L_energyReq_2)
        self.data03.setStretch(0, 2)
        self.data03.setStretch(1, 1)
        self.data03.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.data03)
        self.data04 = QtWidgets.QHBoxLayout()
        self.data04.setSpacing(0)
        self.data04.setObjectName("data04")
        self.L_displayName_3 = QtWidgets.QHBoxLayout()
        self.L_displayName_3.setSpacing(0)
        self.L_displayName_3.setObjectName("L_displayName_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.L_displayName_3.addWidget(self.label_11)
        self.CM_range = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.CM_range.setObjectName("CM_range")
        self.L_displayName_3.addWidget(self.CM_range)
        self.data04.addLayout(self.L_displayName_3)
        self.data04.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.data04)
        self.data02 = QtWidgets.QHBoxLayout()
        self.data02.setSpacing(0)
        self.data02.setObjectName("data02")
        self.L_price_3 = QtWidgets.QHBoxLayout()
        self.L_price_3.setSpacing(0)
        self.L_price_3.setObjectName("L_price_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.L_price_3.addWidget(self.label_5)
        self.CM_description = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.CM_description.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.CM_description.setObjectName("CM_description")
        self.L_price_3.addWidget(self.CM_description)
        self.L_price_3.setStretch(0, 1)
        self.L_price_3.setStretch(1, 4)
        self.data02.addLayout(self.L_price_3)
        self.data02.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.data02)
        self.data01 = QtWidgets.QHBoxLayout()
        self.data01.setSpacing(0)
        self.data01.setObjectName("data01")
        self.L_price = QtWidgets.QHBoxLayout()
        self.L_price.setSpacing(0)
        self.L_price.setObjectName("L_price")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.L_price.addWidget(self.label_4)
        self.CM_story0 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.CM_story0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.CM_story0.setObjectName("CM_story0")
        self.L_price.addWidget(self.CM_story0)
        self.L_price.setStretch(0, 1)
        self.L_price.setStretch(1, 4)
        self.data01.addLayout(self.L_price)
        self.data01.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.data01)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.CMT_settingTab.addTab(self.CMT_baseSetting, "")
        self.CMT_greateSetting = QtWidgets.QWidget()
        self.CMT_greateSetting.setObjectName("CMT_greateSetting")
        self.CMT_settingTab.addTab(self.CMT_greateSetting, "")
        self.verticalLayout.addWidget(self.CMT_settingTab)
        self.CM_addNewCard.addLayout(self.verticalLayout)
        self.CM_main = QtWidgets.QVBoxLayout()
        self.CM_main.setContentsMargins(20, 20, 20, 20)
        self.CM_main.setObjectName("CM_main")
        self.CM_header = QtWidgets.QVBoxLayout()
        self.CM_header.setObjectName("CM_header")
        self.title_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.title_2.setStyleSheet("font: 9pt \"Adobe 黑体 Std R\";\n"
"\n"
"text-align: center;\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.CM_header.addWidget(self.title_2)
        self.CM_main.addLayout(self.CM_header)
        self.CM_contenter = QtWidgets.QHBoxLayout()
        self.CM_contenter.setObjectName("CM_contenter")
        self.textEdit = QtWidgets.QVBoxLayout()
        self.textEdit.setObjectName("textEdit")
        self.cardMakeTap_code = QtWidgets.QVBoxLayout()
        self.cardMakeTap_code.setObjectName("cardMakeTap_code")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("padding:15px;\n"
"\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.label_2.setObjectName("label_2")
        self.cardMakeTap_code.addWidget(self.label_2)
        self.CM_codeSource = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.CM_codeSource.setStyleSheet("")
        self.CM_codeSource.setObjectName("CM_codeSource")
        self.cardMakeTap_code.addWidget(self.CM_codeSource)
        self.textEdit.addLayout(self.cardMakeTap_code)
        self.cardMakeTap_remap = QtWidgets.QVBoxLayout()
        self.cardMakeTap_remap.setObjectName("cardMakeTap_remap")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setStyleSheet("padding:15px;\n"
"\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.label_8.setObjectName("label_8")
        self.cardMakeTap_remap.addWidget(self.label_8)
        self.CM_remapCodeSource = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.CM_remapCodeSource.setStyleSheet("")
        self.CM_remapCodeSource.setObjectName("CM_remapCodeSource")
        self.cardMakeTap_remap.addWidget(self.CM_remapCodeSource)
        self.textEdit.addLayout(self.cardMakeTap_remap)
        self.CM_contenter.addLayout(self.textEdit)
        self.CM_main.addLayout(self.CM_contenter)
        self.CM_footer = QtWidgets.QHBoxLayout()
        self.CM_footer.setObjectName("CM_footer")
        self.CM_clearCardMakeData = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.CM_clearCardMakeData.setFont(font)
        self.CM_clearCardMakeData.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CM_clearCardMakeData.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 150, 255);\n"
"\n"
"margin-left:100px;\n"
"margin-right:100px;\n"
"padding:10px;\n"
"border-radius:20px;")
        self.CM_clearCardMakeData.setObjectName("CM_clearCardMakeData")
        self.CM_footer.addWidget(self.CM_clearCardMakeData)
        self.CM_addCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.CM_addCard.setFont(font)
        self.CM_addCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CM_addCard.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 150, 255);\n"
"\n"
"margin-left:100px;\n"
"margin-right:100px;\n"
"padding:10px;\n"
"border-radius:20px;")
        self.CM_addCard.setObjectName("CM_addCard")
        self.CM_footer.addWidget(self.CM_addCard)
        self.CM_main.addLayout(self.CM_footer)
        self.CM_addNewCard.addLayout(self.CM_main)
        self.CM_addNewCard.setStretch(0, 1)
        self.CM_addNewCard.setStretch(1, 2)
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
        self.CMT_settingTab.setCurrentIndex(0)
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">卡牌制作</span></p></body></html>"))
        self.PeopleMake.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">人物制作</span></p></body></html>"))
        self.ContentTabList.setTabText(self.ContentTabList.indexOf(self.HomeTab), _translate("MainWindow", "Tab 1"))
        self.label_6.setText(_translate("MainWindow", "卡片名"))
        self.label_7.setText(_translate("MainWindow", "花费"))
        self.label_9.setText(_translate("MainWindow", "消耗能量"))
        self.label_11.setText(_translate("MainWindow", "作用范围"))
        self.label_5.setText(_translate("MainWindow", "卡牌介绍"))
        self.label_4.setText(_translate("MainWindow", "故事"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_baseSetting), _translate("MainWindow", "Tab 1"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_greateSetting), _translate("MainWindow", "Tab 2"))
        self.title_2.setText(_translate("MainWindow", "添加新卡片"))
        self.label_2.setText(_translate("MainWindow", "Code代码"))
        self.CM_codeSource.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Remap Code代码"))
        self.CM_remapCodeSource.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CM_clearCardMakeData.setText(_translate("MainWindow", "清空"))
        self.CM_addCard.setText(_translate("MainWindow", "添加"))
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
