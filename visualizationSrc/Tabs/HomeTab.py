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
from ..qtUI.addCard import Ui_MainWindow

class Home:
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow):
        self.UI = UI
        self.initCardItemClick()
    def initCardItemClick(self):
        UI = self.UI
        def CardMakeCardClick(event):
            from PyQt5 import QtCore
            if event.buttons() == QtCore.Qt.LeftButton:
                UI.ContentTabList_C.showTab('CardMake')
        UI.CardMakeCard.mousePressEvent = CardMakeCardClick
