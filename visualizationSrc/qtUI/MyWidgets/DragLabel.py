#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   DragLineEdit.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/26 3:32
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

class DragLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self._path = ""
        self._fill = True
        self.endswith = ".png"
    def setEndswith(self,endswith:str=".png"):
        self.endswith = endswith
    def setDragEndCallback(self,DragEndCallback):
        self._DragEndCallback = DragEndCallback
    def dragEnterEvent(self, e):
        if e.mimeData().text().endswith(self.endswith):
            e.accept()
        else:
            e.ignore()
    def dropEvent(self, e):
        self.path = e.mimeData().text().replace('file:///', '')
        try: self._DragEndCallback()
        except Exception as e:print(e)
    def _showImg(self):
        if self.path == "":return
        try:
            if self._fill: p = QPixmap(self._path).scaled(self.width(),self.height())
            else: p = QPixmap(self._path)
            self.setPixmap(p)
        except:pass

    @property
    def fill(self):
        return self._fill
    @fill.setter
    def fill(self,fill):
        self._fill = fill
    @property
    def path(self):
        return self._path
    @path.setter
    def path(self,path):
        self._path = path
        self.setToolTip(path)
        self._showImg()