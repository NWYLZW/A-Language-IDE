#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CardControler.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/11 4:34
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import os
import win32com
from win32com.client import Dispatch

# 进程可见，False是它后台
from visualizationSrc.Bean.CardBean import Card

Visible = False

def excel_open(filePath, sheetName, fun, VBA=""):
    xlApp = win32com.client.DispatchEx("Excel.Application")
    xlApp.Visible = Visible
    xlApp.DisplayAlerts = 0
    try:
        xlBook = xlApp.Workbooks.Open(filePath,False)
        sht = xlBook.Worksheets(sheetName)
        fun(sht)
        print("WRITE FINISHED")
        xlBook.Close(True)
        if VBA !="":
            useVBA(xlApp, filePath, VBA)
    except Exception as e:
        print(e)
    finally:
        xlApp.Quit()
def useVBA(xlApp, filePath, VBA):
    xlBook = xlApp.Workbooks.Open(filePath,False)
    xlBook.Application.Run(VBA)
    xlBook.Close(True)

current_path = os.path.abspath(__file__)
DatabaseXlsPath = (os.path.dirname(current_path)) + '/' + '../../Database/Database.xls'

if __name__ == '__main__':
    filePath = DatabaseXlsPath
    c = Card(
        id=10001, displayName="转运咒语", price=100, energyReq=0,
        range=0,
        description="传送至灰雾之上1个回合",
        code="LoadLevel:get_currentLevelId:;\nLog:get_currentLevelId:;",
        story0="“福生玄黄仙尊。”\n“福生玄黄天君。”\n“福生玄黄上帝。”\n“福生玄黄天尊。”")
    def __insertCard(sht):
        preCell = None
        for i in range(1,sht.usedrange.rows.count):
            cell = sht.Cells(i+1, 1)
            if cell.Value == None:
                if i == 1: preId = 10000
                else: preId = preCell.Value
                c.id = preId + 1
                t = c.toTuple()
                for j in range(t.__len__()):
                    if t[j] != "":sht.Cells(i + 1, j+1).Value = t[j]
                break
            preCell = cell
    excel_open(filePath, "Card", __insertCard, "CsvExportBook")