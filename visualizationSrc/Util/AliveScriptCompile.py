#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   AliveScriptCompile.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/28 11:08
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import re
class funUnit(object):
    def __init__(self, funStr):
        funNameRe = r"[a-z,A-Z][a-z,A-Z,0-9,\_]*"
        # 获取参数内容
        getFunArgvRe = r"\((\$.*\,?)*\)"
        # 获取函数内容
        funArgvRe = r"\(.*\)"
        funMainRe = r"\{[^\}]+\}"
        self.name = re.sub(funArgvRe + funMainRe, "", funStr)
        self.argv = re.findall(
        funNameRe + getFunArgvRe + funMainRe
        ,funStr)[0].split(',')
        self.content = re.sub(funNameRe + funArgvRe, "", funStr)
    def toDict(self):
        return {
            "name":self.name,
            "argv":self.argv,
            "content":self.content,
        }
    def to_A_Command(self, argv):
        A_Command = "{setLocalVarPos}\n{setCommandPos}"
        tempStr = ""
        if len(argv)>0:
            for i in range(len(self.argv)):
                arg = self.argv[i]          # type: str
                tempStr += "SetLocalVar: "+arg.replace("$","")+", "+str(argv[i])+";"
        return ("If:{True:}{"+A_Command.format(**{
            "setLocalVarPos":tempStr,
            "setCommandPos":"If:{True:}"+self.content+"{}",
        })+"}{}").replace('\n', '').replace('\t', '').replace(' ', '')
class AliveScriptCompile:
    def __init__(self,AliveScriptStr):
        self.AliveScriptStr = AliveScriptStr
        self.funNameRe = r"[a-z,A-Z,\_][a-z,A-Z,0-9,\_]*"
        # 获取参数内容
        self.getFunArgvRe = r"\((\$.*\,?)*\)"
        # 获取函数内容
        self.funArgvRe = r"\(.*\)"
        self.funMainRe = r"\{[^\}]+\}"
        self.funDict = {}
        defFuns = re.findall(
            self.funNameRe + self.funArgvRe + self.funMainRe
            , AliveScriptStr)
        for fun in defFuns:
            temp = funUnit(fun)
            self.funDict[temp.name] = temp
    def parsingFunction(self):
        # 删除定义部分
        rspStr = re.sub(
            self.funNameRe + self.funArgvRe + self.funMainRe
            ,"", self.AliveScriptStr)
        # 删除空行
        rspStr = re.sub('\n(\n)*( )*(\n)*\n','',rspStr)
        # 搜索已使用的函数
        useFuns = re.findall(
            self.funNameRe + self.funArgvRe + ';',
            rspStr)
        # 将已使用的函数替换为指令集
        for useFun in useFuns:  # type: str
            funUintx = self.funDict[
                useFun.split('(')[0]
            ]
            argv = re.findall(
                        r"(?<=\()\S+(?=\))"
                        , useFun)
            loadCommand = funUintx.to_A_Command(
                argv[0].split(',') if len(argv)>0 else []
            )
            rspStr = rspStr.replace(
                useFun,loadCommand
            )
        return rspStr
    def parsingKeywords(self):
        const_find_re = "const\ *[a-z,A-Z,\_][a-z,A-Z,0-9,\_]*\ *=\ *.*;"
        constList = re.findall(
            const_find_re,self.AliveScriptStr)
        for constItem in constList:
            temp = re.findall(
                "const\ *([a-z,A-Z,\_][a-z,A-Z,0-9,\_]*)\ *=\ *(.*);",
                constItem)
            self.AliveScriptStr = re.sub(
                constItem,"SetVar: "+temp[0][0]+", {"+temp[0][1]+'};',self.AliveScriptStr)
        let_re = "let\ *[a-z,A-Z,\_][a-z,A-Z,0-9,\_]*\ *=\ *.*;"
        letList = re.findall(
            let_re,self.AliveScriptStr)
        for letItem in letList:
            temp = re.findall(
                "let\ *([a-z,A-Z,\_][a-z,A-Z,0-9,\_]*)\ *=\ *(.*);",
                letItem)
            self.AliveScriptStr = re.sub(
                letItem,"SetLocalVar: "+temp[0][0]+", {"+temp[0][1]+'};',self.AliveScriptStr)
    def to_A_Command(self):
        self.parsingKeywords()
        rspStr = self.parsingFunction()
        return rspStr

if __name__ == '__main__':
    testScript = """\
fun0($a,$b,$c){
    Log: $a;
    Log: $b;
    Log: $c;
}
const x = 4;
let y = 1;
Log: $x;
fun0(1,2,3);\
"""
    ASC = AliveScriptCompile(testScript)
    print(ASC.to_A_Command())
