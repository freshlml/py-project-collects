# Python程序结构
```
fresh  
  |--xy  # 因为相对导入不能跨过top level packge, so, 此xy是必要的
  |   |--common  
  |   |--utils  
  |   |--a.py  
  |   
  |--XyApplication.py  
  |--test_a.py
```
- 在fresh目录下创建module测试xy包中代码，如test_a.py
- XyApplication.py中使用**绝对导入**导入xy包及其子包内容，XyApplication.py直接运行
- xy包中modules使用**相对导入**导入xy包及其子包内容，这样xy包中内容可任意被其他程序依赖
