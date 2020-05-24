#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   buildUI.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 2:54
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   构建项目的UI与资源的py文件
'''
import os
import re

if __name__ == '__main__':
    os.system("pyrcc5 qtUI/AL_IDE_MainInterFace.qrc -o qtUI/AL_IDE_MainInterFace_rc.py")
    def buildUiFile(path=""):
        os.system("python -m PyQt5.uic.pyuic qtUI/"+path+".ui -o qtUI/"+path+".py")
        with open('qtUI/'+path+'.py', 'r+', encoding="utf-8") as f:
            str = f.read()
        regex = r'(?<!from\ \.[1-100]\ )import\ .*_rc'
        result = re.findall(regex, str)
        for r in result:
            str = re.sub(regex, "from "+"."*(path.count('/')+1)+" " + r, str)
        with open('qtUI/'+path+'.py', 'w+', encoding="utf-8") as f:
            f.write(str)

    buildUiFile("mainInterFace")
    buildUiFile("messageBox")

    buildUiFile("CardControler/cardItemModel")
    buildUiFile("CardControler/cardDetailsModel")
    buildUiFile("CardControler/cardControler")

    buildUiFile("OnlineServer/onlineServer")
    buildUiFile("OnlineServer/roomItemModel")
    buildUiFile("OnlineServer/dialog/createRoomDialog")

    buildUiFile("dialog/loginDialog")
