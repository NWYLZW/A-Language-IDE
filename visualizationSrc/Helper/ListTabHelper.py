#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   ListTabHelper.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/27 17:27
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ..qtUI.helpUI.ListTab import ListTabItemModel
class ListTabWidget_ListItem(QWidget, ListTabItemModel.Ui_listItem):
    def __init__(self,parent=None,LTW=None):
        super().__init__(parent)
        self.LTW = LTW
        # 设置背景色
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.initClick()
    def deleteLater(self) -> None:
        self._widgetX.deleteLater()
        super().deleteLater()
    def setWidget(self,widget:QWidget):
        self._widgetX = widget
    def getWidget(self):
        return self._widgetX
    def refreshUI(self,
                  title:str="",
                  content:str="",
                  icoImage=None,
                  isShowClose:bool=None,):
        if title != "":
            self.title.setToolTip(title)
            if len(title) > 10: title = title[:4]+'..'+title[-4:]
            self.title.setText(title)
        if content != "":
            self.content.setToolTip(content)
            if len(content) > 10: content = content[:4]+'..'+content[-4:]
            self.content.setText(content)
        if icoImage:
            self.ico.setPixmap(icoImage.scaled(32,32))
            self.ico.setStyleSheet("")
        if not isShowClose:
            self.removeBTN.hide()
    def initClick(self):
        def removeMy():
            if not self.LTW: return
            self.LTW.removeWidgetTab(self.LTW.listItemWidgetIndex(self))
        self.removeBTN.clicked.connect(removeMy)

from ..qtUI.helpUI.ListTab import ListTab
class ListTabHelper(QWidget, ListTab.Ui_Form):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.__initData()
        self._initScrollArea()

    def __initData(self):
        self._currentIndex = -1
        self._removeWidgetBefore = lambda : None
        self._removeWidgetAfter = lambda : None
        self._l_itemList = []
    def _initScrollArea(self):
        self._VL = QVBoxLayout()
        self._VL.setSpacing(0)
        self._VL.setContentsMargins(0,0,0,0)
        self.tabsScrollAreaWidget.setLayout(self._VL)
    def addWidgetTab(self,widget:QWidget=None,
                      title:str="Tab_",
                      content:str="",
                      icoImage=None,
                      isShowClose:bool=None,
                     ):
        l_item = ListTabWidget_ListItem(self,self)
        l_item.refreshUI(
            title=title,
            content=content,
            icoImage=icoImage,
            isShowClose=isShowClose,)
        l_item.setWidget(widget)

        def changeTab(evt):
            if evt.buttons() == Qt.LeftButton:
                self.setCurrentIndex(self.listItemWidgetIndex(l_item))
        l_item.mousePressEvent = changeTab

        self._VL.addWidget(l_item)
        self._l_itemList.append(l_item)
        self.tabsScrollAreaWidget.setMaximumHeight(50*len(self._l_itemList))
        return len(self._l_itemList)-1

    def currentTabChangeBefore(self):
        pass
    def currentTabChangeAfter(self):
        pass
    def setCurrentIndex(self,index):
        if index >= 0 and index < len(self._l_itemList):
            self.currentTabChangeBefore()

            if self._currentIndex != -1:
                currentWidgetItem = self.widgetListItem(self._currentIndex)
                currentWidgetItem.setStyleSheet(
                    "#"+currentWidgetItem.objectName()+"{background-color: rgb(255, 255, 255);}"
                    "#"+currentWidgetItem.objectName()+":hover{background-color: rgb(229, 229, 229);}"
                )
                currentWidget = currentWidgetItem.getWidget()
                currentWidget.hide()
                currentWidget.setParent(None)
                self.mainContent.removeWidget(currentWidget)

            self._currentIndex = index
            wantToWidgetItem = self.widgetListItem(index)
            wantToWidget = wantToWidgetItem.getWidget()
            wantToWidgetItem.setStyleSheet(
                "#"+wantToWidgetItem.objectName()+"{background-color: rgb(229, 229, 229);}"
            )
            self.mainContent.addWidget(wantToWidget)
            wantToWidget.setHidden(False)

            self.currentTabChangeAfter()
            return self._currentIndex
        else: return -1

    def currentWidget(self):
        return self.widgetListItem(self._currentIndex)
    def widgetListItem(self,index)->ListTabWidget_ListItem:
        if index >= 0 and index < len(self._l_itemList):
            return self._l_itemList[index]
        else: return None
    def widgetTab(self,index)->QWidget:
        return self.widgetListItem(index).getWidget()
    def widgetIndex(self,widget)->int:
        if widget:
            for index in range(len(self._l_itemList)):
                if self.widgetListItem(index).getWidget() == widget:
                    return index
        return -1
    def listItemWidgetIndex(self, listItemWidget)->int:
        if listItemWidget:
            return self._l_itemList.index(listItemWidget)
        return -1

    def removeWidgetBefore(self):
        pass
    def removeWidgetAfter(self):
        pass
    def removeWidgetTab(self,index):
        if index >= 0 and index < len(self._l_itemList):
            self.removeWidgetBefore()
            if index == self._currentIndex:
                self.setCurrentIndex(0)

            l_item = self._l_itemList[index]    # type: ListTabWidget_ListItem
            self._l_itemList.remove(l_item)
            self._VL.removeWidget(l_item)
            l_item.setParent(None)
            l_item.deleteLater()
            del l_item

            self.tabsScrollAreaWidget.setMaximumHeight(50*len(self._l_itemList))
            self.removeWidgetAfter()
            return True
        else: return False
