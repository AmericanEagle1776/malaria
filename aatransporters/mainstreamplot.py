import odesysivp
import config
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as npo
import pickle

# creating an array of results for different values for the absolute mrna expression and the protein half life
step = 0
rna_range = np.linspace(10, 10000, 20)
half_life_range = np.linspace(1, 1000, 20)
eval_timepoints = np.linspace(0, 53, 1000)
results = [] #this will be the results with nesting order rna, half life
for rna_abundance in rna_range:
    odesysivp.mean_expr = rna_abundance
    curr_rna_results = []
    for half_life in half_life_range:
        odesysivp.phalf = half_life
        result = solve_ivp(lambda t, y: odesysivp.f(t, y, config.told), (0, 53), odesysivp.y0,
                           t_eval=eval_timepoints)
        if not result.success:  # error handling for failed solve
            print(result)
            raise StopIteration('solve failed - message is:', result.message)
        print(f'you are on step {step}')
        step += 1
        curr_rna_results.append(result)

    results.append(curr_rna_results)


with open('resultsshape.txt', 'w') as f: #quick check on results shape
    f.write('shape of results array is:')
    f.write(str(np.shape(results)))

with open('results', 'wb') as f: #pickling the results so i dont have to work them out ever fucking toime
        pickle.dump(results, f)



