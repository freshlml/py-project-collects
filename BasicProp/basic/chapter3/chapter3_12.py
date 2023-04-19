
# True and False literals
print(type(True))  # <class 'bool'>, True被解析成 class bool 类型的实例对象
print(type(False))  # <class 'bool'>, False被解析成 class bool 类型的实例对象

# class bool is immutable
a = True
b = True
print(a is b)  # True, 程序中所有的True均为同一个对象


# 对象真值测试, __bool__协议方法, __len__协议方法
#     if obj:  # 触发 __bool__ or __len__ 协议方法: return __bool__() or return __len__() > 0
#
# class int 类型 __bool__ 协议方法: return 整数值 != 0
if 1:
    print("整数值 != 0")

# class float 类型 __bool__ 协议方法: return 浮点数 != 0.0
if 0.1:
    print("浮点数 != 0.0")

# class str 类型 __len__ 协议方法
if "some":
    print("non-empty")

# None is false
if None:
    print("None is true")
else:
    print("None is false")


print("-------1-------")


# 逻辑运算， and、or、not
# a and b:  测试对象a，如果对象a为False返回对象a(短路)[注意不是返回False对象]
lo = 0
ret = lo and '1'
print(ret)        # 0
print(ret is lo)  # True
print(type(ret))  # <class 'int'>

# a and b: 测试对象a，如果对象a为True，返回对象b
lo = ''
ret = 1 and lo
print(ret)        # ''
print(ret is lo)  # True
print(type(ret))  # <class 'str'>

# a or b: 测试对象a，如果对象a为True，返回对象a(短路)[注意不是返回True对象]
lo = 1
ret = lo or ''
print(ret)        # 1
print(ret is lo)  # True
print(type(ret))  # <class 'int'>

# a or b: 测试对象a，如果对象a为False，返回对象b
lo = ' '
ret = 0 or lo
print(ret)        # ' '
print(ret is lo)  # True
print(type(ret))  # <class 'str'>

# 虽然是逻辑运算的规则不同(一般的逻辑运算返回true or false), 但与真值表一致
lo = 1
if lo or '':
    print("真值测试")


