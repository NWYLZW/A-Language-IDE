#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   UserUtil.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/22 14:05
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
__all__ = ["UserUtil"]

import time

from visualizationSrc.Util.frozenDir import appPath
import os,json

defaultUserDict = {
    "UserName":"无名",
    "GamePath":"D:\\Steam\\steamapps\\common\\Tetra Project\\",
}
cardPKGs = {
    "MYSELF_CARD_PKG":{},
}
importCardList = {}

class base(object):
    def __init__(self):
        self.userDataPath = appPath() + "/../AL-IDE_Data"
        if not os.path.exists(self.userDataPath):
            os.makedirs(self.userDataPath)

class user(base):
    def __init__(self):
        super().__init__()
        self._initUserJson()
    def _initUserJson(self):
        if not os.path.isfile(self.userDataPath + "/user.json"):
            with open(self.userDataPath + "/user.json", mode="w", encoding="utf-8"):pass
        with open(self.userDataPath + "/user.json", mode="r", encoding="utf-8") as f:
            try: self.userDict = json.loads(f.read())
            except: self.userDict = defaultUserDict
        self._saveUserDict()
    def _saveUserDict(self):
        with open(self.userDataPath + "/user.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.userDict))
    @property
    def gamePath(self):
        return self._getUserValue("GamePath")
    @gamePath.setter
    def gamePath(self,value):
        self._setUserValue("GamePath",value)
    @property
    def userName(self):
        return self._getUserValue("UserName")
    @userName.setter
    def userName(self,value):
        self._setUserValue("UserName",value)
    def _getUserValue(self,key):
        return self.userDict.get(
            key,
            defaultUserDict.get(
                key
            )
        )
    def _setUserValue(self,key,value):
        self.userDict[key] = value
        self._saveUserDict()

class card(base):
    def __init__(self):
        super().__init__()
        self._initCardPKGJson()
    def _initCardPKGJson(self):
        if not os.path.isfile(self.userDataPath + "/cardPKG.json"):
            with open(self.userDataPath + "/cardPKG.json", mode="w", encoding="utf-8"):pass
        if not os.path.isfile(self.userDataPath + "/importCardList.json"):
            with open(self.userDataPath + "/importCardList.json", mode="w", encoding="utf-8"):pass

        with open(self.userDataPath + "/cardPKG.json", mode="r", encoding="utf-8") as f:
            try: self.cardPKGs = json.loads(f.read())
            except: self.cardPKGs = cardPKGs
        with open(self.userDataPath + "/importCardList.json", mode="r", encoding="utf-8") as f:
            try: self.importCardList = json.loads(f.read())
            except: self.importCardList = importCardList
        self._saveCardPKGDict()
    def _saveCardPKGDict(self):
        with open(self.userDataPath + "/cardPKG.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.cardPKGs))
        with open(self.userDataPath + "/importCardList.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.importCardList))
    def _getCardImportData(self, author, displayName):
        returnDict = self.cardPKGs\
            .get(author,{displayName: {}})\
                .get(displayName,{})
        returnDict["author"] = author
        return returnDict
    def _getAuthorAndDisplayName(self, card):
        authorAndDisplayName = self.importCardList.get(card.get('id',"-10001"),"")
        if authorAndDisplayName == "": authorAndDisplayName = None
        else: authorAndDisplayName = authorAndDisplayName.split('.')
        return authorAndDisplayName

class UserUtil(user,card):
    def __init__(self):
        super().__init__()

    def addCard(self, author, card:dict, reprintedAuthorList):
        if author == self.userName: author = "MYSELF_CARD_PKG"
        if self.cardPKGs.get(author,"") == "":
            self.cardPKGs[author] = {}
        cardPKGs = self.cardPKGs[author]
        cardPKGs[card.get("displayName","无名")] = {}
        cardPKGs[card.get("displayName","无名")]["reprintedAuthorList"] = reprintedAuthorList
        cardPKGs[card.get("displayName","无名")]["importCardTime"] = time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time()))
        self.importCardList[card.get("id","-10000")] = author+'.'+card.get("displayName","无名")
        self._saveCardPKGDict()
    def cardIsIn(self,card):
        if self._getAuthorAndDisplayName(card): return True
        else: return False
    def getCardImportDataByCard(self, card):
        authorAndDisplayName = self._getAuthorAndDisplayName(card)
        if authorAndDisplayName: return self._getCardImportData(authorAndDisplayName[0],authorAndDisplayName[1])
        else:return None
    def delCard(self,card):
        authorAndDisplayName = self._getAuthorAndDisplayName(card)
        print(authorAndDisplayName)
        if authorAndDisplayName:
            del self.cardPKGs[authorAndDisplayName[0]][authorAndDisplayName[1]]
            del self.importCardList[card.get("id","-10000")]
            self._saveCardPKGDict()
        return None
