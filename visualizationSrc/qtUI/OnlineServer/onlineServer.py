# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/OnlineServer/onlineServer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1152, 651)
        Form.setStyleSheet("#ScrollWidget{\n"
"    background-color: rgba(255, 255, 255);\n"
"}\n"
"#toFirstBtn{\n"
"    border-image: url(:/ico/Data/qrc/ico/first.png);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border-radius: 5px;\n"
"}\n"
"#toFirstBtn:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/firsted.png);\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: rgb(216, 216, 216);\n"
"    min-height: 5px;\n"
"    border-radius: 5px;\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(710, 590, 41, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toFirstBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.toFirstBtn.setMinimumSize(QtCore.QSize(32, 32))
        self.toFirstBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.toFirstBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toFirstBtn.setText("")
        self.toFirstBtn.setObjectName("toFirstBtn")
        self.verticalLayout.addWidget(self.toFirstBtn)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 1131, 52))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.Search = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.Search.setContentsMargins(0, 0, 0, 0)
        self.Search.setSpacing(10)
        self.Search.setObjectName("Search")
        self.Search_Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.Search_Input.setStyleSheet("#Search_Input{\n"
"    margin: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"}")
        self.Search_Input.setObjectName("Search_Input")
        self.Search.addWidget(self.Search_Input)
        self.horizontalWidget_7 = QtWidgets.QWidget(self.horizontalLayoutWidget_3)
        self.horizontalWidget_7.setStyleSheet("QPushButton{\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"#buildRoom{\n"
"    border-image: url(:/ico/Data/qrc/ico/build.png);\n"
"}\n"
"#buildRoom:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/builded.png);\n"
"}\n"
"#refreshRoom{\n"
"    border-image: url(:/ico/Data/qrc/ico/refresh.png);\n"
"}\n"
"#refreshRoom:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/refreshed.png);\n"
"}")
        self.horizontalWidget_7.setObjectName("horizontalWidget_7")
        self.btnList_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_7)
        self.btnList_4.setContentsMargins(5, 1, 5, 1)
        self.btnList_4.setSpacing(5)
        self.btnList_4.setObjectName("btnList_4")
        self.buildRoom = QtWidgets.QPushButton(self.horizontalWidget_7)
        self.buildRoom.setMinimumSize(QtCore.QSize(32, 32))
        self.buildRoom.setMaximumSize(QtCore.QSize(32, 32))
        self.buildRoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buildRoom.setText("")
        self.buildRoom.setObjectName("buildRoom")
        self.btnList_4.addWidget(self.buildRoom)
        self.refreshRoom = QtWidgets.QPushButton(self.horizontalWidget_7)
        self.refreshRoom.setMinimumSize(QtCore.QSize(32, 32))
        self.refreshRoom.setMaximumSize(QtCore.QSize(32, 32))
        self.refreshRoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshRoom.setText("")
        self.refreshRoom.setObjectName("refreshRoom")
        self.btnList_4.addWidget(self.refreshRoom)
        self.Search.addWidget(self.horizontalWidget_7)
        self.Search.setStretch(0, 1)
        self.Search.setStretch(1, 2)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(750, 590, 391, 41))
        self.widget.setStyleSheet("QPushButton{\n"
"    background: rgba(205, 205, 205);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    color: white;\n"
"    background: rgba(44, 44, 44);\n"
"}\n"
"#leftBTN{\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-image: url(:/ico/Data/qrc/ico/left-square.png);\n"
"}\n"
"#leftBTN:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/left-squared.png);\n"
"}\n"
"#rightBTN{\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-image: url(:/ico/Data/qrc/ico/right-square.png);\n"
"}\n"
"#rightBTN:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/right-squared.png);\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 391, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.pageBTN_List = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.pageBTN_List.setContentsMargins(0, 0, 0, 0)
        self.pageBTN_List.setObjectName("pageBTN_List")
        self.leftBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.leftBTN.setMinimumSize(QtCore.QSize(32, 32))
        self.leftBTN.setMaximumSize(QtCore.QSize(32, 32))
        self.leftBTN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftBTN.setText("")
        self.leftBTN.setObjectName("leftBTN")
        self.pageBTN_List.addWidget(self.leftBTN)
        self.rightBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.rightBTN.setMinimumSize(QtCore.QSize(32, 32))
        self.rightBTN.setMaximumSize(QtCore.QSize(32, 32))
        self.rightBTN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rightBTN.setText("")
        self.rightBTN.setObjectName("rightBTN")
        self.pageBTN_List.addWidget(self.rightBTN)
        self.cardScroll = QtWidgets.QScrollArea(Form)
        self.cardScroll.setGeometry(QtCore.QRect(10, 70, 1131, 511))
        self.cardScroll.setStyleSheet("")
        self.cardScroll.setWidgetResizable(True)
        self.cardScroll.setObjectName("cardScroll")
        self.ScrollWidget = QtWidgets.QWidget()
        self.ScrollWidget.setGeometry(QtCore.QRect(0, 0, 1119, 2000))
        self.ScrollWidget.setMinimumSize(QtCore.QSize(0, 2000))
        self.ScrollWidget.setObjectName("ScrollWidget")
        self.cardScroll.setWidget(self.ScrollWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toFirstBtn.setToolTip(_translate("Form", "<html><head/><body><p>第一页</p></body></html>"))
        self.Search_Input.setPlaceholderText(_translate("Form", "搜索想查找的房间的名字(回车搜索)"))
        self.buildRoom.setToolTip(_translate("Form", "<html><head/><body><p>建房</p></body></html>"))
        self.refreshRoom.setToolTip(_translate("Form", "<html><head/><body><p>刷新</p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
