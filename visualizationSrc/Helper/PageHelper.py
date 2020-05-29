#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   PageHelper.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/24 19:37
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from abc import abstractmethod
from math import ceil

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout

class PageHelper:
    def __init__(self, UI, PageItemNum):
        self._UI = UI
        self._PageItemNum = PageItemNum
        self._currentPageNum = 0
        self._isFilter = False
        self._tempHL_List = []
        self._numBTN_List = []

        self._initClick()
    def _initClick(self):
        def leftClick(evt):
            if self._currentPageNum>0:
                self.toPage(self._currentPageNum-1)
        self._UI.leftBTN.clicked.connect(leftClick)
        def rightClick(evt):
            if self._currentPageNum<self.pageCount-1:
                self.toPage(self._currentPageNum+1)
        self._UI.rightBTN.clicked.connect(rightClick)
        def toFirst(evt):
            if self._currentPageNum!=0:
                self.toPage(0)
        self._UI.toFirstBtn.clicked.connect(toFirst)
    def _initScrollArea(self, scrollArea):
        widget = QWidget()
        self._VL = QVBoxLayout()
        self._VL.setContentsMargins(0,0,0,0)
        self._scrollArea = scrollArea
        self._scrollArea.setWidget(widget)
        widget.setLayout(self._VL)

    @abstractmethod
    def _generatePage(self,newDataList):
        '''
        生成每个页面的布局
        :return:
        '''
        pass
    @abstractmethod
    def dataList(self):
        if not self._isFilter:
            return []
        else:
            return []
    @property
    def _currentPageDataList(self):
        # 生成卡牌列表
        oldDataList = self.dataList()
        endValue = (self._currentPageNum + 1) * self._PageItemNum
        if endValue>len(oldDataList):endValue=len(oldDataList)
        newDataList = oldDataList[self._currentPageNum * self._PageItemNum:endValue]
        return newDataList

    @property
    def pageCount(self):
        return ceil((len(self.dataList()) / self._PageItemNum))

    def _clearScroll(self):
        while len(self._tempHL_List)>0:
            tempHL = self._tempHL_List[0]           # type: QHBoxLayout
            self._tempHL_List.remove(tempHL)
            while tempHL.count()>0:
                child = tempHL.takeAt(0)
                if child.widget():
                    child.widget().setParent(None)
                    del child
            tempHL.deleteLater();del tempHL
    def _refreshBtnList(self):
        while len(self._numBTN_List)>0:
            numBTN = self._numBTN_List[0]           # type: QPushButton
            self._numBTN_List.remove(numBTN)
            numBTN.setParent(None)
            numBTN.deleteLater();del numBTN
        # 生成按钮列表
        font = QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(12)
        count = 0;continueFlag = False
        start = self._currentPageNum
        if self.pageCount - start<5:
            start = self.pageCount - 5
        for i in range(start, self.pageCount):
            if i < 0 or i == self.pageCount:continue
            if continueFlag and i != self.pageCount-1:continue
            count += 1
            numBTN = QPushButton(None)
            self._UI.pageBTN_List.insertWidget(count, numBTN)
            self._numBTN_List.append(numBTN)
            numBTN.setMinimumSize(QtCore.QSize(28, 28));numBTN.setMaximumSize(QtCore.QSize(28, 28))
            numBTN.setFont(font)

            if count == 4 and self.pageCount-1-start>5:
                numBTN.setText("...")
                continueFlag=True;continue
            else:
                numBTN.setText(str(i + 1))
            def numBTNClick(index):
                def __numBTNClick():
                    self.toPage(index)
                return __numBTNClick
            numBTN.clicked.connect(numBTNClick(i))
            numBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            if i == self._currentPageNum:
                numBTN.setStyleSheet("background-color:rgb(69, 138, 202);")
            else:
                numBTN.setStyleSheet("")

        # 刷新指针状态
        if self._currentPageNum<=0: self._UI.leftBTN.setCursor(QCursor(QtCore.Qt.ForbiddenCursor))
        else:self._UI.leftBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        if self._currentPageNum>=self.pageCount-1: self._UI.rightBTN.setCursor(QCursor(QtCore.Qt.ForbiddenCursor))
        else:self._UI.rightBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    def _refreshEle(self):
        self._clearScroll()
        self._generatePage(self._currentPageDataList)
        self._refreshBtnList()

    def filter(self,filterStr):
        self.filterStr = filterStr
        if self.filterStr == "":
            self._isFilter = False
        else:
            self._isFilter = True
        self._refreshEle()
    def toPage(self,pageNum:int=0):
        if pageNum<0: return
        self._currentPageNum = pageNum
        self._refreshEle()