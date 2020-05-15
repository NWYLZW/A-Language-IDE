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

from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTabBar, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QTextBrowser, \
    QPushButton

from ..Controler.Bean.CardBean import Card
from ..Controler.CardControler import CardControler
from ..qtUI import cardItemModel, cardDetailsModel
from ..qtUI.mainInterFace import Ui_MainWindow
from ..Util.HighLighterUtil import HighLighter

class CardDetails_Model:
    def __init__(self):
        pass

class CardMake:
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow):
        self.UI = UI
        self.mainWindow = mainWindow
        self.cardControler = CardControler()

        self.Tab = UI.CMT_Tab
        self.CardList = UI.CMT_CardList
        self.cardEditTabList = []

        self.settingTab = UI.CMT_settingTab

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
        for index in range(len(cardList)):
            card = cardList[index]
            cardItemEle = QWidget()
            cardItemModel.Ui_Form().setupUi(cardItemEle)
            cardItemEle.findChild(QLabel,"cardItemModel_ID").setText('id:  '+card['id'])
            cardItemEle.findChild(QLabel,"cardItemModel_DisplayName").setText('卡牌名:  '+card['displayName'])
            cardItemEle.findChild(QLabel,"cardItemModel_Description").setText('卡牌简介:  '+card['description'])
            cardItemEle.findChild(QTextBrowser,"cardItemModel_Code").setText(card['code'])
            cardItemEle.findChild(QTextBrowser,"cardItemModel_Story").setText(card['story'])
            edit = cardItemEle.findChild(QPushButton,"cardItemModel_edit")
            def editCard(index):
                def __editCard():
                    self.__editCard(cardList[index]['id'])
                return __editCard
            edit.clicked.connect(editCard(index))

            tempHL.addWidget(cardItemEle)
        cardScroll.setWidget(tempWidget)
    def initCardListTab(self):
        self.refreshCardList(self.cardControler.getCardList())
    def initTab(self):
        self.Tab.tabBar().setTabButton(0,QTabBar.RightSide,None)
        self.Tab.setTabText(0,"卡牌列表")
        for i in range(1,self.Tab.count()):
            self.Tab.removeTab(i)
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

    def __editCard(self,cardId):
        for cardEditTabItem in self.cardEditTabList:
            if cardEditTabItem["id"]==cardId:
                self.Tab \
                    .addTab(cardEditTabItem["tab"], cardEditTabItem['displayName']+'('+cardEditTabItem['id']+')')
                self.Tab.setCurrentWidget(cardEditTabItem["tab"])
                return

        card = self.cardControler.getCardById(cardId)
        cardEditTabEle = QWidget()
        cardDetailsModel.Ui_Form().setupUi(cardEditTabEle)
        cardEditTabDict = {
            "tab":cardEditTabEle,
            "id":cardId,
            "displayName":card['displayName'],
        }
        self.cardEditTabList.append(cardEditTabDict)
        def __closeTab(currentIndex):
            currentQWidget = self.Tab.widget(currentIndex)
            if currentQWidget == None: return
            currentQWidget.deleteLater()
            self.Tab.removeTab(currentIndex)
            for cardEditTabDict in self.cardEditTabList:
                if cardEditTabDict['index'] == currentIndex:
                    self.cardEditTabList.remove(cardEditTabDict)
                    return
        self.Tab.tabCloseRequested.connect(__closeTab)
        cardEditTabDict['index'] = self.Tab\
            .addTab(cardEditTabEle,card['displayName']+'('+card['id']+')')
        self.Tab.setCurrentWidget(cardEditTabEle)

class cardDetail:
    def __init__(self):
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