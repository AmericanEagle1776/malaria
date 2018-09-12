import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.integrate as odeint
import numpy as np
from proteins import Protein
import math

prot1 = Protein('PFL0420w')
e = prot1.expr
t = np.linspace(0, 53, 53, endpoint=True)
print(e)
print(t)

for x in e:

    if math.isnan(x):

        a = e.index(x)
        del t[a]

#egood = [x for x in e if math.isnan(x) == False]
print(e)

def func(x, a, b, c, d, e):

    return x**4*a + x**3*b + x**2*c + x*d + e


a = curve_fit(func, t, e)
print(a)

fig = plt.figure()

plot1 = fig.add_subplot(111)
plot1.plot(t, e, label= 'relative expression')
plot1.set_ylabel('relative expression to mean')
plot1.set_xlabel('time in hrs')
plt.show()

