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
from time import sleep

from PyQt5.QtWidgets import QMainWindow, QApplication

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
    from visualizationSrc.Util.CompleterUtil import Completer
    from visualizationSrc.Util.HighLighterUtil import HighLighter
    from visualizationSrc.qtUI.addCard import Ui_MainWindow
    UI = Ui_MainWindow()
    UI.setupUi(mainWindow)

    from PyQt5.QtCore import Qt
    mainWindow.setWindowFlags(Qt.FramelessWindowHint)
    def initToolBar():
        def close_windowClick(event):
            from PyQt5 import QtCore
            if event.buttons() == QtCore.Qt.LeftButton:
                sleep(0.1);mainWindow.close()
        UI.close_window.mousePressEvent = close_windowClick
    initToolBar()

    # 设置语法高亮
    UI.completer = Completer()
    from visualizationSrc.Util.TextEditorUtil import TextEditor
    def QTextEditToTextEditor(parent,mQTextEdit):
        parent.removeWidget(mQTextEdit);mQTextEdit.setParent(None)
        mQTextEdit = TextEditor()
        parent.addWidget(mQTextEdit)
        initFont(mQTextEdit)

        mQTextEdit.set_completer(UI.completer.completer)
        mQTextEdit.HL = HighLighter(mQTextEdit.document())
        return mQTextEdit

    UI.codeSource = QTextEditToTextEditor(UI.cardMakeTap_code,UI.codeSource)
    UI.remapCodeSource = QTextEditToTextEditor(UI.cardMakeTap_remap,UI.remapCodeSource)

    return UI