

# 如果类指定了metaclass, 则其metaclass必须是其基类的metaclass的子类(当存在基类时)
# 如果类未指定metaclass, 则从其基类获取metaclass(当存在基类时)。如果没有基类，则metaclass默认指向class type
# 类的metaclass指向T，类的__class__指针就指向T，即类的类型为T
class QMeta(type):
    attr = "1"


class Q(object, metaclass=QMeta):
    pass


class W(Q):
    pass


print(W.mro())  # W Q object
print(W.__class__)  # class QMeta


class R(W):
    pass


print(R.__class__)  # class QMeta
print("--------------------metaclass规则---------------------")


class A(object):
    def __init__(self):
        pass
# class type:
#   def __call__(cls, *args, **kwds):
#       cls is type
#       ins = cls.__new__(cls, 'A', *args, **kwds)  # 搜索到class type中__new__方法，构造cls的实例对象
#       cls.__init__(ins, *args, **kwds)  # 搜索到class type中的__init__方法，do nothing
#       return ins
# type调用，触发__call__协议方法，在type.__class__的mro路径中搜索，搜到class type的__call__方法
# A = type('A', A.__bases__, A.__dict__)


print(type(A))  # <class 'type'>
print(A.__class__)  # <class 'type'>


# class type:
#   def __call__(cls, *args, **kwds):
#       cls is A
#       ins = cls.__new__(cls, 'A', *args, **kwds) # A.__new__，搜到object中__new__, 构造cls的实例对象
#       cls.__init__(ins, *args, **kwds) # A.__init__，搜到A中__init__
#       return ins
# A调用，触发__call__协议方法，在A.__class__的mro路径中搜索，搜到class type中的__call__方法
a = A()
print("-----------------1---------------")


class SpamMeta(type):

    def __new__(mcs, *args, **kwargs):
        print("SpamMeta __new__", type(mcs))  # SpamMeta __new__ <class 'type'>
        print("SpamMeta __new__", mcs)  # SpamMeta __new__ <class '__main__.SpamMeta'>
        cls = type.__new__(mcs, *args, **kwargs)
        print("SpamMeta __new__", cls)  # SpamMeta __new__ <class '__main__.Spam'>
        return cls

    def __init__(cls, *args, **kwargs):
        print("SpamMeta __init__", type(cls))  # SpamMeta __init__ <class '__main__.SpamMeta'>
        print("SpamMeta __init__", cls)  # SpamMeta __init__ <class '__main__.Spam'>
        cls.s = "s"

    def __call__(cls, *args, **kwargs):
        print("SpamMeta __call__", type(cls))  # SpamMeta __init__ <class '__main__.SpamMeta'>
        print("SpamMeta __call__", cls)  # SpamMeta __init__ <class '__main__.Spam'>
        ins = type.__call__(cls, *args, **kwargs)
        ins.tag = "tag"
        return ins
# class type:
#   def __call__(cls, *args, **kwds):
#       cls is type
#       ins = cls.__new__(cls, 'SpamMeta', *args, **kwds)  # 搜索到class type中__new__方法，构造cls的实例对象
#       cls.__init__(ins, *args, **kwds)  # 搜索到class type中的__init__方法，do nothing
#       return ins
# type调用，触发__call__协议方法，在type.__class__的mro路径中搜索，搜到class type的__call__方法
# SpamMeta = type('SpamMeta', SpamMeta.__bases__, SpamMeta.__dict__)


print(type(SpamMeta))  # <class 'type'>
print(SpamMeta.__class__)  # <class 'type'>
print("-----------------2---------------")


class Spam(object, metaclass=SpamMeta):
    def __init__(self, param):
        self.param = param
        print("Spam __init__")

    def __call__(self, *args, **kwargs):
        print("Spam __call__")
# class type:
#   def __call__(cls, *args, **kwds):
#       cls is SpamMeta
#       ins = cls.__new__(cls, 'Spam', *args, **kwds)  # 搜到SpamMeta中__new__方法，构造cls的实例对象
#       cls.__init__(ins, *args, **kwds)  # 搜到SpamMeta中__init__方法，调用SpamMeta.__init__
#       return cls_ins
# 调用SpamMeta，触发__call__协议方法，在SpamMeta.__class__的mro路径中搜索，搜到class type的__call__方法
# Spam = SpamMeta('Spam', Spam.__bases__, Spam.__dict__)


print(type(Spam))  # <class '__main__.SpamMeta'>
print(Spam.__class__)  # <class '__main__.SpamMeta'>

print(Spam.s)  # s

# class SpamMeta:
#   def __call__(cls, *args, **kwargs):
#       cls is Spam
#       ins = type.__call__(cls, *args, **kwargs)
#                  ins = cls.__new__(cls, *args, **kwargs)  # Spam.__new__, 搜到object中__new__，构造cls的实例对象
#                  cls.__init__(ins, *args, **kwargs)       # Spam.__init__，搜到Spam中__init__
#       return ins
# 调用Spam，触发__call__协议方法，从Spam.__class__的mro路径中搜索，搜到SpamMeta中的__call__方法
spam = Spam("param")
print(spam.tag, spam.param)  # tag param

# 调用spam，触发__call__协议方法，从spam.__class的mro路径中搜索，搜到Spam中的__call__方法
spam()  # Spam __call__


# metaclass conflict, LM继承PM即可
class PM(type):
    pass


class P(metaclass=PM):
    pass


class LM(type):
    pass


class L(P, metaclass=LM):
    pass



