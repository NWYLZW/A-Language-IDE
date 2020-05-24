# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/OnlineServer/roomItemModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(483, 221)
        Form.setMinimumSize(QtCore.QSize(0, 220))
        Form.setStyleSheet("#From{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.RoomItemModel = QtWidgets.QWidget(Form)
        self.RoomItemModel.setGeometry(QtCore.QRect(10, 10, 461, 201))
        self.RoomItemModel.setStyleSheet("#RoomItemModel{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QTextBrowser{\n"
"    border: none;\n"
"}\n"
"QPushButton{\n"
"    border: 1px solid gray;\n"
"}\n"
"#joinRoom{\n"
"    border-image: url(:/ico/Data/qrc/ico/join.png);\n"
"}\n"
"#joinRoom:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/joined.png);\n"
"}\n"
"#reportRoom{\n"
"    border-image: url(:/ico/Data/qrc/ico/report.png);\n"
"}\n"
"#reportRoom:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/reported.png);\n"
"}")
        self.RoomItemModel.setObjectName("RoomItemModel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.RoomItemModel)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 201))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 100))
        self.label.setMaximumSize(QtCore.QSize(200, 100))
        self.label.setStyleSheet("border-image: url(:/picture/Data/qrc/roomImg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roomNameAndId = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.roomNameAndId.setFont(font)
        self.roomNameAndId.setObjectName("roomNameAndId")
        self.verticalLayout.addWidget(self.roomNameAndId)
        self.roomerName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.roomerName.setFont(font)
        self.roomerName.setObjectName("roomerName")
        self.verticalLayout.addWidget(self.roomerName)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.roomUsersCount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.roomUsersCount.setFont(font)
        self.roomUsersCount.setObjectName("roomUsersCount")
        self.verticalLayout.addWidget(self.roomUsersCount)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.joinRoom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.joinRoom.setMinimumSize(QtCore.QSize(32, 32))
        self.joinRoom.setMaximumSize(QtCore.QSize(32, 32))
        self.joinRoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.joinRoom.setText("")
        self.joinRoom.setObjectName("joinRoom")
        self.verticalLayout_2.addWidget(self.joinRoom)
        self.reportRoom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reportRoom.setMinimumSize(QtCore.QSize(32, 32))
        self.reportRoom.setMaximumSize(QtCore.QSize(32, 32))
        self.reportRoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reportRoom.setText("")
        self.reportRoom.setObjectName("reportRoom")
        self.verticalLayout_2.addWidget(self.reportRoom)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButton_4.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(32, 32))
        self.pushButton_2.setMaximumSize(QtCore.QSize(32, 32))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.roomNameAndId.setText(_translate("Form", "无名(ID:1)"))
        self.roomerName.setText(_translate("Form", "房主"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Adobe 黑体 Std R\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:600;\">房主还没有写介绍哦</span></p></body></html>"))
        self.roomUsersCount.setText(_translate("Form", "人数"))
        self.joinRoom.setToolTip(_translate("Form", "<html><head/><body><p>连线房间</p></body></html>"))
        self.reportRoom.setToolTip(_translate("Form", "<html><head/><body><p>举报房间</p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
