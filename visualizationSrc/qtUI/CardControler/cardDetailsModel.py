# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/CardControler/cardDetailsModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 640)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 150, 255);\n"
"    padding:5px;\n"
"    border-radius:10px;\n"
"}")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1121, 641))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.CM_addNewCard = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.CM_addNewCard.setContentsMargins(0, 0, 0, 0)
        self.CM_addNewCard.setSpacing(0)
        self.CM_addNewCard.setObjectName("CM_addNewCard")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.CMT_settingTab = QtWidgets.QTabWidget(self.horizontalLayoutWidget_2)
        self.CMT_settingTab.setMaximumSize(QtCore.QSize(384, 16777215))
        self.CMT_settingTab.setObjectName("CMT_settingTab")
        self.CMT_baseSetting = QtWidgets.QWidget()
        self.CMT_baseSetting.setObjectName("CMT_baseSetting")
        self.scrollArea = QtWidgets.QScrollArea(self.CMT_baseSetting)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -1, 361, 601))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 599))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(359, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 341, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.data03 = QtWidgets.QHBoxLayout()
        self.data03.setSpacing(0)
        self.data03.setObjectName("data03")
        self.L_displayName = QtWidgets.QHBoxLayout()
        self.L_displayName.setSpacing(0)
        self.L_displayName.setObjectName("L_displayName")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.L_displayName.addWidget(self.label_6)
        self.CM_displayName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CM_displayName.setObjectName("CM_displayName")
        self.L_displayName.addWidget(self.CM_displayName)
        self.data03.addLayout(self.L_displayName)
        self.L_price_2 = QtWidgets.QHBoxLayout()
        self.L_price_2.setSpacing(0)
        self.L_price_2.setObjectName("L_price_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.L_price_2.addWidget(self.label_7)
        self.CM_price = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.CM_price.setObjectName("CM_price")
        self.L_price_2.addWidget(self.CM_price)
        self.data03.addLayout(self.L_price_2)
        self.L_energyReq_2 = QtWidgets.QHBoxLayout()
        self.L_energyReq_2.setSpacing(0)
        self.L_energyReq_2.setObjectName("L_energyReq_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.L_energyReq_2.addWidget(self.label_9)
        self.CM_energyReq = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.CM_energyReq.setObjectName("CM_energyReq")
        self.L_energyReq_2.addWidget(self.CM_energyReq)
        self.data03.addLayout(self.L_energyReq_2)
        self.data03.setStretch(0, 2)
        self.data03.setStretch(1, 1)
        self.data03.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.data03)
        self.data04 = QtWidgets.QHBoxLayout()
        self.data04.setSpacing(0)
        self.data04.setObjectName("data04")
        self.L_displayName_3 = QtWidgets.QHBoxLayout()
        self.L_displayName_3.setSpacing(0)
        self.L_displayName_3.setObjectName("L_displayName_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.L_displayName_3.addWidget(self.label_11)
        self.CM_range = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.CM_range.setObjectName("CM_range")
        self.L_displayName_3.addWidget(self.CM_range)
        self.data04.addLayout(self.L_displayName_3)
        self.data04.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.data04)
        self.data02 = QtWidgets.QHBoxLayout()
        self.data02.setSpacing(0)
        self.data02.setObjectName("data02")
        self.L_price_3 = QtWidgets.QHBoxLayout()
        self.L_price_3.setSpacing(0)
        self.L_price_3.setObjectName("L_price_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.L_price_3.addWidget(self.label_5)
        self.CM_description = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.CM_description.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.CM_description.setObjectName("CM_description")
        self.L_price_3.addWidget(self.CM_description)
        self.L_price_3.setStretch(0, 1)
        self.L_price_3.setStretch(1, 4)
        self.data02.addLayout(self.L_price_3)
        self.data02.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.data02)
        self.data01 = QtWidgets.QHBoxLayout()
        self.data01.setSpacing(0)
        self.data01.setObjectName("data01")
        self.L_price = QtWidgets.QHBoxLayout()
        self.L_price.setSpacing(0)
        self.L_price.setObjectName("L_price")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.L_price.addWidget(self.label_4)
        self.CM_story0 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.CM_story0.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"padding:5px;\n"
"border:1px solid #afafaf; \n"
"border-radius:10px;")
        self.CM_story0.setObjectName("CM_story0")
        self.L_price.addWidget(self.CM_story0)
        self.L_price.setStretch(0, 1)
        self.L_price.setStretch(1, 4)
        self.data01.addLayout(self.L_price)
        self.data01.setStretch(0, 2)
        self.verticalLayout_2.addLayout(self.data01)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.CMT_settingTab.addTab(self.CMT_baseSetting, "")
        self.CMT_greateSetting = QtWidgets.QWidget()
        self.CMT_greateSetting.setObjectName("CMT_greateSetting")
        self.CMT_settingTab.addTab(self.CMT_greateSetting, "")
        self.verticalLayout.addWidget(self.CMT_settingTab)
        self.CM_addNewCard.addLayout(self.verticalLayout)
        self.CM_main = QtWidgets.QVBoxLayout()
        self.CM_main.setContentsMargins(10, 10, 10, 10)
        self.CM_main.setSpacing(10)
        self.CM_main.setObjectName("CM_main")
        self.CM_contenter = QtWidgets.QHBoxLayout()
        self.CM_contenter.setObjectName("CM_contenter")
        self.textEdit = QtWidgets.QVBoxLayout()
        self.textEdit.setSpacing(0)
        self.textEdit.setObjectName("textEdit")
        self.cardMakeTap_code = QtWidgets.QVBoxLayout()
        self.cardMakeTap_code.setObjectName("cardMakeTap_code")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setStyleSheet("padding:10px;\n"
"font-size:18px;\n"
"font-weight:600;")
        self.label_2.setObjectName("label_2")
        self.cardMakeTap_code.addWidget(self.label_2)
        self.CM_codeSource = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.CM_codeSource.setStyleSheet("")
        self.CM_codeSource.setObjectName("CM_codeSource")
        self.cardMakeTap_code.addWidget(self.CM_codeSource)
        self.textEdit.addLayout(self.cardMakeTap_code)
        self.cardMakeTap_remap = QtWidgets.QVBoxLayout()
        self.cardMakeTap_remap.setObjectName("cardMakeTap_remap")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setStyleSheet("padding:10px;\n"
"font-size:18px;\n"
"font-weight:600;")
        self.label_8.setObjectName("label_8")
        self.cardMakeTap_remap.addWidget(self.label_8)
        self.CM_remapCodeSource = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.CM_remapCodeSource.setStyleSheet("")
        self.CM_remapCodeSource.setObjectName("CM_remapCodeSource")
        self.cardMakeTap_remap.addWidget(self.CM_remapCodeSource)
        self.textEdit.addLayout(self.cardMakeTap_remap)
        self.CM_contenter.addLayout(self.textEdit)
        self.CM_main.addLayout(self.CM_contenter)
        self.CM_footer = QtWidgets.QHBoxLayout()
        self.CM_footer.setContentsMargins(100, -1, 100, -1)
        self.CM_footer.setSpacing(200)
        self.CM_footer.setObjectName("CM_footer")
        self.CM_printCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.CM_printCard.setFont(font)
        self.CM_printCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CM_printCard.setStyleSheet("")
        self.CM_printCard.setCheckable(False)
        self.CM_printCard.setObjectName("CM_printCard")
        self.CM_footer.addWidget(self.CM_printCard)
        self.CM_addCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.CM_addCard.setFont(font)
        self.CM_addCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CM_addCard.setStyleSheet("")
        self.CM_addCard.setObjectName("CM_addCard")
        self.CM_footer.addWidget(self.CM_addCard)
        self.CM_main.addLayout(self.CM_footer)
        self.CM_addNewCard.addLayout(self.CM_main)
        self.CM_addNewCard.setStretch(0, 1)
        self.CM_addNewCard.setStretch(1, 2)

        self.retranslateUi(Form)
        self.CMT_settingTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "卡片名"))
        self.label_7.setText(_translate("Form", "花费"))
        self.label_9.setText(_translate("Form", "消耗能量"))
        self.label_11.setText(_translate("Form", "作用范围"))
        self.label_5.setText(_translate("Form", "卡牌介绍"))
        self.label_4.setText(_translate("Form", "故事"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_baseSetting), _translate("Form", "Tab 1"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_greateSetting), _translate("Form", "Tab 2"))
        self.label_2.setText(_translate("Form", "Code代码"))
        self.CM_codeSource.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("Form", "Remap Code代码"))
        self.CM_remapCodeSource.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CM_printCard.setText(_translate("Form", "印卡"))
        self.CM_addCard.setText(_translate("Form", "添加"))
