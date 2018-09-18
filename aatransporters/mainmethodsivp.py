import odesysivp
import config
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


result = solve_ivp(lambda t, y: odesysivp.f(t, y, config.told), (0, 50), odesysivp.y0, t_eval=np.linspace(0, 50, 1000))

P1 = []
Pe = []


fig = plt.figure()

plot1 = fig.add_subplot(311)
plot1.plot(result.t, result.y[0], label='Prot {} expr'.format(odesysivp.p1.name))
plot1.set_ylabel('amount of protein')
plot1.set_xlabel('time in hrs')
plot1.legend(fontsize='small')

plot2 = fig.add_subplot(312)
plot2.plot(result.t, result.y[1], label='test protein for protein half life of 43 mins')
plot2.set_ylabel('amount of protein')
plot2.set_xlabel('time in hrs')
plot2.legend(fontsize='small')

plot3 = fig.add_subplot(313)

plot3.plot(result.t, result.y[3], label='protein {}'.format(odesysivp.p2.name))
plot3.set_ylabel('amount of protein')
plot3.set_xlabel('time in hrs')
plot3.legend(fontsize='small')
plt.show()
