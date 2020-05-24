#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   HomeTab.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 4:05
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   主页
'''
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtCore

from .. import MyWindow
from ..Controler.ContentTabListControler import ContentTabList
from ..Util.ServerUserUtil import server
from ..Util.UserUtil import UserUtil
from ..Util.frozenDir import appPath
from ..config import GamePath
from ..qtUI.mainInterFace import Ui_MainWindow

class loginThread(QThread):
    signal = pyqtSignal()
    def __init__(self):
        super().__init__()
    def __del__(self):
        self.wait()
    def run(self):
        self.signal.emit()

from ..qtUI.dialog import loginDialog
class loginDialogHelper(QDialog, loginDialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("登陆")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.isCLickLogin = False
        self._initClick()
        self._initThread()
    def _initThread(self):
        def loginThreadFun():
            rsp = server.user.login(self.userName.text(),self.PWD.text())
            typeX = rsp.get('type',None)
            if typeX and typeX > 0:
                self.close()
            else:
                self.loginBTN.setText(rsp.get("content"))
            self.isCLickLogin = False
            QTimer.singleShot(1000, lambda: self.loginBTN.setText("登陆"))
        self.loginThreadX = loginThread()
        self.loginThreadX.signal.connect(loginThreadFun)
    def _initClick(self):
        def login():
            self.isCLickLogin = True
            if not self.isCLickLogin:return
            self.loginBTN.setText("伺服娘正在处理你的请求...")
            if self.userName.text() and self.PWD.text():
                self.loginThreadX.start()
        self.loginBTN.clicked.connect(login)

class Home:
    def __init__(self,UI:Ui_MainWindow,mainWindow:MyWindow.MyWindow,CTL:ContentTabList):
        self.UI = UI
        self.mainWindow = mainWindow
        self.CTL = CTL
        self.initCardItemClick()
        self.setSimpleData()
        self.initClick()
    def setSimpleData(self):
        u = UserUtil()
        temp = appPath().split('\\')
        self.UI.ModName.setText(temp[len(temp)-1])
        tempGamePath = GamePath
        if len(GamePath)>30:
            tempGamePath = GamePath[:14]+'...'+GamePath[-14:]
        self.UI.GamePath.setText(tempGamePath)
        self.UI.GamePath.setToolTip(GamePath)
        self.UI.UserName.setText(u.userName)
    def initClick(self):
        def sel_GamePath():
            directory = QFileDialog.getExistingDirectory(None, "getExistingDirectory", "C:\\")
            UserUtil().gamePath = directory
            self.setSimpleData()
        self.UI.sel_GamePath.clicked.connect(sel_GamePath)
        def userLogin():
            if server.user.isLogin:
                self.mainWindow.showWarn(
                    "登陆错误",
                    self.__class__.__name__,
                    "请勿重复登录应用"
                );return
            tempDialog = loginDialogHelper()
            tempDialog.exec_()
        self.UI.userLogin.clicked.connect(userLogin)
        def userLogout():
            if not server.user.isLogin:
                self.mainWindow.showWarn(
                    "登出",
                    self.__class__.__name__,
                    "还未登陆"
                );return
            rsp = server.user.logout()
            typeX = rsp.get('type',None)
            if typeX and typeX > 0:
                self.mainWindow.showWarn(
                "登出",self.__class__.__name__,
                rsp.get('content'))
                server.user.isLogin = False
            else: self.mainWindow.showWarn(
                "登出",self.__class__.__name__,
                rsp.get('content'))
        self.UI.userLogout.clicked.connect(userLogout)
    def initCardItemClick(self):
        UI = self.UI
        def windowClick(Element):
            def __windowClick(event):
                if event.buttons() == QtCore.Qt.LeftButton:
                    Element.clickType = QtCore.Qt.LeftButton
                Element.down = True
            return __windowClick
        def windowRelease(Element):
            def __windowRelease(event):
                if Element.clickType == QtCore.Qt.LeftButton:
                    if Element == UI.CardControler and Element.down:
                        self.CTL.showTab('CardControler')
                    elif Element == UI.OnlineServer and Element.down:
                        self.CTL.showTab('OnlineServer')
                Element.down = False
            return __windowRelease
        def connectClick(Ele,fun):
            Ele.mousePressEvent = fun
        def connectRelease(Ele:QtWidgets,fun):
            Ele.mouseReleaseEvent = fun

        for Ele in [UI.CardControler,UI.OnlineServer]:
            connectClick(Ele,windowClick(Ele))
            connectRelease(Ele,windowRelease(Ele))
