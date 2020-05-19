#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardControler.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 4:34
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from visualizationSrc.Controler.Helper.CSVHelperControler import CSVHelperControler

class CardControler(CSVHelperControler):
    def __init__(self):
        super().__init__("Card")
    def _setRowDictDefaultValue(self):
        self.DefaultValue = {
                'id': '10000',
                'displayName':"无名",
                'price':0,
                "energyReq":0,
                "range":0,
                "spreadRadius":0,
                "spreadShapeTextureId":"",
                "aimTypeCode":"",
                "perferredTargetTypeCode":"",
                "tagCode":"",
                "description":"",
                "story":"",
                "code":"",
                "remapCode":"",
                "backgroundId":"",
                "effectCode":"Sound:Shoot",
                "characterModelSkinId":"",
                "minUnlockGrade":1,
        }
    def getCardList(self)->list:
        return self._rowList
    def addCard(self,**cardDict):
        # 自动管理ID
        mID = self._rowList[len(self._rowList) - 1].get('id', '10000')
        newCard = self._addRow(cardDict)
        newCard['id'] = str(int(mID)+1)
        return newCard
    def updataCard(self,**cardDict):
        cardID = cardDict.get('id','')
        if cardID == '': return False
        if self.getCardById(cardID)=={}: return False
        return self._updataRowByfieldName('id',cardDict)
    def getCardById(self,cardId) -> dict:
        return self._getRowByfieldName('id', cardId)
    def delCardById(self,cardId):
        return self._delRowByfieldName('id', cardId)