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
import os,json

defaultUserDict = {
    "UserName":"无名",
    "PWD":"***",
    "GamePath":"D:\\Steam\\steamapps\\common\\Tetra Project\\",
    "recentProject":[

    ],
}
cardPKGs = {
    "MYSELF_CARD_PKG":{},
}
importCardList = {}

class base(object):
    def __init__(self):
        self.userConfigPath = "{0}\\AppData\\Local\\AL-IDE_Data\\Config".format(os.path.expanduser('~'))
        if not os.path.exists(self.userConfigPath):
            os.makedirs(self.userConfigPath)

class user(base):
    def __init__(self):
        super().__init__()
        self._initUserJson()
    def _initUserJson(self):
        if not os.path.isfile(self.userConfigPath + "/user.json"):
            with open(self.userConfigPath + "/user.json", mode="w", encoding="utf-8"):pass
        with open(self.userConfigPath + "/user.json", mode="r", encoding="utf-8") as f:
            try: self.userDict = json.loads(f.read())
            except: self.userDict = defaultUserDict
        self._saveUserDict()
    def _saveUserDict(self):
        with open(self.userConfigPath + "/user.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.userDict))
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
    @property
    def PWD(self):
        return self._getUserValue("PWD")
    @PWD.setter
    def PWD(self,value):
        self._setUserValue("PWD",value)
    def pushNewProject(self, new_pro_path):
        if os.path.isfile(new_pro_path+"/Database/Database.xls"):
            pathList = self.getRecentProjectPathList()
            for pro_path in pathList:
                if pro_path == new_pro_path:
                    pathList.remove(pro_path);break
            pathList.insert(0, new_pro_path)
            self._saveUserDict()
            return True
        return False
    def getRecentProjectPathList(self):
        return self._getUserValue("recentProject")
    def getRecentProjectPath(self):
        pathList = self.getRecentProjectPathList()
        if len(pathList)!=0 \
                and pathList[0]: return pathList[0]
        return ""

class card(base):
    def __init__(self):
        super().__init__()
        self._initCardPKGJson()
    def _initCardPKGJson(self):
        if not os.path.isfile(self.userConfigPath + "/cardPKG.json"):
            with open(self.userConfigPath + "/cardPKG.json", mode="w", encoding="utf-8"):pass
        if not os.path.isfile(self.userConfigPath + "/importCardList.json"):
            with open(self.userConfigPath + "/importCardList.json", mode="w", encoding="utf-8"):pass

        with open(self.userConfigPath + "/cardPKG.json", mode="r", encoding="utf-8") as f:
            try: self.cardPKGs = json.loads(f.read())
            except: self.cardPKGs = cardPKGs
        with open(self.userConfigPath + "/importCardList.json", mode="r", encoding="utf-8") as f:
            try: self.importCardList = json.loads(f.read())
            except: self.importCardList = importCardList
        self._saveCardPKGDict()
    def _saveCardPKGDict(self):
        with open(self.userConfigPath + "/cardPKG.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(self.cardPKGs))
        with open(self.userConfigPath + "/importCardList.json", mode="w", encoding="utf-8") as f:
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
        self.exeDataPath = "{0}\\AppData\\Local\\AL-IDE_Data\\".format(os.path.expanduser('~'))

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
