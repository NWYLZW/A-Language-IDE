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
        self.serverCardCommandWrraper = \
"""Log: "<serverCard>";
Log: preCardId=>{GetVar:preCardId};
Log: thisCardId=>{get_cardId:};
Log: thisSelPos=>{$selPos};
commands
SetVar: preCardId,{get_cardId:};
Log: thisPosition=>{$position};
Log: "</serverCard>";"""
        self.commandGroupWrraper = \
"""
If:{True:}{
{commandGroupListStr}
}{}
"""
    def createUserInPostion(self,userVarName,x,y):
        c = """
        With:{
            CreateCha:
                40,
                {NewVector3:{pos_x},0,{pos_y}}
            ;
        }{
            SetStageVar: {userVarName},$user;
        };
        """
        CH.addCommand(c
                      .replace("{pos_x}",str(x))
                      .replace("{pos_y}",str(y))
                      .replace("{userVarName}",userVarName)
                      )
    def moveUserToPostion(self,userVarName,x,y):
        c = """
        With:{GetStageVar:{userVarName}}{
            Log: $user;
            $user.MoveTo:{
                NewVector3:{pos_x},0,{pos_y};
            };
            Log: $userPosition;
        };
        """
        CH.addCommand(c
                      .replace("{pos_x}",str(x))
                      .replace("{pos_y}",str(y))
                      .replace("{userVarName}",userVarName)
                      )
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
    def runServerCardToGame(self,commandStr:str):
        commandStr = self.serverCardCommandWrraper.replace("commands",commandStr)
        self.addCommand(commandStr)
if __name__ == '__main__':
    CH = CommandHelper()
    CH.createUserInPostion("tester01",3,17)
    CH.moveUserToPostion("tester01",3,20)
    CH.moveUserToPostion("tester01",3,18)
    CH.commit()
