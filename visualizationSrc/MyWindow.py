#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   MyWindow.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 9:45
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   初始化UI界面
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from PyQt5.uic.properties import QtWidgets

from . import config
from .qtUI import mainInterFace

class MyWindow(QMainWindow,mainInterFace.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # 去除默认边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 背景透明（就是ui中黑色背景的那个控件）
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

        self.initUI()
        from .Controler.ContentTabListControler import ContentTabList
        ContentTabList(self,self)
    def initToolBar(self):
        def windowClick(Element):
            def __windowClick(event):
                from PyQt5 import QtCore
                if event.buttons() == QtCore.Qt.LeftButton:
                    Element.down = True
            return __windowClick
        def windowRelease(Element):
            def __windowRelease(event):
                if Element == self.close_window and Element.down:
                    self.close()
                elif Element == self.min_window and Element.down:
                    self.showMinimized()
                elif Element == self.max_window and Element.down:
                    pass
                else:pass
                Element.down = False
            return __windowRelease
        def connectClick(Ele,fun):
            Ele.mousePressEvent = fun
        def connectRelease(Ele:QtWidgets,fun):
            Ele.mouseReleaseEvent = fun
        for Ele in [self.close_window,self.min_window,self.max_window]:
            connectClick(Ele,windowClick(Ele))
            connectRelease(Ele,windowRelease(Ele))
    def initUI(self):
        self.setupUi(self)
        self.initToolBar()
        self.EXETitle.setText(config.ExeName +' ' + config.Version)
    def mousePressEvent(self, event):
        if event.button()== Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
