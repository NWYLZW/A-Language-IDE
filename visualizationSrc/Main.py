#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   Main.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/10 23:06
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :
'''
__all__ = ["mainWindowStart"]
import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from .MyWindow import MyWindow
from .Util.UserUtil import UserUtil
from .Util.frozenDir import appPath

def mainWindowStart():
    APP = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.initContentTabList()
    mainWindow.show()

    sys._excepthook = sys.excepthook
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = my_exception_hook
    # 检验文件夹是否正确
    from re import search
    if not search(r".*:.*\\TetraProject\\Packages\\.*(?<!\\)$", appPath()):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.critical(mainWindow, '错误', '请将文件放置于你的Mod文件夹下', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        QTimer.singleShot(200, lambda: mainWindow.close())
    else:
        from .config import GamePath
        GamePath = UserUtil().gamePath
    try: sys.exit(APP.exec_())
    except: print("Exiting")