# simple model of malaria affected population
# time will be in days
# population size in number of individuals


# initial conditions
G0 = 300  # 1000 healthy people
K0 = 300  # 10 infected, poorly people
I0 = 300  # 0 infected, immune people
Mg0 = 10  # 1000 uninfected mosquito vectors
Mi0 = 300  # 300 infected mosquito vectors
T0 = 0  # dead humans
Cg0 = 50  # healthy children - no immunity
Ci0 = 50  # infected children
# PR0 = (K0+I0)/(K0+I0+G0) # initial parasite ratio

y0 = [G0, K0, I0, Mg0, Mi0, T0, Cg0, Ci0]  # initial conditions vector

# parameters
HIR = 0.3  # chance of infection for human by infected mosquito bite
# EIR = BR * Mii/(Mgi+Mii)200 #entomological innoculation rate in 1/a maybe another day
BR = 100  # bite rate - bites per year total
BiR = 0.5  # birth rate humans
ICR = 10  # infection clearance rate is 2 in smith 2005 in infections cleared per year
IAR = 0.3  # fraction of infected population that becomes immune each year
MIR = 1  # mosquito infection rate when biting infectious human
MBR = 0.5  # replication of population mosquitos
HOADR = 0.05  # old age death rate - we have no age profile so well see
HMDR = 0.05  # malaria death rate for infected humans
MOADR = 0.5  # mosquito old age death rate - half of mosquitos in a given year will die of old age
MCR = 0  # mosquito control rate - killing of mosquitos
HMS = 5  # how many mosquitos does (the blood of) one human support



def f(y, t):  # function f solves dy/dt = f(y, t), where y is state vector and t is time(integration variable)


    # curent size of population
    Gi = y[0]
    Ki = y[1]
    Ii = y[2]
    Mgi = y[3]
    Mii = y[4]
    Ti = y[5]
    Cgi = y[6]
    Cii = y[7]

    hapop = Gi + Ki + Ii  # human adult population
    hpop = Gi + Ki + Ii + Cgi + Cii  # human population
    mpop = Mgi + Mii  # whole mosquito population

    r1 = HIR * BR * Mii / mpop  # human infection rate
    r2 = ICR / r1  # r1 #* Ii  #rate of losing immunity
    r3 = IAR  # human immunity acquisition rate
    r4 = BR * MIR * (Ii + Ki) / hpop  # mosquito infection rate
    r5 = MBR  # mosquito birth rate
    r6 = HMDR  # human malaria death rate 
    r7 = HOADR  # healthy population old age deaths
    r8 = (MOADR + MCR)  # mosquito natural death rate
    r9 = BiR  # human birth rate
    r11 = 0.1  # children to adult rate
    r10 = MBR * HMS * hpop / mpop  # human population dependent mosquito birth rate


    dGdt  = - r1 * Gi + r2 * Ii - r7 * Gi + r11 * (Cgi + Cii)  # dG/dt
    dKdt  = + r1 * Gi - r3 * Ki - r6 * Ki - r7 * Ki  # dK/dt
    dIdt  = - r2 * Ii + r3 * Ki - r7 * Ii  # dI/dt
    dMgdt = - r4 * Mgi + r5 * mpop - r8 * Mgi + r10 * mpop  # dMg/dt
    dMidt = + r4 * Mgi - r8 * Mii  # dMi/dt
    dTdt  = + r6 * Ki + r7 * (Gi + Ki + Ii + Cii)  # dT/dt
    dCgdt = - r1 * Cgi + r9 * hapop - r11 * Cgi  # dCg/dt
    dCidt = + r1 * Cgi - r11 * Cii - r6 * Cii  # dCi/dt



    return [dGdt, dKdt, dIdt, dMgdt, dMidt, dTdt, dCgdt, dCidt]


