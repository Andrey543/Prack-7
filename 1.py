import math
def y(x):
    return math.log((1/math.e**(math.sin(x)+1))/(5/4+1/x**15),1+x**2)
print(y(1))
print(y(10))
print(y(1000))

