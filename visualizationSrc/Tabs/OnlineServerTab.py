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
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QWidget, QHBoxLayout

from ..Helper.PageHelper import PageHelper
from ..Util.LogUtil import log, logLevel
from ..qtUI.OnlineServer import onlineServer
from ..qtUI.OnlineServer import roomItemModel as roomItemModelUI

class OnlineServerTab(QWidget, onlineServer.Ui_main):
    def __init__(self, mainWindow=None):
        super().__init__(None)
        self.setupUi(self)
        self.initData()
        self.initUI()

        try:
            self.roomPC = roomPageControler(self)
            self.roomPC.toPage()
        except Exception as e: mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );log.record(logLevel.ERROR, 'OnlineServerTab.__init__', e)
    def _refreshRoomListFromServer(self):
        self.roomList = [
            {
                "id": 0,
                "roomName": "开黑快乐小房间",
                "dateTime": "2020-06-05 01:50:20",
                "users": [1,2,3],
            },
        ]
        # self.roomList = self.server.room.list()
    def initData(self):
        self.roomList = []
        from visualizationSrc import server
        self.server = server

        self._refreshRoomListFromServer()
    def initUI(self):
        pass

class roomPageControler(PageHelper):
    def __init__(self, OST:OnlineServerTab):
        super().__init__(OST, 5)
        self._OST = OST
        self._initScrollArea(OST.roomScroll)
    def dataList(self):
        if not self._isFilter:
            self._roomList = self._OST.roomList
            return self._roomList
        else:
            newRoomList = []
            for room in self._roomList:
                if room['roomName'].find(self.filterStr)!=-1:
                    newRoomList.append(room)
            return newRoomList
    def _generatePage(self,newDataList):
        for index in range(len(newDataList)):
            roomDict = newDataList[index]
            intemEle = roomItemModel()
            # intemEle.setCardControlerTab(self._OST)
            intemEle.refeshData(roomDict)
            if index%2 == 0:
                tempHL = QHBoxLayout()
                self._VL.addLayout(tempHL)
                self._tempHL_List.append(tempHL)
            intemEle.parentLayout = tempHL
            tempHL.addWidget(intemEle)

class roomItemModel(QWidget, roomItemModelUI.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.BlurRadius = 10
        self.setupUi(self)
        self.initUI()
    def refeshData(self,roomDict):
        self.roomDict = roomDict
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