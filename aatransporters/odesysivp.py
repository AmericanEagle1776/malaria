import numpy as np
from proteins import Protein
import numpy.polynomial.polynomial as npo
import config
from decimal import *

timegrid = np.linspace(0, 53, 100, endpoint=True)  # timegrid for integration in hours

p1 = Protein('PFL0420w')
p2 = Protein('PFB0435c')

meanexpr = 100  # mean expression in absolute numbers of mrnas - speculative
phalf = 43   # protein half life in minutes (43), Belle Tanay 2006
pdecay_rate = np.log(2) * 60 / phalf  # protein decay rate for x = x0 * e^(-pdecay_rate*t) in 1/h

# start values and ensuing vector
p10 = 1110  # a protein
pe0 = 10000  # a test protein
p1dep = 0  # depreciated/denatured p1
p20 = 1110
y0 = [p10, pe0, p1dep, p20]


def f(t, y, told): #tlist, xdictionary):  # timestep function
    """
    declares the integration functions

    :param y: the list of variables
    :param t: the time
    :param told : the time of the timestep before
    :return:  list of variables for t
    """

    delta_t = t-told  # the time difference between this step and last step
    p1i = y[0]  # current protein
    pei = y[1]  # expiring test protein
    p1dep = y[2]
    p2i = y[3]
    #for start_time in tlist:
    #    p1i += xdictionary[start_time]*np.exp(-pdecay_rate*(t-start_time))

    r1 = p1i * np.exp(-delta_t * pdecay_rate)  # a linearised term for exponential decay - r1 = delta x
    r2 = p2i * np.exp(-delta_t * pdecay_rate)  # a linearised term for exponential decay - r1 = delta x

    dp1dt = + npo.polyval(p1.get_expr_by_time(p1.expr), t - (p1.get_read_time() / 360))[0] *\
            meanexpr * 360 * p1.init_rate - r1
    dpedt = - pdecay_rate * np.exp(-pdecay_rate * t) * pe0
    dp1depdt = p1i * pdecay_rate * np.exp(-delta_t * pdecay_rate)
    dp2dt = + npo.polyval(p2.get_expr_by_time(p2.expr), t - (p2.get_read_time() / 360))[0]\
            * meanexpr * 360 * p2.init_rate - r2

    #tlist.append(t)
    #xdictionary[t] = npo.polyval(p1exprpol, t - (p1rt / 360))[0]
    config.told = float(t)

    return [dp1dt, dpedt, dp1depdt, dp2dt]
