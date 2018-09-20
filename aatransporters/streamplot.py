import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('results.pickle', 'rb') as fp:
    results = pickle.load(fp)

results_ab_vals = []
for by_half in results:
    curr = []
    for x in by_half:
        curr.append(x.y[0][900])
    results_ab_vals.append(curr)

print(np.shape(results_ab_vals))
#plot1 = fig.add_subplot(111)
#plot1.imshow(results)
#plt.imshow(results)
print('abs vals is', results_ab_vals)
#print(results_ab_vals)
fig = plt.figure()
plot1 = fig.add_subplot(111)
plot1.imshow(results_ab_vals, cmap='inferno', origin='lower')
plot1.set_ylabel('rna value')
plot1.set_xlabel('half life')

xticks = []
for xtick in np.linspace(0.1, 100, 7):
    xticks.append(round(xtick, 0))
plot1.set_xticklabels(xticks)

yticks = []
for ytick in np.linspace(1, 10000, 7):
    yticks.append(round(ytick, 0))
plot1.set_yticklabels(yticks)

for tick in plot1.get_xticklabels():
    tick.set_rotation(45)
#cbar = plt.colorbar(plot1)

plt.show()
