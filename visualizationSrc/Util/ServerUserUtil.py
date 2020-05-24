#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   ServerUserUtil.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/24 5:15
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
__all__ = ["server"]
import requests

from .LogUtil import log, logLevel

class httpUtil:
    def __init__(self, session, parent, childUrl):
        self._session = session
        self.parent = parent
        self._childUrl = childUrl
        self.headersBase = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        }
        pass
    @property
    def serverHost(self):
        return self.parent.serverRoot
    def _postJsonByRoute(self, route, json):
        url = self.serverHost + self._childUrl + route
        try:
            content = self._session.post(url, headers=self.headersBase, json=json, timeout=3)
            return content.json()
        except requests.exceptions.RequestException as e:
            log.record(logLevel.ERROR, 'httpUtil._postJsonByRoute', e)
            return {}
        except Exception as e:
            log.record(logLevel.ERROR, 'httpUtil._postJsonByRoute', e)
            return {}
    def _getJsonByRoute(self, route):
        url = self.serverHost + self._childUrl + route
        try:
            content = self._session.get(url, timeout=3)
            return content.json()
        except requests.exceptions.RequestException as e:
            log.record(logLevel.ERROR, 'httpUtil._postJsonByRoute', e)
            return None
        except Exception as e:
            log.record(logLevel.ERROR, 'httpUtil._getJsonByRoute', e)
            return None

class user(httpUtil):
    def __init__(self, session, parent):
        super().__init__(session, parent, "/user")
        self.isLogin = False
    def login(self, userName, PWD):
        rspJson = self._postJsonByRoute("/login", {
            'userName': userName,
            'PWD': PWD,
        })
        if rspJson == {}: return rspJson
        self.userName = userName
        self.PWD = PWD
        self.isLogin = True
        return rspJson
    def logout(self):
        if not self.isLogin: return {}
        rspJson = self._getJsonByRoute("/logout")
        self.isLogin = False
        return rspJson
    def data(self, userId):
        rspJson = self._postJsonByRoute("/data", {
            'userId': userId,
        })
        return rspJson
    def register(self, userName, PWD):
        if self.isLogin: return {}
        rspJson = self._postJsonByRoute("/register", {
            'userName': userName,
            'PWD': PWD,
        })
        self.userName = userName
        self.PWD = PWD
        return rspJson
class room(httpUtil):
    def __init__(self, session, parent):
        super().__init__(session, parent, "/room")
        self.inRoom = False
        self.roomId = -1
    def list(self):
        rspJson = self._getJsonByRoute("/list")
        if rspJson:
            return rspJson
        else:return []
    def create(self,roomName):
        rspJson = self._postJsonByRoute("/create", {
            'roomName': roomName,
        })
        return rspJson
    def join(self,roomId):
        rspJson = self._postJsonByRoute("/join", {
            'roomId': roomId,
        })
        return rspJson
    def exit(self,roomId):
        rspJson = self._postJsonByRoute("/exit", {
            'roomId': roomId,
        })
        return rspJson
    def sendMessageToOther(self):
        pass

class ServerUtil:
    def __init__(self):
        self._serverAPI_Url = "http://localhost"
        self.headersBase = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        }
        self._session = requests.session()
        self.user = user(self._session, self)
        self.room = room(self._session, self)
    @property
    def serverRoot(self):
        return self._serverAPI_Url
    @serverRoot.setter
    def serverRoot(self, apiUrl):
        self._serverAPI_Url = "http://"+apiUrl
        self.user.logout()
server = ServerUtil()