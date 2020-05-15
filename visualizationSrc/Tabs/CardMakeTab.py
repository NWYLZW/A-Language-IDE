#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardMakeTab.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 4:06
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   卡牌制作界面
'''
import copy

from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTabBar, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QTextBrowser

from ..Controler.Bean.CardBean import Card
from ..Controler.CardControler import CardControler
from ..qtUI import cardItemModel
from ..qtUI.mainInterFace import Ui_MainWindow
from ..Util.HighLighterUtil import HighLighter

class CardDetails_Model:
    def __init__(self):
        pass

class CardMake:
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow):
        self.UI = UI
        self.mainWindow = mainWindow
        self.Tab = UI.CMT_Tab
        self.CardList = UI.CMT_CardList
        self.CardDetails_Model = UI.CMT_CardDetails_Model

        self.settingTab = UI.CMT_settingTab
        self.cardControler = CardControler()

        self.initTab()
        self.initCardListTab()
        self.initTextEditor()
        self.initSettingTab()
        self.initClick()
    def refreshCardList(self,cardList):
        UI = self.UI
        cardScroll =UI.CMT_C_cardScroll
        tempWidget = QWidget()
        tempHL = QVBoxLayout()
        tempWidget.setLayout(tempHL)
        for card in cardList:
            tempx = QWidget()
            cardItemModel.Ui_Form().setupUi(tempx)
            tempx.findChild(QLabel,"cardItemModel_ID").setText('id:  '+card['id'])
            tempx.findChild(QLabel,"cardItemModel_DisplayName").setText('卡牌名:  '+card['displayName'])
            tempx.findChild(QLabel,"cardItemModel_Description").setText('卡牌简介:  '+card['description'])
            tempx.findChild(QTextBrowser,"cardItemModel_Code").setText(card['code'])
            tempx.findChild(QTextBrowser,"cardItemModel_Story").setText(card['story'])

            tempHL.addWidget(tempx)
        cardScroll.setWidget(tempWidget)
    def initCardListTab(self):
        self.refreshCardList(self.cardControler.getCardList())
    def initTab(self):
        self.Tab.tabBar().setTabButton(0,QTabBar.RightSide,None)
        self.Tab.setTabText(0,"卡牌列表")
        for i in range(1,self.Tab.count()):
            self.Tab.removeTab(i)
        pass
    def initTextEditor(self):
        UI = self.UI
        def initFont(editor):
            from PyQt5.QtGui import QFont
            editor.setPlainText('')
            font = editor.font()
            font.setFamily('Consolas')
            font.setStyleHint(QFont.Monospace)
            font.setPointSize(14)
            editor.setFont(font)
            editor.setTabStopWidth(16)
        from visualizationSrc.Util.TextEditorUtil import TextEditor
        def QTextEditToTextEditor(parent,mQTextEdit):
            parent.removeWidget(mQTextEdit);mQTextEdit.setParent(None)
            mQTextEdit = TextEditor()
            parent.addWidget(mQTextEdit)
            initFont(mQTextEdit)

            mQTextEdit.set_completer(UI.completer.completer)
            mQTextEdit.HL = HighLighter(mQTextEdit.document())
            return mQTextEdit

        UI.CM_codeSource = QTextEditToTextEditor(UI.cardMakeTap_code,UI.CM_codeSource)
        UI.CM_remapCodeSource = QTextEditToTextEditor(UI.cardMakeTap_remap,UI.CM_remapCodeSource)
    def initSettingTab(self):
        tabTextList = ["基础设置","高级设置"]
        for i in range(tabTextList.__len__()):
            self.settingTab.setTabText(i,tabTextList[i])
    def initClick(self):
        UI = self.UI
        mainWindow = self.mainWindow
        def __insertCard():
            if self.cardControler.addCard(**Card(
                displayName=UI.CM_displayName.text(), price=UI.CM_price.text(), energyReq=UI.CM_energyReq.text(),
                range=UI.CM_range.text(),
                description=UI.CM_description.toPlainText(),
                story=UI.CM_story0.toPlainText(),
                code=UI.CM_codeSource.toPlainText(),
                remapCode=UI.CM_remapCodeSource.toPlainText()
            ).toDict())[1]:
                QMessageBox.information(
                    mainWindow,
                    '成功', '添加成功',
                    QMessageBox.Yes)
            else:
                QMessageBox.ctitical(
                    mainWindow,
                    '错误', '发送了一个错误',
                    QMessageBox.Yes)
        UI.CM_addCard.clicked.connect(__insertCard)
