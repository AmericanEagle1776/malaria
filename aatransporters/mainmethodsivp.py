import odesysivp
import config
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as npo


result = solve_ivp(lambda t, y: odesysivp.f(t, y, config.told), (0, 53), odesysivp.y0, t_eval=np.linspace(0, 53, 1000))

P1 = []
Pe = []


fig = plt.figure()

plot1 = fig.add_subplot(311)
plot1.plot(result.t, result.y[0], label='Prot {} expr'.format(odesysivp.p1.name))
plot1.set_ylabel('amount of protein')
plot1.set_xlabel('time in hrs')
plot1.legend(fontsize='small')

plot2 = fig.add_subplot(312)
plot2.plot(result.t, result.y[3], label='protein {}'.format(odesysivp.p2.name))
plot2.set_ylabel('amount of protein')
plot2.set_xlabel('time in hrs')
plot2.legend(fontsize='small')

#plot2 = fig.add_subplot(313)
#plot2.plot(result.t, result.y[4], label='protein {}'.format(odesysivp.p3.name))
#plot2.set_ylabel('amount of protein')
#plot2.set_xlabel('time in hrs')
#plot2.legend(fontsize='small')

plt.show()
#plt.savefig('proteinabundances.pdf')
