from proteins import Protein
import odesys
from scipy.integrate import odeint
import matplotlib.pyplot as plt


prot1 = Protein('PFL0420w')
e = prot1.expr

#t = np.linspace(0, 53, 53, endpoint=True)
t = range(0, 53, 1)
#print(e)
#print(t)

p1 = Protein('PFL0420w')
p1e = p1.expr
p1ct = p1.get_start_clearance_time(p1)       # a.append(e.index(x))

p10 = 0
y0 = [p10]

result = odeint(odesys.f, odesys.y0, odesys.timegrid)

P1 = result[0]
print(P1)
fig = plt.figure()

plot1 = fig.add_subplot(111)
plot1.plot(odesys.timegrid, P1, label='Prot {} expr'.format(prot1.name))
plot1.set_ylabel('')
plot1.set_xlabel('time in hrs')
plt.show()
