# -*- coding: utf-8 -*-
import ctypes
import time

ahk1 = ctypes.cdll.AutoHotkey  # load AutoHotkey
ahk1.ahktextdll("")
while not ahk1.ahkReady():
    time.sleep(0.01)
goahk = ahk1.ahkExec

def getahkval(aa):
    aa = str(aa)
    val = ctypes.cast(ahk.ahkgetvar(aa, 0), ctypes.c_wchar_p).value
    return val

def ahk(aa):
    aa = str(aa)
    goahk(aa)


def msgbox(aa):
    aa = str(aa)
    goahk('msgbox ' + aa)


def send(aa):
    aa = str(aa)
    goahk('send ' + aa)


def sleep(aa):
    aa = str(aa)
    goahk('sleep ' + aa)


def click(aa):
    aa = str(aa)
    goahk('click ' + aa)


def zhaotu(a, b, c, d, e):
    goahk('aa=' + str(a))
    goahk('bb=' + str(b))
    goahk('cc=' + str(c))
    goahk('dd=' + str(d))
    goahk('ee=' + str(e))

    mingling = r'''
    Loop
    {
    Sleep 200
    ImageSearch,x,y,%aa%,%bb%,%cc%,%dd%,%ee%.png
    if ErrorLevel
        continue
    else
        break
        }
    '''
    goahk(mingling)

    xx = ctypes.cast(ahk.ahkgetvar("x", 0), ctypes.c_wchar_p).value
    yy = ctypes.cast(ahk.ahkgetvar("y", 0), ctypes.c_wchar_p).value

    zb = xx + ',' + yy
    return zb


def dianji(a, b, c, d, e):
    goahk('aa=' + str(a))
    goahk('bb=' + str(b))
    goahk('cc=' + str(c))
    goahk('dd=' + str(d))
    goahk('ee=' + str(e))

    mingling = r'''
    Loop
    {
    Sleep 200
    ImageSearch,x,y,%aa%,%bb%,%cc%,%dd%,%ee%.png
    if ErrorLevel
        continue
    else
        break
        }
    Click %x%,%y%
    '''
    goahk(mingling)
