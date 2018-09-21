import odesysivp
from scipy.integrate import solve_ivp
import numpy as np
import pickle
import multiprocessing as mp
from multiprocessing import Queue
mp.set_start_method('fork')

# creating an array of results for different values for the absolute mrna expression and the protein half life
rna_range = np.linspace(10, 1000, 50)  # choosing the values for which i will solve
half_life_range = np.linspace(0.1, 100, 50)
eval_timepoints = np.linspace(0, 53, 1000)  # gives me solutions at these points so i know what shape the solution has

results = []  # this will be the results with nesting order rna, half life so 2d 'array' of objects

# the following: a solution for each chosen rna and half life value - this allows me to generate stream plots
#for rna_abundance in rna_range:
#    mean_expr = rna_abundance
#    curr_rna_results = []

q = Queue()


def results_by_half_life(mean_expr):
    list_of_results = []
    step = 0
    for half_life in half_life_range:
        phalf = half_life
        pdecay_rate = np.log(2) * 60 / phalf
        result = solve_ivp(lambda t, y: odesysivp.f(t, y, mean_expr, pdecay_rate), (0, 53), odesysivp.y0,
                           t_eval=eval_timepoints)

        if not result.success:  # error handling for failed solve
            print(result)
            raise StopIteration('solve failed - message is:', result.message)
        #print(f'you are on step {step}')
        step += 1
        list_of_results.append(result)
    print(f'calculation for mrna = {mean_expr} done (50 decay rates)')
    q.put(list_of_results)


processes = []
for mean_expr in rna_range:
    p = mp.Process(target=results_by_half_life, args=(mean_expr, ))
    processes.append(p)
    print('starting')
    p.start()

print('all started')

results = []
#while True:
#    try:
#        result = q.get(False, 0.01)
#        results.append(result)
#
#    except q.empty():
#        pass
#    allExited = True
#    for t in processes:
#        if t.exitcode is None:
#            allExited = False
#            break
#    if allExited & q.empty():
#        break

while 1:
    running = any(p.is_alive() for p in processes)
    while not q.empty():
        results.append(q.get())
    if not running:
        break

join_count = 0

for proc in processes:
    print(f'joining {join_count}')
    join_count += 1
    proc.join()

print('all joined')


#results = []
#while not q.empty():
#    print('queue not yet empty')
#    results.append(q.get())

print('should be done')

#if __name__ == '__main__':
#
#    for mean_expr in rna_range:
#        p = mp.Process(target=results_by_half_life(), args=mean_expr)
#        p.start()


with open('resultsshape.txt', 'w') as f:  # quick check on results shape
    f.write('shape of results array is:')
    f.write(str(np.shape(results)))

with open('results.pickle', 'wb') as f:  # pickling the results so i dont have to work them out every time
        pickle.dump(results, f)
        print('results written to results')



