# simple model of malaria affected population
# time will be in days
# population size in number of individuals

import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#initial conditions
G0  = 1000 #1000 healthy people
K0  = 10   #10 infected, poorly people
I0  = 0    #0 infected, immune people
Mg0 = 1000 #1000 uninfected mosquito vectors
Mi0 = 300  #300 infected mosquito vectors
T0 = 0 #dead humans
#PR0 = (K0+I0)/(K0+I0+G0) # initial parasite ratio

y0 = [G0, K0, I0, Mg0, Mi0, T0]# PR0] #initial conditions vector

#parameters
IR = 0.4 #chance of infection for human by infected mosquito bite
#EIR = BR * Mii/(Mgi+Mii)200 #entomological innoculation rate in 1/a maybe another day
BR = 1000 #bite rate - bites per year total
ICR  = 10 #infection clearance rate is 2 in smith 2005 in infections cleared per year
IAR = 0.3 #fraction of infected population that becomes immune each year
MIR = 1 #mosquito infection rate when biting infectious human
MBR = 0.5 #replication of population mosquitos
OADR = 0.1 #old age death rate - we have no age profile so well see
HMDR = 0.1 #malaria death rate for infected humans
MOADR = 0.5 #mosquito ld age death rate - half of mosquitos in a given year will die of old age
MCR = 100 #mosquito control rate - killing of mosquitos

#solve space
start  = 0.0
end = 1
number_of_points = 201
timegrid = np.linspace(start, end, number_of_points)



def f(y, t):#function f solves dy/dt = f(y, t), where y is state vector and t is time(integration variable)

    #curent size of population
    Gi  = y[0] 
    Ki  = y[1]
    Ii  = y[2]
    Mgi = y[3]
    Mii = y[4]
    Ti  = y[5]

    hpop = Gi+Ki+Ii #whole human population
    mpop = Mgi + Mii #whole mosquito population

    #PR0 = y[5] #(K0+I0)/(K0+I0+G0) 
    r1 = IR * BR * Mii/mpop #human infection rate
    r2 = (ICR - (IR * BR * Mii))   #rate of losing immunity
    r3 = IAR  #human immunity acquisition rate
    r4 = BR * MIR * (Ii+Ki)/hpop  #mosquito infection rate
    r5 = MBR #mosquito birth rate 
    r6 = HMDR  # human malaria death rate 
    r7 = OADR  #healthy population old age deaths
    r8 = (MOADR + MCR) #mosquito natural death rate

    f0 = - r1*Gi + r2*Ii - r7*Gi  #dG/dt
    f1 = + r1*Gi - r3*Ki - r6*Ki - r7*Ki #dK/dt
    f2 = - r2*Ii + r3*Ki - r7*Ii #dI/dt
    f3 = - r4*Mgi + r5*mpop - r8*Mgi #dMg/dt
    f4 = + r4*Mgi - r8*Mii #dMi/dt
    f5 = + r6*Ki + r7*(Gi+Ki+Ii) #dT/dt
    
    

    return [f0, f1, f2, f3, f4, f5]


result = odeint(f, y0, timegrid) #the integration takes place with dy/dt given by f, y0 by y0 and the integration variable with limits by timegrid

G =[]
for row in result:
    G.append(row[0])

K =[]
for row in result:
    K.append(row[1])

I =[]
for row in result:
    I.append(row[2])

Mg =[]
for row in result:
    Mg.append(row[3])

Mi =[]
for row in result:
    Mi.append(row[4])

T =[]
for row in result:
    T.append(row[5])

r3 = IAR * K0
r6 = HMDR * K0
print(r3+r6 , '<- r3+r6') # a check

fig = plt.figure()

plot1 = fig.add_subplot(311)
plot1.plot(timegrid, G, label='healthyppl')
plot1.plot(timegrid, K, label='sick ppl')
plot1.plot(timegrid, I, label='immune ppl')
plot1.set_xlabel('time in years')
plot1.set_ylabel('number of ppl')
plot1.legend(fontsize='small')

plot2 = fig.add_subplot(312)
plot2.plot(timegrid, Mg, label='healthy mosquitos')
plot2.plot(timegrid, Mi, label='infected mosquitos')
plot2.set_xlabel('time in years')
plot2.set_ylabel('number of mosquitos')
plot2.legend(fontsize='small')

plot3 = fig.add_subplot(313)
plot3.plot(timegrid, T, label='dead ppl')
plot3.set_xlabel('time in years')
plot3.set_ylabel('number of ppl')
plot3.legend(fontsize='small')

plt.show()



