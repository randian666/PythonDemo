#!/usr/bin/python
# -*- coding: UTF-8 -*-

#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

person('liuxun',20)
person('liuxun',20,city='beijing',size=180)
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('liuxun',20,**kw)
#
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用
# 其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a,b,c=0,*args,**kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
#在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去
func(1,2)
func(1,2,3)
args=(4,5,6)
func(1,3,3,*args,**kw)
func(*args,**kw)
#默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
