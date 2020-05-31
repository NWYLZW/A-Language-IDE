#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   ProtagonistControlerTab.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/31 17:09
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import json
import subprocess
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from .. import MyWindow
from ..Controler.CharacterControler import ProtagonistControler
from ..Helper.ListTabHelper import ListTabHelper
from ..Helper.PageHelper import PageHelper
from ..Util.LogUtil import log, logLevel
from ..Util.UserUtil import UserUtil
from ..Util.frozenDir import tempPath, currentProPath
from ..qtUI.CharacterControler import characterLibWidget, protagonistLibItemModel


class ProtagonistControlerTab(ListTabHelper):
    def __init__(self, mainWindow: MyWindow.MyWindow):
        super().__init__(None)
        self.mainWindow = mainWindow
        self._initData()
        self._initTab()
    def _initData(self):
        self.protagonistControler = ProtagonistControler()
        self.PLT = protagonistLibTab(self)
    def _initTab(self):
        imgPath = tempPath()+"\\visualizationSrc\\Data\\qrc\\cardPkg.png"
        self.addWidgetTab(
            widget=self.PLT,
            title="主要角色",
            content="当前共有主要角色"+str(len(self.protagonistControler.getProtagonistList()))+"个",
            icoImage=QPixmap(imgPath),
            isShowClose=False,
        )
        self.setCurrentIndex(0)
    def _addProtagonistDetailTab(self, protagonistDict):
        if protagonistDict != "newProtagonist":
            index = self.addWidgetTab(
                # TODO 添加编辑详情界面
                widget=QWidget(),
                title=protagonistDict['displayName'] + '(ID:' + protagonistDict['id'] + ')',
                content=protagonistDict['description'],
                icoImage=None,
                isShowClose=True,
            )
            return index
        else:
            index = self.addWidgetTab(
                # TODO 添加编辑详情界面
                widget=QWidget(),
                title= "新建角色*",
                content="还没有设置描述哦~",
                icoImage=None,
                isShowClose=True,
            )
            return index
    def removeNewProtagonistTab(self, newProtagonistTabWidget):
        self.removeWidgetTab(self.widgetIndex(newProtagonistTabWidget))
    def toProtagonistDetailTab(self, ProtagonistDict):
        return self.setCurrentIndex(self._addProtagonistDetailTab(ProtagonistDict))
    def _initClick(self):
        pass

class protagonistLibTab(QWidget,characterLibWidget.Ui_main):
    def __init__(self, PCT: ProtagonistControlerTab):
        super().__init__(None)
        self.PCT = PCT
        self.mainWindow = PCT.mainWindow
        self.setupUi(self)
        self._initData()

        try:
            self.protagonistPC = protagonistPageControler(self)
            self.protagonistPC.toPage()
        except Exception as e: self.mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );log.record(logLevel.ERROR, 'protagonistLibTab.__init__', e)

        self._initClick()
    def _initData(self):
        self.cardSelList = []
    def _initClick(self):
        pass
    def toCardDetailTab(self, protagonistDict):
        return self.PCT.toProtagonistDetailTab(protagonistDict)

class protagonistPageControler(PageHelper):
    def __init__(self, PLT:protagonistLibTab):
        super().__init__(PLT, 20)
        self.PLT = PLT
        self._initScrollArea(PLT.protagonistScroll)
    def dataList(self):
        if not self._isFilter:
            self._protagonistList = self.PLT.PCT.protagonistControler.getProtagonistList()
            return self._protagonistList
        else:
            newProtagonistList = []
            for protagonist in self._protagonistList:
                if protagonist['displayName'].find(self.filterStr)!=-1:
                    newProtagonistList.append(protagonist)
            return newProtagonistList
    def _generatePage(self,newDataList):
        for index in range(len(newDataList)):
            protagonistDict = newDataList[index]
            protagonistItemEle = scrollProtagonistItem(self.PLT)
            protagonistItemEle.refeshData(protagonistDict)
            if index%3 == 0:
                tempHL = QHBoxLayout()
                tempHL.cardItemEleList = []
                self._VL.addLayout(tempHL)
                self._tempHL_List.append(tempHL)
            protagonistItemEle.parentLayout = tempHL
            tempHL.addWidget(protagonistItemEle)
            tempHL.cardItemEleList.append(protagonistItemEle)
class scrollProtagonistItem(
    protagonistLibItemModel.Ui_main,
    QWidget
):
    def __init__(self, PLT:protagonistLibTab=None):
        super().__init__(None)
        self.PLT = PLT
        self._initData()

        self.setupUi(self)
        self._initUI()
        self._initClick()
    def _initData(self):
        pass
    def _initUI(self):
        pass
    def _initClick(self):
        pass
    def refreshHudIcon(self, protagonistDict):
        def getModName(path):
            temp = path.split('/')
            return temp[len(temp) - 1]
        import os
        HudIconPath = currentProPath() +"/CharacterHudIcon/ALIDE_Data"
        if not os.path.exists(HudIconPath):
            os.makedirs(HudIconPath)
        HudIconPath = HudIconPath + '/' + protagonistDict.get('id', '1') + ".png"
        HudAseIconPath = currentProPath() +"/CharacterHudIcon/" + protagonistDict.get('id', '1') + ".ase"

        def isNewAseFile():
            dictX = {}
            project_Data_PATH = UserUtil().exeDataPath+getModName(currentProPath())
            if not os.path.exists(project_Data_PATH):
                os.makedirs(project_Data_PATH)
            project_Data_PATH = project_Data_PATH+'\\protagonist.json'
            if not os.path.isfile(project_Data_PATH):
                with open(project_Data_PATH, 'w', encoding="utf-8-sig") as f:
                    f.write(json.dumps(dictX))
            with open(project_Data_PATH, 'r', encoding="utf-8-sig") as f:
                dictX = json.loads(f.read())

            filePreData = dictX.get(HudAseIconPath,None)
            mtime = time.ctime(os.path.getmtime(HudAseIconPath))

            if filePreData and filePreData == mtime:
                    return False
            dictX[HudAseIconPath] = "%s" % mtime
            with open(project_Data_PATH, 'w', encoding="utf-8-sig") as f:
                f.write(json.dumps(dictX))
            return True
        if (os.path.isfile(HudAseIconPath) and isNewAseFile()) or not os.path.isfile(HudIconPath):
            cmdStr = \
                tempPath() + "./visualizationSrc/Data/externProgram/Aseprite/Aseprite.exe --batch "\
                + HudAseIconPath +\
                " --save-as "\
                + HudIconPath
            subprocess.Popen(cmdStr)
        try:
            QTimer.singleShot(
                200, lambda: \
                self.characterHudIcon.setPixmap(QPixmap(HudIconPath).scaled(64, 64))
            )
            self.characterHudIcon.setStyleSheet("border-image: none;")
        except Exception as e:log.record(logLevel.ERROR, 'scrollProtagonistItem.refeshData characterHudIcon', e)
    def refeshData(self, protagonistDict):
        self.protagonistDict = protagonistDict

        self.characterID.setText("ID:" + protagonistDict.get('id','-0'))
        self.characterName.setText(protagonistDict.get('displayName',''))
        self.characterHP.setText(protagonistDict.get('hp','-0')+'/'+protagonistDict.get('hp','-0'))
        self.characterEnergy.setText(protagonistDict.get('energy','-0'))
        self.characterStamina.setText(protagonistDict.get('stamina','-0'))
        self.desp.setText(protagonistDict.get('description','-0'))
        self.refreshHudIcon(protagonistDict)
