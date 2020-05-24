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
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QWidget, QHBoxLayout, QCompleter, QDialog

from ..Helper.PageHelper import PageHelper
from ..Util.LogUtil import log, logLevel
from ..Util.ServerUserUtil import server
from ..qtUI.OnlineServer import onlineServer
from ..qtUI.OnlineServer import roomItemModel as roomItemModelUI

class createRoomThread(QThread):
    signal = pyqtSignal()
    def __init__(self):
        super().__init__()
    def __del__(self):
        self.wait()
    def run(self):
        self.signal.emit()

from ..qtUI.OnlineServer.dialog import createRoomDialog
class createRoomDialogHelper(QDialog, createRoomDialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("创建房间")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.isCLickCreate = False
        self._initClick()
        self._initThread()
    def _initThread(self):
        def createRoomThreadFun():
            rsp = server.room.create(self.roomName.text())
            typeX = rsp.get('type',None)
            if typeX and typeX > 0:
                server.room.inRoom = True
                server.room.roomId = rsp.get('message',-1)
                self.close()
            else:
                self.createRoom.setText(rsp.get("content"), "好像与伺服娘断连了哦")
            self.isCLickCreate = False
            QTimer.singleShot(1000, lambda: self.createRoom.setText("创建"))
        self.createRoomThreadX = createRoomThread()
        self.createRoomThreadX.signal.connect(createRoomThreadFun)
    def _initClick(self):
        def createRoom():
            self.isCLickCreate = True
            if not self.isCLickCreate:return
            if self.roomName.text() != "":
                self.createRoom.setText("伺服娘正在处理你的请求...")
                self.createRoomThreadX.start()
        self.createRoom.clicked.connect(createRoom)

class OnlineServerTab(QWidget, onlineServer.Ui_main):
    def __init__(self, mainWindow=None):
        self.mainWindow = mainWindow
        super().__init__(None)
        self.setupUi(self)
        self.initData()
        self.initUI()
        self.initClick()

        try:
            self.roomPC = roomPageControler(self)
            self.refreshRoomListFromServer()
        except Exception as e: mainWindow.showErr(
                "获取列表发生了错误",
                self.__class__.__name__,
                str(e)
            );log.record(logLevel.ERROR, 'OnlineServerTab.__init__', e)
    def refreshRoomListFromServer(self):
        self.roomList = [
        ]
        self.roomList = self.server.room.list()
        self.roomPC.toPage()
    def initData(self):
        self.roomList = []
        from visualizationSrc import server
        self.server = server
    def initUI(self):
        pass
    def initClick(self):
        Search_Input = self.Search_Input
        Search_Input\
            .setCompleter(
            QCompleter([card['roomName'] for card in self.roomList])
        )
        Search_Input.returnPressed.connect(lambda : self.roomPC.filter(Search_Input.text()))
        def setServerHost():
            server.serverRoot = self.serverHost_Input.text()
            self.refreshRoomListFromServer()
            self.roomPC.filter(Search_Input.text())
        self.serverHost_Input.returnPressed.connect(setServerHost)

        def refreshRoom():
            self.refreshRoomListFromServer()
            self.roomPC.filter(Search_Input.text())
        self.refreshRoom.clicked.connect(refreshRoom)

        def buildRoom():
            if not server.user.isLogin:
                self.mainWindow.showWarn(
                    "创建房间",
                    self.__class__.__name__,
                    "还未登陆"
                );return
            if server.room.inRoom:
                self.mainWindow.showWarn(
                    "创建房间",
                    self.__class__.__name__,
                    "已在房间中，请先退出房间再创建房间"
                );return

            tempDialog = createRoomDialogHelper()
            tempDialog.exec_()
            if server.room.inRoom:
                self.refreshRoomListFromServer()
        self.buildRoom.clicked.connect(buildRoom)

class roomPageControler(PageHelper):
    def __init__(self, OST:OnlineServerTab):
        super().__init__(OST, 6)
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
            itemEle = roomItemModel(self._OST)
            itemEle.refeshData(roomDict)
            if index%2 == 0:
                tempHL = QHBoxLayout()
                self._VL.addLayout(tempHL)
                self._tempHL_List.append(tempHL)
            itemEle.parentLayout = tempHL
            tempHL.addWidget(itemEle)

class roomItemModel(QWidget, roomItemModelUI.Ui_Form):
    def __init__(self, OST:OnlineServerTab=None):
        super().__init__(None)
        self.BlurRadius = 10
        self._OST = OST
        self.mainWindow = OST.mainWindow
        self.setupUi(self)
        self._initUI()
    def refeshData(self,roomDict):
        self.roomDict = roomDict
        self.roomNameAndId.setText(roomDict.get("roomName","无名")+'(ID:'+str(roomDict.get("id","XXX"))+')')
        self.roomerName.setText("房主名"+roomDict.get("roomerName","****"))
        self.roomUsersCount.setText("人数: " + str(len(roomDict.get("users", []))) + "/10")
        inRoom = False
        for user in roomDict.get('users', []):
            if user.get('inRoom', False): inRoom = True;break
        if inRoom:
            self.joinRoom.setToolTip("断开连接")
            self.joinRoom.setStyleSheet("#joinRoom{border-image: url(:/ico/Data/qrc/ico/join_green.png);}")
        else:
            self.joinRoom.setToolTip("连接")
            self.joinRoom.setStyleSheet("#joinRoom{border-image: url(:/ico/Data/qrc/ico/join.png);}")
        self._initClick(inRoom)
    def _initUI(self):
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
    def _initClick(self, inRoom):
        if inRoom:
            def exitRoom():
                rsp = server.room.exit(self.roomDict.get('id','None'))
                typeX = rsp.get('type',None)
                if typeX and typeX > 0:
                    self.mainWindow.showInfo(
                    "退出房间",self.__class__.__name__,
                    rsp.get('content', "好像与伺服娘断连了哦"))
                    server.room.roomId = self.roomDict.get('id','None')
                    server.room.inRoom = False
                    self._OST.refreshRoomListFromServer()
                else:
                    self.mainWindow.showWarn(
                    "退出房间",self.__class__.__name__,
                    rsp.get('content', "好像与伺服娘断连了哦"))
            self.joinRoom.clicked.connect(exitRoom)
        else:
            def joinRoom():
                rsp = server.room.join(self.roomDict.get('id','None'))
                typeX = rsp.get('type',None)
                if typeX and typeX > 0:
                    self.mainWindow.showInfo(
                    "加入房间",self.__class__.__name__,
                    rsp.get('content', "好像与伺服娘断连了哦"))
                    server.room.roomId = -1
                    server.room.inRoom = True
                    self._OST.refreshRoomListFromServer()
                else:
                    self.mainWindow.showWarn(
                    "加入房间",self.__class__.__name__,
                    rsp.get('content', "好像与伺服娘断连了哦"))
            self.joinRoom.clicked.connect(joinRoom)