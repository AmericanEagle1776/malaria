import pandas as pd
pd.options.mode.use_inf_as_na = True

aatr = pd.read_excel('aatransporters.xls', header=0)
aatr2 = aatr.set_index('Name')  # make table where names are indices
expr = pd.read_excel('3d7expression.xls', header=25)
expr2 = expr.set_index('PlasmoDB_ID')
codonspeeds = pd.read_excel('codonspeedsx.xls', header=0)
codonspeeds.set_index('value')
cd = {'A':1, 'C':2, 'G':3, 'U':4}  # for codon labelling

def get_length(name):

    x = aatr2.loc[name, 'length']  # get place where indices are name and length
    return x  # return length value


def get_pseq(name): #read file into list
    with open(name + 'protseq') as f:
        pseq = []
        for line in f:

            for c in line:
                if c == '\n':
                    continue
                else:
                    pseq.append(c)

    return pseq


def get_rseq(name): #read file into list
    with open(name + 'mrnaseq') as f:
        rseq = []
        for line in f:

            for c in line:
                if c == '\n':
                    continue
                else:
                    #if c == 'T':     # these translate dna to rna
                    #    c = 'A'
                    #elif c == 'G':
                    #    c = 'C'
                    #elif c == 'C':
                    #    c = 'G'
                    #elif c == 'A':
                    #   c = 'U'
                    if c == 'T':  # this translates cdna to rna - it its right bc then the sequence starts on aug
                        c = 'U'
                    rseq.append(c)

    return rseq

def get_expr(name):  # makes list of expression values in 3d7expression

    exprlist = []
    for x in range(53):
        exprlist.append(expr2.loc[name, 'Timepoint ' + str(x+1)])

    return exprlist

def get_codon_clear_time(codon):

    index = 0
    a =100
    for x in codon:
<<<<<<< HEAD
=======
        index = a * cd[x]
        a /= 10

    time = 0
    time = codonspeeds.loc[index, time]
    return time


>>>>>>> ba9f4d2d38716f329e42cf7ebc7405236510deee


