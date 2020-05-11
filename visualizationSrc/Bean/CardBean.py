#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardBean.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 1:02
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   卡类
'''

class Card(object):
    def __init__(self,
                 # id、名字、价格、能量需求
                 id=0,displayName="无名",price=0,energyReq=0,
                 # 使用半径、扩散半径、扩散作用位置图片(RangeShapeTexture/XXX.png)
                 range=0,spreadRadius="",spreadShapeTextureId="",
                 # 瞄准类型、使用目标类型（影响AI）
                 aimTypeCode="",perferredTargetTypeCode="",
                 # 标签、卡面简介、卡牌故事
                 tagCode="",description="",story0="",
                 # 执行代码、remap代码
                 code="",remapCode="",
                 # 卡牌背景图、使用时特效代码、实体皮肤ID
                 backgroundId=1,effectCode="Sound:Shoot",characterModelSkinId="",
                 # 最小解锁分数(卡牌解锁限制)
                 minUnlockGrade=1,
                 # 职业类型
                 professionalTypes=""):
        self.id = id
        self.displayName = displayName
        self.price = price
        self.energyReq = energyReq
        self.range = range
        self.spreadRadius = spreadRadius
        self.spreadShapeTextureId = spreadShapeTextureId
        self.aimTypeCode = aimTypeCode
        self.perferredTargetTypeCode = perferredTargetTypeCode
        self.tagCode = tagCode
        self.description = description
        self.code = code
        self.remapCode = remapCode
        self.backgroundId = backgroundId
        self.effectCode = effectCode
        self.minUnlockGrade = minUnlockGrade
        self.story0 = story0
        self.characterModelSkinId = characterModelSkinId
        self.professionalTypes = professionalTypes
    def toTuple(self) -> tuple:
        return (
            self.id,
            self.displayName,
            self.price,
            self.energyReq,
            self.range,
            self.spreadRadius,
            self.spreadShapeTextureId,
            self.aimTypeCode,
            self.perferredTargetTypeCode,
            self.tagCode,
            self.description,
            self.code,
            self.remapCode,
            self.backgroundId,
            self.effectCode,
            self.minUnlockGrade,
            self.story0,
            self.characterModelSkinId,
            self.professionalTypes,
        )