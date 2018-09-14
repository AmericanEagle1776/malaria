from proteins import Protein    
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as npo


p1 = Protein('PFL0420w') # new protein
p1e = p1.expr #protein expression list, relative
p1ct = p1.get_start_clearance_time(p1) # ribosome start area clearance g
p1rt = p1.get_read_time(p1)  # ribosome read time for whole protein
p1l = p1.length  # protein length in no of amino acids
p1exprpol = p1.get_expr_by_time(p1e)  # polynomial fit of protein expression, returns numpy Polynomial
meanexpr = 100

p1timegrid = np.linspace(0, 53, 100)
p1list = []
for t in p1timegrid:
	p1i = npo.polyval(t, p1exprpol)*meanexpr + t/p1ct + t/p1rt
	p1list.append(p1i)

fig = plt.figure()
t = np.linspace(0, 53, 100)
exprlist = npo.polyval(t, p1exprpol) # should give values of polynomial at times in t
plot1= fig.add_subplot(211)
plot1.plot(t, exprlist, label='rna relative expression as shown by polynomial')
plot1.set_xlabel('time in s')
plot1.set_ylabel('relative expression')
plot1= fig.add_subplot(212)
plot1.plot(p1timegrid, p1list, label='protein absolute expression ')
plot1.set_xlabel('time in s')
plot1.set_ylabel('expression')
plt.show()

