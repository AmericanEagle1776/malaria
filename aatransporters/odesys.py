import numpy as np
from proteins import Protein
from dataimport import get_codon_clear_time


#def get_start_clearance_time(protein):
#
#    time = 0
#    counter = 0
#    for codon in protein.codons:
#        counter += 1
#        time += get_codon_clear_time(codon)
#        if counter == 10:
#            break
#
#    return time
#
#
#def get_read_time(protein):
#
#    time = 0
#    counter = 0
#    for codon in protein.codons:
#        counter +=1
#        if np.isnan(get_codon_clear_time(codon)):
#            continue
#        else:
#            time += get_codon_clear_time(codon)
#
#        if counter == protein.length:
#            break
#
#    return time


timegrid = np.linspace(0, 53, 100, endpoint=True)  # timegrid for intergation


p1 = Protein('PFL0420w')
p1e = p1.expr
p1ct = p1.get_start_clearance_time(p1)
p1rt = p1.get_read_time(p1)
p1l = p1.length
p1exprpol = p1.get_expr_by_time(p1e)
#print(p1e)
#print('p1 length = ', p1l)
#print('start clear time', p1ct)
#print('readtime',  p1rt)
p10 = 0
y0 = [p10]
exprabs = 100  # max expression in absolute numbers - speculative

def f(y, t):
    """
    declares the integration functions

    :param y: the list of varibles
    :param t:   the time
    :return:  list of variables for t + i
    """

    p1i = y[0]

    dp1dt = p1exprpol.polyval(t) * exprabs + t * (1/p1ct) + t*(1/p1rt)

    return[dp1dt]


