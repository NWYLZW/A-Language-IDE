#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   ImportExportCardUtil.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/21 2:13
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   导入导出卡牌帮助文件
'''
__all__ = ["importCard","exportCard"]
modelStr=\
"""// @author:                         {author}
// @reprintedAuthor:                {reprintedAuthor}
// @displayName:                    {displayName}
// @price:                          {price}
// @energyReq:                      {energyReq}
// @range:                          {range}
// @spreadRadius:                   {spreadRadius}
// @spreadShapeTextureId:           {spreadShapeTextureId}
// @aimTypeCode:                    {aimTypeCode}
// @perferredTargetTypeCode:        {perferredTargetTypeCode}
// @tagCode:                        {tagCode}
// @backgroundUrl:                  {backgroundUrl}
// @effectCode:                     {effectCode}
// @minUnlockGrade:                 {minUnlockGrade}
// @characterModelSkinId:           {characterModelSkinId}
// @story:                          {story}
// @description:                    {description}
// @note:                           {note}
// @modifyTime:                     {modifyTime}
// @code:
{code}
// @remapCode:
{remapCode}
"""
# (?<=\/\/ \@code\:\n)(.*(\n))*(?=\/\/ \@.*\:\n)
# (?<=\/\/ \@code\:\n)(.*(\n))*((?=\/\/ \@.*\:\n)|.*)
DefaultDict = {
    "author":"匿名",
    "reprintedAuthor":"原创作者",
    "displayName":"没有名字的一张牌牌",
    "price":"0",
    "energyReq":"0",
    "range":"0",
    "spreadRadius":"0",
    "spreadShapeTextureId":"0",
    "aimTypeCode":"",
    "perferredTargetTypeCode":"",
    "tagCode":"",
    "backgroundUrl":"",
    "effectCode":"",
    "minUnlockGrade":"0",
    "characterModelSkinId":"0",
    "modifyTime":"",
    "note":"",
    "story":"",
    "description":"",
    "code":"",
    "remapCode":"",
}
def importCard(import_card_str:str="",)\
        ->dict:
    '''
    从字符串导出card字典
    :param import_card_str: 导入字符串
    :return: 导出字符串
    '''
    dictx = {}
    if import_card_str=="":return dictx
    try:
        import re
        for key in DefaultDict:
            if key == "code":
                allList = re.findall(r'(?<=\/\/ \@code\:\n)(.*(\n))*(?=\/\/ \@.*\:\n)', import_card_str, re.M | re.I)  # type: list[str]
            elif key == "remapCode":
                allList = re.findall(r'(?<=\/\/ \@code\:\n)(.*(\n))*((?=\/\/ \@.*\:\n)|.*)', import_card_str, re.M | re.I)  # type: list[str]
            else:
                allList = re.findall(r'(?<=\/\/ \@'+key+'\: ).*', import_card_str, re.M | re.I)  # type: list[str]

            if len(allList) > 0:
                if key != "note":
                    if key in ["code","remapConde"]:
                        dictx[key] = "".join(allList[0])
                    elif key in ["story","description"]:
                        dictx[key] = allList[0].replace('\\n', '\n').replace(' ','')
                    else:
                        dictx[key] = allList[0].replace(' ','')
                else:
                    dictx[key] = [note.replace(' ','') for note in allList]
            else: continue
    except Exception as e:print(e);
    return dictx
def exportCard(export_card_dict:dict={},)\
        ->str:
    '''
    从card字典导出字符串
    :param export_card_dict: 导入字典
    :return: 导出字符串
    '''
    newDict = DefaultDict.copy()
    temp_export_card_dict = export_card_dict.copy()
    temp_export_card_dict['story'] = export_card_dict['story'].replace('\n', '\\n')
    temp_export_card_dict['description'] = export_card_dict['description'].replace('\n', '\\n')
    newDict.update(**temp_export_card_dict)
    return modelStr.format(**newDict)