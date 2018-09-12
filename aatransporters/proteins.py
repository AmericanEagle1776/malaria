import numpy as np
from dataimport import get_length
from dataimport import get_seq


class Protein:

    def __init__(self, name):

        self.name = name
        self.length = self.get_length1(name)
        self.seq = self.get_seq1(name)

    def get_length1(self, name):
        x = get_length(name)
        return x

    def get_seq1(self, name):
        x = get_seq(name)
        return x

