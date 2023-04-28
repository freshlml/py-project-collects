

# python 类，对象，继承模型
class E(object):
    attr = "e"

    def m(self):
        print("e_m")
        return self

    def __call__(self, *args, **kwargs):
        print("e_call")


class D(object):
    attr = "d"

    def m(self):
        print("d_m")
        return self


class F(object):
    attr = "f"

    def m(self):
        print("f_m")
        return self


class C(D, F):
    attr = "c"

    def m(self):
        print("c_m")
        return self


class B(E, D):
    pass


class AMeta(type):
    attr = "a_meta"
    attr1 = "a_meta"

    def __new__(mcs, *args, **kwargs):
        cls = type.__new__(mcs, *args, **kwargs)
        return cls

    def __init__(cls, *args, **kwargs):
        pass

    def __call__(cls, *args, **kwargs):
        print("a_meta_call")
        return type.__call__(cls, *args, **kwargs)

    def m(self):
        print("a_meta_m")
        return self

    def m1(self):
        print("a_meta_m")
        return self


class A(B, C, metaclass=AMeta):

    def __init__(self):
        self.attr1 = "attr"
        self.m = lambda: print(1)


# print(AMeta.mro())
print(A.mro())  # A B E C D F object
print(A.attr)    # e,   在A类上搜索属性, A类的mro路径 + (A类作为实例对象)A.__class__的mro路径
print(A.attr1)   # a_meta
A.m(None)         # e_m, 在A类上搜索方法, A类的mro路径 + (A类作为实例对象)A.__class__的mro路径
A.m1()           # a_meta_m, 在A类上调用方法的self约定: (A类作为实例对象)A.__class__的mro路径 中搜索到的方法将自身作为第一个参数, self约定的原理@see chapter6_29_2
print("------------1------------")
# 调用A，触发__call__协议方法，在A.__class__的mro路径中搜索，搜到AMeta中__call__
#   1.AMeta的__call__中代码逻辑
#   2.总会委托给class type的__call__,从而
#      1).A.__new__,搜到object中__new__，构造A类的实例对象
#      2).A.__init__,搜到A中__init__，A.__init__(第"1)"步构造的A类实例对象)
a = A()        # a_meta_call
A.__call__(None)  # e_call, A类(显示)调用__call__协议方法，和普通方法搜索规则一致
print(a.attr)  # e, A类的实例对象上搜索属性, 实例对象 + 实例对象.__class__的mro路径
a.m()          # 1, A类的实例对象上搜索方法, 实例对象 + 实例对象.__class__的mro路径
print()        # ,  A类的实例对象上调用方法的self约定: 实例对象.__class__的mro路径 中搜索到的方法将自身作为第一个参数
a.__call__ = lambda *args: print("a_call")
a()            # e_call, (隐式)触发__call__协议方法，从a.__class__的mro路径 中搜索
a.__call__()   # a_call, A类的实例对象(显示)调用__call__协议方法，和普通方法搜索规则一致
print("------------2------------")


class F(object):
    a = "F"

    def aa(self):
        print("f_aa")
        return self


class E(F):
    a = "E"

    def aa(self):
        print("e_aa")
        return self


# class G(F, E):  # TypeError: Cannot create a consistent method resolution order (MRO) for bases F, E
#    pass




