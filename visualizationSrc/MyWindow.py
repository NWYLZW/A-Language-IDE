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
from PyQt5.QtWidgets import QMainWindow
from . import config
from .qtUI import mainInterFace

class MyWindow(QMainWindow,mainInterFace.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI()
    def initUI(self):
        # 去除默认边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        # 初始化工具条
        def initToolBar():
            def close_windowClick(event):
                from PyQt5 import QtCore
                if event.buttons() == QtCore.Qt.LeftButton:
                    from time import sleep
                    sleep(0.1);self.close()
            self.close_window.mousePressEvent = close_windowClick
        initToolBar()
        from .Controler.ContentTabListControler import ContentTabList
        ContentTabList(self,self)
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

