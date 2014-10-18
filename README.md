
#Introduce:

### Choose the version and download : 2.x or 3.x
### Move the two files to the path "Lib\site-packages"
### PS: You can do some extra things by downloading the "overdue" files
### Always make sure that: do not forget the 'u' before strings.

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

# 选择对应版本并将文件下载到"Lib\site-packages"路径中，用法如上，也可以参考过期文件夹中的内容做一些额外的事情