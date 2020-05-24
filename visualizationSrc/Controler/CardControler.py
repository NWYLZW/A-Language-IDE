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
from .Helper.CSVHelperControler import CSVHelperControler
from ..Util.AL_Util.compileHelper import CompileHelper

class CardControler(CSVHelperControler):
    def __init__(self):
        super().__init__("Card")
        # 编译帮助类
        self.CompileHelper = CompileHelper()
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
        if cardDict != {}:
            try: cardDict['id'] = str(int(mID)+1)
            except: return {}
        newCard = self._addRow(cardDict)
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
    def checkCode(self,cardId):
        '''
        :param cardId:
        :return: [
        0: 无误
        1: code部分有误
        2: remapCode部分有误
        3: 未找到id对应的卡牌字典
        ]
        '''
        card = self.getCardById(cardId)
        if card == {}: return 3
        if card.get('code', 'Error')=="" \
                or self.CompileHelper.canCompile(card.get('code', 'Error')):
            if card.get('remapCode', 'Error')==""\
                    or self.CompileHelper._canCompile(card.get('remapCode', 'Error')): return 0
            else: return 2
        else: return 1
    def printCard(self,cardId):
        if cardId == "newCard":
            return False
        import os
        from ..Util.frozenDir import appPath
        messageTxtPath = os.path.expanduser('~')+'\AppData\Local\Temp\TetraProject'
        if not os.path.exists(messageTxtPath):
            os.makedirs(messageTxtPath)
        with open(messageTxtPath+'\message.txt','w',encoding='utf-8') as f1:
            f1.write("Card:'"+cardId+"','id',"+os.path.abspath(appPath()+"/Database/Database.xls")+";")
        return True