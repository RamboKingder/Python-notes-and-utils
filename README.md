# Python 学习笔记

### 学习资源
[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)

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

#### 多行语句
如果一条python语句很长，可以哟个反斜杠 \ 把语句隔开

#### Python3有用的标准库函数
`os.getcwd()`返回当前的的工作目录

`os.system()` 执行系统命令

`glob.glob("*.py")` 会返回指定路径中匹配的文件

`sys.argv` 如果是在cmd执行脚本，例如`python main.py arg1 arg2`那么`sys.argv`会捕获参数

## Python程序打包成EXE可执行程序
`pip install pyinstaller`先用pip命令安装这个必要的包

`pyinstaller -F -w test.py`就会在dist目录下生成一个可执行程序

-F 表示生成单一可执行文件 -w 表示程序运行时不显示命令窗口

![](/images/pyinstaller.PNG)

