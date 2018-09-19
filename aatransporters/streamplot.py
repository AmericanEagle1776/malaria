import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('results', 'rb') as fp:
    results = pickle.load(fp)

results_ab_vals = []

for by_half in results:
    curr = []
    for x in by_half:
        curr.append(x.y[0][500])
    results_ab_vals.append(curr)

#plot1 = fig.add_subplot(111)
#plot1.imshow(results)
#plt.imshow(results)
print(results_ab_vals)
#print(results_ab_vals)
fig = plt.figure()
plot1 = fig.add_subplot(111)
plot1.imshow(results_ab_vals, cmap='autumn')
plot1.set_xlabel('rna value')
plot1.set_ylabel('half life')

plt.show()
