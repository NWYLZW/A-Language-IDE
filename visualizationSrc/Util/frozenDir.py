#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   frozenDir.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 7:12
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
# -*- coding: utf-8 -*-
import sys,os

from .UserUtil import UserUtil

def appPath():
    """Returns the application run path."""
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    return os.getcwd()
def currentProPath():
    """Returns the current project path."""
    return UserUtil().getRecentProjectPath()
def tempPath():
    """Returns the application temp path."""
    if hasattr(sys, 'frozen'):
        return sys._MEIPASS
    return os.getcwd()