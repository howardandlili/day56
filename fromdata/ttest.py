#!/user/bin/env python
__author__ = 'Howie'
from sympy import *

x,y,z = symbols('x y z')
f = solve([x+x+x-30 , x+y+y-20, z+y+y-13],[x,y,z])
print(f)
print(f[x]+f[y]*f[z])