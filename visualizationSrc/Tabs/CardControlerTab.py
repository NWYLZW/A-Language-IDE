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
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCompleter, QApplication, QHBoxLayout, QLabel, \
    QGraphicsDropShadowEffect

from .. import MyWindow
from ..Controler.Bean.CardBean import Card
from ..Controler.CardControler import CardControler
from ..Helper.ListTabHelper import ListTabHelper
from ..Helper.PageHelper import PageHelper
from ..Util.ComboCheckBox import ComboCheckBox
from ..Util.ImportExportCardUtil import *
from ..Util.LogUtil import logLevel, log
from ..Util.UserUtil import UserUtil
from ..Util.frozenDir import tempPath, appPath
from ..Util.windowsHelp import openTetraProject
from ..qtUI.CardControler import cardItemModel, cardDetailsModel, cardLibWidget
from ..qtUI.MyWidgets.HighLighter import HighLighter
from ..Util.CompleterUtil import Completer

class CardControlerTab(ListTabHelper):
    def __init__(self, mainWindow: MyWindow.MyWindow):
        super().__init__(None)
        self.mainWindow = mainWindow
        self._initData()
        self._initTab()
    def _initData(self):
        self.cardControler = CardControler()
        self.CLT = cardLibTab(self)
    def _initTab(self):
        imgPath = tempPath()+"\\visualizationSrc\\Data\\qrc\\cardPkg.png"
        self.addWidgetTab(
            widget=self.CLT,
            title="卡库",
            content="当前卡库共有"+str(len(self.cardControler.getCardList()))+"张卡牌",
            icoImage=QPixmap(imgPath),
            isShowClose=False,
        )
        self.setCurrentIndex(0)
    def _addCardDatailTab(self, cardDict):
        if cardDict != "newCard":
            index = self.addWidgetTab(
                widget=cardDetailTab(self,cardDict),
                title= cardDict['displayName']+'(ID:'+cardDict['id']+')',
                content=cardDict['description'],
                icoImage=QPixmap(appPath()+"/CardArt"+'/'+str(cardDict.get('id','Unknown'))+'.png'),
                isShowClose=True,
            )
            return index
        else:
            index = self.addWidgetTab(
                widget=cardDetailTab(self, {}),
                title= "新建卡牌*",
                content="还没有设置描述哦~",
                icoImage=None,
                isShowClose=True,
            )
            return index
    def removeNewCardTab(self, newCardTabWidget):
        self.removeWidgetTab(self.widgetIndex(newCardTabWidget))
    def toCardDetailTab(self, cardDict):
        return self.setCurrentIndex(self._addCardDatailTab(cardDict))
    def _initClick(self):
        pass

class cardLibTab(QWidget,cardLibWidget.Ui_main):
    def __init__(self, CCT: CardControlerTab):
        super().__init__(None)
        self.CCT = CCT
        self.mainWindow = CCT.mainWindow
        self.setupUi(self)
        self._initData()

        try:
            self.cardPC = cardPageControler(self)
            self.cardPC.toPage()
        except Exception as e: self.mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );log.record(logLevel.ERROR, 'CardControlerTab.__init__', e)

        self._initClick()
    def _initData(self):
        self.cardSelList = []
    def _initClick(self):
        makeNewCardBtn = self.makeNewCard
        def makeNewCard():
            self.toCardDetailTab("newCard")
        makeNewCardBtn.clicked.connect(makeNewCard)

        Search_Input = self.Search_Input
        Search_Input\
            .setCompleter(
            QCompleter([card['displayName'] for card in self.CCT.cardControler.getCardList()])
        )
        Search_Input.returnPressed.connect(lambda : self.cardPC.filter(Search_Input.text()))

        delBtn = self.delSelCard
        def delSelCard():
            if len(self.cardSelList)==0:
                self.mainWindow.showWarn(
                    "删除卡牌",
                    self.__class__.__name__,
                    "还没有选择卡牌"
                );return
            tempList = []
            for cardId in self.cardSelList:
                tempList.append(self.CCT.cardControler.getCardById(cardId))
                self.CCT.cardControler.delCardById(cardId)
            self.cardSelList = []
            self.cardPC.toPage()
            self.mainWindow.showInfo(
                "删除卡牌",
                self.__class__.__name__,
                "删除:"+','.join([
                "ID为:"+str(card.get('id','NoID'))+","+
                "名称为:"+str(card.get('displayName','无名'))+"的卡牌" for card in tempList
                ])
            )
        delBtn.clicked.connect(delSelCard)
    def toCardDetailTab(self, cardDict):
        return self.CCT.toCardDetailTab(cardDict)

class cardPageControler(PageHelper):
    def __init__(self, CLT:cardLibTab):
        super().__init__(CLT, 30)
        self.CLT = CLT
        self._initScrollArea(CLT.cardScroll)
    def dataList(self):
        if not self._isFilter:
            self._cardList = self.CLT.CCT.cardControler.getCardList()
            return self._cardList
        else:
            newCardList = []
            for card in self._cardList:
                if card['displayName'].find(self.filterStr)!=-1:
                    newCardList.append(card)
            return newCardList
    def _generatePage(self,newDataList):
        for index in range(len(newDataList)):
            card = newDataList[index]
            cardItemEle = scrollCradItem(self.CLT)
            cardItemEle.refeshData(card, card.get('id','newCard') in self.CLT.cardSelList)
            if index%3 == 0:
                tempHL = QHBoxLayout()
                tempHL.cardItemEleList = []
                self._VL.addLayout(tempHL)
                self._tempHL_List.append(tempHL)
            cardItemEle.parentLayout = tempHL
            tempHL.addWidget(cardItemEle)
            tempHL.cardItemEleList.append(cardItemEle)

class scrollCradItem(
    cardItemModel.Ui_main,
    QWidget
):
    def __init__(self, CLT:cardLibTab=None):
        super().__init__(None)
        self.CLT = CLT
        self._initData()

        self.setupUi(self)
        self._initUI()
        self._initClick()
    def _initData(self):
        self.WIDTH = 470;self.HEIGHT = 370
        self.BlurRadius = 10
        self.isSel = False
        self.isShowDetails = False
        self.clipboard = QApplication.clipboard()
    def _initUI(self):
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
    def _initClick(self):
        def clickCardItem(tag):
            def __clickCardItem():
                if tag == 'edit':
                    self.index = self.CLT.toCardDetailTab(self.cardDict)
                elif tag == 'sel':
                    self.isSel = not self.isSel
                    if self.isSel:
                        self.CLT.cardSelList.append(self.cardDict['id'])
                    else:
                        self.CLT.cardSelList.remove(self.cardDict['id'])
                    self.refeshData(self.cardDict,self.isSel)
                elif tag == 'print':
                    self.printCard()
                elif tag == 'import':
                    importDict = importCard(self.clipboard.text())
                    if importDict == {}:
                        self.CLT.mainWindow.showWarn(
                            "导入卡牌",
                            self.__class__.__name__,
                            "导入名称为:" + str(importDict.get('displayName', '无名'))+
                            "\n发生了错误，请检验剪切板字符串格式(win + v)"
                        )
                    else:
                        self.CLT.mainWindow.showInfo(
                            "导入卡牌",
                            self.__class__.__name__,
                            "导入名称为:" + str(importDict.get('displayName', '无名'))+
                            "\n成功"
                        )
                        importDict['id'] = self.cardDict.get('id','100000000')
                        self.refeshData(importDict)
                        try:
                            self.CLT.cardControler.updataCard(**importDict)
                            # 记录导入卡牌数据至用户数据中
                            u = UserUtil()
                            if importDict.get("author","") == "": author = u.userName
                            else: author = importDict.get("author","")
                            if importDict.get("reprintedAuthor","") == "": reprintedAuthor = []
                            else: reprintedAuthor = importDict.get("reprintedAuthor","")
                            u.addCard(author, importDict, reprintedAuthor)
                        except Exception as e:log.record(logLevel.ERROR, 'cradItem_C.clickCardItem', e)
                elif tag == 'export':
                    self.clipboard.setText(exportCard(self.cardDict))
                    self.CLT.mainWindow.showInfo(
                        "导出卡牌",
                        self.__class__.__name__,
                        "导出名称为:" + str(self.cardDict.get('displayName', '无名'))+
                        "\n成功"
                    )
            return __clickCardItem
        self.cardEdit.clicked.connect(clickCardItem('edit'))
        self.cardSelect.clicked.connect(clickCardItem('sel'))
        self.cardPrint.clicked.connect(clickCardItem('print'))
        self.cardImport.clicked.connect(clickCardItem('import'))
        self.cardExport.clicked.connect(clickCardItem('export'))
        def showDetails():
            parentLayout = self.parentLayout
            for item in parentLayout.cardItemEleList:
                if item != self:
                    item.isShowDetails = False
                    item.details()
                    item._initUI()
            self.isShowDetails = not self.isShowDetails
            self.details()
            self._initUI()
        self.detailsBTN.clicked.connect(showDetails)

    def refeshData(self,cardDict:dict,isSel:bool=None):
        self.cardDict = cardDict
        if isSel: self.isSel = isSel

        self.NameAndId.setText(cardDict['displayName']+'(ID:'+cardDict['id']+')')
        self.price.setText(cardDict['price'])
        self.description.setText(cardDict['description'])
        self.description.setReadOnly(True)
        self.story.setText(cardDict['story'])
        self.story.setReadOnly(True)
        import os
        backgroundImgPath = appPath()+"/CardBackground/"+cardDict.get('backgroundId','1')+"/Card.png"
        cardArtImgPath = appPath()+"/CardArt"+'/'+str(cardDict.get('id','Unknown'))+'.png'
        if os.path.exists(backgroundImgPath):
            try:
                self.backgroundImg.setPixmap(QPixmap(backgroundImgPath).scaled(310,310))
                # QPixmap图片大小自适应
                self.backgroundImg.setScaledContents(True)
                self.backgroundImg.setStyleSheet("border-image: none;")
            except Exception as e:log.record(logLevel.ERROR, 'cradItem_C.refeshData backgroundImg', e)
        if os.path.exists(cardArtImgPath):
            try:
                self.cardArt.setPixmap(QPixmap(cardArtImgPath).scaled(80,80))
                self.cardArt.setStyleSheet("border-image: none;")
            except Exception as e:log.record(logLevel.ERROR, 'cradItem_C.refeshData cardArt', e)
        if self.isSel:
            self.cardSelect.setStyleSheet("QPushButton{border-image: url(:/ico/Data/qrc/ico/selected.png);}")
        else:
            self.cardSelect.setStyleSheet("QPushButton{border-image: url(:/ico/Data/qrc/ico/select.png);}")
    def details(self):
        if self.isShowDetails:
            self.setMinimumWidth(470)
            self.cardItem.setGeometry(10,10,450,340)
        else:
            self.setMinimumWidth(280)
            self.cardItem.setGeometry(10,10,260,340)
        self._initUI()
    def printCard(self):
        mainWindow = self.CLT.mainWindow
        if self.CLT.CCT.cardControler.printCard(self.cardDict.get('id', 'newCard')):
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

class cardDetailTab(
    cardDetailsModel.Ui_Form,
    QWidget
):
    def __init__(self,
                 CCT:CardControlerTab=None,
                 cardDict={}
                 ):
        super().__init__(None)
        self.setupUi(self)
        self.CCT = CCT
        self.mainWindow = CCT.mainWindow
        self.cardDict = cardDict

        self._initTextEditor()
        self._initComboCheckBox()
        self._initBetterSettingInterface()
        self._initClick()
        self._initQuickKey()

        self.refreshData()
    def refreshData(self,cardDict=None):
        if cardDict: self.cardDict = cardDict
        else:cardDict = self.cardDict
        self.cardId = cardDict.get('id','newCard')
        if self.cardId != "newCard":
            self.CM_displayName.setText(cardDict['displayName'])
            if cardDict.get('price')=="":cardDict['price'] = "0"
            self.CM_price.setValue(int(cardDict.get('price','0')))
            if cardDict.get('energyReq')=="":cardDict['energyReq'] = "0"
            self.CM_energyReq.setValue(float(cardDict.get('energyReq','0')))
            if cardDict.get('range')=="":cardDict['range'] = "0"
            self.CM_range.setValue(float(cardDict.get('range','0')))
            self.CM_description.setText(cardDict['description'])
            self.CM_story0.setText(cardDict['story'])
            self.CM_codeSource.setText(cardDict['code'])
            self.CM_remapCodeSource.setText(cardDict['remapCode'])

            if cardDict.get('spreadRadius')=="":cardDict['spreadRadius'] = "0"
            self.spreadRadius.setValue(float(cardDict.get('spreadRadius','0')))
            if cardDict.get('minUnlockGrade')=="":cardDict['minUnlockGrade'] = "0"
            self.minUnlockGrade.setValue(int(cardDict.get('minUnlockGrade','0')))
            for sel in cardDict['aimTypeCode'].split(';'):
                self.aimTypeCode.selQCheckBoxByName(sel.split(':')[0])
            for sel in cardDict['perferredTargetTypeCode'].split(';'):
                self.perferredTargetTypeCode.selQCheckBoxByName(sel.split(':')[0])
            for sel in cardDict['tagCode'].split(';'):
                self.tagCode.selQCheckBoxByName(sel.split(':')[0])
            import os
            from ..Util.frozenDir import appPath
            cardArtPath = appPath()+"/CardArt/"+str(self.cardId)+".png"
            if os.path.isfile(cardArtPath):
                self.selCardArtImg.path = cardArtPath
                self.selCardArtImg.setStyleSheet("")
    def _initTextEditor(self):
        def initFont(editor):
            from PyQt5.QtGui import QFont,QFontMetrics
            editor.setPlainText('')
            font = editor.font()
            font.setFamily('Consolas')
            font.setStyleHint(QFont.Monospace)
            font.setPointSize(14)
            editor.setFont(font)

            metrics = QFontMetrics(editor.font())
            editor.setTabStopWidth(metrics.width(' ')*4)
        def QTextEditToTextEditor(mQTextEdit):
            initFont(mQTextEdit)
            mQTextEdit.set_completer(Completer().completer)
            mQTextEdit.HL = HighLighter(mQTextEdit.document())
        QTextEditToTextEditor(self.CM_codeSource)
        QTextEditToTextEditor(self.CM_remapCodeSource)
    def _initClick(self):
        mainWindow = self.CCT.mainWindow
        cardControler = self.CCT.cardControler
        def __saveCard():
            def cpSelCardArtToModCardArt():
                # 复制选择card art到指定cardArt目录中
                import os, shutil
                from ..Util.frozenDir import appPath
                if os.path.isfile(self.selCardArtImg.path) \
                        and self.selCardArtImg.path != appPath() + "/CardArt/" + str(self.cardId) + ".png":
                    shutil.copyfile(self.selCardArtImg.path, appPath() + "/CardArt/" + str(self.cardId) + ".png")
            if self.cardDict == {}:
                newCard = cardControler.addCard(**self.getCard().toDict())
                if newCard!={}:
                    self.mainWindow.showInfo(
                        "添加卡牌",
                        self.__class__.__name__,
                        "成功新添ID为:"+str(newCard.get('id','newCard'))+",\n"+
                        "名称为:"+self.CM_displayName.text()+"的卡牌"
                    )
                    self.CCT.CLT.cardPC.toPage(self.CCT.CLT.cardPC.pageCount - 1)
                    self.CCT.removeNewCardTab(self)
                    self.CCT.toCardDetailTab(newCard)

                    cpSelCardArtToModCardArt()
                    return True
                else:
                    mainWindow.showWarn(
                        "添加卡牌",
                        self.__class__.__name__,
                        "新添名称为:" + self.cardDict.get('displayName') + "发生了错误" + ",\n" +
                        "请保证文件读取权限、卡牌列表最后一张卡牌ID为数字"
                    )
                    return False
            else:
                if cardControler.updataCard(**self.getCard().toDict()):
                    mainWindow.showInfo(
                        "修改卡牌",
                        self.__class__.__name__,
                        "修改ID为:" + self.cardId +",\n" +
                        "名称为:" + self.cardDict.get('displayName') + "成功"
                    )
                    self.CCT.CLT.cardPC.toPage()
                    cpSelCardArtToModCardArt()
                    return True
                else:
                    mainWindow.showWarn(
                        "修改卡牌",
                        self.__class__.__name__,
                        "修改ID为:" + self.cardId +",\n" +
                        "名称为:" + self.cardDict.get('displayName') + "发生了错误" + ",\n" +
                        "请保证文件读取权限"
                    )
                    return False
        self.saveCard.clicked.connect(__saveCard)
        def __printCard():
            if not __saveCard(): return
            result = cardControler.checkCode(self.cardDict.get('id', 'newCard'))
            if result == 0:pass
            elif result == 1: mainWindow.showWarn(
                    "印卡",
                    self.__class__.__name__,
                    "code部分出现了语法错误"
                );return
            elif result == 2: mainWindow.showWarn(
                    "印卡",
                    self.__class__.__name__,
                    "remapCode部分出现了语法错误"
                );return
            elif result == 3: mainWindow.showWarn(
                    "印卡",
                    self.__class__.__name__,
                    "未找到对应id卡牌字典"
                );return
            if cardControler.printCard(self.cardDict.get('id', 'newCard')):
                mainWindow.showInfo(
                    "扩印卡牌",
                    self.__class__.__name__,
                    "扩印ID为:"+str(self.cardId)+",\n"+
                    "名称为:"+self.CM_displayName.text()+"的卡牌"
                )
                openTetraProject()
            else:
                mainWindow.showWarn(
                    "印卡",
                    self.__class__.__name__,
                    "印卡时发生了错误"+",\n"+
                    "请先添加卡牌"
                )
        self.printCard.clicked.connect(__printCard)
    def _initQuickKey(self):
        def __keyPressEvent(event):
            if (event.key() == Qt.Key_1):
                if QApplication.keyboardModifiers() == Qt.AltModifier:
                    self.printCard.click()
            if (event.key() == Qt.Key_S):
                if QApplication.keyboardModifiers() == Qt.ControlModifier:
                    self.saveCard.click()
        self.keyPressEvent = __keyPressEvent
    def _initComboCheckBox(self):
        def __comboBoxToComboCheckBox(items,parent,this):
            parent.removeWidget(this);this.setParent(None)
            comboBox = ComboCheckBox()
            comboBox.setGeometry(this.geometry())
            comboBox.setMinimumSize(this.size())
            comboBox.loadItems(items)
            parent.addWidget(comboBox)
            return comboBox

        self.aimTypeCode = __comboBoxToComboCheckBox([
            'EnvOnly','Single0nly','AllowOutOfStageBorder',
            'ChaTagExclude','Boss','Trap','Turret',
            'HpLessThanSelf','NotAllowSelf',
            'ChaTagLimit','Machine','ThrougWall',
        ],self.aimTypeCode_L,self.aimTypeCode)
        self.perferredTargetTypeCode = __comboBoxToComboCheckBox([
            "emy","self","player",
            "died","HasBuff","lowHpP","lowHpPltmt",
            "Breakable","tmt",
        ],self.perferredTargetTypeCode_L,self.perferredTargetTypeCode)
        self.tagCode = __comboBoxToComboCheckBox([
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
        ],self.tagCode_L,self.tagCode)
    def _initBetterSettingInterface(self):
        self.backgrondImgWidgetList = []
        tempWidget = QWidget()
        tempHL = QHBoxLayout()
        tempWidget.setLayout(tempHL)
        tempHL.setContentsMargins(0,0,0,0)

        import os
        from ..Util.frozenDir import appPath
        backgroundImgPath = appPath()+"/CardBackground"
        if not os.path.exists(backgroundImgPath):
            os.makedirs(backgroundImgPath)
        backgrondImgId = self.cardDict.get('backgroundId', '1')
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

        self.backgroundImgScroll.setWidget(tempWidget)
    def getCard(self):
        if self.CM_displayName.text() == "":
            self.CM_displayName.setText("无名")
        return Card(
            id=self.cardId,
            displayName=self.CM_displayName.text(), price=self.CM_price.text(), energyReq=self.CM_energyReq.text(),
            range=self.CM_range.text(),
            description=self.CM_description.toPlainText(),
            story=self.CM_story0.toPlainText(),
            code=self.CM_codeSource.toPlainText(),
            remapCode=self.CM_remapCodeSource.toPlainText(),
            spreadRadius=self.spreadRadius.value(),
            minUnlockGrade=self.minUnlockGrade.value(),
            aimTypeCode=";".join(self.aimTypeCode.currentText()),
            perferredTargetTypeCode=";".join(self.perferredTargetTypeCode.currentText()),
            tagCode=";".join(self.tagCode.currentText()),
            effectCode=self.effectCode.text(),
            backgroundId=self.selBackgrondImgName,
        )