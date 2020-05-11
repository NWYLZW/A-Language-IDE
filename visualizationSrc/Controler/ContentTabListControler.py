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
from ..qtUI.addCard import Ui_MainWindow

class ContentTabList():
    def __init__(self,UI:Ui_MainWindow):
        self.UI = UI
        from ..Tabs.CardMakeTab import CardMake
        self.CardMake_C = CardMake(UI)
        from ..Tabs.HomeTab import Home
        self.Home_C = Home(UI)
        for i in range(1,UI.ContentTabList.count()):
            UI.ContentTabList.removeTab(i)
        self.initTabName()
    def initTabName(self):
        self.UI.ContentTabList.setTabText(0, "主页")
    def showTab(self,TabName):
        TabNameList = ['CardMake']
        if not TabName in TabNameList: return
        TabNameHash = {
            'CardMake':{
                'CN':"卡牌制作",
                'tab':self.UI.CardMakeTab,
                'isShow':False
            },
        }
        if not TabNameHash[TabName]['isShow']:
            self.UI.ContentTabList\
                .addTab(TabNameHash[TabName]['tab'],TabNameHash[TabName]['CN'])
            TabNameHash[TabName]['isShow'] = True
        self.UI.ContentTabList.setCurrentWidget(TabNameHash[TabName]['tab'])
