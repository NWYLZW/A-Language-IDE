# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\messageBox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Message_Box(object):
    def setupUi(self, Message_Box):
        Message_Box.setObjectName("Message_Box")
        Message_Box.resize(511, 162)
        Message_Box.setStyleSheet("#Message_Box{\n"
"    background-color:rgb(0, 0, 0);\n"
"}\n"
"#Message_Box_widget{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.Message_Box_widget = QtWidgets.QWidget(Message_Box)
        self.Message_Box_widget.setGeometry(QtCore.QRect(10, 10, 491, 141))
        self.Message_Box_widget.setObjectName("Message_Box_widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Message_Box_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 491, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MessageKindImg = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.MessageKindImg.setMaximumSize(QtCore.QSize(64, 64))
        self.MessageKindImg.setStyleSheet("#MessageKindImg{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-image: url(:/message/Data/qrc/message/information.png);\n"
"}")
        self.MessageKindImg.setObjectName("MessageKindImg")
        self.horizontalLayout.addWidget(self.MessageKindImg)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MessageTitle = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.MessageTitle.setStyleSheet("#MessageTitle{\n"
"    padding: 5px;\n"
"    color: rgb(100, 100, 100);\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"}")
        self.MessageTitle.setObjectName("MessageTitle")
        self.verticalLayout.addWidget(self.MessageTitle)
        self.MessageContent = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.MessageContent.setStyleSheet("#MessageContent{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.MessageContent.setObjectName("MessageContent")
        self.verticalLayout.addWidget(self.MessageContent)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.messageKindName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.messageKindName.setStyleSheet("QLabel{\n"
"    color: rgb(140, 140, 140);\n"
"}")
        self.messageKindName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.messageKindName.setObjectName("messageKindName")
        self.horizontalLayout_2.addWidget(self.messageKindName)
        self.messageDateTime = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.messageDateTime.setStyleSheet("QLabel{\n"
"    color: rgb(140, 140, 140);\n"
"}")
        self.messageDateTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.messageDateTime.setObjectName("messageDateTime")
        self.horizontalLayout_2.addWidget(self.messageDateTime)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Message_Box)
        QtCore.QMetaObject.connectSlotsByName(Message_Box)

    def retranslateUi(self, Message_Box):
        _translate = QtCore.QCoreApplication.translate
        Message_Box.setWindowTitle(_translate("Message_Box", "Form"))
        self.MessageTitle.setText(_translate("Message_Box", "标题"))
        self.MessageContent.setHtml(_translate("Message_Box", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">没有内容</p></body></html>"))
        self.messageKindName.setText(_translate("Message_Box", "TextLabel"))
        self.messageDateTime.setText(_translate("Message_Box", "TextLabel"))
from . import AL_IDE_MainInterFace_rc
