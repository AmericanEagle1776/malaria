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
Mi0 = 30  #300 infected mosquito vectors
T0 = 0 #dead humans
#PR0 = (K0+I0)/(K0+I0+G0) # initial parasite ratio

y0 = [G0, K0, I0, Mg0, Mi0, T0]# PR0] #initial conditions vector

#parameters
HIR = 0.3 #chance of infection for human by infected mosquito bite
#EIR = BR * Mii/(Mgi+Mii)200 #entomological innoculation rate in 1/a maybe another day
BR = 100 #bite rate - bites per year total
BiR = 1 #birth rate humans
ICR  = 10 #infection clearance rate is 2 in smith 2005 in infections cleared per year
IAR = 0.3 #fraction of infected population that becomes immune each year
MIR = 1 #mosquito infection rate when biting infectious human
MBR = 0.5 #replication of population mosquitos
OADR = 0.05 #old age death rate - we have no age profile so well see
HMDR = 0.05 #malaria death rate for infected humans
MOADR = 0.5 #mosquito old age death rate - half of mosquitos in a given year will die of old age
MCR = 0 #mosquito control rate - killing of mosquitos


def f(y, t):#function f solves dy/dt = f(y, t), where y is state vector and t is time(integration variable)

    #curent size of population
    Gi  = y[0] 
    Ki  = y[1]
    Ii  = y[2]
    Mgi = y[3]
    Mii = y[4]
    Ti  = y[5]

    hpop = Gi + Ki + Ii #whole human population
    mpop = Mgi + Mii #whole mosquito population

    r1 = HIR * BR * Mii/mpop #human infection rate
    r2 = ICR/r1 #r1 #* Ii  #rate of losing immunity
    r3 = IAR  #human immunity acquisition rate
    r4 = BR * MIR * (Ii+Ki)/hpop  #mosquito infection rate
    r5 = MBR   #mosquito birth rate 
    r6 = HMDR  # human malaria death rate 
    r7 = OADR  #healthy population old age deaths
    r8 = (MOADR + MCR) #mosquito natural death rate
    r9 = BiR #human birth rate
    r10 = MBR * 10 * hpop/mpop #human population dependent mosqioto birth rate

    f0 = - r1*Gi + r2*Ii - r7*Gi + r9*hpop #dG/dt
    f1 = + r1*Gi - r3*Ki - r6*Ki - r7*Ki #dK/dt
    f2 = - r2*Ii + r3*Ki - r7*Ii #dI/dt
    f3 = - r4*Mgi + r5*mpop - r8*Mgi + r10*mpop #dMg/dt
    f4 = + r4*Mgi - r8*Mii #dMi/dt
    f5 = + r6*Ki + r7*(Gi+Ki+Ii) #dT/dt
    
    

    return [f0, f1, f2, f3, f4, f5]
