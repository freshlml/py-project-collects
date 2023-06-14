# 第一: 动态类型
Python语言是动态类型的语言，*变量*没有类型，变量存储引用值，引用值指向任意类型的*对象*。Python语言中的对象可以表述为: **实例对象**，**类对象**，**元类对象**。
```python
var_i = 123  # var_i变量，指向class int类的实例对象 (class int类型的对象)
```


# 第二: 面向对象模型
*实例对象*通过__class__指针指向*类(对象)*，*类(对象)*通过__class__指针指向*元类(对象)*，元类是一种特殊的类，元类指向元类，最上层元类`class type`指向自己。类通过__bases__指针指向基类。
> > 基类(对象)   __class__     元类(对象)
> > __bases__                 
> > 类(对象)     __class__     元类(对象)
> > __class__
> > 实例对象
## 类型
对象的__class__指针指向的目标即为对象的类型。实例对象的__class__指向类，类对象的__class__指向元类。
## 继承模型
属性搜索机制



# 第三: Python的内置核心类型
## <class 'int'>，整数
整数字面量：二进制整数面量:0b11011; 八进制整数面量:0o71011; 十六进制整数面量:0xabc1209。整数字面量被解析成<class 'int'>类型的对象 (<class 'int'>类的实例对象)
- immutable
- hashable
- non-size-limit
```shell script
var_i = 123
                             <class 'int'>类
                             __class__
变量var_i  ---> class int类的实例对象 ------
                                  | 123  |
                                   ------
```

## <class 'float'>，浮点数
浮点数字面量：3.14e-10。浮点数字面量被解析成<class 'float'>类型的对象 (<class 'float'>类的实例对象)
- 8个字节表示的IEEE 754双精度浮点数
- immutable
- hashable
### 其他数字类型
- Decimal类型十进制小数类：存储精确; 指定小数保存位数和舍入规则。
- Fraction分数类型：分子，分母以整数存储; 存储精确; 可表示任何有理数。
- 复数类型：3+4j, 3.0+4.0j, todo

## <class 'str'>，字符串
字符串字面量: "中h𝄞"。字符串字面量被解析成<class 'str'>类型的对象 (<class 'str'>类的实例对象)
- immutable: 通过<class str>类中的replace,split等方法不能够修改原字符串
- iterable
- hashable
- 合并运算: s1 + s2，合并运算(协议方法)，新创建字符串对象保存s1，s2合并后的值
- 重复运算: s1 * 8, 重复运算(协议方法)，新创建字符串对象保存s1重复8次的字符串
- 索引取值、分片取值，@see chapter2.py/# 第二题、索引运算和分片运算
- 索引赋值、分片赋值报错
- 属于python中序列
```shell script
s = "中h𝄞"
                             <class 'str'>类
                             __class__
变量s  --->  <class 'str'>类的实例对象{
                        [
                            引用          -------> class<'int'>类的实例对象, 存unicode字符'中'的码点
                            引用          -------> class<'int'>类的实例对象, 存unicode字符'h'的码点
                            引用          -------> class<'int'>类的实例对象, 存unicode字符'𝄞'的码点
                        ]
                   }
```
控制字符(不可显字符)的表示:
- ASKII换行: LF(码点值为10，unicode规范兼容ASKII，在unicode中"换行"的码点值仍为10), 在python中使用转义字符\n表示，或者使用chr(codePoint: int)函数: chr(10)
- ASKII回车: CR(码点值为13)
- ...


## <class 'tuple'>，元组
tuple字面量: (1, "2", [1, 2], ("3", 2))
- 元素任意类型的对象
- 有序
- immutable
- iterable
- hashable
- 索引取值、分片取值，@see chapter2.py/# 第二题、索引运算和分片运算

## <class 'list'>，列表
列表字面量: [1, '字符串', ['2', '子列表']]
- 元素任意类型的对象
- 有序
- mutable
- iterable
- 索引运算、分片运算，@see chapter2.py/# 第二题、索引运算和分片运算
- 嵌套：二维数组m = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]   m[0]-->[1,2,3], m[1][2]-->6
- 相等性:    l1 = [1, [2], 3]
            l2 = [1, [3], 2]
            print(l1 < l2)  # True, 最高有效位比较法
- 列表解析表达式: col = [per[1] for per in m]
- type(lst) == list or isinstance(type(lst))
```shell script
lst = [1, ["1", 2], "123"]
                                class <'list'>类
                                __class__
变量lst ------->  class<'list'>类的实例对象{
                        [
                            引用         -------> class<'int'>类的实例对象
                            引用         -------> class<'list'>类的实例对象
                            引用         -------> class<'str'>类的实例对象
                        ]
                    }
```

## <class 'dict'>，字典
字典字面量: {"key1": "value", "key2": ['list']}
- key: 必须hashable
- value可以是任意对象
- 无序性
- mutable
- iterable
- non-duplicate key
- allow None key and None value
- hash映射表: key的hash运算找桶，hash碰撞时比较key的值，如果key值相等，覆盖
- d[key]: 根据key取值,没有key抛异常(与返回None值区别开来)
- d[key]=value: 覆盖或者插入
- 嵌套
- 列表解析表达式

## <class 'set'>，集合
集合字面量: {1, '2'}
- 元素: 必须hashable
- 无序
- mutable
- non-duplicate key
- allow None key
- iterable

## <class 'bytes'>，字节序列
字面量: b'1fb'，每个字符的码点必须<=0x7f，字面量被当成<class 'bytes'>类型的对象 (<class 'bytes'>类的实例对象)
- immutable
- hashable
- iterable
- 有序
- 索引取值，分片取值

## <class 'NoneType'>
字面量: None

## <class 'bool'>
字面量: True，False



# Python中<class 'int'>类与Java中int类型的对比
Java中int类型的模型: 
int a = 1;  // int类型变量a ----
                          | 1  |
                           ----

int a = 1;      # 线程栈中创建 int类型的变量a，存储1
int b = a;      # 线程栈中创建 int类型的变量b，存储1
a = a + 2;      # 取变量a的值，执行加法，得到3，将3存入变量a

Python中<class 'int'>类的实例对象的模型:
a = 1  # 变量a， ----                <class 'int'>的实例对象 {
               |引用 | ---------->                            1
                ----                                       } 

a = 1           # a ---> class int类型的对象{存1}
b = a           # b ---> class int类型的对象{存1}，此时a，b变量中存有相同的引用值
a = a + 2       # a ---> class int类型的对象{存3}：a变量取得整数1，和整数2做加法运算，得到整数3，创建class int类型的对象存3

Java中类似<class 'int'>类的不可变设计:
class String, immutable
String a = "abc";   # String类型变量a，指向 String类型对象{"abc"}
String b = a;       # String类型变量b，指向 String类型对象{"abc"}，此时a，b变量中存有相同的引用值
a = a + "--";       # 取变量a的值 + "--" 得到 "abc--", 新创建字符串对象("abc--"), 变量a指向字符串对象("abc--")


    