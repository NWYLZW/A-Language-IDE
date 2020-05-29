# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\CommandList\CommandListShowTab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setStyleSheet("#toFirstBtn{\n"
"    border-image: url(:/ico/Data/qrc/ico/first.png);\n"
"}\n"
"#toFirstBtn:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/firsted.png);\n"
"}\n"
"\n"
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
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.topLayer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.topLayer.setMinimumSize(QtCore.QSize(40, 32))
        self.topLayer.setMaximumSize(QtCore.QSize(32, 32))
        self.topLayer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.topLayer.setToolTipDuration(-5)
        self.topLayer.setStyleSheet("#topLayer{border-image: url(:/ico/Data/qrc/ico/topLayer.png);}\n"
"#topLayer:hover{border-image: url(:/ico/Data/qrc/ico/topLayered.png);}")
        self.topLayer.setText("")
        self.topLayer.setObjectName("topLayer")
        self.horizontalLayout.addWidget(self.topLayer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Search_Input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Search_Input.setObjectName("Search_Input")
        self.horizontalLayout_2.addWidget(self.Search_Input)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cardCommandScroll = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.cardCommandScroll.setMinimumSize(QtCore.QSize(0, 0))
        self.cardCommandScroll.setWidgetResizable(True)
        self.cardCommandScroll.setObjectName("cardCommandScroll")
        self.cardCommandScrollWidget = QtWidgets.QWidget()
        self.cardCommandScrollWidget.setGeometry(QtCore.QRect(0, 0, 463, 2000))
        self.cardCommandScrollWidget.setMinimumSize(QtCore.QSize(0, 2000))
        self.cardCommandScrollWidget.setObjectName("cardCommandScrollWidget")
        self.cardCommandScroll.setWidget(self.cardCommandScrollWidget)
        self.verticalLayout.addWidget(self.cardCommandScroll)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toFirstBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.toFirstBtn.setMinimumSize(QtCore.QSize(32, 32))
        self.toFirstBtn.setMaximumSize(QtCore.QSize(32, 32))
        self.toFirstBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toFirstBtn.setText("")
        self.toFirstBtn.setObjectName("toFirstBtn")
        self.verticalLayout_2.addWidget(self.toFirstBtn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 41))
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
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "指令列表"))
        self.topLayer.setToolTip(_translate("Form", "<html><head/><body><p>置顶</p></body></html>"))
        self.Search_Input.setPlaceholderText(_translate("Form", "搜索指令"))
        self.toFirstBtn.setToolTip(_translate("Form", "<html><head/><body><p>第一页</p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
