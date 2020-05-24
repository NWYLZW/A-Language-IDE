#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   OnlineServerTab.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/24 4:48
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QWidget

from ..Helper.PageHelper import PageHelper
from ..Util.LogUtil import log, logLevel
from ..qtUI.OnlineServer import onlineServer
from ..qtUI.OnlineServer import roomItemModel as roomItemModelUI

class OnlineServerTab(QWidget, onlineServer.Ui_Form):
    def __init__(self, mainWindow=None):
        super().__init__(None)
        self.setupUi(self)
        self.initUI()
        try:
            self.roomPC = roomPageControler(self)
            self.roomPC.toPage()
        except Exception as e: mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );log.record(logLevel.ERROR, 'CardControlerTab.__init__', e)
        from visualizationSrc import server
        self.server = server
    def _refreshRoomListFromServer(self):
        self.roomList = self.server.room.list()
    def initUI(self):
        pass

class roomPageControler(PageHelper):
    def __init__(self, OST:OnlineServerTab):
        super().__init__(OST, 30)
        self._OST = OST
        self._initScrollArea(OST.roomScroll)
    def dataList(self):
        if not self._isFilter:
            return []
        else:
            return []
    def _generatePage(self,newDataList):
        for index in range(len(newDataList)):
            pass

class roomItemModel(QWidget, roomItemModelUI.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
    def initData(self):
        pass
    def initUI(self):
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)