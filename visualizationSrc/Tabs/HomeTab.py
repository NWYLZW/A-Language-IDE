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
from PyQt5.uic.properties import QtWidgets

from ..Controler.ContentTabListControler import ContentTabList
from ..qtUI.mainInterFace import Ui_MainWindow

class Home:
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow,CTL:ContentTabList):
        self.UI = UI
        self.mainWindow = mainWindow
        self.CTL = CTL
        self.initCardItemClick()
    def initCardItemClick(self):
        UI = self.UI
        from PyQt5 import QtCore
        def windowClick(Element):
            def __windowClick(event):
                if event.buttons() == QtCore.Qt.LeftButton:
                    Element.clickType = QtCore.Qt.LeftButton
                Element.down = True
            return __windowClick
        def windowRelease(Element):
            def __windowRelease(event):
                if Element.clickType == QtCore.Qt.LeftButton:
                    if Element == UI.CardControler:
                        self.CTL.showTab('CardControler')
                Element.down = False
            return __windowRelease
        def connectClick(Ele,fun):
            Ele.mousePressEvent = fun
        def connectRelease(Ele:QtWidgets,fun):
            Ele.mouseReleaseEvent = fun

        for Ele in [UI.CardControler]:
            connectClick(Ele,windowClick(Ele))
            connectRelease(Ele,windowRelease(Ele))
