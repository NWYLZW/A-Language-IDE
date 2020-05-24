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
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QWidget

from ..Helper.PageHelper import PageHelper
from ..qtUI.OnlineServer import onlineServer
from ..qtUI.OnlineServer import roomItemModel as roomItemModelUI

class OnlineServerTab(QWidget, onlineServer.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()

class roomPageControler(PageHelper):
    def __init__(self, UI):
        super().__init__(UI, 1)
    def dataList(self):
        if not self._isFilter:
            pass
        else:
            pass
    def _generatePage(self,newDataList):
        for index in range(len(newDataList)):
            pass

class roomItemModel(QWidget, roomItemModelUI.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()
    def initData(self):
        pass
    def initUI(self):
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)