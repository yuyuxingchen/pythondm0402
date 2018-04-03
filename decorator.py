#-*- coding: utf-8 -*-
# def decorator(func):
#      func()
#      return func
# @decorator
# def hello():
#      print('hello,zhangx!')
#带有__call__方法的类
class Reader():
    def __init__(self,name,nationality):
        self.name = name
        self.nationality = nationality
    # def __call__(self):
    #     print('Reader: %s Nationality: %s' % (self.name,self.nationality))
'''被写作函数的装饰器可以用一下两种方式来表达'''
'''不带参数的装饰器，引用装饰器时直接用装饰器的名称即可'''
# def simple_decorator(function):
#     print('doing decoration')
#     return function
# @simple_decorator
# def function():
#     print('inside function')
'''带参数的装饰器，引用装饰器时需要给定参数'''
# def decorator_with_arguments(arg):
#     print('defining the decorator')
#     def _decorator(function):
#         '''在内部函数中arg参数也是可以用的'''
#         print('doing decoration,',arg)
#         return function
#     return _decorator
#
# @decorator_with_arguments('abc')
# def function():
#     print('inside function')


# def replacing_decorator_with_arguments(arg):
#     print('defining the decorator')
#     def _decorator(function):
#         '''在内部函数中arg参数也是可以用的'''
#         print('doing decoration,',arg)
#     def _wrapper(*args,**kwargs):
#         print('inside wrapper,',args,kwargs)
#         return function(*args,**kwargs)
#         return _wrapper
#     return _decorator
#
# @replacing_decorator_with_arguments('abc')
# def function(*args,**kwargs):
#     print('inside function,', args,kwargs)
#     return 14