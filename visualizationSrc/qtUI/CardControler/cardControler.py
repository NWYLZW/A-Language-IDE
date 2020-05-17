# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/CardControler/cardControler.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1161, 668)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("#Form{\n"
"    padding:10px;\n"
"}")
        self.CardControler_Tabs = QtWidgets.QTabWidget(Form)
        self.CardControler_Tabs.setGeometry(QtCore.QRect(0, 0, 1141, 651))
        self.CardControler_Tabs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.CardControler_Tabs.setTabPosition(QtWidgets.QTabWidget.West)
        self.CardControler_Tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.CardControler_Tabs.setElideMode(QtCore.Qt.ElideNone)
        self.CardControler_Tabs.setUsesScrollButtons(True)
        self.CardControler_Tabs.setDocumentMode(True)
        self.CardControler_Tabs.setTabsClosable(True)
        self.CardControler_Tabs.setMovable(True)
        self.CardControler_Tabs.setTabBarAutoHide(False)
        self.CardControler_Tabs.setObjectName("CardControler_Tabs")
        self.CardList = QtWidgets.QWidget()
        self.CardList.setObjectName("CardList")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.CardList)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 371, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.Search = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.Search.setContentsMargins(0, 0, 0, 0)
        self.Search.setObjectName("Search")
        self.Search_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.Search_label.setObjectName("Search_label")
        self.Search.addWidget(self.Search_label)
        self.Search_Input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.Search_Input.setStyleSheet("#Search_Input{\n"
"    margin: 5px;\n"
"    padding: 5px;\n"
"}")
        self.Search_Input.setObjectName("Search_Input")
        self.Search.addWidget(self.Search_Input)
        self.cardScroll = QtWidgets.QScrollArea(self.CardList)
        self.cardScroll.setGeometry(QtCore.QRect(20, 70, 1091, 571))
        self.cardScroll.setWidgetResizable(True)
        self.cardScroll.setObjectName("cardScroll")
        self.cardScrollWidget = QtWidgets.QWidget()
        self.cardScrollWidget.setGeometry(QtCore.QRect(0, 0, 1089, 569))
        self.cardScrollWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.cardScrollWidget.setObjectName("cardScrollWidget")
        self.cardScroll.setWidget(self.cardScrollWidget)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.CardList)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(380, 10, 561, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.btnList = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.btnList.setContentsMargins(5, 0, 5, 0)
        self.btnList.setSpacing(5)
        self.btnList.setObjectName("btnList")
        self.makeNewCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.makeNewCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.makeNewCard.setStyleSheet("background: #2866bd;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 8px;")
        self.makeNewCard.setObjectName("makeNewCard")
        self.btnList.addWidget(self.makeNewCard)
        self.delSelCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.delSelCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delSelCard.setStyleSheet("background: #2866bd;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 8px;")
        self.delSelCard.setObjectName("delSelCard")
        self.btnList.addWidget(self.delSelCard)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.pushButton_3.setStyleSheet("background: #2866bd;\n"
"color: #fff;\n"
"padding: 10px;\n"
"border: none;\n"
"border-radius: 8px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.btnList.addWidget(self.pushButton_3)
        self.btnList.setStretch(0, 2)
        self.btnList.setStretch(1, 2)
        self.btnList.setStretch(2, 3)
        self.CardControler_Tabs.addTab(self.CardList, "")
        self.NoneTab = QtWidgets.QWidget()
        self.NoneTab.setMaximumSize(QtCore.QSize(1127, 651))
        self.NoneTab.setObjectName("NoneTab")
        self.CardControler_Tabs.addTab(self.NoneTab, "")

        self.retranslateUi(Form)
        self.CardControler_Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Search_label.setText(_translate("Form", "搜索"))
        self.makeNewCard.setText(_translate("Form", "制作新卡"))
        self.delSelCard.setText(_translate("Form", "删除已选"))
        self.pushButton_3.setText(_translate("Form", "导出信息至Excel"))
        self.CardControler_Tabs.setTabText(self.CardControler_Tabs.indexOf(self.CardList), _translate("Form", "Tab 1"))
        self.CardControler_Tabs.setTabText(self.CardControler_Tabs.indexOf(self.NoneTab), _translate("Form", "Tab 2"))
