#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CharacterControler.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/31 14:55
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from .Helper.CSVHelperControler import CSVHelperControler

class CharacterControler(CSVHelperControler):
    '''
    tagCode
    Main：主角，会出现在角色选择界面
    EnvObject：环境物体
    0bstacle：阻挡玩家通过，也阻挡射程
    Targetable：即使是障碍物，也可以被瞄准
    AllowBeTargetedEvenTeammate：即使是队友也可以被瞄准
    NotCombatable：不能战斗
    NotAllowCombatUI：不显示战斗UI，比如血条之类的
    NotAllowBuffUT：不显示Buff的UI
    NotAllowTakeImpulse：不会被击退
    NotAllowAimBySingle0nly：不会被single0nly的卡瞄准
    Trap：陷阱（可以踩上去
    NotAllowBeHarmed：不会再受伤
    '''
    def __init__(self):
        super().__init__("Character")
    def _setRowDictDefaultValue(self):
        self.DefaultValue = {
            "id":"",
            "displayName":"",
            "modelId":"",
            "modelSkinId":"",
            "description":"",
            "story":"",
            "//comment":"",
            "minUnlockGrade":"",
            "minimapModelId":"",
            "tagCode":"",
            "fieldCode":"",
            "energy":"",
            "stamina":"",
            "moveSpeed":"",
            "initialHandCardCount":"",
            "startTurnDrawHandCardCount":"",
            "//usedInCharactersetId":"",
            "hp":"",
            "gameRoundPowerUpCode":"",
            "selfCardTagCode":"",
            "selfCardCode":"",
            "interactionPlotId":"",
            "dropFilterCode":"",
            "initialRunCardId0":"",
            "initialRunCardId1":"",
            "initialRunCardId2":"",
            "initialRunCardId3":"",
            "cardId0":"",
            "cardId1":"",
            "cardId2":"",
            "cardId3":"",
            "cardId4":"",
            "cardId5":"",
            "cardId6":"",
            "cardId7":"",
            "cardId8":"",
        }
    def getCharacterList(self)->list:
        return self._rowList
    def getCharacterById(self,CharacterId):
        return self._getRowByfieldName('id', CharacterId)
    def getCharacterByName(self,CharacterName):
        return self._getRowByfieldName('displayName', CharacterName)

    def delCharacterById(self,CharacterId) -> bool:
        return self._delRowByfieldName('id', CharacterId)

    def updataCharacter(self,CharacterDict) -> bool:
        CharacterName = CharacterDict.get('id','')
        if CharacterName == '': return False
        if self.getCharacterByName(CharacterName)=={}: return False
        return self._updataRowByfieldName('id',CharacterDict)

    def addCharacter(self,CharacterDict) -> object:
        CharacterId = CharacterDict.get('id','')
        if CharacterId == '': return None
        if self.getCharacterById(CharacterId)!={}: return None
        return self._addRow(CharacterDict)

class ProtagonistControler(CharacterControler):
    def __init__(self):
        super().__init__()
    def getProtagonistList(self):
        protagonistList = []
        for character in self.getCharacterList():
            tagCode = character.get('tagCode','')
            if "Main" in tagCode.split(';') or "Main" == tagCode:
                for field in character.get('fieldCode','').split(';'):
                    if field == '':continue
                    temp = field.replace('\n','').split(':')
                    character[temp[0]] = temp[1]
                protagonistList.append(character)
        return protagonistList