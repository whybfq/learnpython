
#!/usr/bin/python
#-*- coding: utf8 -*-

u'''''
 Script file: walk_around.py

Purpose:
 A simulation applet, random walk, starting from 0, with a 1 or -1 step, equal probability. Take a total of 1000 steps.
 
Record of revisions:
Date           Programmer          Description of change
=====          ==============      ===========================
30-May-2018                         Original
 
Define variables:
position     --the position
step         --it can be 1 or -1
'''


import random
position=0
walk=[position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
