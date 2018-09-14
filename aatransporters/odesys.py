import numpy as np
from proteins import Protein
from dataimport import get_codon_clear_time

def get_rib_clearance_time(protein):

	time = 0
	counter = 0
	for codon in protein.rseq:
		counter += 1
		time += get_codon_clear_time(codon)
		if counter == 10:
			break

	return time



p1 = Protein('PFL0420w')
p1e = p1.expr
p1ct = get_rib_clearance_time(p1)
print(p1ct)
p10 = 0
y0 = [p10]

#def f(y, t):
#
#	p1i = y[0]
#
#	f0 = 




