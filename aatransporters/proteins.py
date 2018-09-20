import numpy as np
import scipy.optimize as spo
import dataimport as di


class Protein:

    def __init__(self, name, start_time=0):

        self.name = name
        self.length = self.get_length1(name)  # get length in amount of amino acids via helper function
        self.pseq = self.get_pseq1(name)  # get protein amino acid sequence via helper function
        self.rseq = self.get_rseq1(name)  # get rna sequence via helper function
        self.expr = self.get_expr1(name)  # get expression of rna via helper function
        self.codons = self.get_codons(self.rseq)  # writes a list of codon 3tuples
        self.rel_expr_by_time = self.get_expr_by_time(self.expr)  # gets an expression profile
        self.start_clearance_time = self.get_start_clearance_time()  # time for ribosome to run first ten codons
        self.read_time = self.get_read_time()
        self.start_time = start_time
        self.init_rate = 1/(self.start_time+self.start_clearance_time)

    def get_length1(self, name):    # these next methods get stuff from he dataimport.py
        length = di.get_length(name)
        return length

    def get_pseq1(self, name):
        pseq = di.get_pseq(name)
        return pseq

    def get_rseq1(self, name):
        rseq = di.get_rseq(name)
        return rseq

    def get_expr1(self, name):
        expr = di.get_expr(name)
        return expr

    def get_codons(self, rseq):  # make list of nucleotides into list of codons # TODO: check for start and stop

        codons = []
        counter = 0
        d = {}

        for r in rseq:
            if counter < 3:
                d[f'r{counter}'] = r
                counter += 1

            else:
                codons.append((d['r0'], d['r1'], d['r2']))
                d = {}
                counter = 0

        return codons

    def get_expr_by_time(self, expr):

        n = len(expr)
        tlist = list(range(n))
        nanlist = []

        for x in expr:
            if np.isnan(x):
                nanlist.insert(0, expr.index(x))

        for x in nanlist:
            del expr[x]
            del tlist[x]

        def func(x, a, b, c, d, e, f, g, h, i):  # , j, k, l, m):
            return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7+i*x**8  # +j*x**9+k*x**10+l*x**11+m*x**12

        popt, pcov = spo.curve_fit(func, tlist, expr)
        exprcurve = popt
        return exprcurve

    def get_start_clearance_time(self):  # time for ribosome clearance of first ten codons

        time = 0
        counter = 0
        for codon in self.codons:
            counter += 1
            time += di.get_codon_clear_time(codon)
            if counter == 10:
                break

        return time

    def get_read_time(self):  # total read time of protein by ribosome

        time = 0
        counter = 0
        for codon in self.codons:
            counter += 1
            if np.isnan(di.get_codon_clear_time(codon)):
                continue
            else:
                time += di.get_codon_clear_time(codon)

            if counter == self.length:
                break

        return time

