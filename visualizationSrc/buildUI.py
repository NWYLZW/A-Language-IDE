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
import json
import os
import re
import time

if __name__ == '__main__':
    os.system("pyrcc5 qtUI/AL_IDE_MainInterFace.qrc -o qtUI/AL_IDE_MainInterFace_rc.py")
    buildUI_Dict = {

    }
    buildUI_DATA_PATH = "Data/buildUI_DATA.json"
    if not os.path.isfile(buildUI_DATA_PATH):
        with open(buildUI_DATA_PATH, 'w', encoding="utf-8-sig") as f:
            f.write(json.dumps(buildUI_Dict))
    with open(buildUI_DATA_PATH, 'r', encoding="utf-8-sig") as f:
        buildUI_Dict = json.loads(f.read())

    def buildUiFile(path=""):
        uiPath = "qtUI/"+path+".ui"
        filePreData = buildUI_Dict.get(uiPath,None)
        mtime = time.ctime(os.path.getmtime(uiPath))
        if filePreData:
            if filePreData == mtime: return
        else:
            buildUI_Dict[uiPath] = "%s" % mtime

        os.system("python -m PyQt5.uic.pyuic "+uiPath+" -o qtUI/"+path+".py")
        with open('qtUI/'+path+'.py', 'r+', encoding="utf-8") as f:
            str = f.read()
        regex = r'(?<!from\ \.[1-100]\ )import\ .*_rc'
        result = re.findall(regex, str)
        for r in result:
            str = re.sub(regex, "from "+"."*(path.count('/')+1)+" " + r, str)
        with open('qtUI/'+path+'.py', 'w+', encoding="utf-8") as f:
            f.write(str)

    def record(folder):
        for name in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, name)):
                record(os.path.join(folder, name))
            elif name.endswith(".ui"):
                uiFileName = os.path\
                    .join(folder, name)\
                    .replace(".\\qtUI\\","")\
                    .replace(".ui","")
                buildUiFile(uiFileName)
    record(".")

    with open(buildUI_DATA_PATH, 'w', encoding="utf-8-sig") as f:
        f.write(json.dumps(buildUI_Dict))
