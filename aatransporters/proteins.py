import numpy as np
from dataimport import get_length, get_pseq, get_rseq, get_expr


class Protein:

    def __init__(self, name):

        self.name = name
        self.length = self.get_length1(name)  # get length in amount of amino acids via helper function
        self.pseq = self.get_pseq1(name)  # get protein amino acid sequence via helper function
        self.rseq = self.get_rseq1(name)  # get rna sequence via helper function
        self.expr = self.get_expr1(name)  # get expression of rna via helper function
        self.codons = self.get_codons(self.rseq)  # writes a list of codon 3tuples

    def get_length1(self, name):
        length = get_length(name)
        return length

    def get_pseq1(self, name):
        pseq = get_pseq(name)
        return pseq

    def get_rseq1(self, name):
        rseq = get_rseq(name)
        return rseq

    def get_expr1(self, name):
        expr = get_expr(name)
        return expr

    def get_codons(self, rseq):  # make list of nucleotides into list of codons # TODO: check for start and stop

        codons = []
        counter = 0
        d = {}

        for r in rseq:
            if counter < 3:
                d["r{}".format(counter)] = r
                counter += 1

            else:
                codons.append((d['r0'], d['r1'], d['r2']))
                d = {}
                counter = 0

        return codons
