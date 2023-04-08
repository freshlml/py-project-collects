# encoding: utf-8

a = 1           # a ---> class int类型的对象{存1}
b = a           # b ---> class int类型的对象{存1}，此时a，b变量中存有相同的引用值
a = a + 2       # a ---> class int类型的对象{存3}：a变量取得整数1，和整数2做加法运算，得到整数3，创建class int类型的对象存3

print(a)  # 3
print(b)  # 1

# 练习题
# 1、
A = 'spam'
B = A
B = 'shrubbery'

print(A)  # spam
print(B)  # shrubbery

# 2、
C = ["spam"]
D = C
D.append("shrubbery")
D[0] = 'berry'

print(C)  # ['berry', 'shrubbery']
print(D)  # ['berry', 'shrubbery']

# 3、
F = ['spam']
G = F[:]            # 1、分片取值，拷贝引用值，2、新创建list存拷贝的引用值
G[0] = 'shrubbery'

print(F)  # ['spam']
print(G)  # ['shrubbery']

# 4、
N = [1, 2]
F = ['spam', N]
G = F[:]     # 1、分片取值，拷贝引用值，2、创建列表对象存引用值，G指向该对象

# G的第二个元素和F的第二个元素都指向N变量指向的列表对象
print(F[1] is G[1])  # True
print(F[1] is N)     # True
# 所以此时要特别注意，因为列表是可变对象


