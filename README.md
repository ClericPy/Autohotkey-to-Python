

## this repository is abandoned, please using the better choice https://github.com/spyoungtech/ahk



> Not compatible with python2

##Demo:

```python
# coding:utf-8
from ahk import getahk,goahk
goahk(u'''msgbox Hello World
msgbox From Pyld
pyld=12345
''')
print(getahk(u'pyld'))
```
getahk not support 64-bit autohotkey.dll
