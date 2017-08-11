#!/usr/bin/python
# -*- coding: UTF-8 -*-

############################list###############################################
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates=['Michael','Bob','lisi']
print classmates
print "list长度:",len(classmates)
print classmates[0]
# 如果要取最后一个元素，除了计算索引位置外，还可以用‐1做索引，直接获取最后一个元素
print classmates[-1]
#倒数第二个
print classmates[-2]


# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('刘勋')
print classmates[-1]
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1,"张三")
print classmates[1]
# 要删除list末尾的元素，用pop()方法：
print classmates.pop()
print classmates[-1]

# 要删除list末尾的元素，用pop()方法：
print classmates.pop(1)

# 要删除list末尾的元素，用pop()方法：
classmates[1]='岳飞';
print classmates[1];
# 要删除list末尾的元素，用pop()方法：
classmates.append(222222222)
print classmates.pop();

# list元素也可以是另一个list
s=['java','java',['asp','c#'],'ss']
print len(s);
print s[2];
print s[2][0]
############################tuple###############################################
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates=('zhangsan','lisi','bob')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样
# 的，你可以正常地使用classmates[0]，classmates[‐1]，但不能赋值成另外的元素。

print classmates[0]

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
sss=(1,)
print sss[0]

# “可变的”tuple
ddd=('a','b',['c','d'])
ddd[2][0]='cccc';
print ddd;


# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。