import numpy as np
from dataimport import get_length
from dataimport import get_pseq
from dataimport import get_rseq
from dataimport import get_expr



class Protein:

    def __init__(self, name):

        self.name = name
        self.length = self.get_length1(name)  # get length in amount of amino acids via helper function
        self.pseq = self.get_pseq1(name)  # get protein amino acid sequence via helper function
        self.rseq = self.get_rseq1(name)  # get rna sequence via helper function
        self.expr = self.get_expr1(name)  # get expression of rna via helper function


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

