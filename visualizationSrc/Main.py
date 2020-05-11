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

from visualizationSrc.Util.CompleterUtil import Completer
from visualizationSrc.Util.HighLighterUtil import HighLighter
from visualizationSrc.qtUI.addCard import Ui_MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    UI = Ui_MainWindow()
    UI.setupUi(mainWindow)

    from PyQt5.QtGui import QFont
    # 设置语法高亮
    UI.codeSource.setPlainText('')
    font = UI.codeSource.font()
    font.setFamily('Consolas')
    font.setStyleHint(QFont.Monospace)
    font.setPointSize(14)
    UI.codeSource.setFont(font)
    UI.codeSource.setTabStopWidth(20)
    UI.highlighter = HighLighter(UI.codeSource.document())

    # TODO select block of text - Ctrl+/ and they become comments
    UI.completer = Completer()
    UI.codeSource.set_completer(UI.completer.completer)
    mainWindow.show()

    sys._excepthook = sys.excepthook
    def my_exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    sys.excepthook = my_exception_hook
    try: sys.exit(app.exec_())
    except: print("Exiting")