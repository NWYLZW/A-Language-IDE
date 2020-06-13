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
    str = re.sub(r'name=\'.*\',', 'name=\'' + ExeConfig.ExeName + '\',', str)
    str = re.sub(r'debug=.*,', 'debug='+boolToStr(ExeConfig.Debug)+',', str)
    str = re.sub(r'console=.*,', 'console='+boolToStr(ExeConfig.Console)+',', str)
    str = re.sub(r'icon=\'.*\'', 'icon=\''+ExeConfig.Ico+'\'', str)

    with open('start.spec', 'w+', encoding="utf-8") as f:
        f.write(str)
    os.system("pyinstaller start.spec")
    import os


    def copy_dir(source, target):
        if not (os.path.isdir(source) and os.path.isdir(target)):
            return
        for a in os.walk(source):
            for d in a[1]:
                dir_path = os.path.join(a[0].replace(source, target), d)
                if not os.path.isdir(dir_path):
                    os.makedirs(dir_path)
            for f in a[2]:
                dep_path = os.path.join(a[0], f)
                arr_path = os.path.join(a[0].replace(source, target), f)
                shutil.copy(dep_path, arr_path)
    try:
        copy_dir(
            './dist/ALIDE【原石计划Mod开发IDE】',
            os.path.join(
                os.path.expanduser('~'),
                'Documents\TetraProject\Packages\ALIDE【原石计划Mod开发IDE】'))
    except Exception as e:print(e)
    packageJsonPath = os.path.join(
                os.path.expanduser('~'),
                'Documents\TetraProject\Packages\ALIDE【原石计划Mod开发IDE】\PackageInfo.json')
    import json
    with open(packageJsonPath, 'r', encoding="utf-8-sig") as f:
        buildUI_Dict = json.loads(f.read())
    buildUI_Dict['description']=ExeConfig.ModContent
    with open(packageJsonPath, 'w', encoding="utf-8") as f:
        f.write(json.dumps(buildUI_Dict,
                           ensure_ascii=False,
                           indent=4,
                           separators=(',', ':')))