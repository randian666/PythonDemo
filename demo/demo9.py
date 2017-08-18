#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image


im=Image.open("E:/new.jpg")
print im.format,im.size


##面对对象
class Student(object):
    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且调用时，不用传递该参数。除此之外和普通函数没有什么区别，仍然可以用默认参数、可变参数、关键字参数。
    def __init__(self,name,score):
        self.name=name;
        self.score=score;
    #数据封装：可以直接在类的内部定义访问数据的函数，封装数据的函数是和类关联起来的。称之为的类的方法。
    #定义一个类的方法，除了第一个参数是self外，其他和普通函数一样。调用该方法，只需要在实例变量上直接调用。除了self不用传递，其他参数正常传入
    def print_score(self):
        print '%s:%s' % (self.name,self.score)
    def get_grade(self):
        if self.score>90:
            return "A"
        elif self.score>=60:
            return "B"
        else:
            return "C"

zhangsan=Student('张三',11)
zhangsan.print_score()
#可以自由的给一个实例变量绑定属性
zhangsan.sss=1111
print zhangsan.sss
print zhangsan.get_grade()


#总结
#类是创建实例的模板，而实例是一个一个具体的对象，各个实例拥有的数据都是互相独立，互不影响，方法就是与实例绑定的函数。和普通函数不同，方法可以直接访问实例的数据；


#访问限制；如果内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在python中，实例的变量名如果以__开头，就变成一个私有变量（private）,只有内部可以访问，外部不能访问。
class Student2(object):
    def __init__(self,name,score):
        self.__name=name;
        self.__score=score;

    def print_self(self):
        print '%s:%s' % (self.__name,self.__score)

    #如果外部代码要获取内部属性，可以给类属性增加get_这样的方法
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score;
    #如果外部代码要修改内部属性，可以给类属性增加set_这样的方法,这样的好处就是可以对参数做检查。
    def set_name(self,name):
        self.__name=name;
    def set_score(self,score):
        self.__score=score;
lisi=Student2("李四",89);
lisi.print_self();
print lisi.get_name()
lisi.set_score(100)
print lisi.get_score()

#在python中变量名类似__XX__的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以不能用__name__,__score__这样的变量名。
#__开头的变量也不是一定不能从外部访问，可以通过_Student2__name访问,这是因为python解释器对外把__name变量改成了_Student2__name。但是不建议这么做。不同的版本会改成不同的变量名。
print lisi._Student2__name

####继承和多态；当我们定义一个类的时候，可以从某个现有的类继承，新的类称为子类，而被继承的类称为基类、父类、或超类
class Animal(object):
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    #当子类和父类都存在相同的方法时，子类的方法覆盖了父类的方法。运行的时候总会调用子类的方法。这就是多态。
    def run(self):
        print 'Dog is running...'
class Cat(Animal):
    def run(self):
        print 'Cat is running...'
dog=Dog();
cat=Cat();
#自动拥有了父类的run方法
dog.run();
cat.run();
#当我们定义一个类的时候我们实际上就定义了一种数据类型，和python自带的数据类型，比如str、list、dict没什么两样
a=list([1,2,3,4]);
b=Animal();
c=Dog();
#判断变量是否是某个烈性可以用isinstance()判断
print  isinstance(a,list)
print  isinstance(b,Animal)
print  isinstance(c,Dog)
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。反过来就不行。
print  isinstance(c,Animal)


def run_twice(animal):
    animal.run();

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
#小结
#继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；
#有了继承，才能有多态。在调用类实例方法的时候，尽量把变量是作为父类类型，这样，所有子类类型都可以正常被接受；任何时候，如果没有合适类可以继承，就继承Object类。

#使用type()判断对象类型
print type(dog)
#Python把每种type类型都定义好了常量，放在types模块里，使用之前需要导入
import types
print type('1234')==types.StringType
print type('23')==types.TypeType  #所有类型本身的类型就是TypeType
print isinstance('23',str) #能用type()判断的基本类型也可以用isinstance()判断

#使用dir()；如果要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list。
print dir('ABC')
print dir(dog)
#类似__xxx___的属性和方法在py中都是有特殊用途的，比如__len__方法返回长度。
print 'ABC'.__len__()
class MyObject(object):
    def __init__(self,x=9,y=10):
        self.x=x;
        self__y=y;
    def __len__(self):
        return 100
obj=MyObject();
print obj.__len__()

#操作对象状态
print hasattr(obj,'x') #有属性x么
print hasattr(obj,'y') #有属性y么 私有属性查看不了
setattr(obj,'z',222)  #给对象设置一个属性
print hasattr(obj,'z')
print getattr(obj,'x','404') #获取属性 如果属性不存在就返回404
print hasattr(obj,'__len__') #获取对象的方法是否存在
fn=getattr(obj,'__len__'); #获取对象的方法 并赋值给变量
print fn()
