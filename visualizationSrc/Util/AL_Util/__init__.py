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
        # 不能使用 import clr直接引入clr
        # 会导致无法打包程序
        import clr
        temp = clr.AddReference(TetraProject_Data_Managed_DLL_PATH)
        import GameCore
    else:
        GameCore = None
except Exception as e:
    log.record(logLevel.ERROR, 'import_module("clr")', e)
    GameCore = None