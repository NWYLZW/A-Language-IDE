#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File           :   main.py
@License        :   (C)Copyright 2020
@Modify Time    :   2020/5/25 6:15
@Author         :   Superme
@Contact        :   yijie4188@gmail.com
@Desciption     :   
'''
import _thread
import socket
from flask import Flask, request, abort


class ClientMain:
    def __init__(self):
        self.port = None
        self.runAfterFun = lambda : print("未设置启动回调")
        pass
    def startClient(self):
        try:
            _thread.start_new_thread(self._initApp, ())
        except:
            print("Error: 无法启动线程")
    def setClicentRunAfter(self,fun):
        self.runAfterFun = fun

    def _initApp(self):
        self.app = Flask(__name__)
        def isUseLocalIPort(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect(("localhost", port))
                return True
            except OSError:
                return False
            finally:
                s.close()
        for port in range(60000,655535):
            if isUseLocalIPort(port):continue
            self.port = port;break
        @self.app.route("/api/acceptMessage",methods=["POST"])
        def acceptMessage():
            return self.__acceptMessage(request.json)
        self.runAfterFun()
        self.startClientApp()
    def setAcceptMessage(self, fun):
        self.acceptMessage = fun
        pass
    def __acceptMessage(self, json):
        if json.get("api_key",None) \
                and json.get("api_key")=="^&8UGYUui4596sad":
            self.acceptMessage(json)
        abort(403)
    def startClientApp(self):
        self.app.run(
            host="0.0.0.0",
            port=self.port,
            debug=False,
        )
