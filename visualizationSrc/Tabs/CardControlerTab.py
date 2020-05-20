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
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTabBar, QWidget, QVBoxLayout, QCompleter, QApplication, QHBoxLayout, QLabel, \
    QGraphicsDropShadowEffect

from .. import MyWindow
from ..Controler.Bean.CardBean import Card
from ..Controler.CardControler import CardControler
from ..Util.ComboCheckBox import ComboCheckBox
from ..Util.windowsHelp import openTetraProject
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
        self.cardSelList = []
        self.cardEditTabList = []
        self.PC = PageControler(mainWindow,self)
        try:
            self.cardControler = CardControler()
            self.PC.toPage()
        except Exception as e: mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );print(e)

        self.initTab()
        self.initClick()
    def initTab(self):
        self.Tab.tabBar().setTabButton(0,QTabBar.RightSide,None)
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
        Search_Input.returnPressed.connect(lambda : self.PC.filter(Search_Input.text()))

        delBtn = self.UI.delSelCard
        def delSelCard():
            for cardId in self.cardSelList:
                self.cardControler.delCardById(cardId)
            self.cardSelList = []
            self.PC.toPage()
        delBtn.clicked.connect(delSelCard)

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

class PageControler:
    def __init__(self,mainWindow:MyWindow.MyWindow,CCT:CardControlerTab):
        self.mainWindow = mainWindow
        self._CCT = CCT
        self._UI = CCT.UI
        self._PageItemNum = 50
        self._currentPageNum = 0
        self._isFilter = False
        self._tempHL_List = []

        widget = QWidget()
        self._VL = QVBoxLayout()
        self._cardScroll = CCT.UI.cardScroll
        self._cardScroll.setWidget(widget)
        widget.setLayout(self._VL)
        self._initClick()
    @property
    def cardList(self):
        if not self._isFilter:
            self._cardList = self._CCT.cardControler.getCardList()
            return self._cardList
        else:
            newCardList = []
            for card in self._cardList:
                if card['displayName'].find(self.filterStr)!=-1:
                    newCardList.append(card)
            return newCardList
    @property
    def pageCount(self):
        return int(len(self.cardList) / self._PageItemNum) + 1
    def _initClick(self):
        pass

    def _refreshEle(self):
        while len(self._tempHL_List)>0:
            tempHL = self._tempHL_List[0]           # type: QHBoxLayout
            self._tempHL_List.remove(tempHL)
            while tempHL.count()>0:
                child = tempHL.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
                    del child
            tempHL.deleteLater();del tempHL
        for index in range(len(self.cardList[
                               self._currentPageNum * self._PageItemNum:
                               (self._currentPageNum + 1) * self._PageItemNum]
                           )):
            card = self.cardList[index]
            cardItemEle = cradItem_C()
            cardItemEle.setCardControlerTab(self._CCT)
            cardItemEle.refeshData(card)
            if index%2 == 0:
                tempHL = QHBoxLayout()
                self._VL.addLayout(tempHL)
                self._tempHL_List.append(tempHL)
            tempHL.addWidget(cardItemEle)
    def filter(self,filterStr):
        self.filterStr = filterStr
        if self.filterStr == "":
            self._isFilter = False
        else:
            self._isFilter = True
        self._refreshEle()
    def toPage(self,pageNum:int=0):
        self._currentPageNum = pageNum
        self._refreshEle()

class cradItem_C(QWidget,cardItemModel.Ui_main):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.WIDTH = 470;self.HEIGHT = 370
        self.BlurRadius = 10
        self.isSel = False
        self.setupUi(self)
        self._initUI()
    def setCardControlerTab(self,CCT:CardControlerTab):
        self.CCT = CCT
    def refeshData(self,cardDict:dict):
        if self.CCT == None:
            raise ValueError("未设置CCT")
        self.cardDict = cardDict

        self.NameAndId.setText(cardDict['displayName']+'(ID:'+cardDict['id']+')')
        self.price.setText(cardDict['price'])
        self.description.setText(cardDict['description'])
        self.description.setReadOnly(True)
        self.story.setText(cardDict['story'])
        self.story.setReadOnly(True)
        import os
        from ..Util.frozenDir import appPath
        backgroundImgPath = appPath()+"/CardBackground/"+cardDict.get('backgroundId','1')+"/Card.png"
        cardArtImgPath = appPath()+"/CardArt"+'/'+str(cardDict.get('id','Unknown'))+'.png'
        if os.path.exists(backgroundImgPath):
            try:
                self.backgroundImg.setPixmap(QPixmap(backgroundImgPath))
                # QPixmap图片大小自适应
                self.backgroundImg.setScaledContents(True)
                self.backgroundImg.setStyleSheet("border-image: none;")
            except Exception as e:print(e)
        if os.path.exists(cardArtImgPath):
            try:
                self.cardArt.setPixmap(QPixmap(cardArtImgPath))
                # QPixmap图片大小自适应
                self.cardArt.setScaledContents(True)
                self.cardArt.setStyleSheet("border-image: none;")
            except Exception as e:print(e)
        self.initClick()
    def initClick(self):
        cardDict = self.cardDict
        def clickCardItem(tag):
            def __clickCardItem():
                if tag == 'edit':
                    self.CCT.toCardDetailTab(cardDict['id'])
                elif tag == 'sel':
                    self.isSel = not self.isSel
                    if self.isSel:
                        self.CCT.cardSelList.append(cardDict['id'])
                        self.cardSelect.setStyleSheet("QPushButton{border-image: url(:/ico/Data/qrc/ico/selected.png);}")
                    else:
                        self.CCT.cardSelList.remove(cardDict['id'])
                        self.cardSelect.setStyleSheet("QPushButton{border-image: url(:/ico/Data/qrc/ico/select.png);}")
                elif tag == 'print':
                    self.printCard()
            return __clickCardItem
        self.cardEdit.clicked.connect(clickCardItem('edit'))
        self.cardSelect.clicked.connect(clickCardItem('sel'))
        self.cardPrint.clicked.connect(clickCardItem('print'))
    def _initUI(self):
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
    def printCard(self):
        mainWindow = self.CCT.mainWindow
        if self.CCT.cardControler.printCard(self.cardDict.get('id','newCard')):
            mainWindow.showInfo(
                "扩印卡牌",
                self.__class__.__name__,
                "扩印ID为:"+str(self.cardDict.get('id','newCard'))+",\n"+
                "名称为:"+self.cardDict.get('displayName','无名')+"的卡牌"
            )
            openTetraProject()
        else:
            mainWindow.showWarn(
                "印卡",
                self.__class__.__name__,
                "印卡时发生了错误"+",\n"+
                "请先添加卡牌"
            )

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
        self.initComboCheckBox()
        self.initData()
        self.initClick()
        self.initQuickKey()
        self.initBetterSettingInterface()
    def initData(self):
        card = self.card
        self.cardId = card.get('id','newCard')
        if card["id"] != "newCard":
            self.UI.CM_displayName.setText(card['displayName'])
            if card.get('price')=="":card['price'] = "0"
            self.UI.CM_price.setValue(int(card.get('price','0')))
            if card.get('energyReq')=="":card['energyReq'] = "0"
            self.UI.CM_energyReq.setValue(float(card.get('energyReq','0')))
            if card.get('range')=="":card['range'] = "0"
            self.UI.CM_range.setValue(float(card.get('range','0')))
            self.UI.CM_description.setText(card['description'])
            self.UI.CM_story0.setText(card['story'])
            self.UI.CM_codeSource.setText(card['code'])
            self.UI.CM_remapCodeSource.setText(card['remapCode'])

            if card.get('spreadRadius')=="":card['spreadRadius'] = "0"
            self.UI.spreadRadius.setValue(float(card.get('spreadRadius','0')))
            if card.get('minUnlockGrade')=="":card['minUnlockGrade'] = "0"
            self.UI.minUnlockGrade.setValue(int(card.get('minUnlockGrade','0')))
            for sel in card['aimTypeCode'].split(';'):
                self.UI.aimTypeCode.selQCheckBoxByName(sel.split(':')[0])
            for sel in card['perferredTargetTypeCode'].split(';'):
                self.UI.perferredTargetTypeCode.selQCheckBoxByName(sel.split(':')[0])
            for sel in card['tagCode'].split(';'):
                self.UI.tagCode.selQCheckBoxByName(sel.split(':')[0])

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
    def getCard(self):
        UI = self.UI
        if UI.CM_displayName.text() == "":
            UI.CM_displayName.setText("无名")
        return Card(
            id=self.cardId,
            displayName=UI.CM_displayName.text(), price=UI.CM_price.text(), energyReq=UI.CM_energyReq.text(),
            range=UI.CM_range.text(),
            description=UI.CM_description.toPlainText(),
            story=UI.CM_story0.toPlainText(),
            code=UI.CM_codeSource.toPlainText(),
            remapCode=UI.CM_remapCodeSource.toPlainText(),
            spreadRadius=UI.spreadRadius.value(),
            minUnlockGrade=UI.minUnlockGrade.value(),
            aimTypeCode=";".join(UI.aimTypeCode.currentText()),
            perferredTargetTypeCode=";".join(UI.perferredTargetTypeCode.currentText()),
            tagCode=";".join(UI.tagCode.currentText()),
            effectCode=UI.effectCode.text(),
            backgroundId=self.selBackgrondImgName,
        )
    def initClick(self):
        UI = self.UI
        mainWindow = self.mainWindow
        def __saveCard():
            if self.card["id"] == "newCard":
                newCard = self.cardControler.addCard(**self.getCard().toDict())
                if newCard!={}:
                    self.mainWindow.showInfo(
                        "添加卡牌",
                        self.__class__.__name__,
                        "成功新添ID为:"+str(newCard.get('id','newCard'))+",\n"+
                        "名称为:"+UI.CM_displayName.text()+"的卡牌"
                    )
                    self.cardMake.PC.toPage(self.cardMake.PC.pageCount)
                    self.cardMake.removeNewCardTab()
                    self.cardMake.toCardDetailTab(str(newCard.get('id','newCard')))
                else:
                    self.mainWindow.showWarn(
                        "添加卡牌",
                        self.__class__.__name__,
                        "新添名称为:"+self.card.get('displayName')+"发生了错误"+",\n"+
                        "请保证文件读取权限、卡牌列表最后一张卡牌ID为数字"
                    )
            else:
                if self.cardControler.updataCard(**self.getCard().toDict()):
                    self.mainWindow.showInfo(
                        "修改卡牌",
                        self.__class__.__name__,
                        "修改ID为:"+self.cardId+",\n"+
                        "名称为:"+self.card.get('displayName')+"成功"
                    )
                    self.cardMake.PC.toPage()
                else:
                    self.mainWindow.showWarn(
                        "修改卡牌",
                        self.__class__.__name__,
                        "修改ID为:"+self.cardId+",\n"+
                        "名称为:"+self.card.get('displayName')+"发生了错误"+",\n"+
                        "请保证文件读取权限"
                    )
        UI.saveCard.clicked.connect(__saveCard)
        def __printCard():
            if self.cardControler.printCard(self.card.get('id','newCard')):
                mainWindow.showInfo(
                    "扩印卡牌",
                    self.__class__.__name__,
                    "扩印ID为:"+str(self.cardId)+",\n"+
                    "名称为:"+UI.CM_displayName.text()+"的卡牌"
                )
                openTetraProject()
            else:
                mainWindow.showWarn(
                    "印卡",
                    self.__class__.__name__,
                    "印卡时发生了错误"+",\n"+
                    "请先添加卡牌"
                )
        UI.printCard.clicked.connect(__printCard)
    def initQuickKey(self):
        def __keyPressEvent(event):
            UI = self.UI
            if (event.key() == Qt.Key_1):
                if QApplication.keyboardModifiers() == Qt.AltModifier:
                    UI.printCard.click()
            if (event.key() == Qt.Key_S):
                if QApplication.keyboardModifiers() == Qt.ControlModifier:
                    UI.saveCard.click()
        self.Widget.keyPressEvent = __keyPressEvent
    def initComboCheckBox(self):
        def __comboBoxToComboCheckBox(items,parent,this):
            parent.removeWidget(this);this.setParent(None)
            comboBox = ComboCheckBox()
            comboBox.setGeometry(this.geometry())
            comboBox.setMinimumSize(this.size())
            comboBox.loadItems(items)
            parent.addWidget(comboBox)
            return comboBox

        self.UI.aimTypeCode = __comboBoxToComboCheckBox([
            'EnvOnly','Single0nly','AllowOutOfStageBorder',
            'ChaTagExclude','Boss','Trap','Turret',
            'HpLessThanSelf','NotAllowSelf',
            'ChaTagLimit','Machine','ThrougWall',
        ],self.UI.aimTypeCode_L,self.UI.aimTypeCode)
        self.UI.perferredTargetTypeCode = __comboBoxToComboCheckBox([
            "emy","self","player",
            "died","HasBuff","lowHpP","lowHpPltmt",
            "Breakable","tmt",
        ],self.UI.perferredTargetTypeCode_L,self.UI.perferredTargetTypeCode)
        self.UI.tagCode = __comboBoxToComboCheckBox([
            "Bomb","Boxing","Bullet","BulletCraft",
            "Craft","CardContainer","CombatonlyPosiBuff","CombatOnly",
            "Dedicated ","Debuff","DebuffProp",
            "Elec","EnvObject","Equipment",
            "Food",
            "Hidden",
            "Ice",
            "Machine",
            "NanbaPattern","NotAllowContainerFill","NotAllowDestroy0nUse","NotAllowTakeInteraction",
            "Prop","PosiBuff",
            "Turret","Trap",
            "Unremovable",
        ],self.UI.tagCode_L,self.UI.tagCode)
    def initBetterSettingInterface(self):
        self.backgrondImgWidgetList = []
        UI = self.UI
        tempWidget = QWidget()
        tempHL = QHBoxLayout()
        tempWidget.setLayout(tempHL)
        tempHL.setContentsMargins(0,0,0,0)

        import os
        from ..Util.frozenDir import appPath
        backgroundImgPath = appPath()+"/CardBackground"
        if not os.path.exists(backgroundImgPath):
            os.makedirs(backgroundImgPath)
        backgrondImgId = self.card.get('backgroundId','1')
        selStyle = "QWidget{background-color: rgb(255,255,255);border-radius:10px;}"
        noselStyle = "QWidget:hover{background-color: rgb(255,255,255);border-radius:10px;}"
        for childDirName in os.listdir(backgroundImgPath):
            childDirPath = backgroundImgPath+'/'+childDirName+'/'

            backgrondImgWidget = QWidget()
            self.backgrondImgWidgetList.append(backgrondImgWidget)
            backgrondImgWidget.setMinimumWidth(100)
            backgrondImgWidget.setObjectName("backgrondImgWidget_"+childDirName)
            if backgrondImgId==childDirName:
                self.selBackgrondImgName = childDirName
                backgrondImgWidget.setStyleSheet(selStyle)
            else:
                backgrondImgWidget.setStyleSheet(noselStyle)
            try:
                tempVL = QVBoxLayout()
                tempVL.setContentsMargins(0, 0, 0, 0)

                backgroundImgName = QLabel(backgrondImgWidget)
                backgroundImgName.setGeometry(QtCore.QRect(0, 0, 100, 20))
                backgroundImgName.setMinimumSize(100,20)
                backgroundImgName.setText(childDirName)
                backgroundImgName.setAlignment(Qt.AlignCenter)
                backgroundImgName.setStyleSheet("QLabel{font-size:18px;}")

                backgroundImg = QLabel(backgrondImgWidget)
                backgroundImg.setGeometry(QtCore.QRect(0, 0, 100, 100))
                backgroundImg.setMinimumSize(100,100)
                backgroundImg.setPixmap(QPixmap(childDirPath+'Card.png'))
                tempVL.addWidget(backgrondImgWidget)

                tempHL.addLayout(tempVL)
            except:pass
            def selThisImg(childDirName,backgrondImgWidget):
                def __selThisImg(evt):
                    if evt.buttons() == QtCore.Qt.LeftButton:
                        self.selBackgrondImgName = childDirName
                        for backgrondImgWidgetX in self.backgrondImgWidgetList:
                            backgrondImgWidgetX.setStyleSheet(noselStyle)
                        backgrondImgWidget.setStyleSheet(selStyle)
                return __selThisImg

            backgrondImgWidget.mousePressEvent = selThisImg(childDirName,backgrondImgWidget)

        UI.backgroundImg.setWidget(tempWidget)
        # 必须加这句，不然没有scrollBar的样式
        UI.backgroundImg.horizontalScrollBar().setStyleSheet("")
        pass
