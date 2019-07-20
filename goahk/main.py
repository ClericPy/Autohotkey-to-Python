#! python3
import ctypes
import time
import sys
import pathlib

dll_file_path = pathlib.Path(__file__).parent / f'AutoHotkey{sys.hash_info.width}.dll'
ahk_instance = ctypes.cdll.LoadLibrary(str(dll_file_path))

ahk_instance.ahktextdll("")

while not ahk_instance.ahkReady():
    time.sleep(0.1)


def goahk(code: str):
    """run source code with autohotkey."""
    return ahk_instance.ahkExec(code)


def getahk(var_name: str):
    """get var value from ahk script by var name"""
    result = ahk_instance.ahkgetvar(var_name, 0)
    result = ctypes.cast(result, ctypes.c_wchar_p)
    return result.value


__all__ = ['goahk', 'getahk']


def test():
    goahk(u'''msgbox Hello World;
var_name=sss
    ''')
    print(getahk('var_name'), flush=1)


if __name__ == "__main__":
    test()
