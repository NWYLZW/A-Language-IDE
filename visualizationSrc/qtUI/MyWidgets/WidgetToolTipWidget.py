#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   WidgetToolTipWidget.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/6/13 18:48
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
__all__ = ["WidgetToolTipWidget"]
from PyQt5.QtCore import QEvent, Qt, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QDockWidget, QGraphicsDropShadowEffect

class MyQDockWidgetFloat(QDockWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.BlurRadius = 10
        self.initUI()
    def initUI(self):
        # 默认隐藏
        self.hide()
        # 设置浮动
        self.setFloating(True)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 去除默认边框
        temp = QWidget();self.setTitleBarWidget(temp);del temp
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(self.BlurRadius)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
    def setWidget(self, widget: QWidget) -> None:
        super().setWidget(widget)
    def show(self) -> None:
        self.setGeometry(QRect(0,0,self.geometry().width(),self.geometry().height()))
        super().show()

class WidgetToolTipWidget(QLabel):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self._dockWidget = None
    def setToolTipWidget(self, toolTipWidget: QWidget):
        self._toolTipWidget = toolTipWidget
    def enterEvent(self, evt: QEvent) -> None:
        if self._dockWidget == None:
            self._dockWidget = MyQDockWidgetFloat(self)
        if self._dockWidget.widget() == None:
            self._dockWidget.setWidget(self._toolTipWidget)
        self._dockWidget.show()
    def leaveEvent(self, evt: QEvent) -> None:
        self._dockWidget.hide()
