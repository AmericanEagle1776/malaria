from proteins import Protein
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as npo

p1 = Protein('PFL0420w')  # new protein
p2 = Protein('PFB0435c')
p1e = p1.expr  # protein expression list, relative
p1ct = p1.get_start_clearance_time(p1)  # ribosome start area clearance g
p1rt = p1.get_read_time(p1)  # ribosome read time for whole protein
p1l = p1.length  # protein length in no of amino acids
p1exprpol = p1.get_expr_by_time(p1e)  # polynomial fit of protein expression, returns numpy Polynomial
p2e = p2.expr  # protein expression list, relative
p2ct = p2.get_start_clearance_time(p2)  # ribosome start area clearance g
p2rt = p2.get_read_time(p2)  # ribosome read time for whole protein
p2l = p2.length  # protein length in no of amino acids
p2exprpol = p2.get_expr_by_time(p2e)  # polynomial fit of protein expression, returns numpy Polynomial
meanexpr = 100

p1timegrid = np.linspace(0, 53, 100)
p1list = []
for t in p1timegrid:
    p1i = npo.polyval(t - (p1rt / 360), p1exprpol) * meanexpr * 360 / p1ct
    p1list.append(p1i)

p2timegrid = np.linspace(0, 53, 100)
p2list = []
for t in p2timegrid:
    p2i = npo.polyval(t - (p2rt / 360), p2exprpol) * meanexpr * 360 / p2ct
    p2list.append(p2i)

fig = plt.figure()
t = np.linspace(0, 53, 100)
t2 = np.linspace(0, 53, 51)
exprlist = npo.polyval(t, p1exprpol)  # should give values of polynomial at times in t
plot1 = fig.add_subplot(113)
plot1.plot(t, exprlist, label='rna relative expression as shown by polynomial')
plot1.plot(t2, p1e, label='data')
plot1.set_ylabel('relative expression')
plot1 = fig.add_subplot(213)
plot1.plot(p1timegrid, p1list, label='protein absolute expression ')
plot1.set_xlabel('time in hrs')
plot1.set_ylabel('expression')
plot2 = fig.add_subplot(313)
plt.show()
