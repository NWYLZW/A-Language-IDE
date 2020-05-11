# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addCard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from visualizationSrc.Util.TextEditorUtil import TextEditor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 640)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1152, 640))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Main.setObjectName("Main")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Main)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1151, 642))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget_2)
        self.tabWidget.setMaximumSize(QtCore.QSize(384, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.baseSetting = QtWidgets.QWidget()
        self.baseSetting.setObjectName("baseSetting")
        self.scrollArea = QtWidgets.QScrollArea(self.baseSetting)
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
        self.data01_2 = QtWidgets.QHBoxLayout()
        self.data01_2.setSpacing(0)
        self.data01_2.setObjectName("data01_2")
        self.L_price_2 = QtWidgets.QHBoxLayout()
        self.L_price_2.setSpacing(0)
        self.L_price_2.setObjectName("L_price_2")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.L_price_2.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.L_price_2.addWidget(self.lineEdit_4)
        self.data01_2.addLayout(self.L_price_2)
        self.L_displayName_2 = QtWidgets.QHBoxLayout()
        self.L_displayName_2.setSpacing(0)
        self.L_displayName_2.setObjectName("L_displayName_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.L_displayName_2.addWidget(self.label_7)
        self.spinBox_3 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.L_displayName_2.addWidget(self.spinBox_3)
        self.data01_2.addLayout(self.L_displayName_2)
        self.L_energyReq_2 = QtWidgets.QHBoxLayout()
        self.L_energyReq_2.setSpacing(0)
        self.L_energyReq_2.setObjectName("L_energyReq_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.L_energyReq_2.addWidget(self.label_9)
        self.spinBox_4 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.L_energyReq_2.addWidget(self.spinBox_4)
        self.data01_2.addLayout(self.L_energyReq_2)
        self.data01_2.setStretch(0, 2)
        self.data01_2.setStretch(1, 1)
        self.data01_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.data01_2)
        self.data01_3 = QtWidgets.QHBoxLayout()
        self.data01_3.setSpacing(0)
        self.data01_3.setObjectName("data01_3")
        self.L_displayName_3 = QtWidgets.QHBoxLayout()
        self.L_displayName_3.setSpacing(0)
        self.L_displayName_3.setObjectName("L_displayName_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.L_displayName_3.addWidget(self.label_11)
        self.spinBox_5 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_5.setObjectName("spinBox_5")
        self.L_displayName_3.addWidget(self.spinBox_5)
        self.data01_3.addLayout(self.L_displayName_3)
        self.data01_3.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.data01_3)
        self.data01_4 = QtWidgets.QHBoxLayout()
        self.data01_4.setSpacing(0)
        self.data01_4.setObjectName("data01_4")
        self.L_price_3 = QtWidgets.QHBoxLayout()
        self.L_price_3.setSpacing(0)
        self.L_price_3.setObjectName("L_price_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.L_price_3.addWidget(self.label_5)
        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.L_price_3.addWidget(self.textEdit_3)
        self.data01_4.addLayout(self.L_price_3)
        self.data01_4.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.data01_4)
        self.data01 = QtWidgets.QHBoxLayout()
        self.data01.setSpacing(0)
        self.data01.setObjectName("data01")
        self.L_price = QtWidgets.QHBoxLayout()
        self.L_price.setSpacing(0)
        self.L_price.setObjectName("L_price")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.L_price.addWidget(self.label_4)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.L_price.addWidget(self.textEdit_2)
        self.data01.addLayout(self.L_price)
        self.data01.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.data01)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.baseSetting, "")
        self.greateSetting = QtWidgets.QWidget()
        self.greateSetting.setObjectName("greateSetting")
        self.tabWidget.addTab(self.greateSetting, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.main = QtWidgets.QVBoxLayout()
        self.main.setContentsMargins(20, 20, 20, 20)
        self.main.setObjectName("main")
        self.header = QtWidgets.QVBoxLayout()
        self.header.setObjectName("header")
        self.title_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.title_2.setStyleSheet("font: 9pt \"Adobe 黑体 Std R\";\n"
"\n"
"text-align: center;\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.header.addWidget(self.title_2)
        self.main.addLayout(self.header)
        self.contenter = QtWidgets.QHBoxLayout()
        self.contenter.setObjectName("contenter")
        self.textEdit = QtWidgets.QVBoxLayout()
        self.textEdit.setObjectName("textEdit")
        self.code = QtWidgets.QVBoxLayout()
        self.code.setObjectName("code")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("padding:15px;\n"
"\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.label_2.setObjectName("label_2")
        self.code.addWidget(self.label_2)
        self.codeSource = TextEditor(self.horizontalLayoutWidget_2)
        self.codeSource.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.codeSource.setObjectName("codeSource")
        self.code.addWidget(self.codeSource)
        self.textEdit.addLayout(self.code)
        self.remap = QtWidgets.QVBoxLayout()
        self.remap.setObjectName("remap")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setStyleSheet("padding:15px;\n"
"\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.label_8.setObjectName("label_8")
        self.remap.addWidget(self.label_8)
        self.remapCodeSource = TextEditor(self.horizontalLayoutWidget_2)
        self.remapCodeSource.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.remapCodeSource.setObjectName("remapCodeSource")
        self.remap.addWidget(self.remapCodeSource)
        self.textEdit.addLayout(self.remap)
        self.contenter.addLayout(self.textEdit)
        self.main.addLayout(self.contenter)
        self.footer = QtWidgets.QHBoxLayout()
        self.footer.setObjectName("footer")
        self.add = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 150, 255);\n"
"\n"
"margin-left:100px;\n"
"margin-right:100px;\n"
"padding:10px;\n"
"border-radius:20px;")
        self.add.setObjectName("add")
        self.footer.addWidget(self.add)
        self.clear = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 150, 255);\n"
"\n"
"margin-left:100px;\n"
"margin-right:100px;\n"
"padding:10px;\n"
"border-radius:20px;")
        self.clear.setObjectName("clear")
        self.footer.addWidget(self.clear)
        self.main.addLayout(self.footer)
        self.horizontalLayout.addLayout(self.main)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "卡片名"))
        self.label_7.setText(_translate("MainWindow", "花费"))
        self.label_9.setText(_translate("MainWindow", "消耗能量"))
        self.label_11.setText(_translate("MainWindow", "作用范围"))
        self.label_5.setText(_translate("MainWindow", "卡牌介绍"))
        self.label_4.setText(_translate("MainWindow", "故事"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.baseSetting), _translate("MainWindow", "基础设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.greateSetting), _translate("MainWindow", "高级设置"))
        self.title_2.setText(_translate("MainWindow", "添加新卡片"))
        self.label_2.setText(_translate("MainWindow", "Code代码"))
        self.codeSource.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Remap Code代码"))
        self.remapCodeSource.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.add.setText(_translate("MainWindow", "清空"))
        self.clear.setText(_translate("MainWindow", "添加"))
