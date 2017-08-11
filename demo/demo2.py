#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 因为Python的诞生比Unicode标准发布的时间还要早，所以最早的Python只支持ASCII编码，普通的字符串'ABC'在
# Python内部都是ASCII编码的。Python提供了ord()和chr()函数，可以把字母和对应的数字相互转换
print ord('a')
print chr(97)

# Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示，
print u'中文'

# 把u'xxx'转换为UTF­8编码的'xxx'用encode('utf‐8')方法
print u'中国'.encode('utf-8')

# len()函数可以返回字符串的长度
print len(u'ABC')
print len('ABC')
print len(u'中国')
print len('中国')


# 反过来，把UTF­8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf‐8')方法
print '中国'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8');

# Python解释器读取源代码时，为了让它按UTF­8编码读取，我们通常在文件开头写上这两行
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF­8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱
# 码。