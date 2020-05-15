#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   build.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/12 2:54
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import os
import re

if __name__ == '__main__':
    os.system("pyrcc5 qtUI/AL_IDE_MainInterFace.qrc -o qtUI/AL_IDE_MainInterFace_rc.py")
    def buildUiFile(fileName):
        os.system("python -m PyQt5.uic.pyuic qtUI/"+fileName+".ui -o qtUI/"+fileName+".py")
        with open('qtUI/'+fileName+'.py', 'r+', encoding="utf-8") as f:
            str = f.read()
        regex = r'(?<!from\ .\ )import\ .*_rc'
        result = re.findall(regex, str)
        for r in result:
            str = re.sub(regex, "from . " + r, str)
        with open('qtUI/'+fileName+'.py', 'w+', encoding="utf-8") as f:
            f.write(str)

    buildUiFile("mainInterFace")
    buildUiFile("cardItemModel")
