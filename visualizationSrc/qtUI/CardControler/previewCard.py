# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\CardControler\previewCard.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(200, 270)
        main.setMinimumSize(QtCore.QSize(200, 270))
        main.setMaximumSize(QtCore.QSize(200, 270))
        main.setStyleSheet("#main{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.cardShow = QtWidgets.QWidget(main)
        self.cardShow.setGeometry(QtCore.QRect(10, 10, 180, 250))
        self.cardShow.setMinimumSize(QtCore.QSize(180, 250))
        self.cardShow.setMaximumSize(QtCore.QSize(180, 250))
        self.cardShow.setStyleSheet("QTextBrowser{\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    width: 6px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: rgb(216, 216, 216);\n"
"    min-height: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"    background-color: rgb(181, 181, 181);\n"
"}\n"
"QScrollBar::sub-line:vertical\n"
",QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 0px;\n"
"    height: 0;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
",QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    height: 0px;\n"
"    width: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
",QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.cardShow.setObjectName("cardShow")
        self.backgroundImg = QtWidgets.QLabel(self.cardShow)
        self.backgroundImg.setGeometry(QtCore.QRect(-70, -30, 310, 310))
        self.backgroundImg.setMinimumSize(QtCore.QSize(0, 0))
        self.backgroundImg.setMaximumSize(QtCore.QSize(310, 310))
        self.backgroundImg.setStyleSheet("#backgroundImg{border-image: url(:/picture/Data/qrc/Card.png);}")
        self.backgroundImg.setText("")
        self.backgroundImg.setObjectName("backgroundImg")
        self.cardArt = QtWidgets.QLabel(self.cardShow)
        self.cardArt.setGeometry(QtCore.QRect(50, 40, 81, 81))
        self.cardArt.setStyleSheet("#cardArt{border-image: url(:/picture/Data/qrc/Unknown.png);}")
        self.cardArt.setText("")
        self.cardArt.setObjectName("cardArt")
        self.description = QtWidgets.QTextBrowser(self.cardShow)
        self.description.setGeometry(QtCore.QRect(40, 140, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.description.setFont(font)
        self.description.setStyleSheet("")
        self.description.setObjectName("description")
        self.cardName = QtWidgets.QTextBrowser(self.cardShow)
        self.cardName.setGeometry(QtCore.QRect(35, 105, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cardName.setFont(font)
        self.cardName.setStyleSheet("")
        self.cardName.setObjectName("cardName")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.description.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe 黑体 Std R\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">还没有介绍哦~</p></body></html>"))
        self.cardName.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe 黑体 Std R\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">无名</span></p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
