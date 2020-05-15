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
# import win32com
# from win32com.client import Dispatch
#
# # 进程可见，False是它后台
# Visible = False
#
# def excel_open(filePath, sheetName, fun, VBA=""):
#     xlApp = win32com.client.DispatchEx("Excel.Application")
#     xlApp.Visible = Visible
#     xlApp.DisplayAlerts = 0
#     try:
#         xlBook = xlApp.Workbooks.Open(filePath,False)
#         sht = xlBook.Worksheets(sheetName)
#         fun(sht)
#         print("WRITE FINISHED")
#         xlBook.Close(True)
#         if VBA !="":
#             useVBA(xlApp, filePath, VBA)
#             print("VBA FINISHED")
#     except Exception as e:
#         print(e)
#     finally:
#         xlApp.Quit()
#         return 0
# def useVBA(xlApp, filePath, VBA):
#     xlBook = xlApp.Workbooks.Open(filePath,False)
#     xlBook.Application.Run(VBA)
#     xlBook.Close(True)
#
# from ..Util.frozenDir import appPath
# temp = appPath()
# proHome = temp[0] + (lambda : "" if temp[1] else "../../../")()
# DatabaseXlsPath = proHome+'Database/Database.xls'
#
# def insertCard(c):
#     filePath = DatabaseXlsPath
#     # c = Card(
#     #     id=10001, displayName="转运咒语", price=100, energyReq=0,
#     #     range=0,
#     #     description="传送至灰雾之上1个回合",
#     #     code="LoadLevel:get_currentLevelId:;\nLog:get_currentLevelId:;",
#     #     story0="“福生玄黄仙尊。”\n“福生玄黄天君。”\n“福生玄黄上帝。”\n“福生玄黄天尊。”")
#     def __insertCard(sht):
#         preCell = None
#         for i in range(1,sht.usedrange.rows.count):
#             cell = sht.Cells(i+1, 1)
#             if cell.Value == None:
#                 if i == 1: preId = 10000
#                 else: preId = preCell.Value
#                 c.id = preId + 1
#                 t = c.toTuple()
#                 for j in range(t.__len__()):
#                     if t[j] != "":sht.Cells(i + 1, j+1).Value = t[j]
#                 break
#             preCell = cell
#     return excel_open(filePath, "Card", __insertCard, "CsvExportBook")

import csv

class CardControler:
    def __init__(self):
        from ..Util.frozenDir import appPath
        temp = appPath()
        proHome = temp[0] + (lambda : "/" if temp[1] else "../../../")()
        self.csvFileName = proHome+"Database/Card.csv"
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
                    cardDict.get("energyReq",0),
                "range":
                    cardDict.get("range",0),
                "spreadRadius":
                    cardDict.get("spreadRadius",0),
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
                    cardDict.get("backgroundId",1),
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
        except:
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
        pass
    def refreshFile(self):
        with open(self.csvFileName, 'w', encoding="UTF-8-sig", newline='') as f:
            writer = csv.DictWriter(f, self.fieldnames)
            writer.writeheader()
            for row in self.__cardList:
                if row != None: writer.writerow(row)