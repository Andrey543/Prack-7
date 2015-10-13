import math as m
import matplotlib.pyplot as plt

def f(x):
    return m.log((x**2+1)*m.exp(-m.fabs(x)/10),1+m.tan(1/(1+m.sin(x)**2)))
x=[_x/100 for _x in range(-1000,1000)]
p=[f(_y) for _y in x]
plt.plot(x,p)
plt.show()

