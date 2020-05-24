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
    def __init__(self, session, serverAPI_Url, childUrl):
        self._session = session
        self._childUrl = childUrl
        self._serverAPI_Url = serverAPI_Url
        self.headersBase = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        }
        pass
    def _postJsonToUrl(self, route, json):
        url = self._serverAPI_Url + self._childUrl + route
        content = self._session.post(url, headers=self.headersBase, json=json)
        try:
            return content.json()
        except Exception as e:
            log.record(logLevel.ERROR, 'httpUtil._postJsonToUrl', e)
            return {}

class user(httpUtil):
    def __init__(self, session, serverAPI_Url):
        super().__init__(session, serverAPI_Url, "/user")
        self.isLogin = False
    def login(self, userName, PWD):
        rspJson = self._postJsonToUrl("/login",{
            'userName': userName,
            'PWD': PWD,
        })
        self.userName = userName
        self.PWD = PWD
        self.isLogin = True
        return rspJson
    def logout(self):
        if self.isLogin: return {}
        rspJson = self._session.get(self._serverAPI_Url+self._childUrl+"/logout")
        self.isLogin = False
        return rspJson
    def data(self, userId):
        rspJson = self._postJsonToUrl("/data",{
            'userId': userId,
        })
        return rspJson
    def register(self, userName, PWD):
        if self.isLogin: return {}
        rspJson = self._postJsonToUrl("/register",{
            'userName': userName,
            'PWD': PWD,
        })
        self.userName = userName
        self.PWD = PWD
        return rspJson
class room(httpUtil):
    def __init__(self, session, serverAPI_Url):
        super().__init__(session, serverAPI_Url, "/room")
        self.inRoom = -1
    def list(self):
        rspJson = self._session.get(self._serverAPI_Url+self._childUrl+"/logout")
        return rspJson
    def create(self,roomName):
        rspJson = self._postJsonToUrl("/register",{
            'roomName': roomName,
        })
        self.roomName = roomName
        return rspJson
    def join(self,roomId):
        rspJson = self._postJsonToUrl("/join",{
            'roomId': roomId,
        })
        self.roomId = roomId
        return rspJson
    def exit(self,roomId):
        rspJson = self._postJsonToUrl("/exit",{
            'roomId': roomId,
        })
        return rspJson
    def sendMessageToOther(self):
        pass

class ServerUtil:
    def __init__(self):
        self._serverAPI_Url = "http://localhost:15000"
        self.headersBase = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
        }
        self._session = requests.session()
        self._user = user(self._session,self._serverAPI_Url)
        pass
    @property
    def serverRoot(self):
        return self._serverAPI_Url
    @serverRoot.setter
    def serverRoot(self, apiUrl):
        self._serverAPI_Url = apiUrl
        self._user.logout()
server = ServerUtil()