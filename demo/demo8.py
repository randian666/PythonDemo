#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


# 函数本身也可以赋值给变量，即：变量可以指向函数。
f=abs
print  f(-100)

#传入函数
def add(x,y,f):
    return f(x)+f(y)
print add(1,-2,abs)

# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
print '~~~~~~~~~~~~~~map()函数~~~~~~~~~~~~~~~~~~~~~~~~'
# 我们先看map。map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元
# 素，并把结果作为新的list返回。
L=[1,2,3,4,5];
T=(1,2,3);
D=set([1,2,3,5])
def g(x):
    return x*x;
print map(g,L)
print map(g,T)
print map(g,D)
print map(str,L)

print '~~~~~~~~~~~~~~reduce()函数~~~~~~~~~~~~~~~~~~~~~~~~'
# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结
# 果继续和序列的下一个元素做累积计算，
def add(x,y):
    return x+y;
print reduce(add,[1,2,3,4])
print sum([1,2,3,4,5])

def fn(x,y):
    return x*10+y;
print reduce(fn,[1,2,3,4,5])


S=['adam','LISA','barT']
def convet(x):
    return x[0].upper()+x[1:].lower();
print map(convet,S)
print '~~~~~~~~~~~~~~~filter过滤~~~~~~~~~~~~~~~~~~~~~~~~~'

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每
# 个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(x):
    return x%2==0;

print filter(is_odd,[1,2,3,4,5,6,7,8,9])

#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
#一个序列中的空字符串删掉
def not_empty(x):
    return x and x.strip()
print filter(not_empty,['A','','B',None,'C',' ']);
# 用filter()删除1~100的素数
def su(x):
    return x<2 or x%2==0
print filter(su,range(100))


print '~~~~~~~~~~~~~~~sorted排序~~~~~~~~~~~~~~~~~~~~~~~~~'
#倒排序
print sorted([34,34,3,1,34,5,6])
def reversed(x,y):
    if(x>y):
        return -1;
    elif(x<y):
        return 1;
    else:
        return 0;
print sorted([34,34,3,1,34,5,6],reversed);
#忽略大小写排序
def ignore_case(x,y):
    u1=x.upper();
    u2=y.upper();
    if u1<u2:
        return -1;
    elif u1<u2:
        return 1;
    else:
        return 0;
print sorted(['bob', 'about', 'Zoo', 'Credit'],ignore_case)

#函数作为返回值
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参
# 数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closur
# e）”的程序结构拥有极大的威力。
print '~~~~~~~~~~~~~~~函数作为返回值~~~~~~~~~~~~~~~~~~~~~~~~~'
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n;
        return ax;
    return sum;
f=lazy_sum(1,2,3,4,5)
f1=lazy_sum(1,2,3,4,5,6)
print f
print f()
print f1()
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

print '~~~~~~~~~~~~~~~lambda匿名函数~~~~~~~~~~~~~~~~~~~~~~~~~'
#匿名函数 关键字lambda表示匿名函数  匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
print map(lambda x:x*x,[1,2,3,4])

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f=lambda x:x*x;
print f(3)


print '~~~~~~~~~~~~~~~装饰器~~~~~~~~~~~~~~~~~~~~~~~~~'
#装饰器 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
import functools
def wrapper(time='2017-09-09'):
    def log(func):
        @functools.wraps(func)
        def decorator(*args,**kwargs):
            print '%s:func name is %s():'%(time,func.__name__)
            result=func(time, *args, **kwargs);
            print '%s:func name is %s():' % (time, func.__name__)
            return result;
        return decorator;
    return log

@wrapper('2017-09-19')
def now(time):
    print time;

now();
print now.__name__
#使用装饰器计算函数运行时间
import time
def load_time(func):
    @functools.wraps(func)
    def decorator(*args,**kwargs):
        start = time.clock()  # time.clock()第一次调用的时候返回的是程序运行的实际时间
        func(*args,**kwargs)
        stop = time.clock()  # time.clock()第二次调用的时候返回的是第一次调用后，到这次调用的时间间隔
        print '函数：%s运行时间为：%s'%(func.__name__,(stop-start));
    return decorator;
@load_time
def add(x):
    return x*x;
add(999)
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~偏函数~~~~~~~~~~~~~~~~~~~~~~~~~~~'

def int2(x,base=2):
    return int(x,base)

print int2('1000000')

#functools.partial就是帮助我们创建一个偏函数，不需要定义int2()
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新函数，调用这个新函数会更简单
import functools
int2=functools.partial(int,base=2)
print int2('100000')

max2=functools.partial(max,100)
print max2(1,2,3,4,5)

