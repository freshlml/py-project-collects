# Python程序结构
```
项目名称(任意名称)
  |--src目录(不是package)
      |  
      |--com_fresh_xy(package, 名称唯一)
      |     |--common  
      |     |--utils  
      |     |--a.py  
      |   
      |--XyApplication.py  
  |--test目录
      |--test_a.py
```
- 与src目录平级创建test目录，test中创建module用于测试代码，使用绝对导入(将项目目录路径写入sys.path)
- XyApplication.py中使用**绝对导入**导入com_fresh_xy包及其子包内容，XyApplication.py直接运行
- com_fresh_xy包中modules使用**相对导入**导入com_fresh_xy包及其子包内容，这样com_fresh_xy包中内容可任意被其他程序依赖
- 对com_fresh_xy打包并发布
