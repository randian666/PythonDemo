#!/usr/bin/python
# -*- coding: UTF-8 -*-

import demo10

demo10.test()

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
