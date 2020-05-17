#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   UI.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 9:45
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   初始化UI界面
'''
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtWidgets import QMainWindow, QApplication
from .config import *

def initFont(editor):
    from PyQt5.QtGui import QFont
    editor.setPlainText('')
    font = editor.font()
    font.setFamily('Consolas')
    font.setStyleHint(QFont.Monospace)
    font.setPointSize(14)
    editor.setFont(font)
    editor.setTabStopWidth(16)
def init(APP:QApplication,mainWindow:QMainWindow):
    from .qtUI import mainInterFace
    UI = mainInterFace.Ui_MainWindow()
    UI.setupUi(mainWindow)

    from PyQt5.QtCore import Qt
    mainWindow.setWindowFlags(Qt.FramelessWindowHint)
    def initToolBar():
        def close_windowClick(event):
            from PyQt5 import QtCore
            if event.buttons() == QtCore.Qt.LeftButton:
                from time import sleep
                sleep(0.1);mainWindow.close()
        UI.close_window.mousePressEvent = close_windowClick
    initToolBar()

    from .Controler.ContentTabListControler import ContentTabList
    ContentTabList(UI,mainWindow)
    UI.EXETitle.setText(ExeName +' ' + Version)
    return UI