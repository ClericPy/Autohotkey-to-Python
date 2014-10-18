详细内容

0. 所有有关autohotkey与python通过ahk.dll连接，以及ahk入门的东西都在压缩包里了


1. 如果你用的python3，python to autohotkey里的文件可以直接用，如果是python2.x，那请不要理会里面的*.py，删掉，只看zip压缩包里的，那是python2的测试代码与dll动态链接库


2. chm文件是官方中文文档，查找某个函数或语句的用法会用到，熟练以后经常要看，document文件夹里的都是比较基础的教程，稍微看一下就可以了

3. 这些教程没提到区域找图功能，这是主要用来判断鼠标点击的时机的东西，文档里索引ImageSearch有用法，也可以看我自己用的代码

示范代码

oop
{
Sleep 200
ImageSearch, xxxx, yyyy,0, 0,880,620, 4.bmp
if ErrorLevel
	continue
else
    break
	}
Click %xxxx%,%yyyy%

最后click那句看需要

4. ScriptSetting那个文件放到安装目录里，可以修改一些东西。编辑器可以用文本文档，最好用scite。

5. 祝你使用愉快