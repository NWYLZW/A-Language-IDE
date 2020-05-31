# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\CharacterControler\protagonistLibItemModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(310, 250)
        main.setMinimumSize(QtCore.QSize(310, 250))
        main.setMaximumSize(QtCore.QSize(310, 250))
        main.setStyleSheet("#main{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.protagonistItem = QtWidgets.QWidget(main)
        self.protagonistItem.setGeometry(QtCore.QRect(10, 10, 291, 231))
        self.protagonistItem.setMaximumSize(QtCore.QSize(450, 350))
        self.protagonistItem.setStyleSheet("#protagonistItem{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QTextEdit{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: none;\n"
"}\n"
"#edit{\n"
"    border-image: url(:/ico/Data/qrc/ico/edit.png);\n"
"}\n"
"#edit:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/edited.png);\n"
"}\n"
"#deleteBTN{\n"
"    border-image: url(:/ico/Data/qrc/ico/delete.png);\n"
"}\n"
"#deleteBTN:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/deleted.png);\n"
"}\n"
"#more{\n"
"    border-image: url(:/ico/Data/qrc/ico/more.png);\n"
"}\n"
"#more:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/mored.png);\n"
"}")
        self.protagonistItem.setObjectName("protagonistItem")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.protagonistItem)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 271, 211))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.characterHudIcon = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.characterHudIcon.setMinimumSize(QtCore.QSize(64, 64))
        self.characterHudIcon.setMaximumSize(QtCore.QSize(64, 64))
        self.characterHudIcon.setStyleSheet("QLabel{\n"
"    border-image: url(:/picture/Data/qrc/CharacterControler.png);\n"
"}")
        self.characterHudIcon.setText("")
        self.characterHudIcon.setObjectName("characterHudIcon")
        self.verticalLayout_2.addWidget(self.characterHudIcon)
        self.characterID = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.characterID.setFont(font)
        self.characterID.setObjectName("characterID")
        self.verticalLayout_2.addWidget(self.characterID)
        self.verticalLayout_2.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.characterName = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.characterName.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(14)
        self.characterName.setFont(font)
        self.characterName.setObjectName("characterName")
        self.horizontalLayout_4.addWidget(self.characterName)
        self.characterHP = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.characterHP.setFont(font)
        self.characterHP.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.characterHP.setObjectName("characterHP")
        self.horizontalLayout_4.addWidget(self.characterHP)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setMinimumSize(QtCore.QSize(0, 10))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_4.setStyleSheet("QLabel{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(238, 36, 32)\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 10))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_5.setStyleSheet("QLabel{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(80, 158, 211)\n"
"}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.characterEnergy = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.characterEnergy.setFont(font)
        self.characterEnergy.setObjectName("characterEnergy")
        self.horizontalLayout_2.addWidget(self.characterEnergy)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setMinimumSize(QtCore.QSize(0, 10))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_7.setStyleSheet("QLabel{\n"
"    border-radius: 3px;\n"
"    background-color: rgb(177, 175, 176)\n"
"}")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.characterStamina = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(8)
        self.characterStamina.setFont(font)
        self.characterStamina.setObjectName("characterStamina")
        self.horizontalLayout_3.addWidget(self.characterStamina)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edit = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.edit.setMinimumSize(QtCore.QSize(32, 32))
        self.edit.setMaximumSize(QtCore.QSize(32, 32))
        self.edit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit.setText("")
        self.edit.setObjectName("edit")
        self.horizontalLayout_5.addWidget(self.edit)
        self.deleteBTN = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.deleteBTN.setMinimumSize(QtCore.QSize(32, 32))
        self.deleteBTN.setMaximumSize(QtCore.QSize(32, 32))
        self.deleteBTN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteBTN.setText("")
        self.deleteBTN.setObjectName("deleteBTN")
        self.horizontalLayout_5.addWidget(self.deleteBTN)
        self.none = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.none.setMinimumSize(QtCore.QSize(32, 32))
        self.none.setMaximumSize(QtCore.QSize(32, 32))
        self.none.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.none.setText("")
        self.none.setObjectName("none")
        self.horizontalLayout_5.addWidget(self.none)
        self.none_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.none_2.setMinimumSize(QtCore.QSize(32, 32))
        self.none_2.setMaximumSize(QtCore.QSize(32, 32))
        self.none_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.none_2.setText("")
        self.none_2.setObjectName("none_2")
        self.horizontalLayout_5.addWidget(self.none_2)
        self.more = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.more.setMinimumSize(QtCore.QSize(32, 32))
        self.more.setMaximumSize(QtCore.QSize(32, 32))
        self.more.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.more.setText("")
        self.more.setObjectName("more")
        self.horizontalLayout_5.addWidget(self.more)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.desp = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.desp.setObjectName("desp")
        self.verticalLayout_3.addWidget(self.desp)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.characterID.setText(_translate("main", "ID:10001"))
        self.characterName.setText(_translate("main", "红莲"))
        self.characterHP.setText(_translate("main", "10/10"))
        self.characterEnergy.setText(_translate("main", "1"))
        self.characterStamina.setText(_translate("main", "1"))
        self.desp.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">红莲与她的弟弟费里克在童年时期被抓到一个秘密研究所，他们每天都要被用于残忍的人体实验。忍无可忍的红莲决定带着弟弟逃离研究所。</p></body></html>"))
from .. import AL_IDE_MainInterFace_rc
