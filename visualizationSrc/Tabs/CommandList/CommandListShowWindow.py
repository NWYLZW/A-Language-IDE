#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CommandListShowWindow.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/30 1:33
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect

from ... import MyWindow
from ...Controler.CardCommandControler import CardCommandControler
from ...Helper.PageHelper import PageHelper
from ...Util.LogUtil import log, logLevel
from ...qtUI.CommandList import CommandListShowTab, ShowScrollItem


class CommandListShowWindow( QWidget, CommandListShowTab.Ui_Form):
    def __init__(self, mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        super().__init__(None)
        self.setupUi(self)
        self._initData()
        self._initUI()
        try:
            self.cardCommandPC = cardCommandPageControler(self)
            self.cardCommandPC.toPage()
        except Exception as e: self.mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );log.record(logLevel.ERROR, 'CardControlerTab.__init__', e)

        self._initClick()
    def _initData(self):
        self.isTop = True
        self.CCC = CardCommandControler()
    def _initUI(self):
        self._TopHint()
    def _initClick(self):
        def ClickTopHint():
            self.isTop = not self.isTop
            self._TopHint()
        self.topLayer.clicked.connect(ClickTopHint)

        self.Search_Input.returnPressed.connect(lambda : self.cardCommandPC.filter(self.Search_Input.text()))
    def _TopHint(self):
        if self.isTop:
            self.topLayer.setToolTip("取消置顶")
            self.topLayer.setStyleSheet("#topLayer{border-image: url(:/ico/Data/qrc/ico/topLayered.png);}")
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.topLayer.setToolTip("置顶窗口")
            self.topLayer.setStyleSheet("#topLayer{border-image: url(:/ico/Data/qrc/ico/topLayer.png);}#topLayer:hover{border-image: url(:/ico/Data/qrc/ico/topLayered.png);}")
            self.setWindowFlags(QtCore.Qt.Widget)
        self.show()
class cardCommandPageControler(PageHelper):
    def __init__(self, CLSW:CommandListShowWindow):
        super().__init__(CLSW, 50)
        self.CLSW = CLSW
        self._initScrollArea(CLSW.cardCommandScroll)
    def dataList(self):
        if not self._isFilter:
            self._cardCommandList = self.CLSW.CCC.getCardCommandList()
            return self._cardCommandList
        else:
            newCardCommandList = []
            for cardCommand in self._cardCommandList:
                if cardCommand['id'].find(self.filterStr)!=-1 \
                    or cardCommand['description'].find(self.filterStr)!=-1\
                    or cardCommand['quoteDescription'].find(self.filterStr)!=-1:
                    newCardCommandList.append(cardCommand)
            return newCardCommandList
    def _generatePage(self,newDataList):
        for index in range(len(newDataList)):
            cardCommand = newDataList[index]
            cardItemEle = scrollCardCommandItem(self.CLSW)
            cardItemEle.refeshData(cardCommand)
            if index%1 == 0:
                tempHL = QHBoxLayout()
                tempHL.setContentsMargins(0,0,0,0)
                tempHL.setSpacing(0)
                tempHL.cardItemEleList = []
                self._VL.addLayout(tempHL)
                self._tempHL_List.append(tempHL)
            cardItemEle.parentLayout = tempHL
            tempHL.addWidget(cardItemEle)
            tempHL.cardItemEleList.append(cardItemEle)

class scrollCardCommandItem(QWidget, ShowScrollItem.Ui_Form):
    def __init__(self, CLSW:CommandListShowWindow):
        super().__init__(None)
        self.CLSW = CLSW

        self.setupUi(self)
        self._initUI()
    def _initUI(self):
        self.BlurRadius = 10
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
    def refeshData(self, cardCommandDict):
        self.cardCommandDict = cardCommandDict
        self.name.setText(cardCommandDict.get('id'))
        self.desp.setText(cardCommandDict.get('description'))
        if cardCommandDict.get('//comment') != "":
            self.comment.setText(cardCommandDict.get('//comment'))
        else:
            self.comment.hide()
        if cardCommandDict.get('quoteDescription') != "":
            self.quoteDesp.setText(cardCommandDict.get('quoteDescription'))
        else:
            self.quoteDesp.hide()
        self.effectCode.setText(cardCommandDict.get('effectCode'))
        self.tagCode.setText(cardCommandDict.get('//category'))
        self.version.setText(cardCommandDict.get('//addedInVersion'))