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
import sys
import os

def appPath():
    """Returns the base application path."""
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable),True
    return os.path.dirname(__file__),False