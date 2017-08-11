#!/usr/bin/python
# -*- coding: UTF-8 -*-

#高级特性
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
print L

# 取前N个元素，也就是索引为0­(N­1)的元素，可以用循环
print range(3)
for a in range(3):
    print L[a]
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种 操作。
print L[0:3]
#获取前十个
print L[:10]
#获取后十个
print L[-10:]
#获取所有数，每5个取一个
print L[::5]

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
K=(1,2,3,4,5,6,7,8,9,10)
print K[1:3]
print K[:3]
print K[-3:-1]

# 字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片
# 操作，只是操作结果仍是字符串
J='abcdefghji'
print J[:3]
print J[2::3]


#迭代 dict
U={'a':1,'b':2,'c':3}
for key in U:
    print key
for v in U.itervalues():
    print v
for s in "ABCDEF":
    print s

#判断一个对象是否可以迭代
from collections import Iterable
print isinstance('abc',Iterable)


# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变
# 成索引­元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,v in enumerate(['liuxun','zhangsan']):
    print i,v

for i, v in enumerate([(1,2,3),(2,3,4)]):
    print i, v
for i,v in enumerate({'a':1,'b':2}):
    print i,v
#列表生成
L=[]
for n in range(1,11):
    L.append(n)
print L

L=[x*x for x in range(1,11)]
print L
# 还可以使用两层循环，可以生成全排列
Strs=[m+n for m in 'abc' for n in 'xyz'];
print Strs

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
oss=[f for f in os.listdir('.')] # os.listdir可以列出文件和目录
print oss

# for循环其实可以同时使用两个甚至多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.iteritems():
    print k,v
# map变成list
dl=[k+'='+v for k,v in d.iteritems()]
print dl
# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
LL=[s.lower() for s in L]
print LL
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错,可以用isinstance判断类型
# L = ['Hello', 'World', 18, 'Apple', None]
LF=[s.lower() for s in L if isinstance(s,str)]
print LF

#生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包
# 含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用
# 的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样
# 就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generato
# r）。
LG=(d*d for d in range(0,11))
print LG.next(),LG.next(),LG.next(),LG.next(),LG.next(),LG.next(),LG.next(),LG.next(),LG.next(),LG.next(),LG.next()
for d in LG:
    print d

def fib(num):
    n,a,b=0,0,1
    while n<num:
        print b
        a,b=b,a+b
        n=n+1;
fib(4)
# 函数是顺序执行，遇到return语句或者最后一行函数语
# 句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
def fibx(maxnum):
    n, a, b = 0, 0, 1
    while n < maxnum:
        yield b
        a, b = b, a + b
        n = n + 1
for a in fibx(5):
    print a

def odd():
    print "step 1"
    yield 1
    print "step 2"
    yield 2
    print "step 3"
    yield 3
o=odd();
print o.next()
print o.next()
print o.next()
