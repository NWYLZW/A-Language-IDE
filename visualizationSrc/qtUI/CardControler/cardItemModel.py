# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUI/CardControler/cardItemModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(470, 360)
        main.setMinimumSize(QtCore.QSize(470, 360))
        main.setMaximumSize(QtCore.QSize(470, 360))
        main.setStyleSheet("#main{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.cardItem = QtWidgets.QWidget(main)
        self.cardItem.setGeometry(QtCore.QRect(10, 10, 450, 341))
        self.cardItem.setMaximumSize(QtCore.QSize(450, 350))
        self.cardItem.setStyleSheet("#cardItem{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QTextEdit{\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.cardItem.setObjectName("cardItem")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.cardItem)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NameAndId = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.NameAndId.setFont(font)
        self.NameAndId.setStyleSheet("QLabel{\n"
"    padding:5px;\n"
"    font-size:16px;\n"
"    font-weight:600;\n"
"}")
        self.NameAndId.setObjectName("NameAndId")
        self.verticalLayout.addWidget(self.NameAndId)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cardShow = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.cardShow.setMaximumSize(QtCore.QSize(180, 180))
        self.cardShow.setStyleSheet("#cardShow{\n"
"    border-radius: 10px;\n"
"}\n"
"#cardShow:hover{\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.cardShow.setObjectName("cardShow")
        self.backgroundImg = QtWidgets.QLabel(self.cardShow)
        self.backgroundImg.setGeometry(QtCore.QRect(0, 0, 181, 181))
        self.backgroundImg.setMinimumSize(QtCore.QSize(0, 0))
        self.backgroundImg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.backgroundImg.setStyleSheet("border-image: url(:/picture/Data/qrc/Card.png);")
        self.backgroundImg.setText("")
        self.backgroundImg.setObjectName("backgroundImg")
        self.cardArt = QtWidgets.QLabel(self.cardShow)
        self.cardArt.setGeometry(QtCore.QRect(70, 50, 51, 51))
        self.cardArt.setStyleSheet("border-image: url(:/picture/Data/qrc/Unknown.png);")
        self.cardArt.setText("")
        self.cardArt.setObjectName("cardArt")
        self.gridLayout.addWidget(self.cardShow, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(50, 0))
        self.widget.setMaximumSize(QtCore.QSize(50, 250))
        self.widget.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"#cardSelect{\n"
"    border-image: url(:/ico/Data/qrc/ico/select.png);\n"
"}\n"
"#cardEdit{\n"
"    border-image: url(:/ico/Data/qrc/ico/edit.png);\n"
"}\n"
"#cardEdit:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/edited.png);\n"
"}\n"
"#cardExport{\n"
"    border-image: url(:/ico/Data/qrc/ico/export.png);\n"
"}\n"
"#cardExport:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/exported.png);\n"
"}\n"
"#cardImport{\n"
"    border-image: url(:/ico/Data/qrc/ico/import.png);\n"
"}\n"
"#cardImport:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/imported.png);\n"
"}\n"
"#cardPrint{\n"
"    border-image: url(:/ico/Data/qrc/ico/print.png);\n"
"}\n"
"#cardPrint:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/printed.png);\n"
"}\n"
"#cardRelease{\n"
"    border-image: url(:/ico/Data/qrc/ico/release.png);\n"
"}\n"
"#cardRelease:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/released.png);\n"
"}")
        self.widget.setObjectName("widget")
        self.cardSelect = QtWidgets.QPushButton(self.widget)
        self.cardSelect.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.cardSelect.setMinimumSize(QtCore.QSize(30, 30))
        self.cardSelect.setMaximumSize(QtCore.QSize(30, 30))
        self.cardSelect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardSelect.setStyleSheet("")
        self.cardSelect.setText("")
        self.cardSelect.setObjectName("cardSelect")
        self.cardEdit = QtWidgets.QPushButton(self.widget)
        self.cardEdit.setGeometry(QtCore.QRect(10, 50, 30, 30))
        self.cardEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.cardEdit.setMaximumSize(QtCore.QSize(30, 30))
        self.cardEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardEdit.setText("")
        self.cardEdit.setObjectName("cardEdit")
        self.cardExport = QtWidgets.QPushButton(self.widget)
        self.cardExport.setGeometry(QtCore.QRect(10, 90, 30, 30))
        self.cardExport.setMinimumSize(QtCore.QSize(30, 30))
        self.cardExport.setMaximumSize(QtCore.QSize(30, 30))
        self.cardExport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardExport.setText("")
        self.cardExport.setObjectName("cardExport")
        self.cardImport = QtWidgets.QPushButton(self.widget)
        self.cardImport.setGeometry(QtCore.QRect(10, 130, 30, 30))
        self.cardImport.setMinimumSize(QtCore.QSize(30, 30))
        self.cardImport.setMaximumSize(QtCore.QSize(30, 30))
        self.cardImport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardImport.setText("")
        self.cardImport.setObjectName("cardImport")
        self.cardPrint = QtWidgets.QPushButton(self.widget)
        self.cardPrint.setGeometry(QtCore.QRect(10, 170, 30, 30))
        self.cardPrint.setMinimumSize(QtCore.QSize(30, 30))
        self.cardPrint.setMaximumSize(QtCore.QSize(30, 30))
        self.cardPrint.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cardPrint.setText("")
        self.cardPrint.setObjectName("cardPrint")
        self.cardRelease = QtWidgets.QPushButton(self.widget)
        self.cardRelease.setGeometry(QtCore.QRect(10, 210, 30, 30))
        self.cardRelease.setMinimumSize(QtCore.QSize(30, 30))
        self.cardRelease.setMaximumSize(QtCore.QSize(30, 30))
        self.cardRelease.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.cardRelease.setText("")
        self.cardRelease.setObjectName("cardRelease")
        self.verticalLayout_3.addWidget(self.widget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("QLabel{\n"
"    padding:3px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsView_2.setMaximumSize(QtCore.QSize(32, 32))
        self.graphicsView_2.setStyleSheet("border-image: url(:/picture/Data/qrc/tetra.png);")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_3.addWidget(self.graphicsView_2)
        self.price = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(9)
        self.price.setFont(font)
        self.price.setStyleSheet("QLabel{\n"
"    padding:3px;\n"
"}")
        self.price.setObjectName("price")
        self.horizontalLayout_3.addWidget(self.price)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.description = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.description.setObjectName("description")
        self.verticalLayout_2.addWidget(self.description)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.story = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.story.setObjectName("story")
        self.verticalLayout_2.addWidget(self.story)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.NameAndId.setText(_translate("main", "无名(ID:10001)"))
        self.cardSelect.setToolTip(_translate("main", "<html><head/><body><p>选择卡牌</p></body></html>"))
        self.cardEdit.setToolTip(_translate("main", "<html><head/><body><p>编辑卡牌</p></body></html>"))
        self.cardExport.setToolTip(_translate("main", "<html><head/><body><p>导出卡牌</p></body></html>"))
        self.cardImport.setToolTip(_translate("main", "<html><head/><body><p>导入卡牌</p></body></html>"))
        self.cardPrint.setToolTip(_translate("main", "<html><head/><body><p>在游戏中印卡</p></body></html>"))
        self.cardRelease.setToolTip(_translate("main", "<html><head/><body><p>发布</p></body></html>"))
        self.label_2.setText(_translate("main", "标准卡包"))
        self.price.setText(_translate("main", "∞"))
        self.label_4.setText(_translate("main", "简介"))
        self.label_5.setText(_translate("main", "故事"))
from .. import AL_IDE_MainInterFace_rc
