# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\CardControler\cardLibWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1001, 611)
        main.setMaximumSize(QtCore.QSize(1160, 630))
        main.setStyleSheet("#toFirstBtn{\n"
"    border-image: url(:/ico/Data/qrc/ico/first.png);\n"
"}\n"
"#toFirstBtn:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/firsted.png);\n"
"}\n"
"#cardScroll{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    width: 6px;\n"
"    margin: 0px;border: none;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: rgb(216, 216, 216);\n"
"    min-height: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{background-color: rgb(181, 181, 181);}\n"
"QScrollBar:horizontal\n"
"{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    height: 6px;\n"
"    margin: 0px;border: none;\n"
"}\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: rgb(216, 216, 216);\n"
"    min-width: 5px;\n"
"    border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{background-color: rgb(181, 181, 181);}\n"
"\n"
"QScrollBar::up-arrow, QScrollBar::down-arrow,\n"
"QScrollBar::right-arrow, QScrollBar::left-arrow,\n"
"QScrollBar::add-page, QScrollBar::sub-page,\n"
"QScrollBar::add-line, QScrollBar::sub-line\n"
"{\n"
"    border: none;background: none;color: none;height: 0;\n"
"}")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(main)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1001, 611))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.cardLib = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.cardLib.setContentsMargins(10, 10, 10, 10)
        self.cardLib.setSpacing(10)
        self.cardLib.setObjectName("cardLib")
        self.Search = QtWidgets.QHBoxLayout()
        self.Search.setSpacing(0)
        self.Search.setObjectName("Search")
        self.Search_Input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.Search_Input.setMinimumSize(QtCore.QSize(400, 0))
        self.Search_Input.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Search_Input.setStyleSheet("#Search_Input{\n"
"    margin: 5px;\n"
"    padding: 5px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"}")
        self.Search_Input.setObjectName("Search_Input")
        self.Search.addWidget(self.Search_Input)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Search.addItem(spacerItem)
        self.horizontalWidget_4 = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.horizontalWidget_4.setStyleSheet("QPushButton{\n"
"    background: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"#setting{\n"
"    border-image: url(:/ico/Data/qrc/ico/tool.png);\n"
"}\n"
"#makeNewCard{\n"
"    border-image: url(:/ico/Data/qrc/ico/new.png);\n"
"}\n"
"#makeNewCard:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/newed.png);\n"
"}\n"
"#delSelCard{\n"
"    border-image: url(:/ico/Data/qrc/ico/delete.png);\n"
"}\n"
"#delSelCard:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/deleted.png);\n"
"}\n"
"#copyCard{\n"
"    border-image: url(:/ico/Data/qrc/ico/copy.png);\n"
"}\n"
"#copyCard:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/copied.png);\n"
"}\n"
"#pushToExcel{\n"
"    border-image: url(:/ico/Data/qrc/ico/excel.png);\n"
"}")
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.btnList = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.btnList.setContentsMargins(5, 1, 5, 1)
        self.btnList.setSpacing(5)
        self.btnList.setObjectName("btnList")
        self.setting = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.setting.setMaximumSize(QtCore.QSize(32, 32))
        self.setting.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.setting.setText("")
        self.setting.setObjectName("setting")
        self.btnList.addWidget(self.setting)
        self.makeNewCard = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.makeNewCard.setMaximumSize(QtCore.QSize(32, 32))
        self.makeNewCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.makeNewCard.setStyleSheet("")
        self.makeNewCard.setText("")
        self.makeNewCard.setObjectName("makeNewCard")
        self.btnList.addWidget(self.makeNewCard)
        self.delSelCard = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.delSelCard.setMaximumSize(QtCore.QSize(32, 32))
        self.delSelCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delSelCard.setStyleSheet("")
        self.delSelCard.setText("")
        self.delSelCard.setObjectName("delSelCard")
        self.btnList.addWidget(self.delSelCard)
        self.copyCard = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.copyCard.setMaximumSize(QtCore.QSize(32, 32))
        self.copyCard.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.copyCard.setStyleSheet("")
        self.copyCard.setText("")
        self.copyCard.setObjectName("copyCard")
        self.btnList.addWidget(self.copyCard)
        self.pushToExcel = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.pushToExcel.setMaximumSize(QtCore.QSize(32, 32))
        self.pushToExcel.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushToExcel.setStyleSheet("")
        self.pushToExcel.setText("")
        self.pushToExcel.setObjectName("pushToExcel")
        self.btnList.addWidget(self.pushToExcel)
        self.Search.addWidget(self.horizontalWidget_4)
        self.Search.setStretch(0, 1)
        self.Search.setStretch(2, 2)
        self.cardLib.addLayout(self.Search)
        self.cardScroll = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.cardScroll.setStyleSheet("")
        self.cardScroll.setWidgetResizable(True)
        self.cardScroll.setObjectName("cardScroll")
        self.cardScrollWidget = QtWidgets.QWidget()
        self.cardScrollWidget.setGeometry(QtCore.QRect(0, 0, 975, 2000))
        self.cardScrollWidget.setMinimumSize(QtCore.QSize(0, 2000))
        self.cardScrollWidget.setObjectName("cardScrollWidget")
        self.cardScroll.setWidget(self.cardScrollWidget)
        self.cardLib.addWidget(self.cardScroll)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toFirstBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.toFirstBtn.setMinimumSize(QtCore.QSize(32, 32))
        self.toFirstBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.toFirstBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toFirstBtn.setText("")
        self.toFirstBtn.setObjectName("toFirstBtn")
        self.verticalLayout.addWidget(self.toFirstBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.pageBTN_List = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.pageBTN_List.setContentsMargins(0, 0, 0, 0)
        self.pageBTN_List.setObjectName("pageBTN_List")
        self.leftBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.leftBTN.setMinimumSize(QtCore.QSize(32, 32))
        self.leftBTN.setMaximumSize(QtCore.QSize(32, 32))
        self.leftBTN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftBTN.setText("")
        self.leftBTN.setObjectName("leftBTN")
        self.pageBTN_List.addWidget(self.leftBTN)
        self.rightBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rightBTN.setMinimumSize(QtCore.QSize(32, 32))
        self.rightBTN.setMaximumSize(QtCore.QSize(32, 32))
        self.rightBTN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rightBTN.setText("")
        self.rightBTN.setObjectName("rightBTN")
        self.pageBTN_List.addWidget(self.rightBTN)
        self.horizontalLayout.addWidget(self.widget)
        self.horizontalLayout.setStretch(2, 1)
        self.cardLib.addLayout(self.horizontalLayout)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.Search_Input.setPlaceholderText(_translate("main", "搜索想查找的卡牌的名字(回车搜索)"))
        self.setting.setToolTip(_translate("main", "<html><head/><body><p>设置</p></body></html>"))
        self.makeNewCard.setToolTip(_translate("main", "<html><head/><body><p>新建卡牌</p></body></html>"))
        self.delSelCard.setToolTip(_translate("main", "<html><head/><body><p>移至回收站</p></body></html>"))
        self.copyCard.setToolTip(_translate("main", "<html><head/><body><p>复制卡牌</p></body></html>"))
        self.pushToExcel.setToolTip(_translate("main", "<html><head/><body><p>导出至Excel</p></body></html>"))
        self.toFirstBtn.setToolTip(_translate("main", "<html><head/><body><p>第一页</p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
