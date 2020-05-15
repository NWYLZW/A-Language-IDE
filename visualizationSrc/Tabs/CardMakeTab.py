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
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTabBar, QLabel, QWidget, QVBoxLayout, QTextBrowser, \
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

        self.initTab()
        self.initCardListTab()
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
                    self.toCardDetailTab(cardList[index]['id'])
                return __editCard
            edit.clicked.connect(editCard(index))

            tempHL.addWidget(cardItemEle)
        cardScroll.setWidget(tempWidget)
    def initTab(self):
        self.Tab.tabBar().setTabButton(0,QTabBar.RightSide,None)
        self.Tab.setTabText(0,"卡牌列表")
        for i in range(1,self.Tab.count()):
            self.Tab.removeTab(i)
    def initCardListTab(self):
        self.refreshCardList(self.cardControler.getCardList())
    def initClick(self):
        makeNewCardBtn =self.UI.makeNewCard
        def makeNewCard():
            self.toCardDetailTab("newCard")
        makeNewCardBtn.clicked.connect(makeNewCard)

    def removeNewCardTab(self):
        currentQWidget = self.newCardEditTabDict['tab']
        currentQWidget.deleteLater()
        self.Tab.removeTab(self.newCardEditTabDict['index'])
        self.cardEditTabList.remove(self.newCardEditTabDict)
        self.newCardEditTabDict = None
        return
    def toCardDetailTab(self, cardId):
        for cardEditTabItem in self.cardEditTabList:
            if cardEditTabItem["id"]==cardId:
                self.Tab \
                    .addTab(cardEditTabItem["tab"], cardEditTabItem['displayName']+'('+cardEditTabItem['id']+')')
                self.Tab.setCurrentWidget(cardEditTabItem["tab"])
                return
        if cardId != "newCard":
            card = self.cardControler.getCardById(cardId)
        else:
            card = {
                "id":"newCard",
                "displayName":"无名",}
        cardEditTabEle = QWidget()
        uiForm = cardDetailsModel.Ui_Form()
        uiForm.setupUi(cardEditTabEle)
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
        if cardId == "newCard":
            self.newCardEditTabDict = cardEditTabDict
        cardEditTabDict['cardDetail_C'] = cardDetail_C(
            card=card,
            cardDetailsModel_UI=uiForm,
            cardMake=self,)

class cardDetail_C:
    def __init__(self,cardDetailsModel_UI:cardDetailsModel.Ui_Form,card,cardMake):
        self.UI = cardDetailsModel_UI
        from ..Util.CompleterUtil import Completer
        self.UI.completer = Completer()
        self.cardMake = cardMake
        self.mainWindow = cardMake.mainWindow
        self.cardControler = cardMake.cardControler
        self.card = card
        self.initUI()

        self.settingTab = cardDetailsModel_UI.CMT_settingTab
        self.initTextEditor()
        self.initSettingTab()
        self.initClick()
    def initUI(self):
        card = self.card
        if card["id"] != "newCard":
            self.cardId = card.get('id','')
            self.UI.CM_addCard.setText("修改")
            self.UI.CM_displayName.setText(card['displayName'])
            self.UI.CM_price.setValue(int(card['price']))
            self.UI.CM_energyReq.setValue(int(card['energyReq']))
            self.UI.CM_range.setValue(int(card['range']))
            self.UI.CM_description.setText(card['description'])
            self.UI.CM_story0.setText(card['story'])
            self.UI.CM_codeSource.setText(card['code'])
            self.UI.CM_remapCodeSource.setText(card['remapCode'])
        self.UI.CM_price.setMaximum(100000)
        self.UI.CM_energyReq.setMaximum(100000)
        self.UI.CM_range.setMaximum(100000)
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
            if UI.CM_displayName.text() == "":
                UI.CM_displayName.setText("无名")
            if self.card["id"] == "newCard":
                newCardId = self.cardControler.addCard(**Card(
                    displayName=UI.CM_displayName.text(), price=UI.CM_price.text(), energyReq=UI.CM_energyReq.text(),
                    range=UI.CM_range.text(),
                    description=UI.CM_description.toPlainText(),
                    story=UI.CM_story0.toPlainText(),
                    code=UI.CM_codeSource.toPlainText(),
                    remapCode=UI.CM_remapCodeSource.toPlainText()
                ).toDict())
                if newCardId!=-1:
                    QMessageBox.information(
                        mainWindow,
                        '成功', '添加成功',
                        QMessageBox.Yes)
                    self.cardMake.refreshCardList(self.cardControler.getCardList())
                    self.cardMake.removeNewCardTab()
                    self.cardMake.toCardDetailTab(newCardId)
                else:
                    QMessageBox.ctitical(
                        mainWindow,
                        '错误', '发送了错误',
                        QMessageBox.Yes)
            else:
                if self.cardControler.updataCard(**Card(
                    id=self.cardId,
                    displayName=UI.CM_displayName.text(), price=UI.CM_price.text(), energyReq=UI.CM_energyReq.text(),
                    range=UI.CM_range.text(),
                    description=UI.CM_description.toPlainText(),
                    story=UI.CM_story0.toPlainText(),
                    code=UI.CM_codeSource.toPlainText(),
                    remapCode=UI.CM_remapCodeSource.toPlainText()
                ).toDict()):
                    QMessageBox.information(
                        mainWindow,
                        '成功', '修改成功',
                        QMessageBox.Yes)
                    self.cardMake.refreshCardList(self.cardControler.getCardList())
                else:
                    QMessageBox.ctitical(
                        mainWindow,
                        '错误', '发送了错误',
                        QMessageBox.Yes)
        UI.CM_addCard.clicked.connect(__insertCard)
        def __printCard():
            UI.CM_printCard.setStyleSheet(
                "color: rgb(255, 255, 255);background-color: rgb(20, 100, 215);margin-left:100px;margin-right:100px;padding:10px;border-radius:10px;")
            if self.card['id'] == "newCard":
                QMessageBox.Warning(
                    mainWindow,
                    '失败', '请先添加卡牌',
                    QMessageBox.Yes)
            import os
            from ..Util.frozenDir import appPath
            temp = appPath()
            proHome = temp[0] + (lambda : "" if temp[1] else "../../../")()
            with open(os.path.expanduser('~')+'\AppData\Local\Temp\TetraProject\message.txt','w',encoding='utf-8') as f1:
                f1.write("Card:'"+self.cardId+"','id',"+os.path.abspath(proHome+"Database/Database.xls")+";")

            QTimer.singleShot(500, lambda: UI.CM_printCard.setStyleSheet(
                "color: rgb(255, 255, 255);background-color: rgb(50, 150, 255);margin-left:100px;margin-right:100px;padding:10px;border-radius:10px;"))
        UI.CM_printCard.clicked.connect(__printCard)
