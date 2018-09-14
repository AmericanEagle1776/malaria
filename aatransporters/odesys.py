import numpy as np
from proteins import Protein
import numpy.polynomial.polynomial as npo


timegrid = np.linspace(0, 53, 100, endpoint=True)  # timegrid for integration in hours


p1 = Protein('PFL0420w')
p1e = p1.expr  # expression list
p1ct = p1.get_start_clearance_time(p1) # in seconds
p1rt = p1.get_read_time(p1)  # in seconds
p1l = p1.length  # in no of amino acids
p1exprpol = p1.get_expr_by_time(p1e)  # expression polynomial

meanexpr = 100  # mean expression in absolute numbers of mrnas - speculative
p1starttime = 0  # the time the ribosome spends on start region not moving
p1initrate = p1ct + p1starttime  # rate of new ribosomes on start region
p1half = 43*60  # protein half life in seconds, Belle Tanay 2006
p1dr = np.log(2)/p1half
# start values and ensuing vector
p10 = 0
y0 = [p10]


def f(y, t): # timestep function
    """
    declares the integration functions

    :param y: the list of varibles
    :param t:   the time
    :return:  list of variables for t + i
    """

    p1i = y[0] # current protein

    dp1dt = + npo.polyval(t - (p1rt / 360), p1exprpol) * meanexpr * 360 / p1initrate - p1dr*p1i

    return [dp1dt]


