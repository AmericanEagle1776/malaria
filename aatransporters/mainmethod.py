from proteins import Protein
import odesys
import config
from scipy.integrate import odeint
import matplotlib.pyplot as plt


p1 = Protein('PFL0420w')
p1e = p1.expr
p1ct = p1.get_start_clearance_time(p1)       # a.append(e.index(x))

result = odeint(odesys.f, odesys.y0, odesys.timegrid, args=(config.told, [], {}))

print(result)
P1 = []
Pe = []

for row in result:
    P1.append(row[0])
    Pe.append(row[1])
fig = plt.figure()

plot1 = fig.add_subplot(211)
plot1.plot(odesys.timegrid, P1, label='Prot {} expr'.format(odesys.p1.name))
plot1.set_ylabel('amount of protein')
plot1.set_xlabel('time in hrs')
plot1.legend(fontsize='small')

plot2 = fig.add_subplot(212)
plot2.plot(odesys.timegrid, Pe, label='test protein for protein half life of 43 mins')
plot2.set_ylabel('amount of protein')
plot2.set_xlabel('time in hrs')
plot2.legend(fontsize='small')
plt.show()
