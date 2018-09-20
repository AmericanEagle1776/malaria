import odesysivp
import config
from scipy.integrate import solve_ivp
import numpy as np
import pickle

# creating an array of results for different values for the absolute mrna expression and the protein half life
step = 0 # for visual output
rna_range = np.linspace(10, 1000, 50)  # choosing the values for which i will solve
half_life_range = np.linspace(0.1, 100, 50)
eval_timepoints = np.linspace(0, 53, 1000) # gives me solutions at these points so i know what shape the solution has

results = []  # this will be the results with nesting order rna, half life so 2d 'array' of objects

# the following: a solution for each chosen rna and half life value - this allows me to generate stream plots
for rna_abundance in rna_range:
    mean_expr = rna_abundance
    curr_rna_results = []
    for half_life in half_life_range:
        phalf = half_life
        pdecay_rate = np.log(2) * 60 / phalf
        result = solve_ivp(lambda t, y: odesysivp.f(t, y, mean_expr, pdecay_rate), (0, 53), odesysivp.y0,
                           t_eval=eval_timepoints)

        if not result.success:  # error handling for failed solve
            print(result)
            raise StopIteration('solve failed - message is:', result.message)
        print(f'you are on step {step}')
        step += 1
        curr_rna_results.append(result)

    results.append(curr_rna_results)


with open('resultsshape.txt', 'w') as f:  # quick check on results shape
    f.write('shape of results array is:')
    f.write(str(np.shape(results)))

with open('results.pickle', 'wb') as f:  # pickling the results so i dont have to work them out every time
        pickle.dump(results, f)
        print('results written to results')



