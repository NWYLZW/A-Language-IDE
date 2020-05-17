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
from PyQt5.QtWidgets import QMainWindow

from ..Controler.ContentTabListControler import ContentTabList
from ..qtUI.mainInterFace import Ui_MainWindow

class Home:
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow,CTL:ContentTabList):
        self.UI = UI
        self.CTL = CTL
        self.initCardItemClick()
    def initCardItemClick(self):
        UI = self.UI
        def CardControlerClick(event):
            from PyQt5 import QtCore
            if event.buttons() == QtCore.Qt.LeftButton:
                self.CTL.showTab('CardControler')
        UI.CardControler.mousePressEvent = CardControlerClick