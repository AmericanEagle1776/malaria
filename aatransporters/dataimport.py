import pandas as pd

aatr = pd.read_excel('aatransporters.xls', header=1)
expr = pd.read_excel('3d7expression.xls', header=25)
expr2 = expr.set_index('PlasmoDB_ID')


def get_length(name):
    aatr2 = aatr.set_index('Name') #make table where names are indices
    x = aatr2.loc(name, 'length') #get place where indices are name and length
    return x #return length value

def get_seq(name): #read file into list
    with open(name + 'protseq') as f:
        seq = []
        for line in f:
            for c in line:
                seq.append(c)

    return seq

def get_expr(name):  # makes list of expression values in 3d7expression

    exprlist = []
    for x in range(52):
        exprlist.append(expr2.loc(name, 'timstamp' + (x+1)))

    return exprlist

