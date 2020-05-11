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
        MainWindow.resize(768, 640)
        MainWindow.setMinimumSize(QtCore.QSize(768, 640))
        MainWindow.setMaximumSize(QtCore.QSize(768, 640))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.Main = QtWidgets.QWidget(MainWindow)
        self.Main.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Main.setObjectName("Main")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Main)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 771, 641))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.main.setContentsMargins(20, 20, 20, 20)
        self.main.setObjectName("main")
        self.header = QtWidgets.QVBoxLayout()
        self.header.setObjectName("header")
        self.title_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
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
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setStyleSheet("padding:15px;\n"
"\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.label_2.setObjectName("label_2")
        self.code.addWidget(self.label_2)
        self.codeSource = TextEditor(self.verticalLayoutWidget_4)
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
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setStyleSheet("padding:15px;\n"
"\n"
"font-size:20px;\n"
"font-weight:600;\n"
"")
        self.label_8.setObjectName("label_8")
        self.remap.addWidget(self.label_8)
        self.remapCodeSource = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
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
        self.add = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
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
        self.clear = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
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
        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_2.setText(_translate("MainWindow", "添加新卡片"))
        self.label_2.setText(_translate("MainWindow", "Code代码"))
        self.codeSource.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">;</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Remap Code代码"))
        self.remapCodeSource.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">;</span></p></body></html>"))
        self.add.setText(_translate("MainWindow", "清空"))
        self.clear.setText(_translate("MainWindow", "添加"))
