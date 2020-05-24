# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/OnlineServer/dialog/createRoomDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.roomName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.roomName.setClearButtonEnabled(False)
        self.roomName.setObjectName("roomName")
        self.verticalLayout.addWidget(self.roomName)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.roomDesp = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.roomDesp.setObjectName("roomDesp")
        self.verticalLayout.addWidget(self.roomDesp)
        self.createRoom = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.createRoom.setObjectName("createRoom")
        self.verticalLayout.addWidget(self.createRoom)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "房间名"))
        self.label_2.setText(_translate("Dialog", "介绍"))
        self.roomDesp.setPlaceholderText(_translate("Dialog", "介绍一下自己的房间吧(未开发)"))
        self.createRoom.setText(_translate("Dialog", "创建"))
