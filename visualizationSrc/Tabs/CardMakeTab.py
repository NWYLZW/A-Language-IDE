#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardMakeTab.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 4:06
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   卡牌制作界面
'''
from visualizationSrc.qtUI.addCard import Ui_MainWindow
from visualizationSrc.Util.HighLighterUtil import HighLighter

class CardMake:
    def __init__(self,UI:Ui_MainWindow):
        self.UI = UI
        self.settingTab = UI.CMT_settingTab
        self.initTextEditor()
        self.initSettingTab()
    def initSettingTab(self):
        tabTextList = ["基础设置","高级设置"]
        for i in range(tabTextList.__len__()):
            self.settingTab.setTabText(i,tabTextList[i])
    def initTextEditor(self):
        UI = self.UI
        def initFont(editor):
            from PyQt5.QtGui import QFont
            editor.setPlainText('')
            font = editor.font()
            font.setFamily('Consolas')
            font.setStyleHint(QFont.Monospace)
            font.setPointSize(14)
            editor.setFont(font)
            editor.setTabStopWidth(16)
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