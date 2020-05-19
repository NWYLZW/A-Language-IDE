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
import csv

class CardControler:
    def __init__(self):
        from ..Util.frozenDir import appPath
        proHome = appPath()
        self.csvFileName = proHome+"/Database/Card.csv"
        self.__cardList = []
        self.readCard()
        pass
    def getCardList(self)->list:
        return self.__cardList
    def readCard(self):
        with open(self.csvFileName, mode='r+', encoding="UTF-8-sig") as f:
            reader = csv.DictReader(f)
            self.fieldnames = reader.fieldnames
            for row in reader:
                if row['id'] != '': self.__cardList.append(row)
    def addCard(self,**cardDict):
        try:
            mID = self.__cardList[len(self.__cardList) - 1].get('id', '10000')
            cardDict.update({
                'id': str(int(mID) + 1),
                'displayName':
                    cardDict.get("displayName","无名"),
                'price':
                    cardDict.get("price",0),
                "energyReq":
                    cardDict.get("energyReq",0.0),
                "range":
                    cardDict.get("range",0.0),
                "spreadRadius":
                    cardDict.get("spreadRadius",0.0),
                "spreadShapeTextureId":
                    cardDict.get("spreadShapeTextureId",""),
                "aimTypeCode":
                    cardDict.get("aimTypeCode",""),
                "perferredTargetTypeCode":
                    cardDict.get("perferredTargetTypeCode",""),
                "tagCode":
                    cardDict.get("tagCode",""),
                "description":
                    cardDict.get("description",""),
                "story":
                    cardDict.get("story",""),
                "code":
                    cardDict.get("code",""),
                "remapCode":
                    cardDict.get("remapCode",""),
                "backgroundId":
                    cardDict.get("backgroundId",""),
                "effectCode":
                    cardDict.get("effectCode","Sound:Shoot"),
                "characterModelSkinId":
                    cardDict.get("characterModelSkinId",""),
                "minUnlockGrade":
                    cardDict.get("minUnlockGrade",1),
            })
            self.__cardList.append(cardDict)
            self.refreshFile()
            return int(mID)+1
        except Exception as e:
            print(e)
            return -1
    def updataCard(self,**cardDict):
        mcardDict = self.getCardById(cardDict.get('id',None))
        if mcardDict == None: return False
        mcardDict.update({
            'displayName':
                cardDict.get("displayName",mcardDict.get("displayName")),
            'price':
                cardDict.get("price",mcardDict.get("price")),
            "energyReq":
                cardDict.get("energyReq",mcardDict.get("energyReq")),
            "range":
                cardDict.get("range",mcardDict.get("range")),
            "spreadRadius":
                cardDict.get("spreadRadius",mcardDict.get("spreadRadius")),
            "spreadShapeTextureId":
                cardDict.get("spreadShapeTextureId",mcardDict.get("spreadShapeTextureId")),
            "aimTypeCode":
                cardDict.get("aimTypeCode",mcardDict.get("aimTypeCode")),
            "perferredTargetTypeCode":
                cardDict.get("perferredTargetTypeCode",mcardDict.get("perferredTargetTypeCode")),
            "tagCode":
                cardDict.get("tagCode",mcardDict.get("tagCode")),
            "description":
                cardDict.get("description",mcardDict.get("description")),
            "story":
                cardDict.get("story",mcardDict.get("story")),
            "code":
                cardDict.get("code",mcardDict.get("code")),
            "remapCode":
                cardDict.get("remapCode",mcardDict.get("remapCode")),
            "backgroundId":
                cardDict.get("backgroundId",mcardDict.get("backgroundId")),
            "effectCode":
                cardDict.get("effectCode",mcardDict.get("effectCode")),
            "characterModelSkinId":
                cardDict.get("characterModelSkinId",mcardDict.get("characterModelSkinId")),
            "minUnlockGrade":
                cardDict.get("minUnlockGrade",mcardDict.get("minUnlockGrade")),
        })
        self.refreshFile()
        return True
    def getCardById(self,cardId) -> dict:
        index = self.getCardIndexById(cardId)
        if index == -1: return {}
        return self.__cardList[index]
    def getCardIndexById(self,cardId) -> int:
        if cardId == None: return -1
        for index in range(len(self.__cardList)):
            if str(self.__cardList[index]['id']) == str(cardId):
                return index
        return -1
    def delCardById(self,cardId):
        index = self.getCardIndexById(cardId)
        if index == -1: return False
        del self.__cardList[index]
        self.refreshFile()
        return True
    def refreshFile(self):
        f = None
        try:
            f = open(self.csvFileName, 'w', encoding="UTF-8-sig", newline='')
            writer = csv.DictWriter(f, self.fieldnames)
            writer.writeheader()
            for row in self.__cardList:
                if row != None: writer.writerow(row)
        except Exception as e:
            try:f.close()
            except:pass
            print(e)