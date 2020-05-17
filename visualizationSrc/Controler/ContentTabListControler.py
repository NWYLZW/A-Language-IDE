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
from PyQt5.QtWidgets import QMainWindow, QTabBar

from ..qtUI import mainInterFace

class ContentTabList():
    def __init__(self,UI:mainInterFace.Ui_MainWindow,mainWindow:QMainWindow):
        self.UI = UI
        self.mainWindow = mainWindow
        self.ContentTabList = self.UI.ContentTabList

        from ..Tabs.HomeTab import Home
        self.Home_C = Home(UI,mainWindow,self)

        self.initTab()
    def initTab(self):
        from ..Tabs.CardControlerTab import CardControlerTab
        self.TabNameList = ['CardControler']
        self.TabNameHash = {
            'CardControler':{
                'CN':"卡牌管理",
                'widget':CardControlerTab(self.mainWindow).Widget,
                'isAdd':False
            },
        }

        self.ContentTabList.tabBar().setTabButton(0,QTabBar.RightSide,None)
        self.ContentTabList.setTabText(0, "主页")
        for i in range(1,self.ContentTabList.count()):
            self.ContentTabList.removeTab(i)

        self.initTabClose()
    def initTabClose(self):
        def __closeTab(currentIndex):
            currentQWidget = self.ContentTabList.widget(currentIndex)
            if currentQWidget == None: return
            self.ContentTabList.removeTab(currentIndex)
            for key in self.TabNameHash:
                dict = self.TabNameHash[key]
                if dict['widget'] == currentQWidget:
                    dict['isAdd'] = False
        self.ContentTabList.tabCloseRequested.connect(__closeTab)
    def showTab(self,TabName):
        if not TabName in self.TabNameList: return
        TabNameHash = self.TabNameHash
        if not TabNameHash[TabName]['isAdd']:
            self.ContentTabList\
                .addTab(TabNameHash[TabName]['widget'],TabNameHash[TabName]['CN'])
            TabNameHash[TabName]['isAdd'] = True
        self.ContentTabList.setCurrentWidget(TabNameHash[TabName]['widget'])
