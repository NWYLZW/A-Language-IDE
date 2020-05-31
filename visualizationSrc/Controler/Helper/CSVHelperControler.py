#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   CSVHelperControler.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/17 7:09
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import csv
from abc import abstractmethod, ABCMeta

class CSVHelperControler(object):
    __metaclass__ = ABCMeta
    def __init__(self,csvName=None):
        from ...Util.frozenDir import currentProPath
        proHome = currentProPath()
        self.csvFileName = proHome+"/Database/"+csvName+".csv"
        self._rowList = []
        self._readFromFile()
        self._setRowDictDefaultValue()
        pass
    def _getRowList(self)->list:
        return self._rowList
    def _readFromFile(self):
        with open(self.csvFileName, mode='r+', encoding="UTF-8-sig") as f:
            reader = csv.DictReader(f)
            self.fieldnames = reader.fieldnames
            for row in reader:
                if row['id'] != '': self._rowList.append(row)
    def _refreshFile(self):
        with open(self.csvFileName, 'w', encoding="UTF-8-sig", newline='') as f:
            writer = csv.DictWriter(f, self.fieldnames)
            writer.writeheader()
            for row in self._rowList:
                if row != None: writer.writerow(row)
    @abstractmethod
    def _setRowDictDefaultValue(self):
        '''
        设置单元行内每个单元格的默认值
        :return:
        '''
        self.DefaultValue = {}
        pass

    def _getRowByfieldName(self, fieldName, fieldValue) -> dict:
        index = self._getRowIndexByfieldName(fieldName, fieldValue)
        if index == -1: return {}
        return self._rowList[index]
    def _getRowIndexByfieldName(self, fieldName, fieldValue) -> int:
        if fieldValue == None or not(fieldName in self.fieldnames): return -1
        for index in range(len(self._rowList)):
            if str(self._rowList[index][fieldName]) == str(fieldValue):
                return index
        return -1
    def _delRowByfieldName(self, fieldName, fieldValue):
        index = self._getRowIndexByfieldName(fieldName, fieldValue)
        if index == -1: return False
        del self._rowList[index]
        self._refreshFile()
        return True
    def _updataRowByfieldName(self, fieldName, newRowDict):
        oldDict = self._getRowByfieldName(fieldName, newRowDict.get(fieldName, None))
        if oldDict == None: return False
        for key in oldDict:
            oldDict.update({
                key:newRowDict.get(key,oldDict.get(key))
            })
        self._refreshFile()
        return True
    def _addRow(self, newRowDict) -> dict:
        try:
            for key in newRowDict:
                newRowDict.update({
                    key:newRowDict.get(key,self.DefaultValue.get(key,''))
                })
            # self._refreshFile()
            self._rowList.append(newRowDict)
            self._refreshFile()
            return newRowDict
        except Exception as e:
            from ...Util.LogUtil import log, logLevel
            log.record(logLevel.ERROR, 'CSVHelperControler._addRow', e)
            return {}
