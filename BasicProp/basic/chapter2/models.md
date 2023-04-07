# 第一: 变量，对象
Python语言是动态类型的语言，*变量*没有类型，变量存储引用值，引用值指向*对象*。Python语言中的对象可以表述为: **实例对象**，**类对象**，**元类对象**。
```python
import sys  # sys变量，指向<class 'module'>类的实例对象

var_i = 123  # var_i变量，指向<class 'int'>类的实例对象

var_lam = lambda a, b: a+b  # var_lam变量，指向<class 'function'>类的实例对象

def func(a, b):  # func函数(变量)，指向<class 'function'>类的实例对象
    return a+b

class AMeta(type): # AMeta变量，指向AMeta元类对象,其__class__指向<class 'type'>
    pass

class A(metaclass=AMeta):  # A变量，指向A类对象,其__class__指向<class 'AMeta'>
    pass

```

# 第二: 面向对象模型
*实例对象*通过__class__指针指向*类(对象)*，*类(对象)*通过__class__指针指向*元类(对象)*，元类是一种特殊的类，元类指向元类，最上层元类`class type`指向自己。类通过__bases__指针指向基类。
> > 元类(对象) __bases__ 基类(对象)
> > __class__
> > 类(对象)  __bases__ 基类(对象)
> > __class__
> > 实例对象
## 类型
对象的__class__指针指向的目标即为对象的类型。python有意弱化了类型的概念。
## 继承模型
属性搜索机制

