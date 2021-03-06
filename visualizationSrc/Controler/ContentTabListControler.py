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
from PyQt5.QtWidgets import QTabBar

from .. import MyWindow

class ContentTabList():
    def __init__(self,mainWindow:MyWindow.MyWindow):
        self.mainWindow = mainWindow
        self.ContentTabList = self.mainWindow.ContentTabList

        from ..Tabs.HomeTab import Home
        self.home = Home(self, mainWindow)
        self._initTabs()
    def _initTab(self, TabName, TabCNName, widgetClass):
        try:self.TabNameHash[TabName] = {
                'CN': TabCNName,
                'widgetClass': widgetClass,
                'isAdd': False
            }
        except Exception as e:
            self.mainWindow.showErr(
                "初始化"+TabCNName+"页面出现了错误",
                self.__class__.__name__,
                str(e)
            )
            from ..Util.LogUtil import log, logLevel
            log.record(logLevel.ERROR, TabName+'._initTab', e)
    def _initTabs(self):
        self.ContentTabList.tabBar().setTabButton(0,QTabBar.RightSide,None)

        from ..Tabs.CardControlerTab import CardControlerTab
        from ..Tabs.ProtagonistControlerTab import ProtagonistControlerTab
        from ..Tabs.OnlineServerTab import OnlineServerTab
        self.TabNameList = ['CardControler', 'ProtagonistControler', 'OnlineServer']
        self.TabNameHash = {}
        self._initTab("CardControler","卡牌管理",CardControlerTab)
        self._initTab("ProtagonistControler","角色管理",ProtagonistControlerTab)
        self._initTab("OnlineServer","联机大厅",OnlineServerTab)
        self._initTabClose()
    def clearAllTab(self):
        for key in self.TabNameHash:
            if self.TabNameHash[key].get('widget',None): del self.TabNameHash[key]['widget']
    def _initTabClose(self):
        def __closeTab(closeIndex):
            currentQWidget = self.ContentTabList.widget(closeIndex)
            if currentQWidget == None: return
            self.ContentTabList.removeTab(closeIndex)
            for key in self.TabNameHash:
                dict = self.TabNameHash[key]
                if dict.get('widget', None) == currentQWidget:
                    dict['isAdd'] = False
        self.ContentTabList.tabCloseRequested.connect(__closeTab)
    def showTab(self,TabName):
        if not TabName in self.TabNameList: return
        TabNameHash = self.TabNameHash
        if TabNameHash.get(TabName,None)==None: return
        if not TabNameHash[TabName].get('widget', None):
            TabNameHash[TabName]['widget'] = TabNameHash[TabName]['widgetClass'](self.mainWindow)
        if not TabNameHash[TabName]['isAdd']:
            self.ContentTabList\
                .addTab(TabNameHash[TabName]['widget'],TabNameHash[TabName]['CN'])
            TabNameHash[TabName]['isAdd'] = True
        self.ContentTabList.setCurrentWidget(TabNameHash[TabName]['widget'])
