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
from ...config import GamePath
TetraProject_Data_Managed_DLL_PATH = GamePath + "TetraProject_Data\\Managed\\Assembly-CSharp"
import clr
temp = clr.AddReference(TetraProject_Data_Managed_DLL_PATH)
import GameCore