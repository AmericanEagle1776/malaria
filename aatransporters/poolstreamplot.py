import pickle
import matplotlib.pyplot as plt
import numpy as np
from bisect import bisect_left


def takeClosest(myList, myNumber):
# from https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value#12141207
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before


with open('poolresults.pickle', 'rb') as fp:
    results = pickle.load(fp)

t_to_use = 30  # in hrs
results_ab_vals = []
resultss = results[0]
for by_half in resultss:
    curr = []
    for x in by_half:
        t_in_array = takeClosest(x.t, t_to_use)
        index = list(x.t).index(t_in_array)
        #print(index)
        curr.append(x.y[0][index])
    results_ab_vals.append(curr)

print(np.shape(results_ab_vals))
#print('abs vals is', results_ab_vals)
#print(results_ab_vals)
fig = plt.figure()
plot1 = fig.add_subplot(111)
plot1.imshow(results_ab_vals, cmap='Purples', origin='lower')
plot1.set_ylabel('rna value')
plot1.set_xlabel('half life')

xticks = [0,]
for xtick in np.linspace(0.1, 100, 6):
    xticks.append(round(xtick, 0))
plot1.set_xticklabels(xticks)

yticks = [0]
for ytick in np.linspace(1, 10000, 6):
    yticks.append(round(ytick, 0))
plot1.set_yticklabels(yticks)

for tick in plot1.get_xticklabels():
    tick.set_rotation(45)


plt.show()
