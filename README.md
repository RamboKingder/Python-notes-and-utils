# Python 学习笔记

### 学习资源
[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)

[Python Cheatesheet]()

#### 查看python版本
打开cmd输入命令：`python -V` 或者 `python --version`

#### 在终端执行python脚本
先在cmd使用命令进入hello.py所在的文件夹: `cd /d E:\\...`
再在这个文件夹下使用命令： `python hello.py`

#### Python中 if \_\_name__ == "\_\_main__" 的作用
关于`__name__`：它是python模块的内置类属性，用于存储模块的名称，
程序在独立运行时它的值为`__name__`，当程序被调用是该程序的`__name__`属性就是文件名
因此`if __name__ == "__main__"`下的代码只会在程序独立运行时执行，在被其他程序调用时不会执行

所以当前`if __name__ == "__main__"`的作用就是保证当前模块被别的模块调用时，
用于测试写的代码不会被执行。

#### 系统环境变量
将python添加到系统环境变量之后就可以在cmd中的任意一个目录，使用命令`python`来打开python

#### 编码 
默认是`# -*- coding: utf-8 -*-`，也可以手动添加到py文件的第一行

##### 字符串前加u,r
例：u"我是含有中文字符组成的字符串。"

作用：后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

PS：不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行。一般英文字符在使用各种编码下,，基本都可以正常解析, 所以一般不带u。但是中文有事会出现问题，就要想以前在学校上机敲代码时候一样，优盘一插，源码一拷贝，一打开，中文部分全成框框乱码了。。。贼尴尬。。。

字符串前加r，例如r"\n\t"可以抑制转移，将\n\t都输出出来而不是变成了换行

#### 多行语句
如果一条python语句很长，可以用反斜杠 \ 把语句隔开

#### Python3有用的标准库函数
`os.getcwd()`返回当前的的工作目录

`os.system()` 执行系统命令

`glob.glob("*.py")` 会返回指定路径中匹配的文件

`sys.argv` 如果是在cmd执行脚本，例如`python main.py arg1 arg2`那么`sys.argv`会捕获参数

### 将文件夹变成模块
在文件夹下添加一个空的__init__.py文件即可将文件夹变成一个python模块

例如：在widgets文件夹下有__init__.py和mainwindow.py

就可以使用`from widgets.mainwindow import MainWindow`了


## Python程序打包成EXE可执行程序
`pip install pyinstaller`先用pip命令安装这个必要的包

`pyinstaller -F -w test.py`就会在dist目录下生成一个可执行程序

-F 表示生成单一可执行文件 -w 表示程序运行时不显示命令窗口
