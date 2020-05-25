#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   __init__.py.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/25 6:02
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
__all__ = ["createCM"]
from .main import ClientMain

def createCM(ClicentRunAfter,acceptMessage):
    CM = ClientMain()
    CM.startClient()
    CM.setClicentRunAfter(ClicentRunAfter)
    CM.setAcceptMessage(acceptMessage)
    return CM