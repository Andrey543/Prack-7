import math as m
import pylab
from matplotlib import mlab

t=[_t/100  for _t in range(-1000,1000,1) ]

pylab.ion()

for a in range (1000):
        x=[m.sin(_t+a/100) for _t in t]
        y=[m.cos(2*_t) for _t in t]
        pylab.clf()
        pylab.plot (x,y)
        pylab.draw()

pylab.close()
