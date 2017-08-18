#!/usr/bin/python
# -*- coding: UTF-8 -*-

#面向对象高级编程
class Student(object):
    pass;
#动态绑定属性
stu=Student();
stu.age=19;
print stu.age

#动态绑定方法
from types import MethodType

def set_age(self,age):
    self.age=age;
stu.set_age=MethodType(set_age,stu,Student);
stu.set_age(25);
print stu.age
#只能给一个实例绑定动态属性、方法。对另外一个实例是不起作用的
stu2=Student();
# print stu2.age

#给所有实例都绑定方法，可以给class绑定方法
Student.set_age=MethodType(set_age,None,Student);
stu3=Student();
stu3.set_age(22222);
print stu3.age

#限制绑定属性
class Student2(object):
    __slots__ = ('name','age'); #用tuple定义允许绑定的属性名称，仅对当前类起作用，对继承的子类是不起作用的

stu2_2=Student2();
stu2_2.name='Mi'
stu2_2.age=22
# stu2_2.score=222  #如果动态绑定属性不在类允许绑定的属性名称里面就会报错


#@property装饰器就是负责把一个方法变成属性调用
class Student3(object):
    __slots__ = ('_score', '_age');#用tuple定义允许绑定的属性名称，仅对当前类起作用，对继承的子类是不起作用的
    @property
    def age(self):
         return self._age;
    @age.setter
    def age(self,value):
        self._age=value;

    @property
    def score(self):
        return self._score;
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an int!');
        self._score=value;
stu3=Student3();
stu3.score=111;
stu3.age=222;
print stu3.score
print stu3.age

#多重继承,一个子类可以同时获得多个父类的所有功能
class Animal(object):
    def run(self):
        print "Animal running"
class Runnable(object):
    def run1(self):  #如果这个方法名跟Animal的run同名，执行第一个继承的类的run方法
        print "Runnable running"
class Dog(Animal,Runnable):
    pass

d=Dog();
d.run();
d.run1();



class Fib(object):
    def __init__(self):
        self.a,self.b=0,1;
    # 如果想要一个类作用与for...in循环，就必须实现一个__iter__()方法，改方法返回一个迭代对象.
    def __iter__(self):
        return self;
    #如果要实现跟list一样根据下标取值，需要实现__getitem__()方法
    def __getitem__(self, item):
        a,b=1,1
        if isinstance(item,int):
            for x in range(item):
                a,b=b,a+b;
            return a;
        if isinstance(item,slice): #若要实现list切片功能，需要判断入参类型，如果入参类型为int就返回指定下标的值，如果为slice就返回切片后的数据
            start=item.start;
            stop=item.stop;
            L=[];
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b;
            return L;

    def next(self):
        self.a,self.b=self.b,self.a+self.b;#计算下一个值
        if self.a>100:
            raise StopIteration();#然后for循环就会不断的调用迭代对象的next方法拿到循环的下一个值。知道遇到Stopiteration错误时退出。
        return self.a;

for n in Fib():
    print n
f=Fib();
print f[0],f[100]
print f[0:10]

#利用__getattr__动态返回属性、方法实现REST API链接地址
class Chain(object):
    def __init__(self,path=''):
        self.path=path;
    def __getattr__(self, item):
        if item=='user':
            return lambda x:Chain('%s/%s' % (self.path,x));
        else:
            return Chain('%s/%s' % (self.path,item));
    def __str__(self):
        return self.path;
    def __call__(self, *args, **kwargs):
        print 'name is chain'
c=Chain();
c.path='jd'
print c.user("san").status.time.list
c()

#通过Callable可以判断一个对象是否可以被调用，也就是判断一个变量是对象还是函数
print callable(Chain)
print callable('aaa')
