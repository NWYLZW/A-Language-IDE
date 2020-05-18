#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardControlerTab.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 4:06
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   卡牌制作界面
'''
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QTabBar, QWidget, QVBoxLayout, QCompleter, QApplication

from .. import MyWindow
from ..Controler.Bean.CardBean import Card
from ..Controler.CardControler import CardControler
from ..qtUI.CardControler import cardItemModel, cardDetailsModel, cardControler
from ..Util.HighLighterUtil import HighLighter

class CardControlerTab:
    def __init__(self,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow

        self.Widget = QWidget()
        self.UI = cardControler.Ui_Form()
        self.UI.setupUi(self.Widget)

        self.Tab = self.UI.CardControler_Tabs
        self.CardList = self.UI.CardList
        self.cardEditTabList = []
        try:
            self.cardControler = CardControler()
            self.refreshCardList(self.cardControler.getCardList())
        except Exception as e:
            mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            )
            print(e)

        self.initTab()
        self.initClick()
    def initTab(self):
        self.Tab.tabBar().setTabButton(0,QTabBar.RightSide,None)
        self.Tab.setTabText(0,"卡牌列表")
        for i in range(1,self.Tab.count()):
            self.Tab.removeTab(i)
        self.initTabClose()
    def initTabClose(self):
        def __closeTab(currentIndex):
            currentQWidget = self.Tab.widget(currentIndex)
            if currentQWidget == None: return
            currentQWidget.deleteLater()
            self.Tab.removeTab(currentIndex)
            for cardEditTabDict in self.cardEditTabList:
                if cardEditTabDict['index'] == currentIndex:
                    self.cardEditTabList.remove(cardEditTabDict)
                    break
        self.Tab.tabCloseRequested.connect(__closeTab)
    def initClick(self):
        makeNewCardBtn = self.UI.makeNewCard
        def makeNewCard():
            self.toCardDetailTab("newCard")
        makeNewCardBtn.clicked.connect(makeNewCard)

        Search_Input = self.UI.Search_Input
        Search_Input\
            .setCompleter(
            QCompleter([card['displayName'] for card in self.cardControler.getCardList()])
        )
        def searchCard():
            inputStr = Search_Input.text()
            if inputStr=='': self.refreshCardList(self.cardControler.getCardList())
            newCardList = []
            for card in self.cardControler.getCardList():
                if card['displayName'].find(inputStr)!=-1:
                    newCardList.append(card)
            self.refreshCardList(newCardList)
        Search_Input.returnPressed.connect(searchCard)

        delBtn = self.UI.delSelCard
        def delSelCard():
            for cardId in self.cardSelList:
                self.cardControler.delCardById(cardId)
            self.refreshCardList(self.cardControler.getCardList())
        delBtn.clicked.connect(delSelCard)

    def refreshCardList(self,cardList):
        UI = self.UI
        self.cardSelList = []
        cardScroll =UI.cardScroll
        tempWidget = QWidget()
        tempHL = QVBoxLayout()
        tempWidget.setLayout(tempHL)
        for index in range(len(cardList)):
            card = cardList[index]
            cardItemEle = QWidget()
            cardItemUI = cardItemModel.Ui_Form()
            cardItemUI.setupUi(cardItemEle)

            cardItemUI.cardItemModel_ID.setText('id:  '+card['id'])
            cardItemUI.cardItemModel_DisplayName.setText('卡牌名:  '+card['displayName'])
            cardItemUI.cardItemModel_Description.setText('卡牌简介:  '+card['description'])
            cardItemUI.cardItemModel_Code.setText(card['code'])
            cardItemUI.cardItemModel_Story.setText(card['story'])
            def clickCardItem(index,tag):
                def __editCard():
                    if tag == 'edit':
                        self.toCardDetailTab(cardList[index]['id'])
                    elif tag == 'sel':
                        self.cardSelList.append(cardList[index]['id'])
                return __editCard
            cardItemUI.cardItemModel_edit.clicked.connect(clickCardItem(index,'edit'))
            cardItemUI.cardItemModel_sel.clicked.connect(clickCardItem(index,'sel'))

            tempHL.addWidget(cardItemEle)
        cardScroll.setWidget(tempWidget)
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
        cardEditTabWidget = QWidget()
        uiForm = cardDetailsModel.Ui_Form()
        uiForm.setupUi(cardEditTabWidget)
        cardEditTabDict = {
            "tab":cardEditTabWidget,
            "id":cardId,
            "displayName":card['displayName'],
        }
        self.cardEditTabList.append(cardEditTabDict)
        cardEditTabDict['index'] = self.Tab\
            .addTab(cardEditTabWidget,card['displayName']+'('+card['id']+')')
        self.Tab.setCurrentWidget(cardEditTabWidget)
        if cardId == "newCard":
            self.newCardEditTabDict = cardEditTabDict
        cardEditTabDict['cardDetail_C'] = cardDetail_C(
            card=card,
            cardDetailsModel_UI=uiForm,
            cardDetailsModel_Widget=cardEditTabWidget,
            cardMake=self,)

class cardDetail_C:
    def __init__(self,
                 cardDetailsModel_UI: cardDetailsModel.Ui_Form,
                 cardDetailsModel_Widget: QWidget,
                 card:dict, cardMake:CardControlerTab):
        self.UI = cardDetailsModel_UI
        from ..Util.CompleterUtil import Completer
        self.UI.completer = Completer()
        self.Widget = cardDetailsModel_Widget
        self.cardMake = cardMake
        self.mainWindow = cardMake.mainWindow
        self.cardControler = cardMake.cardControler
        self.card = card

        self.settingTab = cardDetailsModel_UI.CMT_settingTab
        self.initTextEditor()
        self.initSettingTab()
        self.initData()
        self.initClick()
        self.initQuickKey()
    def initData(self):
        card = self.card
        if card["id"] != "newCard":
            self.cardId = card.get('id','')
            self.UI.CM_addCard.setText("修改")
            self.UI.CM_displayName.setText(card['displayName'])
            self.UI.CM_price.setValue(int(card['price']))
            self.UI.CM_energyReq.setValue(float(card['energyReq']))
            self.UI.CM_range.setValue(float(card['range']))
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
                    self.mainWindow.showInfo(
                        "添加卡牌",
                        self.__class__.__name__,
                        "成功新添ID为:"+newCardId+",\n"+
                        "名称为:"+UI.CM_displayName.text()+"的卡牌"
                    )
                    self.cardMake.refreshCardList(self.cardControler.getCardList())
                    self.cardMake.removeNewCardTab()
                    self.cardMake.toCardDetailTab(newCardId)
                else:
                    self.mainWindow.showWarn(
                        "添加卡牌",
                        self.__class__.__name__,
                        "新添名称为:"+self.card.get('displayName')+"发生了错误"+",\n"+
                        "请保证文件读取权限、卡牌列表最后一张卡牌ID为数字"
                    )
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
                    self.mainWindow.showInfo(
                        "修改卡牌",
                        self.__class__.__name__,
                        "修改ID为:"+self.cardId+",\n"+
                        "名称为:"+self.card.get('displayName')+"成功"
                    )
                    self.cardMake.refreshCardList(self.cardControler.getCardList())
                else:
                    self.mainWindow.showWarn(
                        "修改卡牌",
                        self.__class__.__name__,
                        "修改ID为:"+self.cardId+",\n"+
                        "名称为:"+self.card.get('displayName')+"发生了错误"+",\n"+
                        "请保证文件读取权限"
                    )
        UI.CM_addCard.clicked.connect(__insertCard)
        def __printCard():
            originStyleSheet = UI.CM_printCard.styleSheet()
            UI.CM_printCard.setStyleSheet(originStyleSheet+"background-color: rgb(20, 100, 215);")
            def CM_printCard_end():
                QTimer.singleShot(200, lambda: UI.CM_printCard.setStyleSheet(originStyleSheet))

            if self.card['id'] == "newCard":
                mainWindow.showWarn(
                    "印卡",
                    self.__class__.__name__,
                    "印卡时发生了错误"+",\n"+
                    "请先添加卡牌"
                )
                CM_printCard_end()
                return
            import os
            from ..Util.frozenDir import appPath
            messageTxtPath = os.path.expanduser('~')+'\AppData\Local\Temp\TetraProject'
            if not os.path.exists(messageTxtPath):
                os.makedirs(messageTxtPath)
            with open(messageTxtPath+'\message.txt','w',encoding='utf-8') as f1:
                f1.write("Card:'"+self.cardId+"','id',"+os.path.abspath(appPath()+"/Database/Database.xls")+";")
            self.mainWindow.showInfo(
                "扩印卡牌",
                self.__class__.__name__,
                "扩印ID为:"+self.cardId+",\n"+
                "名称为:"+UI.CM_displayName.text()+"的卡牌"
            )
            CM_printCard_end()
        UI.CM_printCard.clicked.connect(__printCard)
    def initQuickKey(self):
        self.Widget.keyPressEvent = self.keyPressEvent
    def keyPressEvent(self, event):
        UI = self.UI
        if (event.key() == Qt.Key_1):
            if QApplication.keyboardModifiers() == Qt.AltModifier:
                UI.CM_printCard.click()
        if (event.key() == Qt.Key_S):
            if QApplication.keyboardModifiers() == Qt.ControlModifier:
                UI.CM_addCard.click()