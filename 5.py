import matplotlib.pyplot as plt
import math
r=input()
def f(x):
    return eval(r)
_x=[x/1000 for x in range(-10000,10000)]
y=[f(x) for x in _x]
plt.plot(_x,y)
plt.xkcd()
plt.show()
