import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import odesys

# solve space
start = 0.0
end = 5
number_of_points = 2001
timegrid = np.linspace(start, end, number_of_points)

result = odeint(odesys.f, odesys.y0, timegrid)  # the integration takes place with dy/dt given by f, y0 by y0 and the integration variable with limits by timegrid

G = []
K = []
I = []
Mg = []
Mi = []
T = []
Cg = []
Ci = []
PR = []  # parasite ratio - fraction of ppl carrying parasite
CR = []  # child ratio - proportion of human population that is a child
IR = []  # immunity ratio - prop of adult pop that is immune


for row in result:
    G.append(row[0])
    K.append(row[1])
    I.append(row[2])
    Mg.append(row[3])
    Mi.append(row[4])
    T.append(row[5])
    Cg.append(row[6])
    Ci.append(row[7])

    PR.append((row[1] + row[2]) / (row[0] + row[1] + row[2]))  # parasite ratio - fraction of ppl carrying parasite
    CR.append((row[6] + row[7])/(row[0] + row[1] + row[2]+ row[6] + row[7]))  # child ratio - proportion of human population that is a child
    IR.append(row[2]/(row[0] + row[1] + row[2]))  # immunity ratio - prop of adult pop that is immune

r3 = odesys.IAR * odesys.K0
r6 = odesys.HMDR * odesys.K0
print(r3 + r6, '<- r3+r6')  # a check

fig = plt.figure()

plot1 = fig.add_subplot(611)
plot1.plot(timegrid, G, label='healthy ppl')
plot1.plot(timegrid, K, label='sick ppl')
plot1.plot(timegrid, I, label='immune ppl')
plot1.set_xlabel('time in years')
plot1.set_ylabel('number of ppl')
plot1.legend(fontsize='small')

plot2 = fig.add_subplot(612)
plot2.plot(timegrid, Mg, label='healthy mosquitoes')
plot2.plot(timegrid, Mi, label='infected mosquitoes')
plot2.set_xlabel('time in years')
plot2.set_ylabel('number of mosquitoes')
plot2.legend(fontsize='small')

plot3 = fig.add_subplot(613)
plot3.plot(timegrid, T, label='dead ppl')
plot3.set_xlabel('time in years')
plot3.set_ylabel('number of dead ppl')
plot3.legend(fontsize='small')

plot4 = fig.add_subplot(614)
plot4.plot(timegrid, PR, label='fraction carrying parasite')
plot4.set_xlabel('time in years')
plot4.set_ylabel('fraction of people')
plot4.legend(fontsize='small')
plot4.axhline(1, color='red')

plot5 = fig.add_subplot(615)
plot5.plot(timegrid, CR, label='proportion of pop child')
plot5.set_xlabel('time in years')
plot5.set_ylabel('fraction of people')
plot5.legend(fontsize='small')

plot6 = fig.add_subplot(616)
plot6.plot(timegrid, IR, label='proportion of adult pop immune')
plot6.set_xlabel('time in years')
plot6.set_ylabel('fraction of people')
plot6.legend(fontsize='small')

plt.show()
