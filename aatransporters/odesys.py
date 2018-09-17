import numpy as np
from proteins import Protein
import numpy.polynomial.polynomial as npo
import config
from decimal import *

timegrid = np.linspace(0, 53, 100, endpoint=True)  # timegrid for integration in hours

p1 = Protein('PFL0420w')
p1e = p1.expr  # expression list
p1ct = p1.get_start_clearance_time(p1)  # in seconds
p1rt = p1.get_read_time(p1)  # in seconds
p1l = p1.length  # in no of amino acids
p1exprpol = p1.get_expr_by_time(p1e)  # expression polynomial

meanexpr = 100  # mean expression in absolute numbers of mrnas - speculative
p1starttime = 0  # the time the ribosome spends on start region not moving
p1initrate = p1ct + p1starttime  # rate of new ribosomes on start region
p1half = 43   # protein half life in minutes (43), Belle Tanay 2006
p1decay_rate = np.log(2) * 60 / p1half  # protein decay rate for x = x0 * e^(-p1decay_rate*t) in 1/h

# start values and ensuing vector
p10 = 1110  # a protein
pe0 = 10000  # a test protein
p1dep = 0  # depreciated/deatured p1
y0 = [p10, pe0, p1dep]


def f(y, t, told, tlist, xdictionary):  # timestep function
    """
    declares the integration functions

    :param y: the list of variables
    :param t: the time
    :return:  list of variables for t
    """

    delta_t = t-told[0]
    p1i = y[0]  # current protein
    pei = y[1]  # expiring test protein
    p1dep = y[2]
    #for start_time in tlist:
    #    p1i += xdictionary[start_time]*np.exp(-p1decay_rate*(t-start_time))

    print(t-config.told[0])
    r1 = p1i * np.exp(-delta_t * p1decay_rate)  # a linearised term for exponential decay - r1 = delta x

    dp1dt = + npo.polyval(p1exprpol, t - (p1rt / 360))[0] * meanexpr * 360 / p1initrate - r1
    dpedt = - p1decay_rate * np.exp(-p1decay_rate * t) * pe0
    dp1depdt = p1i * p1decay_rate * np.exp(-(delta_t) * p1decay_rate)

    #tlist.append(t)
    #xdictionary[t] = npo.polyval(p1exprpol, t - (p1rt / 360))[0]
    config.told[0] = float(t)

    return [dp1dt, dpedt, dp1depdt]
