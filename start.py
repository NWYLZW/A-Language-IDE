#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   start.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 10:14
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   可视化编辑启动文件
'''
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import visualizationSrc.Main as Main

Main.mainWindowStart()