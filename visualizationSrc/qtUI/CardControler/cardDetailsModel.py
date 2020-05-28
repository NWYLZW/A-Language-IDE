# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qtUI\CardControler\cardDetailsModel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 610)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"QTextEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid #afafaf; \n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit{\n"
"    height:25px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid #afafaf; \n"
"    border-radius:4px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:1px solid rgb(0, 170, 255); \n"
"    border-radius:6px;\n"
"}\n"
"#saveCard{\n"
"    border-image: url(:/ico/Data/qrc/ico/save.png);\n"
"}\n"
"#saveCard:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/saved.png);\n"
"}\n"
"#printCard{\n"
"    border-image: url(:/ico/Data/qrc/ico/print.png);\n"
"}\n"
"#printCard:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/printed.png);\n"
"}\n"
"#delCard{\n"
"    border-image: url(:/ico/Data/qrc/ico/delete.png);\n"
"}\n"
"#delCard:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/deleted.png);\n"
"}")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1001, 611))
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
        self.CMT_settingTab.setStyleSheet("")
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 311, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.L_displayName = QtWidgets.QHBoxLayout()
        self.L_displayName.setSpacing(0)
        self.L_displayName.setObjectName("L_displayName")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.L_displayName.addWidget(self.label_6)
        self.CM_displayName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.CM_displayName.setObjectName("CM_displayName")
        self.L_displayName.addWidget(self.CM_displayName)
        self.verticalLayout_2.addLayout(self.L_displayName)
        self.data03 = QtWidgets.QHBoxLayout()
        self.data03.setSpacing(0)
        self.data03.setObjectName("data03")
        self.L_price_2 = QtWidgets.QHBoxLayout()
        self.L_price_2.setSpacing(0)
        self.L_price_2.setObjectName("L_price_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.L_price_2.addWidget(self.label_7)
        self.CM_price = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.CM_price.setMaximum(1000000)
        self.CM_price.setObjectName("CM_price")
        self.L_price_2.addWidget(self.CM_price)
        self.data03.addLayout(self.L_price_2)
        self.L_energyReq_2 = QtWidgets.QHBoxLayout()
        self.L_energyReq_2.setSpacing(0)
        self.L_energyReq_2.setObjectName("L_energyReq_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.L_energyReq_2.addWidget(self.label_9)
        self.CM_energyReq = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.CM_energyReq.setObjectName("CM_energyReq")
        self.L_energyReq_2.addWidget(self.CM_energyReq)
        self.data03.addLayout(self.L_energyReq_2)
        self.data03.setStretch(0, 1)
        self.data03.setStretch(1, 1)
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
        self.CM_range.setDecimals(1)
        self.CM_range.setMaximum(1000000.0)
        self.CM_range.setObjectName("CM_range")
        self.L_displayName_3.addWidget(self.CM_range)
        self.data04.addLayout(self.L_displayName_3)
        self.data04.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.data04)
        self.spreadRadius_L = QtWidgets.QHBoxLayout()
        self.spreadRadius_L.setSpacing(0)
        self.spreadRadius_L.setObjectName("spreadRadius_L")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.spreadRadius_L.addWidget(self.label)
        self.spreadRadius = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spreadRadius.setDecimals(1)
        self.spreadRadius.setMaximum(1000000.0)
        self.spreadRadius.setObjectName("spreadRadius")
        self.spreadRadius_L.addWidget(self.spreadRadius)
        self.verticalLayout_2.addLayout(self.spreadRadius_L)
        self.minUnlockGrade_L = QtWidgets.QHBoxLayout()
        self.minUnlockGrade_L.setSpacing(0)
        self.minUnlockGrade_L.setObjectName("minUnlockGrade_L")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.minUnlockGrade_L.addWidget(self.label_21)
        self.minUnlockGrade = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.minUnlockGrade.setMinimum(1)
        self.minUnlockGrade.setMaximum(1000000)
        self.minUnlockGrade.setObjectName("minUnlockGrade")
        self.minUnlockGrade_L.addWidget(self.minUnlockGrade)
        self.verticalLayout_2.addLayout(self.minUnlockGrade_L)
        self.aim = QtWidgets.QHBoxLayout()
        self.aim.setSpacing(0)
        self.aim.setObjectName("aim")
        self.aimTypeCode_L = QtWidgets.QHBoxLayout()
        self.aimTypeCode_L.setSpacing(0)
        self.aimTypeCode_L.setObjectName("aimTypeCode_L")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.aimTypeCode_L.addWidget(self.label_16)
        self.aimTypeCode = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.aimTypeCode.setObjectName("aimTypeCode")
        self.aimTypeCode_L.addWidget(self.aimTypeCode)
        self.aimTypeCode_L.setStretch(0, 1)
        self.aimTypeCode_L.setStretch(1, 2)
        self.aim.addLayout(self.aimTypeCode_L)
        self.perferredTargetTypeCode_L = QtWidgets.QHBoxLayout()
        self.perferredTargetTypeCode_L.setSpacing(0)
        self.perferredTargetTypeCode_L.setObjectName("perferredTargetTypeCode_L")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.perferredTargetTypeCode_L.addWidget(self.label_17)
        self.perferredTargetTypeCode = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.perferredTargetTypeCode.setObjectName("perferredTargetTypeCode")
        self.perferredTargetTypeCode_L.addWidget(self.perferredTargetTypeCode)
        self.perferredTargetTypeCode_L.setStretch(0, 1)
        self.perferredTargetTypeCode_L.setStretch(1, 2)
        self.aim.addLayout(self.perferredTargetTypeCode_L)
        self.verticalLayout_2.addLayout(self.aim)
        self.tagCode_L = QtWidgets.QHBoxLayout()
        self.tagCode_L.setSpacing(0)
        self.tagCode_L.setObjectName("tagCode_L")
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.tagCode_L.addWidget(self.label_18)
        self.addMyEffect = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.addMyEffect.setMaximumSize(QtCore.QSize(24, 24))
        self.addMyEffect.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.addMyEffect.setStyleSheet("#addMyEffect{\n"
"    border-image: url(:/ico/Data/qrc/ico/plusSquare.png);\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.addMyEffect.setObjectName("addMyEffect")
        self.tagCode_L.addWidget(self.addMyEffect)
        self.tagCode = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.tagCode.setObjectName("tagCode")
        self.tagCode_L.addWidget(self.tagCode)
        self.tagCode_L.setStretch(0, 1)
        self.tagCode_L.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.tagCode_L)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget_2.setMaximumSize(QtCore.QSize(333, 345))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.cardDes_Tab = QtWidgets.QWidget()
        self.cardDes_Tab.setObjectName("cardDes_Tab")
        self.CM_description = QtWidgets.QTextEdit(self.cardDes_Tab)
        self.CM_description.setGeometry(QtCore.QRect(10, 10, 271, 261))
        self.CM_description.setStyleSheet("")
        self.CM_description.setObjectName("CM_description")
        self.tabWidget_2.addTab(self.cardDes_Tab, "")
        self.cardStory_Tab = QtWidgets.QWidget()
        self.cardStory_Tab.setObjectName("cardStory_Tab")
        self.CM_story0 = QtWidgets.QTextEdit(self.cardStory_Tab)
        self.CM_story0.setGeometry(QtCore.QRect(10, 10, 271, 261))
        self.CM_story0.setStyleSheet("")
        self.CM_story0.setObjectName("CM_story0")
        self.tabWidget_2.addTab(self.cardStory_Tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget_2)
        self.verticalLayout_2.setStretch(7, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.CMT_settingTab.addTab(self.CMT_baseSetting, "")
        self.CMT_greateSetting = QtWidgets.QWidget()
        self.CMT_greateSetting.setStyleSheet("QScrollBar\n"
"{\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(200,200,200);\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"    background-color: rgb(100,100,100);\n"
"    min-width: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:hover\n"
"{\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"QScrollBar::right-arrow, QScrollBar::left-arrow,\n"
"QScrollBar::add-line, QScrollBar::sub-line\n"
"{\n"
"    border: none;background: none;color: none;\n"
"}")
        self.CMT_greateSetting.setObjectName("CMT_greateSetting")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.CMT_greateSetting)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 311, 571))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.effectCode_L = QtWidgets.QHBoxLayout()
        self.effectCode_L.setSpacing(0)
        self.effectCode_L.setObjectName("effectCode_L")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_19.setObjectName("label_19")
        self.effectCode_L.addWidget(self.label_19)
        self.effectCode = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.effectCode.setObjectName("effectCode")
        self.effectCode_L.addWidget(self.effectCode)
        self.effectCode_L.setStretch(0, 1)
        self.effectCode_L.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.effectCode_L)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.betterSpread_Search = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.betterSpread_Search.setObjectName("betterSpread_Search")
        self.verticalLayout_4.addWidget(self.betterSpread_Search)
        self.betterSpread = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.betterSpread.setMinimumSize(QtCore.QSize(0, 100))
        self.betterSpread.setMaximumSize(QtCore.QSize(16777215, 100))
        self.betterSpread.setStyleSheet("")
        self.betterSpread.setWidgetResizable(True)
        self.betterSpread.setObjectName("betterSpread")
        self.betterSpread_W = QtWidgets.QWidget()
        self.betterSpread_W.setGeometry(QtCore.QRect(0, 0, 287, 98))
        self.betterSpread_W.setObjectName("betterSpread_W")
        self.betterSpread.setWidget(self.betterSpread_W)
        self.verticalLayout_4.addWidget(self.betterSpread)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.backgroundImg_Search = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.backgroundImg_Search.setObjectName("backgroundImg_Search")
        self.verticalLayout_7.addWidget(self.backgroundImg_Search)
        self.backgroundImgScroll = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.backgroundImgScroll.setMinimumSize(QtCore.QSize(0, 100))
        self.backgroundImgScroll.setMaximumSize(QtCore.QSize(16777215, 100))
        self.backgroundImgScroll.setWidgetResizable(True)
        self.backgroundImgScroll.setObjectName("backgroundImgScroll")
        self.backgroundImg_W = QtWidgets.QWidget()
        self.backgroundImg_W.setGeometry(QtCore.QRect(0, 0, 287, 98))
        self.backgroundImg_W.setObjectName("backgroundImg_W")
        self.backgroundImgScroll.setWidget(self.backgroundImg_W)
        self.verticalLayout_7.addWidget(self.backgroundImgScroll)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.setCardArdImg = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.setCardArdImg.setObjectName("setCardArdImg")
        self.deleteSelCardArt = QtWidgets.QPushButton(self.setCardArdImg)
        self.deleteSelCardArt.setGeometry(QtCore.QRect(240, 0, 51, 51))
        self.deleteSelCardArt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteSelCardArt.setStyleSheet("QPushButton{\n"
"    border-image: url(:/ico/Data/qrc/ico/delete.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border-image: url(:/ico/Data/qrc/ico/deleted.png);\n"
"}")
        self.deleteSelCardArt.setText("")
        self.deleteSelCardArt.setObjectName("deleteSelCardArt")
        self.selCardArtImg = DragLabel(self.setCardArdImg)
        self.selCardArtImg.setGeometry(QtCore.QRect(60, 0, 160, 160))
        self.selCardArtImg.setMinimumSize(QtCore.QSize(160, 160))
        self.selCardArtImg.setMaximumSize(QtCore.QSize(200, 200))
        self.selCardArtImg.setAcceptDrops(True)
        self.selCardArtImg.setStyleSheet("border-image: url(:/picture/Data/qrc/Unknown.png);")
        self.selCardArtImg.setText("")
        self.selCardArtImg.setObjectName("selCardArtImg")
        self.verticalLayout_3.addWidget(self.setCardArdImg)
        self.verticalLayout_3.setStretch(3, 1)
        self.CMT_settingTab.addTab(self.CMT_greateSetting, "")
        self.CMT_previewCard = QtWidgets.QWidget()
        self.CMT_previewCard.setObjectName("CMT_previewCard")
        self.CMT_settingTab.addTab(self.CMT_previewCard, "")
        self.verticalLayout.addWidget(self.CMT_settingTab)
        self.CM_addNewCard.addLayout(self.verticalLayout)
        self.CM_main = QtWidgets.QVBoxLayout()
        self.CM_main.setContentsMargins(10, 10, 10, 10)
        self.CM_main.setSpacing(10)
        self.CM_main.setObjectName("CM_main")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget_2)
        self.tabWidget.setObjectName("tabWidget")
        self.CodeTab = QtWidgets.QWidget()
        self.CodeTab.setObjectName("CodeTab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.CodeTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 641, 521))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.CM_codeSource_L = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.CM_codeSource_L.setContentsMargins(10, 10, 10, 10)
        self.CM_codeSource_L.setSpacing(0)
        self.CM_codeSource_L.setObjectName("CM_codeSource_L")
        self.CM_codeSource = CodeTextEditor(self.verticalLayoutWidget_3)
        self.CM_codeSource.setStyleSheet("")
        self.CM_codeSource.setObjectName("CM_codeSource")
        self.CM_codeSource_L.addWidget(self.CM_codeSource)
        self.tabWidget.addTab(self.CodeTab, "")
        self.RemapCode_Tab = QtWidgets.QWidget()
        self.RemapCode_Tab.setObjectName("RemapCode_Tab")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.RemapCode_Tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 641, 521))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.CM_remapCodeSource_L = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.CM_remapCodeSource_L.setContentsMargins(10, 10, 10, 10)
        self.CM_remapCodeSource_L.setSpacing(0)
        self.CM_remapCodeSource_L.setObjectName("CM_remapCodeSource_L")
        self.CM_remapCodeSource = CodeTextEditor(self.verticalLayoutWidget_4)
        self.CM_remapCodeSource.setStyleSheet("")
        self.CM_remapCodeSource.setObjectName("CM_remapCodeSource")
        self.CM_remapCodeSource_L.addWidget(self.CM_remapCodeSource)
        self.tabWidget.addTab(self.RemapCode_Tab, "")
        self.CM_main.addWidget(self.tabWidget)
        self.CM_footer = QtWidgets.QHBoxLayout()
        self.CM_footer.setContentsMargins(0, -1, 0, -1)
        self.CM_footer.setSpacing(0)
        self.CM_footer.setObjectName("CM_footer")
        self.head = QtWidgets.QHBoxLayout()
        self.head.setObjectName("head")
        self.tools = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        self.tools.setMaximumSize(QtCore.QSize(32, 32))
        self.tools.setStyleSheet("#tools{\n"
"    border-image: url(:/ico/Data/qrc/ico/tool.png);\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.tools.setObjectName("tools")
        self.head.addWidget(self.tools)
        self.CM_footer.addLayout(self.head)
        self.commonTools = QtWidgets.QHBoxLayout()
        self.commonTools.setContentsMargins(10, -1, -1, -1)
        self.commonTools.setSpacing(10)
        self.commonTools.setObjectName("commonTools")
        self.printCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.printCard.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.printCard.setFont(font)
        self.printCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.printCard.setStyleSheet("")
        self.printCard.setText("")
        self.printCard.setCheckable(False)
        self.printCard.setObjectName("printCard")
        self.commonTools.addWidget(self.printCard)
        self.saveCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.saveCard.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.saveCard.setFont(font)
        self.saveCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveCard.setStyleSheet("")
        self.saveCard.setText("")
        self.saveCard.setObjectName("saveCard")
        self.commonTools.addWidget(self.saveCard)
        self.delCard = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.delCard.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        self.delCard.setFont(font)
        self.delCard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delCard.setStyleSheet("")
        self.delCard.setText("")
        self.delCard.setObjectName("delCard")
        self.commonTools.addWidget(self.delCard)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 32))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    border:none;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.commonTools.addWidget(self.textBrowser)
        self.CM_footer.addLayout(self.commonTools)
        self.CM_footer.setStretch(0, 1)
        self.CM_footer.setStretch(1, 10)
        self.CM_main.addLayout(self.CM_footer)
        self.CM_main.setStretch(0, 1)
        self.CM_addNewCard.addLayout(self.CM_main)
        self.CM_addNewCard.setStretch(0, 1)
        self.CM_addNewCard.setStretch(1, 2)

        self.retranslateUi(Form)
        self.CMT_settingTab.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "卡片名"))
        self.label_7.setText(_translate("Form", "花费"))
        self.label_9.setText(_translate("Form", "消耗能量"))
        self.label_11.setText(_translate("Form", "使用半径"))
        self.label.setText(_translate("Form", "扩散半径"))
        self.label_21.setText(_translate("Form", "最小解锁分数(卡牌解锁限制)"))
        self.label_16.setText(_translate("Form", "瞄准类型"))
        self.label_17.setText(_translate("Form", "目标类型"))
        self.label_18.setText(_translate("Form", "卡牌标签"))
        self.addMyEffect.setToolTip(_translate("Form", "<html><head/><body><p>添加自定义标签</p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.cardDes_Tab), _translate("Form", "卡牌描述"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.cardStory_Tab), _translate("Form", "卡牌故事"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_baseSetting), _translate("Form", "基础"))
        self.label_19.setText(_translate("Form", "特效"))
        self.label_3.setText(_translate("Form", "高级扩散(会覆盖基础扩散)"))
        self.betterSpread_Search.setPlaceholderText(_translate("Form", "搜索"))
        self.label_13.setText(_translate("Form", "卡牌背景图"))
        self.backgroundImg_Search.setPlaceholderText(_translate("Form", "搜索"))
        self.deleteSelCardArt.setToolTip(_translate("Form", "<html><head/><body><p>删除卡面</p></body></html>"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_greateSetting), _translate("Form", "高级"))
        self.CMT_settingTab.setTabText(self.CMT_settingTab.indexOf(self.CMT_previewCard), _translate("Form", "预览"))
        self.CM_codeSource.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CodeTab), _translate("Form", "Code"))
        self.CM_remapCodeSource.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RemapCode_Tab), _translate("Form", "RemapCode"))
        self.tools.setToolTip(_translate("Form", "<html><head/><body><p>设置</p></body></html>"))
        self.printCard.setToolTip(_translate("Form", "<html><head/><body><p>alt+1</p></body></html>"))
        self.printCard.setWhatsThis(_translate("Form", "<html><head/><body><p>印卡</p></body></html>"))
        self.saveCard.setToolTip(_translate("Form", "<html><head/><body><p>ctrl+s</p></body></html>"))
        self.saveCard.setWhatsThis(_translate("Form", "<html><head/><body><p>保存</p></body></html>"))
        self.delCard.setToolTip(_translate("Form", "<html><head/><body><p>ctrl+s</p></body></html>"))
        self.delCard.setWhatsThis(_translate("Form", "<html><head/><body><p>保存</p></body></html>"))
from ..MyWidgets.CodeTextEditor import CodeTextEditor
from ..MyWidgets.DragLabel import DragLabel
from .. import AL_IDE_MainInterFace_rc
