# python语言
Python 是一种易于学习又功能强大的编程语言。它提供了高效的*高级数据结构*，还能简单有效地*面向对象编程*。
Python 优雅的语法和*动态类型*，以及*解释型语言*的本质，使它成为多数平台上写脚本和快速开发应用的理想语言。

## 安装Python
可以在不同操作系统平台同时安装多个版本的Python。@link py_install.md

## Python解释器
Python 解释器易于扩展，可以使用 C 或 C++（或者其他可以通过 C 调用的语言）扩展新的功能和数据类型。  

Python解释器的默认实现使用C语言编写，即CPython。其他实现如JPython等。  
### python交互命令行
1. 在系统交互窗口(Cmd窗口,Shell窗口)输入python命令，python命令将调起python解释器，进入交互式命令行。
    ```
   C:\Users\DELL>python
    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
   ```
2. 输入python代码，按回车输入的代码立即被执行
    ```
   >>> print('hello 中')       ##输入python代码
    hello 中                    ##按回车，上述代码执行
    >>> var = 1                 ##输入python代码，回车
    >>> var                     ##输入python代码
    1                           ##回车
    >>>
   ```
3. 输入多行语句。交互命令行中python代码只能一句一句执行，即一句先执行后一句才能执行，多行语句的场景则只适用于复合语句，复合语句的最后需要空行
    ```
   >>> for x in '123':
    ...   print(x)
    ...
    1
    2
    3
    >>>
   ```
### python -m命令语法
```shell script
# 1.将当前工作目录添加到sys.path
# 2.在sys.path中搜索
D:\pyProjects\BasicProp\basic> python -m package_name/module_name

# 搜索package, 运行package下__main__.py
D:\pyProjects\BasicProp\basic> python -m package_name

# 搜索module, 以__main__运行
D:\pyProjects\BasicProp\basic> python -m module_name

# 搜索module, 以__main__运行
D:\pyProjects\BasicProp\basic> python -m package.module
```
### python script
```shell script
# 1.py文件路径可以是绝对路径，或者相对路径，相对于当前工作目录
# 2.将py文件所在目录的绝对路径添加到sys.path
D:\pyProjects\BasicProp\basic> python ./chapter5/test.py

# 1.package路径可以是绝对路径，或者相对路径，相对于当前工作目录
# 2.执行package下__main__.py, 将./basic/chapter5添加到sys.path
D:\pyProjects\BasicProp> python ./basic/chapter5

```

# 特性
- 开发效率：
    相对于 C、C++、java（编译型，静态类型）的编码、编译、测试、再编译这些开发流程。
    解释型，动态类型的Python，使用Python 解释器直接运行源码，无单独的编译阶段。
- 交付：
    可直接交付源代码。
    - 优化工具
        Psyco实施编译器，PVM增强工具，在程序运行时将部分字节码转化为真正的二进制机器码，可以有效的提高运行效率
        Shedskin C++转换器...
    - 冻结二进制文件
        将源代码编译成字节码，和PVM以及程序运行需要的所有支持文件打包。形成一个可执行的文件，如windows上的exe,linux上的可执行二进制文件。工具py2exe、PyInstaller
- 可移植性：
    windows上安装的python解释器将源码编译成字节码，字节码转换成windows平台的二进制机器码。
    同样，mac上安装的python解释器将源码编译成字节码，字节码转换成mac平台的二进制机器码。
- 库：
    标准库, 第三方库。
- 集成：
    Python中编写 C 或者 C++ 扩展。
- 自动内存管理：
    对象内存分配与回收
- 面向对象，函数式编程

# Python的应用领域
- 脚本语言：
    将python用作脚本语言，比脚本语言有更强的可读性和一致性
- 高级语言：
    将Python作为高级语言使用完全没问题
- 系统编程：
    Python集成了操作系统服务的内置接口。标准库绑定了POSIX以及其他操作系统工具: 环境变量，文件，套接字，管道，进程，线程，正则表达式，命令行参数，标准流接口，Shell命令启动器，文件操作
- GUI：
    TKinter的标准面向对象接口Tk GUI API，可以导入其他的GUI库
- Internet：
    Internet模块，Web应用库: Django,TurboGears,web2py,Pylons,Zope,WebWare
- 组件集成：
    C、C++库集成等
- 扩展语言：
    Python 也可用于可定制化软件中的扩展程序语言。
- 数据库接口：
    主流数据库，MySql,Oracle,PostgreSql...
- 数值计算 && 科学计算：
    NumPy, SciPy等库，完美替代Matlab
- 游戏、图像、人工智能、机器人等领域


