#!/usr/bin/python
# -*- coding: UTF-8 -*-
'a test module'

__author__='Liuxun'

import sys

def test():
    args=sys.argv;
    if len(args)==1:
        print 'hello world';
    elif len(args)==2:
        print 'hello, %s' % args[1];
    else:
        print 'Too many args args: %s'% args


if __name__=='__main__':
    test()