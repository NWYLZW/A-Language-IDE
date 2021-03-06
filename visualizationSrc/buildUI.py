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
        uiPath = path+".ui"
        filePreData = buildUI_Dict.get(uiPath,None)
        mtime = time.ctime(os.path.getmtime(uiPath))
        if filePreData:
            if filePreData == mtime: return False
        else:
            buildUI_Dict[uiPath] = "%s" % mtime

        os.system("python -m PyQt5.uic.pyuic "+uiPath+" -o "+path+".py")
        with open(path+'.py', 'r+', encoding="utf-8") as f:
            str = f.read()
        regex = r'(?<!from\ \.[1-100]\ )import\ .*_rc'
        result = re.findall(regex, str)
        for r in result:
            str = re.sub(regex, "from "+"."*(path.count('\\')-1)+" " + r, str)
        with open(path+'.py', 'w+', encoding="utf-8") as f:
            f.write(str)
        return True
    ignoreFolder = [
        ".\\qtUI\\MyWidgets",
    ]
    def record(folder):
        if folder in ignoreFolder:return
        for name in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, name)):
                record(os.path.join(folder, name))
            elif name.endswith(".ui"):
                uiFileName = os.path\
                    .join(folder, name)\
                    .replace(".ui","")
                print("正在构建===>",uiFileName)
                if buildUiFile(uiFileName):
                    print("[构建完成]")
                else:
                    print("[ignore]")
    record(".")

    with open(buildUI_DATA_PATH, 'w', encoding="utf-8-sig") as f:
        f.write(json.dumps(buildUI_Dict))
