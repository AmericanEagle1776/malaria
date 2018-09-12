import matplotlib.pyplot as plt
import scipy.integrate as odeint
import numpy as np
from proteins import Protein

prot1 = Protein('PFL0420w')
e = prot1.expr
t =np.linspace(0, 53, 53)

fig = plt.figure()

plot1 = fig.add_subplot(111)
plot1.plot(t, e, label= 'relative expression')
plot1.set_ylabel('relative expression to mean')
plot1.set_xlabel('time in hrs')
plt.show()