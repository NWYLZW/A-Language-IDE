#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   compileHelper.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/22 13:21
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from . import GameCore
class CompileHelper:
    def __init__(self):
        self.GameCoreCommand = GameCore.Command
        pass
    def _compileCommand(self, commandStr):
        Command = self.GameCoreCommand.Parse(commandStr)
        return Command
    def isCommand(self,commandStr)\
            ->bool:
        return self._compileCommand(commandStr).isCommand