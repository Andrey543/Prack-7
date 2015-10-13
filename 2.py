import numpy as np
import matplotlib.pyplot as plt
def y(x):
    return x*x-6-x
x=np.arange(-20,20,0.01)
plt.plot(x,y(x))
plt.grid(True)
plt.show()

c=0.0000000001
a=-10
b=10
o=20

while o>c:
    k=(a+b)/2
    if (y(k+c)>y(k-c)):
        if (y(k)>0):
            b=k
        else:
            a=k
    else:
        a=k
    o=b-a
print((a+b)/2)


a=-10
b=10
o=20
while o>c:
    k=(a+b)/2
    if (y(k+c)<y(k-c)):
        if (y(k)>0):
            a=k
        else:
            b=k
    else:
        b=k
    o=b-a
print((a+b)/2)
    
