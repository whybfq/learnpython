
#!/usr/bin/python
#-*- coding: utf8 -*-

u'''''财务管理中与时间价值相关函数
变量的含义：
i   利率
'''


import random
position=0
walk=[position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
