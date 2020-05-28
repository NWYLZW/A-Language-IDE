#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   commandHelper.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/25 9:21
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   指令帮助类
'''
from time import sleep


class CommandHelper:
    def __init__(self):
        import os
        self.messageTxtPath = os.path.expanduser('~')+'\AppData\Local\Temp\TetraProject'
        if not os.path.exists(self.messageTxtPath):
            os.makedirs(self.messageTxtPath)

        self.commandStrList = []
        self.commandGroupWrraper = \
"""
If:{True:}{
{commandGroupListStr}
}{}
"""
    def getCommandResultFromLog(self):
        userGameLogPath = "C:\\Users\\Superme\\AppData\\LocalLow\\AliveGameStudio\\TetraProject\\Player.log"
        with open(userGameLogPath,mode="r+",encoding="utf-8")as f:
            loglines = f.readlines()
        tempListList = []
        flag = False;isFirst = False
        for logline in loglines:
            if logline == "<serverCard>\n": flag = True;isFirst = True
            elif logline == "</serverCard>\n": flag = False
            if isFirst:
                tempList = []
                tempListList.append(tempList)
            if flag:
                if not logline in [' \n','\n'] and logline[:10]!="(Filename:":
                    tempList.append(logline)
            isFirst = False
        for tempList in tempListList:
            print(tempList)
    def addCommand(self, commandStr:str):
        self.commandStrList.append(commandStr.replace('\n','').replace('\t','').replace(' ',''))
    def commit(self):
        strX = ';'.join(self.commandStrList)
        with open(self.messageTxtPath+'\message.txt','w',encoding='utf-8') as f1:
            f1.write(
                self.commandGroupWrraper.replace("{commandGroupListStr}",strX) \
                    .replace('\n', '').replace('\t', '').replace(' ', '')
            )
        self.commandStrList = []
if __name__ == '__main__':
    CH = CommandHelper()
    CH.commit()
