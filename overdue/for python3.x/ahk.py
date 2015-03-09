# -*- coding: utf-8 -*-
import ctypes
import time

ahk1 = ctypes.cdll.AutoHotkey  # load AutoHotkey
ahk1.ahktextdll("")
while not ahk1.ahkReady():
    time.sleep(0.01)
goahk = ahk1.ahkExec


def getahk(aa):
    aa = str(aa)
    val = ctypes.cast(ahk1.ahkgetvar(aa, 0), ctypes.c_wchar_p).value
    return val
