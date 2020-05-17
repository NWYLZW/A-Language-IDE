#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   MessageBoxHelper.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/18 4:57
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import time

from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint, QTimer
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect

from ..qtUI import messageBox

class MessageBox(QWidget,messageBox.Ui_Message_Box):
    from enum import Enum, unique
    @unique
    class MessageBox_Tag(Enum):
        Information = 0
        Warning = 1
        Error = 2
    def __init__(self, parent=None):
        super().__init__(parent)
        self.WIDTH = 510;self.HEIGHT = 160
        self.BlurRadius = 10
        self.setupUi(self)
        self.initUI()
        self.hide()
    def initUI(self):
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
    def showMessage(self,
                    Tag:MessageBox_Tag=MessageBox_Tag.Information,
                    KindName:str="None",
                    Title:str="未设置标题",
                    Content:str=""):
        import re
        newStyleSheet = re.sub(
            "qrc\/message\/.*\.png",
            "qrc/message/"+
            ["information","warning","error"][Tag.value]
            +".png",
            self.MessageKindImg.styleSheet())
        self.MessageKindImg.setStyleSheet(newStyleSheet)

        self.messageKindName.setText(KindName)
        self.MessageTitle.setText(Title)
        self.MessageContent.setText(Content)
        self.messageDateTime.setText(time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())))
        if self.isHidden(): self.show();self.isNewShow = True
        self._showMessageIn(10,self.parent().height()-self.HEIGHT-10)
    def _showMessageIn(self,posX,posY):
        self.setGeometry(posX, posY, posX+self.WIDTH, posY+self.HEIGHT)
        self.move(posX, posY+self.HEIGHT+100)
        animation = QPropertyAnimation(self, b'pos', self)

        animation.setKeyValueAt(0.00, QPoint(posX, posY+self.HEIGHT+100))
        animation.setKeyValueAt(0.20, QPoint(posX, posY))
        animation.setKeyValueAt(0.80, QPoint(posX, posY))
        animation.setKeyValueAt(1.00, QPoint(posX, posY+self.HEIGHT+100))
        animation.setDuration(2000)
        animation.start()
        def __animationEndFun():
            if self.isNewShow: pass
            else:
                self.isNewShow = False
                self.hide()
        QTimer.singleShot(2000, __animationEndFun)
