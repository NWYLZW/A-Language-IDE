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
import json
import subprocess

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5.uic.properties import QtWidgets
from PyQt5 import QtCore

from .CommandList.CommandListShowWindow import CommandListShowWindow
from .. import MyWindow
from ..Controler.ContentTabListControler import ContentTabList
from ..Util.ServerUserUtil import server
from ..Util.UserUtil import UserUtil
from ..Util.frozenDir import tempPath, currentProPath
from ..config import GamePath

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
        self._initUI()
        self._initClick()
        self._initThread()
    def _initUI(self):
        self._initData()
        self.userName.setText(self.userName_Data)
        if self.PWD_Data != "***": self.PWD.setText(self.PWD_Data)
    def _initData(self):
        u = UserUtil()
        self.userName_Data = u.userName
        self.PWD_Data = u.PWD
    def _initThread(self):
        def loginThreadFun():
            rsp = server.user.login(self.userName.text(),self.PWD.text())
            typeX = rsp.get('type',None)
            if typeX and typeX > 0:
                u = UserUtil()
                u.userName = self.userName_Data
                u.PWD = self.PWD_Data
                self.close()
            else:
                self.loginBTN.setText(rsp.get("content", "好像与伺服娘断连了哦"))
            self.isCLickLogin = False
            QTimer.singleShot(1000, lambda: self.loginBTN.setText("登陆"))
        self.loginThreadX = loginThread()
        self.loginThreadX.signal.connect(loginThreadFun)
    def _initClick(self):
        def login():
            self.isCLickLogin = True
            if not self.isCLickLogin:return
            if self.userName.text() and self.PWD.text():
                self.loginBTN.setText("伺服娘正在处理你的请求...")
                self.loginThreadX.start()
        self.loginBTN.clicked.connect(login)

class controlMainMenu:
    def __init__(self,CTL:ContentTabList,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        self.CTL = CTL
        self._initClick()
    def _initClick(self):
        def showCommandListShowWindow():
            temp = CommandListShowWindow(self.mainWindow)
            temp.show()
        self.mainWindow.CommandList.clicked.connect(showCommandListShowWindow)
class controlNavMenu:
    def __init__(self,CTL:ContentTabList,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        self.CTL = CTL
        self._initClick()
    def _initClick(self):
        def MagicaVoxel():
            subprocess.Popen(tempPath()+"./visualizationSrc/Data/externProgram/MagicaVoxel/MagicaVoxel.exe")
        self.mainWindow.MagicaVoxel.clicked.connect(MagicaVoxel)
class simpleDataMenu:
    def __init__(self,CTL:ContentTabList,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        self.CTL = CTL
        self._initClick()
    def _initClick(self):
        def sel_GamePath():
            directory = QFileDialog.getExistingDirectory(None, "getExistingDirectory", "C:\\")
            UserUtil().gamePath = directory
            self.setSimpleData()
        self.mainWindow.sel_GamePath.clicked.connect(sel_GamePath)
        def userLogin():
            if server.user.isLogin:
                self.mainWindow.showWarn(
                    "登陆错误",
                    self.__class__.__name__,
                    "请勿重复登录应用"
                );return
            tempDialog = loginDialogHelper()
            tempDialog.exec_()
        self.mainWindow.userLogin.clicked.connect(userLogin)
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
                self.mainWindow.showInfo(
                "登出",self.__class__.__name__,
                rsp.get('content', "好像与伺服娘断连了哦"))
                server.user.isLogin = False
            else: self.mainWindow.showWarn(
                "登出",self.__class__.__name__,
                rsp.get('content', "好像与伺服娘断连了哦"))
        self.mainWindow.userLogout.clicked.connect(userLogout)
    def setSimpleData(self):
        def __setSimpleData():
            u = UserUtil()
            self.mainWindow.UserName.setText(u.userName)

            tempPathX = currentProPath()
            if tempPathX != "":
                temp = tempPathX.split('/')
                self.mainWindow.ModName.setText(temp[len(temp) - 1])
                self.mainWindow.ModeAndPath.setText(temp[len(temp) - 1]+"("+tempPathX+")")
            else:
                self.mainWindow.ModName.setText("未打开工作Mod文件夹")
                return
            PackageInfo = {}
            with open(tempPathX + "/PackageInfo.json", mode="r", encoding="utf-8") as f:
                try: PackageInfo = json.loads(f.read())
                except:pass
            tempGamePath = GamePath
            if len(GamePath)>30:
                tempGamePath = GamePath[:14]+'...'+GamePath[-14:]
            self.mainWindow.GamePath.setText(tempGamePath)
            self.mainWindow.GamePath.setToolTip(GamePath)
            self.mainWindow.description.setText(PackageInfo.get("description","未设置mod介绍，写点什么吧"))
            self.CTL.clearAllTab()

        QTimer.singleShot(200, __setSimpleData)
class menuToolBoxMenu:
    def __init__(self,CTL:ContentTabList,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        self.CTL = CTL
        self._initClick()
    def _initClick(self):
        def __newMod():
            pass
        self.mainWindow.newMod.clicked.connect(__newMod)
        def __openMod():
            import os
            TetraProjectPackagesPath = os.path.join(os.path.expanduser('~'), 'Documents\TetraProject\Packages')
            if not os.path.exists(TetraProjectPackagesPath):
                os.makedirs(TetraProjectPackagesPath)
            directory = QFileDialog.getExistingDirectory(None, "getExistingDirectory", TetraProjectPackagesPath)
            self.setProjectPath(directory)
        self.mainWindow.openMod.clicked.connect(__openMod)
        def __zipMod():
            pass
        self.mainWindow.zipMod.clicked.connect(__zipMod)
    def setProjectPath(self, directory):
        if UserUtil().pushNewProject(directory):
            self.mainWindow.showInfo(
                "打开项目", self.__class__.__name__,
                "打开项目成功")
            self.CTL.home.snM.setSimpleData()
        else:
            self.mainWindow.showWarn(
                "打开项目", self.__class__.__name__,
                "打开项目失败，请保证文件夹为标准Mod文件夹")

class Home:
    def __init__(self,CTL:ContentTabList,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        self.CTL = CTL
        self.initCardItemClick()
        self.cmM = controlMainMenu      (CTL, mainWindow)
        self.cnM = controlNavMenu       (CTL, mainWindow)
        self.snM = simpleDataMenu       (CTL, mainWindow)
        self.snM.setSimpleData()
        self.mtbM = menuToolBoxMenu     (CTL, mainWindow)
    def initCardItemClick(self):
        UI = self.mainWindow
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
