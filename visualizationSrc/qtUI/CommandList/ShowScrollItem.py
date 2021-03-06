# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\CommandList\ShowScrollItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 130)
        Form.setMinimumSize(QtCore.QSize(460, 130))
        Form.setStyleSheet("#Form{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QTextBrowser{\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    padding: 1px;\n"
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
        self.itemMain = QtWidgets.QWidget(Form)
        self.itemMain.setGeometry(QtCore.QRect(10, 10, 441, 111))
        self.itemMain.setMinimumSize(QtCore.QSize(430, 100))
        self.itemMain.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.itemMain.setStyleSheet("#itemMain{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    border: none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#item_delete{\n"
"    border-image: url(:/ico/Data/qrc/ico/delete.png);\n"
"}\n"
"#item_delete:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/deleted.png);\n"
"}\n"
"#item_edite{\n"
"    border-image: url(:/ico/Data/qrc/ico/edit.png);\n"
"}\n"
"#item_edite:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/edited.png);\n"
"}\n"
"#item_more{\n"
"    border-image: url(:/ico/Data/qrc/ico/more.png);\n"
"}\n"
"#item_more:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/mored.png);\n"
"}")
        self.itemMain.setObjectName("itemMain")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.itemMain)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 441, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.name = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.horizontalLayout_4.addWidget(self.name)
        self.version = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.horizontalLayout_4.addWidget(self.version)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.effectCode = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.effectCode.setFont(font)
        self.effectCode.setObjectName("effectCode")
        self.horizontalLayout_3.addWidget(self.effectCode)
        self.tagCode = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.tagCode.setFont(font)
        self.tagCode.setObjectName("tagCode")
        self.horizontalLayout_3.addWidget(self.tagCode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.desp = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.desp.setStyleSheet("")
        self.desp.setObjectName("desp")
        self.verticalLayout_2.addWidget(self.desp)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comment = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.comment.setObjectName("comment")
        self.horizontalLayout_2.addWidget(self.comment)
        self.quoteDesp = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.quoteDesp.setObjectName("quoteDesp")
        self.horizontalLayout_2.addWidget(self.quoteDesp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.item_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.item_delete.setMinimumSize(QtCore.QSize(24, 24))
        self.item_delete.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.item_delete.setText("")
        self.item_delete.setObjectName("item_delete")
        self.verticalLayout_4.addWidget(self.item_delete)
        self.item_edite = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.item_edite.setMinimumSize(QtCore.QSize(24, 24))
        self.item_edite.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.item_edite.setText("")
        self.item_edite.setObjectName("item_edite")
        self.verticalLayout_4.addWidget(self.item_edite)
        self.item_more = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.item_more.setMinimumSize(QtCore.QSize(24, 24))
        self.item_more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.item_more.setText("")
        self.item_more.setObjectName("item_more")
        self.verticalLayout_4.addWidget(self.item_more)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.remapCode = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.remapCode.setObjectName("remapCode")
        self.verticalLayout.addWidget(self.remapCode)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "指令名"))
        self.version.setText(_translate("Form", "版本"))
        self.effectCode.setText(_translate("Form", "特效代码"))
        self.tagCode.setText(_translate("Form", "类别"))
        self.desp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">介绍</p></body></html>"))
        self.comment.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">示例|形容</p></body></html>"))
        self.quoteDesp.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">引用描述</p></body></html>"))
        self.item_delete.setToolTip(_translate("Form", "<html><head/><body><p>删除</p></body></html>"))
        self.item_edite.setToolTip(_translate("Form", "<html><head/><body><p>编辑</p></body></html>"))
        self.item_more.setToolTip(_translate("Form", "<html><head/><body><p>更多</p></body></html>"))
        self.remapCode.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">remapCode</p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
