# 安装多个版本 Python
link Vault/markdown/utils/py_install.md

### python 3.7
C:\Users\DELL\AppData\Local\Programs\Python\Python37  
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python37> .\python.exe -V
Python 3.7.3

C:\Users\DELL\AppData\Local\Programs\Python\Python37> .\python.exe -m pip --version
pip 19.0.3 from c:\users\dell\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
```

### python 3.10
C:\Users\DELL\AppData\Local\Programs\Python\Python310  
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python310> .\python.exe -V
Python 3.10.5

C:\Users\DELL\AppData\Local\Programs\Python\Python310> .\python.exe -m pip --version
pip 22.0.4 from C:\Users\DELL\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
```

### 使用 Python37 解释器执行 sys_path_test.py
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python37> .\python.exe D:\pyProjects\BasicProp\basic\chapter5\sys_path_test.py
['D:\\pyProjects\\BasicProp\\basic\\chapter5',                                              # top_level_package(当前 py 文件所在目录)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',                         # 指向当前解释器的标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']          # 指向当前解释器的标准库第三方包路径
sys.prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
```

### 使用 Python310 解释器执行 sys_path_test.py
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python310> .\python.exe D:\pyProjects\BasicProp\basic\chapter5\sys_path_test.py
['D:\\pyProjects\\BasicProp\\basic\\chapter5',                                               # top_level_package(当前 py 文件所在目录)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib',                         # 指向当前解释器的标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']          # 指向当前解释器的标准库第三方包路径
sys.prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
sys.exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
```

# 虚拟环境
使用 python 标准库的 pip 安装第三方包，安装位置：python 安装目录\lib\site-packages。  

注意：不要使用标准库的 pip 安装第三方包，而是对每个项目创建虚拟环境，将项目依赖的第三包安装在各自的虚拟环境中。  

### 创建 venv 虚拟环境
需要 python 3.4 版本以上?   

使用 pycharm 创建项目时，可以指定同时创建 venv 虚拟环境。本质上是使用 python 的 venv module：venv 实践。  

### 使用虚拟环境的 python 解释器执行 sys_path_test.py
```shell script
(venv) PS D:\py-project-collects\BasicProp\venv\Scripts> .\python ..\..\basic\chapter5\sys_path_test.py
['D:\\py-project-collects\\BasicProp\\basic\\chapter5',                          # top_level_package(当前 py 文件所在目录)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',              # 虚拟环境指向的某一个版本 python 的标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37', 
'D:\\py-project-collects\\BasicProp\\venv',                                      # 虚拟环境的根目录
'D:\\py-project-collects\\BasicProp\\venv\\lib\\site-packages']                  # 虚拟环境的 site-packages 目录，即虚拟环境的第三方包路径
sys.prefix = D:\py-project-collects\BasicProp\venv
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = D:\py-project-collects\BasicProp\venv
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
```

### 在 pycharm 中运行
在 settings/Python/Interpreter 中可以配置用于执行 py 文件的 python 解释器，如可以配置使用标准库 python 解释器或者虚拟环境的 python 解释器。  
```shell script
# 将 settings/Python/Interpreter 配置成虚拟环境的 python 解释器后运行 sys_path_test.py
D:\py-project-collects\BasicProp\venv\Scripts\python.exe D:\py-project-collects\BasicProp\basic\chapter5\sys_path_test.py 
['D:\\py-project-collects\\BasicProp\\basic\\chapter5', 
'D:\\py-project-collects\\BasicProp',                    # 项目根目录，pycharm 添加的，生产环境不一定可信...
'C:\\Program Files\\JetBrains\\PyCharm 2025.3.1.1\\plugins\\python-ce\\helpers\\pycharm_display', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37', 
'D:\\py-project-collects\\BasicProp\\venv', 
'D:\\py-project-collects\\BasicProp\\venv\\lib\\site-packages', 
'C:\\Program Files\\JetBrains\\PyCharm 2025.3.1.1\\plugins\\python-ce\\helpers\\pycharm_matplotlib_backend', 
'C:\\Program Files\\JetBrains\\PyCharm 2025.3.1.1\\plugins\\python-ce\\helpers\\pycharm_altair_backend', 
'C:\\Program Files\\JetBrains\\PyCharm 2025.3.1.1\\plugins\\python-ce\\helpers\\pycharm_plotly_backend']
sys.prefix = D:\py-project-collects\BasicProp\venv
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = D:\py-project-collects\BasicProp\venv
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
```

# venv 实践

### 创建虚拟环境
使用 python -m venv my_env 创建 venv 环境，将在当前命令行所在目录下创建一个 my_env 目录。  

虚拟环境目录说明：
```
my_env
  -Include
  -Lib
    -site-packages          # 默认将虚拟环境指向的 python 的标准库下的 site-packages 复制过来，后续安装的第三方依赖放置在此目录
  -Scripts                  # 虚拟环境的 python 解释器，pip 包管理器等
  pyvenv.cfg                # 配置虚拟环境指向的 python
```
更新虚拟环境：python -m venv my_env --upgrade。可以使用版本更高的 python。可直接删除虚拟环境目录（当然，第三方依赖也会被删除）。  

### 激活虚拟环境
```shell script
PS D:\py-project-collects\BasicProp> .\venv\Scripts\activate  # 激活虚拟环境
(venv) PS D:\py-project-collects\BasicProp>                   # 可以看到，命令提示符切换到了 venv 环境
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/python --version    # 虚拟环境 python 解释器版本
# 激活虚拟环境后，即出现 (venv)，无论在哪个目录，可直接使用 python 命令，pip 命令，它将定位到虚拟环境中的 python 和 pip 而不是系统环境变量指向的命令
```

### 退出虚拟环境
```shell script
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/deactivate    # 退出虚拟环境
PS D:\py-project-collects\BasicProp>                                     # 可以看到，退出了虚拟环境
```

### 第三方依赖管理
不要使用标准库的 pip 安装第三方包，而是在虚拟环境中安装。    
```shell script
PS D:\py-project-collects\BasicProp> .\venv\Scripts\activate  # 激活虚拟环境
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip list                   # 列出虚拟环境已安装的第三方依赖
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip show package_name      # 查看
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip install package_name[==版本号]    # 在虚拟环境安装特定版本的依赖
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip install --upgrade package_name   # 更新到最新版
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip uninstall package_name   # 卸载
```
注意，不要使用 ./venv/Scripts/pip install --upgrade pip 这样更新 pip。而是 ./venv/Scripts/python -m pip install --upgrade pip 这样来更新 pip。  

### 第三方依赖的协同
每一个开发环境和线上环境都创建本地的 venv，pyvenv.cfg 中 name 指向相同的 python 版本。  

将第三方依赖写到 requirements.txt 文件之中随代码一起提交给 git。使用命令可以安装 requirements.txt 文件之中的依赖。  

```shell script
(venv) PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip freeze > requirements.txt  # 将第三方依赖写到 requirements.txt 文件

PS D:\py-project-collects\BasicProp> ./venv/Scripts/pip install -r requirements.txt       # 安装 requirements.txt 文件中的依赖
```
