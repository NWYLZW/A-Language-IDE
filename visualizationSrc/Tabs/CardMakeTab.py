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
from PyQt5.QtWidgets import QMessageBox, QMainWindow

from ..qtUI.addCard import Ui_MainWindow
from ..Util.HighLighterUtil import HighLighter

class CardMake:
    def __init__(self,UI:Ui_MainWindow,mainWindow:QMainWindow):
        self.UI = UI
        self.mainWindow = mainWindow
        self.settingTab = UI.CMT_settingTab
        self.initTextEditor()
        self.initSettingTab()
        self.initClick()

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

        UI.CM_codeSource = QTextEditToTextEditor(UI.cardMakeTap_code,UI.CM_codeSource)
        UI.CM_remapCodeSource = QTextEditToTextEditor(UI.cardMakeTap_remap,UI.CM_remapCodeSource)
    def initSettingTab(self):
        tabTextList = ["基础设置","高级设置"]
        for i in range(tabTextList.__len__()):
            self.settingTab.setTabText(i,tabTextList[i])
    def initClick(self):
        UI = self.UI
        mainWindow = self.mainWindow
        from ..Controler.CardControler import insertCard
        from ..Bean.CardBean import Card
        def __insertCard():
            if insertCard(Card(
                displayName=UI.CM_displayName.text(), price=UI.CM_price.text(), energyReq=UI.CM_energyReq.text(),
                range=UI.CM_range.text(),
                description=UI.CM_description.toPlainText(),
                story0=UI.CM_story0.toPlainText(),
                code=UI.CM_codeSource.toPlainText(),
                remapCode=UI.CM_remapCodeSource.toPlainText()
            )) == 0:
                QMessageBox.information(
                    mainWindow,
                    '成功', '添加成功',
                    QMessageBox.Yes)
            else:
                QMessageBox.ctitical(
                    mainWindow,
                    '错误', '发送了一个错误',
                    QMessageBox.Yes)
        UI.CM_addCard.clicked.connect(__insertCard)
        pass