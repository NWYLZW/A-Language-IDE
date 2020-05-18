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
from .Util import MessageBoxHelper
from .qtUI import mainInterFace

class MyWindow(QMainWindow,mainInterFace.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # 解决输出窗口打印出“UpdateLayeredWindowIndirect failed for ptDst=xxx”的错误
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.initUI()
        self._MessageBox = MessageBoxHelper.MessageBox(self.Main)
        try:
            from .Controler.ContentTabListControler import ContentTabList
            ContentTabList(self,self)
        except Exception as e:print(e)
        self.m_drag = False
    def initToolBar(self):
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
    def showInfo(self,Title,KindName,Content):
        self._MessageBox.showMessage(
            self._MessageBox.MessageBox_Tag.Information,
            Title=Title,
            KindName=KindName,
            Content=Content,
        )
    def showWarn(self,Title,KindName,Content):
        self._MessageBox.showMessage(
            self._MessageBox.MessageBox_Tag.Warning,
            Title=Title,
            KindName=KindName,
            Content=Content,
        )
    def showErr(self,Title,KindName,Content):
        self._MessageBox.showMessage(
            self._MessageBox.MessageBox_Tag.Error,
            Title=Title,
            KindName=KindName,
            Content=Content,
        )

    def mousePressEvent(self, event):
        self.mDragPosition=event.globalPos()-self.pos()
        if event.button()== Qt.LeftButton:
            self.m_drag=True
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.m_drag:
            self.move(event.globalPos()-self.mDragPosition)
            event.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

