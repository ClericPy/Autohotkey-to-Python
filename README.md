#Not compatible with x64
#Introduce:

### Choose the version and download : 2.x or 3.x
### Move the two files to the path "\PythonXX\" (not sys.path)
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

# 选择对应版本并将文件下载到"\PythonXX\"根目录下(似乎不只是sys.path),"Lib\site-packages"路径似乎经常出问题，用法如上，也可以参考过期文件夹中的内容做一些额外的事情，打包成exe的时候记得带上dll文件。不支持64位python，郁闷
