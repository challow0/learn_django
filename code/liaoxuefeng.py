# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n += 2
# print(L)
'''
高级特性：切片
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# # 方法1：
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(r)

# # 方法2：
# print(L[:3])

# L = list(range(100))
# print(L[-2:-1])


'''
   迭代
'''

# d = {'a':1, 'b':2, 'c':3, 'd':4}
# for key in d:
#     print(key)

# # 1. 判断对象是否能迭代
# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance([1,2,3], Iterable))

# # 2. 实现下标的输出 使用enumerate函数
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)

# for x, y in [(1, 1),(2, 4),(3, 9)]:
#     print(x, y)

'''
   列表生成式
'''

# x =  list(range(1, 11))
# print(x)

# print([x * x for x in range(1,11)])

# print([x * x for x in range(1, 11) if x % 2 == 0])

# # 全排列
# print([m + n for m in 'ABC' for n in 'XYZ'])

# # 列出当前目录下的所有文件和目录名
# import os 
# print([d for d in os.listdir('.')])

# d = {'x':'A', 'y':'B','z':'C'}
# for k, v in d.items():
#     print(k,'=',v)
# print([k + '=' + v for k, v in d.items()])

'''
   生成器
'''
# # 列表
# L = [x * x for x in range(10)]
# print(L)

# # 生成器
# g = (x * x for x in range(10))
# print(g)
# for n in g:
#     print(n)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b
#         a, b = b, a+b
#         n = n + 1
#     return 'done'
# fib(6)

# # 将print(b) 更改为 yield b
# f = fib(6)
# print(f)
# # 单独使用for不能获得函数return的值，补货异常才能获得

# for n in f:
#     print(n)
# # 需要
# while True:
#     try:
#         x = next(f)
#         print('g: ', x)
#     except StopIteration as e:
#         print('Generator return value: ', e.value)
#         break
'''
   迭代器
'''
# from collections import Iterable
# # 可以使用isinstance()判断一个对象是否是Iterable对象：
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))

# from collections import Iterator

# print(isinstance([], Iterator))
# print(isinstance({}, Iterator))

# # 加上iter()就变成了Iterator
# print(isinstance(iter([]), Iterator))

'''
   函数式编程：高阶函数(map/reduce)
'''

# f = abs
# print(f(-10))

# def f(x):
#     return x*x
# r = map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

# print(list(map(str, [1,2,3,4,5,6,7,8,9])))


# from functools import reduce
# def add(x, y):
#     return x + y

# print(reduce(add, [1, 3, 5, 7, 9]))

# from functools import reduce

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))
'''
   高阶函数(filter)
'''
# def is_odd(n):
#     return n % 2 ==1

# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

'''
   高阶函数(sorted)
'''
# # 可以对list进行排序
# print(sorted([36, 5, -12, 9, -21]))

# # 按照绝对值的大小进行排序
# print(sorted([36,5, -12, 9 ,-21], key = abs))

# # 字符串排序(按照ASCII码的大小)
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))

# # 忽略大小写
# L = ['bob', 'about', 'Zoo', 'Credits']
# print(sorted(L, key=str.lower))

# # 反向排序
# print(sorted(L, key=str.lower, reverse=True))

'''
   返回函数
'''

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + args
#         return ax
#     return sum

# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)

'''
   匿名函数
'''
# def f1(x):
#     return x * x

# f2 = lambda x : x*x
# print(f1(2), f2(2))

'''
   偏函数
'''
# x = int('12345')
# x = int('12345', base=8)
# print(x)

'''
   模块：使用模块
'''
# __author__ = 'Challow Zhang'
# import sys

# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print('Hello World!')
#     elif len(args) == 2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')

# if __name__=='__main__':
#     test()

'''
   面向对象编程：类和实例
'''
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

'''
   紧接着是(object)，表示该类是从哪个类继承下来的，
   通常，如果没有合适的继承类，就使用object类，
   这是所有类最终都会继承的类。
'''
# class Student(object):
#     pass
# bart = Student()
# print(bart)

'''

注意到__init__方法的第一个参数永远是self，表示创建的实例本身
因此，在__init__方法内部，就可以把各种属性绑定到self，
因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了,
必须传入与__init__方法匹配的参数，但self不需要传,
Python解释器自己会把实例变量传进去：

'''
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self): # 此处只需要传进去一个self便可
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

'''
   访问限制：

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问
'''
# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s: %s' , (self.__name, self.__score))
# # 此时无法从外部访问实例变量的__name和__score
# bart = Student('Bart Simpson', 59)
# print(bart.__name)

# 需要获取name和score，可以给Student类增加get_name和get_score这样的方法：

# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
    
#     def print_score(self):
#         print('%s: %s' , (self.__name, self.__score))

#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
# # 允许外部代码修改score

#     def set_score(self, score):
#         self.__score = score
'''
以双下划线开头，并且以双下划线结尾的，是特殊变量,
特殊变量是可以直接访问的，不是private变量
'''

'''
   继承和多态
'''
# class Animal(object):
#     def run(self):
#         print('Animal is running...')


# class Dog(Animal):
#     def run(self):
#         print('Dog is running...') # 子类可以重写父类的函数
#     def eat(self):
#         print('Eating meat...')
    
# class Cat(Animal):
#     def run(self):
#         print('Cat is running...')

# dog = Dog()
# cat = Cat()
# dog.run()
# cat.run()

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(Animal())
# run_twice(Dog())

'''
   获取对象信息
'''

# x = type(123)
# print(x)

'''

   如果要获得一个对象的所有属性和方法，可以使用dir()函数，
   它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

'''

# print(dir('ABC'))

# print(len('ABC'))

# print('ABC'.__len__)

'''
面向对象高级编程
'''

# 使用__slots__

class Student(object):
    def set_age(self,age):
        self.age = age

s = Student()
s.name = 'Challow'
print(s.name)

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(5)
s.age








