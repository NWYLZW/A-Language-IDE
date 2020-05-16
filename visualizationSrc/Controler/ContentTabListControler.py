#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   ContentTabListControler.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 4:29
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from PyQt5.QtWidgets import QMainWindow
from ..qtUI.mainInterFace import Ui_MainWindow

class ContentTabList():
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow):
        self.UI = UI
        from ..Tabs.CardMakeTab import CardMake
        from ..Tabs.HomeTab import Home
        self.CardMake_C = CardMake(UI,mainWindow)
        self.Home_C = Home(UI,mainWindow)
        for i in range(1,UI.ContentTabList.count()):
            UI.ContentTabList.removeTab(i)
        self.initTabName()
    def initTabName(self):
        self.UI.ContentTabList.setTabText(0, "主页")
    def showTab(self,TabName):
        TabNameList = ['CardControler']
        if not TabName in TabNameList: return
        TabNameHash = {
            'CardControler':{
                'CN':"卡牌管理",
                'tab':self.UI.CardMakeTab,
                'isShow':False
            },
        }
        if not TabNameHash[TabName]['isShow']:
            self.UI.ContentTabList\
                .addTab(TabNameHash[TabName]['tab'],TabNameHash[TabName]['CN'])
            TabNameHash[TabName]['isShow'] = True
        self.UI.ContentTabList.setCurrentWidget(TabNameHash[TabName]['tab'])
