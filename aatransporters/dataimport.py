import pandas as pd

aatr = pd.read_excel('aatransporters.xls', header=0)
aatr2 = aatr.set_index('Name')  # make table where names are indices
expr = pd.read_excel('3d7expression.xls', header=25)
expr2 = expr.set_index('PlasmoDB_ID')


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
                    rseq.append(c)

    return rseq

def get_expr(name):  # makes list of expression values in 3d7expression

    exprlist = []
    for x in range(53):
        exprlist.append(expr2.loc[name, 'Timepoint ' + str(x+1)])

    return exprlist

