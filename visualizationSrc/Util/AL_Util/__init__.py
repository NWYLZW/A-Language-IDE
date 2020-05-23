#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   __init__.py.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/21 22:17
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
__all__ = ['compileHelper']
from ..LogUtil import log, logLevel
from ...config import GamePath
TetraProject_Data_Managed_DLL_PATH = GamePath + "TetraProject_Data\\Managed\\Assembly-CSharp"
import os
try:
    if os.path.isfile(TetraProject_Data_Managed_DLL_PATH+".dll"):
        # 处理clr的引入时出现了找不到python.runtime.dll的错误
        # 最后把个人文件夹下的dll放到系统环境python 中便可打包了
        import clr
        temp = clr.AddReference(TetraProject_Data_Managed_DLL_PATH)
        import GameCore
    else:
        GameCore = None
except Exception as e:
    log.record(logLevel.ERROR, 'import_module("clr")', e)
    GameCore = None