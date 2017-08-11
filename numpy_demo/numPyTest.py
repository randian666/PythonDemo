#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np



def main():
    lst=[[1,3,5],[2,4,6]]
    print type(lst)
    np_lst=np.array(lst);
    print np_lst
    print type(np_lst)
    np_lst=np.array(lst,dtype=float)
    print np_lst
    print '形状',np_lst.shape  #表示np_lst形状 2行3列
    print '维度',np_lst.ndim   #表示np_lst维度 二维数组
    print '数据类型',np_lst.dtype  #表示np_list类型
    print '每项内容的大小',np_lst.itemsize #每一项的大小 单位字节
    print '大小',np_lst.size   #np_list大小
if __name__ == '__main__':
    main()
