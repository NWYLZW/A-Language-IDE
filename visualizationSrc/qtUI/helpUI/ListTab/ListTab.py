# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\helpUI\ListTab\ListTab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1150, 630)
        Form.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1151, 631))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.MainL = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainL.setContentsMargins(0, 0, 0, 0)
        self.MainL.setSpacing(0)
        self.MainL.setObjectName("MainL")
        self.tabsScrollArea = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.tabsScrollArea.setMinimumSize(QtCore.QSize(150, 0))
        self.tabsScrollArea.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tabsScrollArea.setStyleSheet("#tabsScrollArea{\n"
"    border: none;\n"
"    border-right: 1px solid gray;\n"
"    background-color: rgba(255, 255, 255);\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: rgba(255, 255, 255);\n"
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
"}\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
",QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
",QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.tabsScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tabsScrollArea.setWidgetResizable(True)
        self.tabsScrollArea.setObjectName("tabsScrollArea")
        self.tabsScrollAreaWidget = QtWidgets.QWidget()
        self.tabsScrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 150, 629))
        self.tabsScrollAreaWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.tabsScrollAreaWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.tabsScrollAreaWidget.setStyleSheet("")
        self.tabsScrollAreaWidget.setObjectName("tabsScrollAreaWidget")
        self.tabsScrollArea.setWidget(self.tabsScrollAreaWidget)
        self.MainL.addWidget(self.tabsScrollArea)
        self.mainContent = QtWidgets.QGridLayout()
        self.mainContent.setObjectName("mainContent")
        self.MainL.addLayout(self.mainContent)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
