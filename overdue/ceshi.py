#! python2
# -*- coding: utf-8 -*-
from ctypes import *
import time

if __name__ == '__main__':
    ahk = cdll.AutoHotkey  # load AutoHotkey
    ahk.ahktextdll("")  # start script in persistent mode (wait for action)
    # 线程控制，判断线程是否加载
    # while not ahk.ahkReady(): #Wait for AutoHotkey.dll to start
    # time.sleep(0.01)
    # ahk.addScript(u"a=1\nb=2")

    # 从AutoHotkey中读取参数

    # AhkThread.ahkgetvar.a
    #string1 = cast(ahk.ahkgetvar(u"a",0),c_wchar_p).value
    #string2 = cast(ahk.ahkgetvar(u"b",0),c_wchar_p).value
    # 运行MsgBox窗口
    #ahk.ahkExec(u"MsgBox " + string1 + u"\nMsgBox " + string2)

    ##ahk = cdll.AutoHotkey
    # ahk.ahktextdll("")
    # 调用函数
    # time.sleep(0.1)
    #ahk.addScript(u"Func(a=\"\",b=\"\"){\nMsgBox % a \"`n\" b\n}")
    #ahk.ahkFunction(u"func",u"test1", u"test2")

# 调用函数
    string1 = u'Hello'
    string2 = u'World'

    while not ahk.ahkReady():
        time.sleep(0.01)
    ahk.addScript(u"Func(a=\"\",b=\"\"){\nreturn a \" \" b \"!\"\n}")
    string = cast(ahk.ahkFunction(u"func", string1, string2), c_wchar_p).value
    ahk.ahkExec(u"MsgBox " + string)

    while not ahk.ahkReady():  # Wait for AutoHotkey.dll to start
        time.sleep(0.01)
    ahk.addScript(u"a=1\nb=2")

    string1 = cast(ahk.ahkgetvar(u"a", 0), c_wchar_p).value
    string2 = cast(ahk.ahkgetvar(u"b", 0), c_wchar_p).value
    ahk.ahkExec("MsgBox " + string1 + "\nMsgBox " + string2)
