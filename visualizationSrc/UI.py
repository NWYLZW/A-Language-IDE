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
def initFont(editor):
    from PyQt5.QtGui import QFont
    editor.setPlainText('')
    font = editor.font()
    font.setFamily('Consolas')
    font.setStyleHint(QFont.Monospace)
    font.setPointSize(14)
    editor.setFont(font)
    editor.setTabStopWidth(16)
def inity(mainWindow):
    from visualizationSrc.Util.CompleterUtil import Completer
    from visualizationSrc.Util.HighLighterUtil import HighLighter
    from visualizationSrc.qtUI.addCard import Ui_MainWindow
    UI = Ui_MainWindow()
    UI.setupUi(mainWindow)
    initFont(UI.codeSource)
    initFont(UI.remapCodeSource)
    # 设置语法高亮
    UI.completer = Completer()

    UI.codeSource.set_completer(UI.completer.completer)
    UI.remapCodeSource.set_completer(UI.completer.completer)
    UI.codeSourceHighlighter = HighLighter(UI.codeSource.document())
    UI.remapCodeSourceHighlighter = HighLighter(UI.remapCodeSource.document())
    return UI