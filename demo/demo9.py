#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image


im=Image.open("E:/new.jpg")
print im.format,im.size

##面对对象

class Student(object):

    def __init__(self,name,score):
        self.name=name;
        self.score=score;
    def print_score(self):
        print '%s:%s' % (self.name,self.score)


zhangsan=Student('张三',11)
zhangsan.print_score()