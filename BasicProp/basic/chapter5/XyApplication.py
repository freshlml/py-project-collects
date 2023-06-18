# 第一: 当前module XyApplication运行，重命名成__main__，其所在的目录为top-level package
# 第二: 绝对导入
#  如果模块已存在，直接使用
#  否则，根据"模块搜索路径"搜索模块，执行并赋值给变量
#   1.内置模块，如sys等
#   2.sys.path
#     当前py文件所在目录(top-level package): D:\\pyProjects\\BasicProp\\basic\\chapter5
#     环境变量PYTHONPATH指定目录
#     标准库目录: C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\..
#     .pth指定目录
import sys

from xy.common import XyCommon
import xy.utils.XyUtils

print("XyApplication", sys.path, sep=": ", end="\n")

print("XyApplication", XyCommon, sep=": ", end="\n")
print("XyApplication", xy.common, sep=": ", end="\n")

print("XyApplication", xy.utils, sep=": ", end="\n")
print("XyApplication", xy.utils.XyUtils, sep=": ", end="\n")

# 相对导入
# 相对导入语法: from . import; from .. import
# 相对导入不能跨过top level package


# 对当前运行的module，不能使用相对导入，因此一个程序的入口module一般在更浅的目录层次


# note: 在pycharm中运行时将工程目录(D:\\pyProjects\\BasicProp)添加到了sys.path, 因此如下导入也能识别
# from basic.chapter5 import test as test_111111

