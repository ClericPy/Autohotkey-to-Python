import ctypes
import time
import sys
if sys.version.startswith('2'):
    str1 = unicode
elif sys.version.startswith('3'):
    str1 = str
ahk1 = ctypes.cdll.AutoHotkey  # load AutoHotkey
ahk1.ahktextdll("")
while not ahk1.ahkReady():
    time.sleep(0.01)
goahk = ahk1.ahkExec


def getahk(aa):
    aa = str(aa)
    val = ctypes.cast(ahk1.ahkgetvar(aa, 0), ctypes.c_wchar_p).value
    return val
