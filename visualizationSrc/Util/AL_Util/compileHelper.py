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
        if GameCore:
            self.GameCoreCommand = GameCore.Command
            self._canCompile = True
        else:
            self._canCompile = False
        pass
    def _compileCommand(self, commandStr):
        Command = self.GameCoreCommand.Parse(commandStr)
        return Command
    def canCompile(self, commandStr)\
            ->bool:
        if self._canCompile and\
                (self._compileCommand(commandStr).isCommand
                 or self._compileCommand(commandStr).isGroup): return True
        else: return True