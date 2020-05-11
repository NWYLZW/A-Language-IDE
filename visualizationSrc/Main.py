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
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from visualizationSrc import UI

def mainWindowStart():
    APP = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # 防止触发gc机制
    ui = UI.init(APP,mainWindow)
    mainWindow.show()

    sys._excepthook = sys.excepthook
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = my_exception_hook
    try: sys.exit(APP.exec_())
    except: print("Exiting")