#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   build.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/17 1:02
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   构建项目
'''
import os
import re
import shutil

import visualizationSrc.config as ExeConfig

if __name__ == '__main__':
    with open('start.spec', 'r+', encoding="utf-8") as f:
        str = f.read()
    boolToStr = lambda x: "True" if x else "False"
    fileName = ExeConfig.ExeName +'_' + ExeConfig.Version \
               + (lambda : "-debug" if ExeConfig.Debug else "")()\
               + (lambda : "-withConsole" if ExeConfig.Console else "")()
    str = re.sub(r'name=\'.*\'', 'name=\'' + fileName + '\'', str)
    str = re.sub(r'debug=.*,', 'debug='+boolToStr(ExeConfig.Debug)+',', str)
    str = re.sub(r'console=.*,', 'console='+boolToStr(ExeConfig.Console)+',', str)
    str = re.sub(r'icon=\'.*\'', 'icon=\''+ExeConfig.Ico+'\'', str)

    with open('start.spec', 'w+', encoding="utf-8") as f:
        f.write(str)
    os.system("pyinstaller start.spec")
    try:
        import os
        from glob import glob
        for file in glob('./AL-IDE_*.exe'):
            os.remove(file)
        shutil.copy('./dist/'+fileName+'.exe','./'+fileName+'.exe')
    except Exception as e:print(e)