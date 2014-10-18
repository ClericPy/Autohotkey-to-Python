# -*- coding: utf-8 -*-
from ctypes import *
import time

ahk(r'''
MsgBox haha
	''')










def jianqieban(ss):
    mingling='clipboard='+str(ss)
    ahk(mingling)

def ahk(aa):
    ahk1 = cdll.AutoHotkey #load AutoHotkey
    ahk1.ahktextdll("") #start script in persistent mode (wait for action)
    while not ahk1.ahkReady(): 
        time.sleep(0.01)
    ahk1.ahkExec(aa)













# if __name__ == '__main__':
#     ahk = cdll.AutoHotkey #load AutoHotkey
#     ahk.ahktextdll("") #start script in persistent mode (wait for action)
    ##线程控制，判断线程是否加载
    #while not ahk.ahkReady(): #Wait for AutoHotkey.dll to start
        #time.sleep(0.01)
    #ahk.addScript(u"a=1\nb=2")

    ##从AutoHotkey中读取参数

            ##AhkThread.ahkgetvar.a
    #string1 = cast(ahk.ahkgetvar(u"a",0),c_wchar_p).value
    #string2 = cast(ahk.ahkgetvar(u"b",0),c_wchar_p).value
    ##运行MsgBox窗口
    #ahk.ahkExec(u"MsgBox " + string1 + u"\nMsgBox " + string2)

    ##ahk = cdll.AutoHotkey
    ##ahk.ahktextdll("")
    ##调用函数
    #time.sleep(0.1)
    #ahk.addScript("Func(a=\"\",b=\"\"){\nMsgBox % a \"`n\" b\n}")
    #ahk.ahkFunction("func","test1", "test2")

#把python里的参数给AHK
    # string1 = 'Hello' 
    # string2 = 'World'

    # while not ahk.ahkReady(): 
    #     time.sleep(0.01) 
    # ahk.addScript("Func(a=\"\",b=\"\"){\nreturn a \" \" b \"!\"\n}") 
    # string = cast( ahk.ahkFunction("func",string1, string2), c_wchar_p).value 
    # ahk.ahkExec("MsgBox " + string) 

    # while not ahk.ahkReady(): #Wait for AutoHotkey.dll to start
    #     time.sleep(0.01)
    # ahk.addScript("a=1\nb=2")

    # string1 = cast(ahk.ahkgetvar("a",0),c_wchar_p).value
    # string2 = cast(ahk.ahkgetvar("b",0),c_wchar_p).value

    # while not ahk.ahkReady(): 
    #     time.sleep(0.01)    
    # ss='哈哈哈哈啊'
    # mingling='''clipboard='''
    # ahk.ahkExec(mingling+ss)













