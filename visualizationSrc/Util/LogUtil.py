# -*- coding: utf-8 -*-
# Time: 2020/03/29
# 日志记录模块
import logging
import os
import time
from enum import Enum, unique

@unique
class logLevel(Enum):
    ERROR = 0
    WARN = 1
    INFO = 2
    DEBUG = 3

class LOG:
    def __init__(self):
        self.isEnd = False
        self.level = logLevel
        self.__ignoreLevel:logLevel = logLevel.ERROR
        self.__logLevelName = {
            0:"ERROR",
            1:"WARN",
            2:"INFO",
            3:"DEBUG",
        }
        self.__ignoreLevelDict = {}
        self.logPath = "{0}\\AppData\\Local\\AL-IDE_Data\\Log".format(os.path.expanduser('~'))
    def record(self, level:logLevel, TAG:str, message):
        self.isEnd = False
        if not level in self.__ignoreLevelDict:
            if level.value >= self.__ignoreLevel.value:
                head = "[" + self.__logLevelName.get(level.value) + "]" + "\t" + time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime()) + "\t"
                if isinstance(message,Exception): logging.exception(message)
                if TAG != "": print(head+TAG+'\t'+str(message))
                else: print(head+str(message))
                try:
                    if not os.path.exists(self.logPath):
                        os.makedirs(self.logPath)
                    with open(self.logPath + '\\' + self.__logLevelName.get(level.value) + '.log', 'a+', encoding='utf-8') as f1:
                        writeStr = head
                        if TAG != "": writeStr+=TAG + '\t'
                        try: writeStr+=str(message)
                        except: writeStr+="message没有str方法"
                        finally: writeStr+='\n'
                        f1.write(writeStr)
                except Exception as e:print(e)
        self.isEnd = True
    def getLogListFromFile(self,TAG:logLevel):
        with open(self.logPath + '\\' + self.__logLevelName.get(TAG.value)+'.log','r+',encoding='utf-8') as f1:
            return f1.readlines()
    def setIgnoreMinLevel(self, ignoreLevel:logLevel):
        self.__ignoreLevel = ignoreLevel
    def setIgnoreLevel(self, ignoreLevelDict:dict):
        self.__ignoreLevelDict = ignoreLevelDict
log = LOG()