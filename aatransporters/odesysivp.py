import numpy as np
from proteins import Protein
import numpy.polynomial.polynomial as npo
import config
import matplotlib.pyplot as plt

timegrid = np.linspace(0, 53, 100, endpoint=True)  # timegrid for integration in hours

p1 = Protein('PFL0420w')
p2 = Protein('PFB0435c')
#p3 = Protein('PFL1515c')

# fig = plt.figure()
# t1 = np.linspace(0, 53, 1000)
# exprlist = npo.polyval(t1, p3.rel_expr_by_time)
# plot1 = fig.add_subplot(311)
# plot1.plot(t1, exprlist, label='aaaaaaaaaaaaaaa')
# plot1.set_ylabel('amount of proteinfgfgd')
# plot1.set_xlabel('time in hrs')
# plot1.legend(fontsize='small')
# plt.show()

# initialisation for faster runtime
p1_expr_profile = p1.rel_expr_by_time
p1_read_time = p1.read_time
p1_init_rate = p1.init_rate

p2_expr_profile = p2.rel_expr_by_time
p2_read_time = p2.get_read_time()
p2_init_rate = p2.init_rate

#p3_expr_profile = p3.rel_expr_by_time
#p3_read_time = p3.get_read_time()
#p3_init_rate = p3.init_rate

#mean_expr = 100  # mean expression in absolute numbers of mrnas - speculative
#phalf = 43  # protein half life in minutes (43), Belle Tanay 2006
#pdecay_rate = np.log(2) * 60 / phalf  # protein decay rate for x = x0 * e^(-pdecay_rate*t) in 1/h

# start values and ensuing vector
p10 = 11100  # a protein
pe0 = 10000  # a test protein
p20 = 11100
#p30 = 11100
y0 = [p10, pe0, p20]#, p30]
decay_check = [0, ]


def f(t, y, mean_expr, pdecay_rate):  # timestep function
    """
    declares the integration functions

    :param y: the list of variables
    :param t: the time
    :param told : the time of the timestep before
    :return:  list of variables for t
    """

    p1i = y[0]  # current protein
    pei = y[1]  # expiring test protein
    p2i = y[2]
    #p3i = y[4]

    #a = decay_check[-1] - r1
    #decay_check.append(r1)
    dp1dt = (+ npo.polyval(t - (p1_read_time / 3600), p1_expr_profile) * mean_expr * 3600 * p1_init_rate
            - pdecay_rate * p1i)
    dpedt = - pdecay_rate * np.exp(-pdecay_rate * t) * pe0
    #dp1depdt = p1i * pdecay_rate * np.exp(-delta_t * pdecay_rate)
    dp2dt = (+ npo.polyval(t - (p2_read_time / 3600), p2_expr_profile) * mean_expr * 3600 * p2_init_rate
            - pdecay_rate * p2i)
    #dp3dt = (+ npo.polyval(t - (p3_read_time / 3600), p3_expr_profile) * mean_expr * 3600 * p3_init_rate
          # - pdecay_rate * p3i)

    return [dp1dt, dpedt, dp2dt]#, dp3dt]
