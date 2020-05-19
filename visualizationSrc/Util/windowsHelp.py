#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   windowsHelp.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/20 6:08
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
__all__ = ["openTetraProject"]
import win32gui,win32con,re

class cWindow:
    def __init__(self):
        self._hwnd = None
    def SetAsForegroundWindow(self):
        self.hide_always_on_top_windows()
        win32gui.SetForegroundWindow(self._hwnd)
    def Maximize(self):
        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)
    def _window_enum_callback(self, hwnd, regex):
        if self._hwnd is None and re.match(regex, str(win32gui.GetWindowText(hwnd))) is not None:
            self._hwnd = hwnd
    def find_window_regex(self, regex):
        self._hwnd = None
        win32gui.EnumWindows(self._window_enum_callback, regex)
    def hide_always_on_top_windows(self):
        win32gui.EnumWindows(self._window_enum_callback_hide, None)
    def _window_enum_callback_hide(self, hwnd, unused):
        if hwnd != self._hwnd:
            if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) & win32con.WS_EX_TOPMOST:
                className = win32gui.GetClassName(hwnd)
                if not (className == 'Button' or className == 'Shell_TrayWnd'):
                    win32gui.ShowWindow(hwnd, win32con.SW_FORCEMINIMIZE)
def openTetraProject():
    if True:
        try:
            cW = cWindow()
            cW.find_window_regex("TetraProject")
            cW.Maximize()
            cW.SetAsForegroundWindow()
        except Exception as e:
            print(e)