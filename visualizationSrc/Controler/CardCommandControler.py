#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardCommandControler.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/17 6:27
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from visualizationSrc.Controler.Helper.CSVHelperControler import CSVHelperControler

class CardCommandControler(CSVHelperControler):
    def __init__(self):
        super().__init__("CardCommand")
    def _setRowDictDefaultValue(self):
        self.DefaultValue = {
            "id":"无名指令",
            "description":"没有设置介绍",
            "quoteDescription":"没有设置介绍",
            "effectCode":"",
            "remapCode":""
        }
    def getCardCommandByName(self,CardCommandName):
        return self._getRowByfieldName('id', CardCommandName)
    def delCardCommandByName(self,CardCommandName) -> bool:
        return self._delRowByfieldName('id', CardCommandName)
    def updataCardCommand(self,CardCommandDict) -> bool:
        CardCommandName = CardCommandDict.get('id','')
        if CardCommandName == '': return False
        if self.getCardCommandByName(CardCommandName)=={}: return False
        return self._updataRowByfieldName('id',CardCommandDict)
    def addCardCommand(self,CardCommandDict) -> bool:
        CardCommandName = CardCommandDict.get('id','')
        if CardCommandName == '': return False
        if self.getCardCommandByName(CardCommandName)!={}: return False
        return self._addRow(CardCommandDict)