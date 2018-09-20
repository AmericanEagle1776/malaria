import odesysivp
import config
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as npo


result = solve_ivp(odesysivp.f, (0, 53), odesysivp.y0, t_eval=np.linspace(0, 53, 1000))

P1 = []
Pe = []

fig = plt.figure()

plot1 = fig.add_subplot(311)
plot1.plot(result.t, result.y[0], label='protein {}'.format(odesysivp.p1.name))
plot1.set_ylabel('amount of protein')
#plot1.set_xlabel('time in hrs')
plot1.legend(fontsize='small')

polly = odesysivp.p1.rel_expr_by_time
values = []
for time in result.t:
    a = npo.polyval(time, polly) * odesysivp.mean_expr
    values.append(a)

plotrna = fig.add_subplot(312)
plotrna.plot(result.t, values, label=f'{odesysivp.p1.name} mrna expression')
plotrna.set_ylabel('amount of rna')
#plotrna.set_xlabel('time in hrs')
plotrna.legend(fontsize='small')

plot2 = fig.add_subplot(313)
plot2.plot(result.t, result.y[2], label='protein {}'.format(odesysivp.p2.name))
plot2.set_ylabel('amount of protein')
plot2.set_xlabel('time in hrs')
plot2.legend(fontsize='small')

#plot3 = fig.add_subplot(414)
#t_decay = np.linspace(0, 53, np.shape(odesysivp.decay_check)[0])
#plot3.plot(t_decay, odesysivp.decay_check, label='decay')
#plot3.legend(fontsize='small')


#plot3 = fig.add_subplot(313)
#plot3.plot(result.t, result.y[4], label='protein {}'.format(odesysivp.p3.name))
#plot3.set_ylabel('amount of protein')
#plot3.set_xlabel('time in hrs')
#plot3.legend(fontsize='small')

plt.show()
#plt.savefig('proteinabundances.pdf')
