
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import odesys

#solve space
start  = 0.0
end = 2
number_of_points = 2001
timegrid = np.linspace(start, end, number_of_points)


result = odeint(odesys.f, odesys.y0, timegrid) #the integration takes place with dy/dt given by f, y0 by y0 and the integration variable with limits by timegrid

G = []
K = []
I = []
Mg = []
Mi = []
T = []
PR = []

for row in result:
    G.append(row[0])
    K.append(row[1])
    I.append(row[2])
    Mg.append(row[3])
    Mi.append(row[4])
    T.append(row[5])
    PR.append((row[1]+row[2])/(row[0]+row[1]+row[2])) # parasite ratio - fraction of ppl carrying parasite


r3 = odesys.IAR * odesys.K0
r6 = odesys.HMDR * odesys.K0
print(r3+r6 , '<- r3+r6') # a check

fig = plt.figure()

plot1 = fig.add_subplot(411)
plot1.plot(timegrid, G, label='healthyppl')
plot1.plot(timegrid, K, label='sick ppl')
plot1.plot(timegrid, I, label='immune ppl')
plot1.set_xlabel('time in years')
plot1.set_ylabel('number of ppl')
plot1.legend(fontsize='small')

plot2 = fig.add_subplot(412)
plot2.plot(timegrid, Mg, label='healthy mosquitos')
plot2.plot(timegrid, Mi, label='infected mosquitos')
plot2.set_xlabel('time in years')
plot2.set_ylabel('number of mosquitos')
plot2.legend(fontsize='small')

plot3 = fig.add_subplot(413)
plot3.plot(timegrid, T, label='dead ppl')
plot3.set_xlabel('time in years')
plot3.set_ylabel('number of dead ppl')
plot3.legend(fontsize='small')

plot4 = fig.add_subplot(414)
plot4.plot(timegrid, PR, label='fractoin carrying parasite')
plot4.set_xlabel('time in years')
plot4.set_ylabel('fraction of people')
plot4.legend(fontsize='small')
plot4.axhline(1, color = 'red')


plt.show()



