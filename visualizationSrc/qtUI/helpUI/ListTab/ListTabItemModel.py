# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\helpUI\ListTab\ListTabItemModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listItem(object):
    def setupUi(self, listItem):
        listItem.setObjectName("listItem")
        listItem.resize(150, 50)
        listItem.setMinimumSize(QtCore.QSize(150, 50))
        listItem.setMaximumSize(QtCore.QSize(150, 50))
        listItem.setStyleSheet("#listItem{background-color: rgb(255, 255, 255);}\n"
"#listItem:hover{background-color: rgb(229, 229, 229);}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(listItem)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 151, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 8, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ico = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ico.setMaximumSize(QtCore.QSize(32, 32))
        self.ico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ico.setStyleSheet("border-image: url(:/picture/Data/qrc/Unknown.png);")
        self.ico.setText("")
        self.ico.setObjectName("ico")
        self.horizontalLayout.addWidget(self.ico)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.content = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.content.setFont(font)
        self.content.setObjectName("content")
        self.verticalLayout.addWidget(self.content)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.removeBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeBTN.setMinimumSize(QtCore.QSize(16, 16))
        self.removeBTN.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.removeBTN.setFont(font)
        self.removeBTN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeBTN.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-image: url(:/ico/Data/qrc/ico/close.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/closed.png);\n"
"}")
        self.removeBTN.setText("")
        self.removeBTN.setObjectName("removeBTN")
        self.horizontalLayout.addWidget(self.removeBTN)

        self.retranslateUi(listItem)
        QtCore.QMetaObject.connectSlotsByName(listItem)

    def retranslateUi(self, listItem):
        _translate = QtCore.QCoreApplication.translate
        listItem.setWindowTitle(_translate("listItem", "Form"))
        self.title.setText(_translate("listItem", "TextLabel"))
        self.content.setText(_translate("listItem", "TextLabel"))
        self.removeBTN.setToolTip(_translate("listItem", "<html><head/><body><p>关闭标签</p></body></html>"))
from ... import AL_IDE_MainInterFace_rc
