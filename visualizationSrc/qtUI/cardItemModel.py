# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/cardItemModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 210)
        Form.setMinimumSize(QtCore.QSize(1070, 210))
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 1071, 211))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.cardItemModel = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.cardItemModel.setContentsMargins(10, 10, 10, 10)
        self.cardItemModel.setObjectName("cardItemModel")
        self.cardItemModel_sel = QtWidgets.QRadioButton(self.horizontalLayoutWidget_9)
        self.cardItemModel_sel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardItemModel_sel.setText("")
        self.cardItemModel_sel.setObjectName("cardItemModel_sel")
        self.cardItemModel.addWidget(self.cardItemModel_sel)
        self.cardItemModel_left = QtWidgets.QVBoxLayout()
        self.cardItemModel_left.setContentsMargins(5, 5, 5, 5)
        self.cardItemModel_left.setSpacing(5)
        self.cardItemModel_left.setObjectName("cardItemModel_left")
        self.cardItemModel_edit = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.cardItemModel_edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardItemModel_edit.setStyleSheet("background: #2866bd;\n"
"color: #fff;\n"
"padding: 6px;\n"
"border: none;\n"
"border-radius: 8px;")
        self.cardItemModel_edit.setObjectName("cardItemModel_edit")
        self.cardItemModel_left.addWidget(self.cardItemModel_edit)
        self.cardItemModel_Img = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_9)
        self.cardItemModel_Img.setMinimumSize(QtCore.QSize(120, 120))
        self.cardItemModel_Img.setMaximumSize(QtCore.QSize(120, 120))
        self.cardItemModel_Img.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardItemModel_Img.setStyleSheet("border-image: url(:/picture/Data/qrc/Card.png);")
        self.cardItemModel_Img.setObjectName("cardItemModel_Img")
        self.cardItemModel_left.addWidget(self.cardItemModel_Img)
        self.cardItemModel.addLayout(self.cardItemModel_left)
        self.cardItemModel_Data = QtWidgets.QVBoxLayout()
        self.cardItemModel_Data.setContentsMargins(5, 5, 5, 5)
        self.cardItemModel_Data.setSpacing(5)
        self.cardItemModel_Data.setObjectName("cardItemModel_Data")
        self.cardItemModel_BaseData_L = QtWidgets.QHBoxLayout()
        self.cardItemModel_BaseData_L.setContentsMargins(5, 5, 5, 5)
        self.cardItemModel_BaseData_L.setObjectName("cardItemModel_BaseData_L")
        self.cardItemModel_ID = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.cardItemModel_ID.setObjectName("cardItemModel_ID")
        self.cardItemModel_BaseData_L.addWidget(self.cardItemModel_ID)
        self.cardItemModel_DisplayName = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.cardItemModel_DisplayName.setObjectName("cardItemModel_DisplayName")
        self.cardItemModel_BaseData_L.addWidget(self.cardItemModel_DisplayName)
        self.cardItemModel_Description = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.cardItemModel_Description.setObjectName("cardItemModel_Description")
        self.cardItemModel_BaseData_L.addWidget(self.cardItemModel_Description)
        self.cardItemModel_Data.addLayout(self.cardItemModel_BaseData_L)
        self.cardItemModel_Code_L = QtWidgets.QHBoxLayout()
        self.cardItemModel_Code_L.setContentsMargins(5, 5, 5, 5)
        self.cardItemModel_Code_L.setSpacing(0)
        self.cardItemModel_Code_L.setObjectName("cardItemModel_Code_L")
        self.cardItemModel_Code = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_9)
        self.cardItemModel_Code.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:5px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cardItemModel_Code.setObjectName("cardItemModel_Code")
        self.cardItemModel_Code_L.addWidget(self.cardItemModel_Code)
        self.cardItemModel_Data.addLayout(self.cardItemModel_Code_L)
        self.cardItemModel_Story_L = QtWidgets.QHBoxLayout()
        self.cardItemModel_Story_L.setContentsMargins(5, 5, 5, 5)
        self.cardItemModel_Story_L.setSpacing(0)
        self.cardItemModel_Story_L.setObjectName("cardItemModel_Story_L")
        self.cardItemModel_Story = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_9)
        self.cardItemModel_Story.setStyleSheet("border:1px solid #afafaf; \n"
"border-radius:5px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.cardItemModel_Story.setObjectName("cardItemModel_Story")
        self.cardItemModel_Story_L.addWidget(self.cardItemModel_Story)
        self.cardItemModel_Data.addLayout(self.cardItemModel_Story_L)
        self.cardItemModel.addLayout(self.cardItemModel_Data)
        self.cardItemModel.setStretch(2, 8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cardItemModel_edit.setText(_translate("Form", "编辑"))
        self.cardItemModel_ID.setText(_translate("Form", "id:"))
        self.cardItemModel_DisplayName.setText(_translate("Form", "名字:"))
        self.cardItemModel_Description.setText(_translate("Form", "介绍:"))
        self.cardItemModel_Code.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
from . import AL_IDE_MainInterFace_rc
